### 1. TIF 모듈의 목적

TIF 모듈의 핵심 목적은 **서로 다른 스케일(scale)에서 추출된 특징 표현(feature representation)을 효과적으로 융합(fuse)**하는 것입니다.

DS-TransUNet의 인코더는 두 개의 브랜치(branch)로 구성됩니다.
*   **Primary Branch (Small-scale):** 작은 크기의 패치(e.g., 4x4)를 입력받아 세밀한(fine-grained) 특징을 추출합니다.
*   **Complementary Branch (Large-scale):** 큰 크기의 패치(e.g., 8x8)를 입력받아 거친(coarse-grained) 특징, 즉 더 넓은 영역의 전역적(global) 맥락을 추출합니다.

TIF 모듈은 이 두 브랜치에서 나온 특징들을 단순히 합치거나 이어 붙이는(concatenation) 것이 아니라, Transformer의 자기 주의(self-attention) 메커니즘을 통해 상호작용하도록 만들어 의미론적으로 풍부한 특징을 생성합니다.

### 2. TIF 모듈의 입력

인코더의 특정 스테이지(stage) `i`에서 TIF 모듈은 두 개의 특징 맵(feature map)을 입력으로 받습니다. (설명의 편의를 위해 Primary Branch를 기준으로 설명하겠습니다.)

*   **`F^i`**: Primary Branch (small-scale)에서 나온 특징 맵.
    *   크기: `C × h × w` (채널, 높이, 너비)
    *   `F^i`는 `h × w` 개의 픽셀 토큰(pixel token)으로 볼 수 있습니다. `F^i = [f_1, f_2, ..., f_{h×w}]`
*   **`G^i`**: Complementary Branch (large-scale)에서 나온 특징 맵.
    *   크기: `C' × h' × w'`

### 3. TIF 모듈의 작동 원리

TIF 모듈은 아래의 4단계로 작동합니다.

#### 3.1. 정보 요약 (Information Summarization)

먼저, Large-scale 특징 맵 `G^i`의 전역적인 정보를 하나의 대표 토큰으로 요약합니다. 이는 `G^i`의 모든 공간적 정보를 압축하여 `F^i`의 각 픽셀 토큰과 상호작용할 수 있도록 준비하는 과정입니다.

1.  `G^i`에 대해 1차원 전역 평균 풀링(Global Average Pooling)을 적용하여 공간 차원을 제거합니다.
2.  결과를 평탄화(Flatten)하여 `C'` 차원의 단일 벡터 토큰 `ĝ^i`를 생성합니다.

이를 수식으로 표현하면 다음과 같습니다 (논문의 식(4)).

$$
\hat{g}^i = \text{Flatten}(\text{Avgpool}(G^i))
$$

*   `Avgpool`: `G^i`의 공간 차원(`h' × w'`)에 대한 평균을 계산합니다.
*   `Flatten`: 벡터 형태로 변환합니다.
*   결과적으로 `ĝ^i`는 `G^i` 전체의 **전역적 추상 정보(global abstract information)**를 담은 `C' × 1` 크기의 토큰이 됩니다.

#### 3.2. 토큰 시퀀스 생성 (Token Sequence Creation)

다음으로, `F^i`의 모든 픽셀 토큰들과 `G^i`에서 요약된 전역 정보 토큰 `ĝ^i`를 하나의 시퀀스로 결합합니다.

$$
\text{Sequence}_{\text{in}} = [\hat{g}^i, f_1, f_2, \dots, f_{h \times w}]
$$

*   이 시퀀스는 총 `1 + (h × w)`개의 토큰으로 구성됩니다.
*   첫 번째 토큰은 Large-scale 브랜치의 전역 정보를, 나머지 토큰들은 Small-scale 브랜치의 각 픽셀 정보를 나타냅니다.

#### 3.3. 글로벌 자기 주의 연산 (Global Self-Attention Operation)

생성된 토큰 시퀀스 `Sequence_in`을 **표준 Transformer 블록**에 입력합니다.

$$
\text{Sequence}_{\text{out}} = \text{Transformer}(\text{Sequence}_{\text{in}})
$$

*   `Transformer`: Multi-Head Self-Attention (MSA)과 MLP로 구성된 표준 Transformer 인코더 블록입니다.
*   이 과정에서 자기 주의 메커니즘은 시퀀스 내의 **모든 토큰 쌍 간의 관계를 계산**합니다.
*   **핵심:** 이로 인해 `F^i`의 모든 픽셀 토큰(`f_k`)은 `G^i`의 전역 정보 토큰(`ĝ^i`)과 상호작용하게 됩니다. 즉, 세밀한 특징(fine-grained feature)이 거친 특징(coarse-grained feature)의 전역적 맥락 정보를 얻게 됩니다. 반대로, 전역 정보 토큰 또한 모든 픽셀 토큰의 영향을 받아 업데이트됩니다.

#### 3.4. 결과 분리 및 재구성 (Result Separation and Reshaping)

Transformer 블록을 통과한 출력 시퀀스 `Sequence_out`에서 융합된 특징 맵을 다시 추출합니다.

1.  출력 시퀀스는 입력과 동일하게 `1 + (h × w)`개의 토큰으로 구성됩니다. `Sequence_out = [f'_0, f'_1, ..., f'_{h×w}]`
2.  이 중 첫 번째 토큰 `f'_0`(업데이트된 전역 정보 토큰)은 버립니다.
3.  나머지 `h × w`개의 토큰 `[f'_1, ..., f'_{h×w}]`을 원래의 공간적 차원인 `C × h × w`로 재구성(reshape)합니다.

이 재구성된 특징 맵이 TIF 모듈의 최종 출력 `F_out`이 됩니다.

### 4. 수식 기반 요약

위 과정을 논문의 식(5)를 사용하여 요약하면 다음과 같습니다.

$$
[f'_0, f'_1, \dots, f'_{h \times w}] = \text{Transformer}([\hat{g}^i, f_1, f_2, \dots, f_{h \times w}])
$$

$$
F_{\text{out}} = [f'_1, f'_2, \dots, f'_{h \times w}] \in \mathbb{R}^{C \times (h \times w)} \rightarrow \text{Reshape to } \mathbb{R}^{C \times h \times w}
$$

*   `F_out`은 이제 `G^i`의 전역적 맥락이 반영된, 의미론적으로 더욱 풍부해진 Small-scale 특징 맵입니다.
*   이와 동일한 과정이 반대 방향(Large-scale 브랜치 기준)으로도 한 번 더 수행되어, `G^i` 또한 `F^i`의 세밀한 정보를 융합하게 됩니다.
