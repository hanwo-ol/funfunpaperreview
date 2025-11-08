### 배경: 목표 설정

메타-러닝의 목표는 여러 태스크(에피소드)로부터 학습하여 새로운 태스크에 빠르게 적응하는 것입니다. 이 논문은 이를 **계층적 베이지안 모델(Hierarchical Bayesian Model)**로 접근합니다.

*   **전역 잠재 변수 (Global Latent Variable) $\theta$**: 모든 태스크에 공유되는 사전 지식(prior knowledge)입니다. 신경망 가중치의 사전 분포(prior distribution)의 파라미터(예: 평균, 분산)에 해당합니다.
*   **지역 잠재 변수 (Local Latent Variable) $\phi_i$**: $i$번째 태스크에 특화된 파라미터입니다. $i$번째 태스크를 푸는 신경망의 실제 가중치($\phi_i$)를 의미합니다.
*   **데이터 $D_i$**: $i$번째 태스크의 데이터셋입니다.

이 구조는 "각 태스크의 신경망 가중치 $\phi_i$는 공통된 사전 분포 $p(\phi|\theta)$에서 샘플링된다"는 것을 의미합니다.

---

### 수식 전개 시작: 데이터의 로그 가능도 (Log-Likelihood)

우리의 최종 목표는 주어진 모든 데이터 $D = \{D_1, D_2, ..., D_M\}$이 나타날 확률, 즉 **가능도(Likelihood)**를 최대화하는 것입니다. 로그를 씌운 형태인 로그 가능도를 사용하는 것이 일반적입니다.

$$
\log p(D_1, ..., D_M)
$$

각 태스크는 독립적으로 샘플링되었다고 가정하므로, 확률의 곱으로 표현할 수 있습니다.

$$
\log \left[ \prod_{i=1}^{M} p(D_i) \right]
$$

### 1단계: 계층 모델을 이용한 가능도 확장

이제 $p(D_i)$를 계층 모델에 따라 확장해야 합니다. $D_i$가 나타날 확률은 잠재 변수 $\phi_i$와 $\theta$에 대해 **주변화(marginalize)**, 즉 모든 가능한 경우를 적분하여 얻을 수 있습니다.

먼저, 전역 변수 $\theta$가 주어졌을 때 $D_i$의 확률은 다음과 같습니다.

$$
p(D_i | \theta) = \int p(D_i | \phi_i) p(\phi_i | \theta) d\phi_i
$$

(해석: $\theta$로부터 특정 $\phi_i$가 샘플링되고, 그 $\phi_i$로부터 데이터 $D_i$가 생성될 모든 가능성을 적분)

이제 전역 변수 $\theta$ 자체도 우리가 모르는 값이므로, $\theta$에 대해서도 주변화해야 합니다.

$$
p(D_i) = \int p(D_i | \theta) p(\theta) d\theta = \int \left[ \int p(D_i | \phi_i) p(\phi_i | \theta) d\phi_i \right] p(\theta) d\theta
$$

모든 태스크 $D_1, ..., D_M$에 대해 이를 적용하면 논문의 첫 번째 수식이 완성됩니다.

$$
\log p(D_1, ..., D_M) = \log \left[ \int p(\theta) \left( \prod_{i=1}^{M} \int p(D_i|\phi_i) p(\phi_i|\theta) d\phi_i \right) d\theta \right]
$$

**문제점**: 이 적분은 신경망처럼 복잡한 모델에서는 해석적으로 계산하는 것이 불가능합니다. 이것이 바로 **변분 추론(Variational Inference)**이 필요한 이유입니다.

### 2단계: 변분 추론 도입과 증거 하한(ELBO) 유도 (가장 중요한 생략된 부분)

계산 불가능한 진짜 사후분포 $p(\theta, \phi | D)$ 대신, 다루기 쉬운 근사 사후분포 $q(\theta; \psi)$와 $q(\phi_i; \lambda_i)$를 도입합니다. 우리의 목표는 이 $q$가 진짜 사후분포 $p$와 최대한 비슷해지도록 파라미터 $\psi$와 $\lambda_i$를 학습하는 것입니다.

변분 추론은 로그 가능도에 대한 **증거 하한(Evidence Lower Bound, ELBO)**을 유도합니다. 이 하한을 최대화하는 것이 로그 가능도를 간접적으로 최대화하는 효과를 줍니다.

$$
\log \left[ \prod_{i=1}^{M} p(D_i) \right] \ge \mathcal{L}(\psi, \lambda_1, ..., \lambda_M)
$$

이제 이 ELBO($\mathcal{L}$)를 유도해 보겠습니다. (논문에서는 이 과정이 생략되어 있습니다)

1.  먼저, 근사 분포 $q$를 곱하고 나누어줍니다. (전체 잠재 변수를 $Z = \{\theta, \phi_1, ..., \phi_M\}$로 표기)

$$
\log p(D) = \log \int p(D, Z) dZ = \log \int q(Z) \frac{p(D, Z)}{q(Z)} dZ
$$

2.  위 식은 $q(Z)$에 대한 기댓값 형태로 표현할 수 있습니다.

$$
\log \mathbb{E}_{q(Z)} \left[ \frac{p(D, Z)}{q(Z)} \right]
$$

3.  **젠센 부등식(Jensen's Inequality)**을 적용합니다. 로그 함수는 오목(concave) 함수이므로 $\log(\mathbb{E}[X]) \ge \mathbb{E}[\log(X)]$가 성립합니다.

$$
\ge \mathbb{E}_{q(Z)} \left[ \log \frac{p(D, Z)}{q(Z)} \right]
$$

4.  이제 기댓값 안의 로그를 분해하고, $p(D,Z)$를 우리 모델에 맞게 확장합니다.

$$p(D, Z) = p(D|\phi)p(\phi|\theta)p(\theta) = p(\theta) \prod_{i=1}^M p(D_i|\phi_i)p(\phi_i|\theta)$$

$q(Z) = q(\theta) \prod_{i=1}^M q(\phi_i)$ (평균장 가정)

$$
\ge \mathbb{E}_{q(\theta)\prod q(\phi_i)} \left[ \log \frac{p(\theta) \prod_{i=1}^M p(D_i|\phi_i)p(\phi_i|\theta)}{q(\theta)\prod_{i=1}^M q(\phi_i)} \right]
$$

5.  로그의 성질($\log(ab) = \log a + \log b$)을 이용해 항들을 분리합니다.

$$
\ge \mathbb{E}_{q(\theta)\prod q(\phi_i)} \left[ \sum_{i=1}^M \log p(D_i|\phi_i) + \sum_{i=1}^M \log \frac{p(\phi_i|\theta)}{q(\phi_i; \lambda_i)} + \log \frac{p(\theta)}{q(\theta; \psi)} \right]
$$

6.  기댓값을 각 항에 분배하고 KL 발산(Kullback-Leibler divergence) 형태로 정리합니다.

$\text{KL}(q\Vert p) = \mathbb{E}_q[\log \frac{q}{p}] = -\mathbb{E}_q[\log \frac{p}{q}]$

$$
= \sum_{i=1}^M \mathbb{E}_{q(\theta;\psi)} \left[ \mathbb{E}_{q(\phi_i;\lambda_i)}[\log p(D_i|\phi_i)] \right] - \sum_{i=1}^M \mathbb{E}_{q(\theta;\psi)} \left[ \text{KL}(q(\phi_i;\lambda_i) \Vert  p(\phi_i|\theta)) \right] - \text{KL}(q(\theta;\psi) \Vert  p(\theta))
$$

이 마지막 식이 바로 논문의 `\mathcal{L}(\psi, \lambda_1, ..., \lambda_M)`에 해당하는 **ELBO**입니다. 논문에서는 기댓값 순서를 조금 다르게 표현했을 뿐, 본질적으로 동일한 식입니다.

$$
\mathcal{L} = \mathbb{E}_{q(\theta;\psi)} \left[ \sum_{i=1}^M \mathbb{E}_{q(\phi_i;\lambda_i)}[\log p(D_i|\phi_i)] - \text{KL}(q(\phi_i;\lambda_i) \Vert  p(\phi_i|\theta)) \right] - \text{KL}(q(\theta;\psi) \Vert  p(\theta))
$$

### 3단계: 최적화 문제로의 전환 (수식 1, 2)

이제 우리의 목표는 이 ELBO($\mathcal{L}$)를 최대화하는 $\psi$와 $\lambda_i$를 찾는 것입니다. 이것이 바로 **수식 (1)** 입니다.

$$
\underset{\psi, \lambda_1, ..., \lambda_M}{\arg\max} \quad \mathbb{E}_{q(\theta;\psi)} \left[ \sum_{i=1}^M \mathbb{E}_{q(\phi_i;\lambda_i)}[\log p(D_i|\phi_i)] - \text{KL}(q(\phi_i;\lambda_i) \Vert  p(\phi_i|\theta)) \right] - \text{KL}(q(\theta;\psi) \Vert  p(\theta)) \quad (1)
$$

수식 (1)은 세 부분으로 해석할 수 있습니다.
1.  $\mathbb{E}[\log p(D_i|\phi_i)]$: **재구성 항(Reconstruction Term)**. 데이터 $D_i$를 얼마나 잘 설명하는지를 나타냅니다. (이 값을 최대화)
2.  $\text{KL}(q(\phi_i) \Vert  p(\phi_i|\theta))$: **지역 정규화 항(Local Regularizer)**. 태스크별 사후분포 $q(\phi_i)$가 사전분포 $p(\phi_i|\theta)$에서 너무 멀어지지 않도록 규제합니다. (KL은 거리와 유사하므로 최소화, 즉 `-KL`은 최대화)
3.  $\text{KL}(q(\theta) \Vert  p(\theta))$: **전역 정규화 항(Global Regularizer)**. 전역 사후분포 $q(\theta)$가 하이퍼파라미터 $p(\theta)$에서 너무 멀어지지 않도록 규제합니다. (마찬가지로 `-KL`은 최대화)

일반적으로 최적화 문제는 손실 함수를 '최소화'하는 것으로 표현합니다. 따라서 `argmax F(x)`는 `argmin -F(x)`와 같습니다. 수식 (1)의 모든 항에 음수 부호를 붙여 최소화 문제로 바꾸면 **수식 (2)**가 됩니다.

$$
\underset{\psi, \lambda_1, ..., \lambda_M}{\arg\min} \quad \mathbb{E}_{q(\theta;\psi)} \left[ \sum_{i=1}^M -\mathbb{E}_{q(\phi_i;\lambda_i)}[\log p(D_i|\phi_i)] + \text{KL}(q(\phi_i;\lambda_i) \Vert  p(\phi_i|\theta)) \right] + \text{KL}(q(\theta;\psi) \Vert  p(\theta)) \quad (2)
$$

이것이 바로 경사 하강법을 통해 우리가 실제로 최적화할 최종 손실 함수입니다.




----


### 1. `p(D, Z)` 확장하기: 확률의 연쇄 법칙 (Chain Rule of Probability)

먼저 $p(D, Z)$가 어떻게 확장되는지부터 살펴보겠습니다. 이것은 확률의 기본 법칙인 연쇄 법칙을 적용한 것입니다.

*   **Z란 무엇인가?**: $Z = \{\theta, \phi_1, ..., \phi_M\}$ 는 모델에 있는 모든 모르는(잠재) 변수들의 집합입니다.
*   **D란 무엇인가?**: $D = \{D_1, ..., D_M\}$ 는 우리가 관찰한 모든 데이터의 집합입니다.

결합 확률(joint probability) $p(D, Z)$는 "데이터 $D$와 잠재 변수 $Z$가 동시에 나타날 확률"을 의미합니다. 이를 연쇄 법칙에 따라 분해하면 다음과 같습니다.

$$ p(D, Z) = p(D | Z) \cdot p(Z) $$

이제 각 부분을 우리 모델의 계층 구조(논문의 그림 1a)에 맞게 더 분해해 보겠습니다.

1.  **$p(Z)$ 분해하기**:
    *   $Z = \{\theta, \phi_1, ..., \phi_M\}$ 의 결합 확률은 $p(\theta, \phi_1, ..., \phi_M)$ 입니다.
    *   계층 모델의 가정에 따라, $\phi_i$들은 $\theta$가 주어졌을 때 서로 조건부 독립(conditionally independent)입니다. 즉, $\theta$ 값을 알면 $\phi_1$이 무엇인지는 $\phi_2$에 영향을 주지 않습니다. 또한, $\phi_i$의 생성은 오직 $\theta$에만 의존합니다.
    *   따라서 다음과 같이 분해할 수 있습니다.

$$ p(Z) = p(\theta) \cdot p(\phi_1, ..., \phi_M | \theta) = p(\theta) \cdot \prod_{i=1}^{M} p(\phi_i | \theta) $$

2.  **$p(D | Z)$ 분해하기**:
    *   $p(D | Z) = p(D_1, ..., D_M | \theta, \phi_1, ..., \phi_M)$ 입니다.
    *   모델 구조상, 데이터 $D_i$의 생성은 오직 해당 태스크의 파라미터인 $\phi_i$에만 의존합니다. $\phi_i$ 값을 알면, 다른 $\phi_j$나 전역 파라미터 $\theta$는 $D_i$에 영향을 주지 않습니다.
    *   따라서 다음과 같이 분해할 수 있습니다.

$$ p(D|Z) = \prod_{i=1}^{M} p(D_i | \phi_i) $$

3.  **최종 결합**: 위 1, 2번 결과를 모두 합치면 $p(D, Z)$에 대한 최종 분해식이 나옵니다.

$$ p(D, Z) = \left( \prod_{i=1}^{M} p(D_i | \phi_i) \right) \cdot \left( p(\theta) \cdot \prod_{i=1}^{M} p(\phi_i | \theta) \right) $$

이를 정리하면 4번 과정의 첫 번째 줄 식이 완성됩니다.

$$ p(D, Z) = p(\theta) \prod_{i=1}^{M} p(D_i | \phi_i) p(\phi_i | \theta) $$

---

### 2. `q(Z)` 확장하기와 평균장 가정 (Mean-Field Assumption)

이제 $q(Z)$를 분해할 차례입니다. 여기서 바로 **평균장 가정**이 등장합니다.

*   **문제**: 진짜 사후분포 $p(Z|D)$에서는 잠재 변수들($\theta, \phi_1, ..., \phi_M$) 사이에 복잡한 상관관계가 존재할 수 있습니다. 예를 들어, 데이터를 관찰하고 나니 '$\theta$가 특정 값일 때 $\phi_1$은 다른 값일 가능성이 높다'와 같은 의존성이 생길 수 있습니다. 이 복잡한 의존성을 모두 모델링하는 것은 매우 어렵습니다.

*   **해결책 (평균장 가정)**: **"어려우니, 그냥 모든 잠재 변수들이 근사 분포 `q`에서는 서로 독립이라고 가정하자!"** 이것이 바로 평균장 가정입니다. 즉, 근사 사후분포 $q(Z)$에서 각 잠재 변수 그룹이 서로 완전히 분리되어 상호작용하지 않는다고 단순화하는 것입니다.

*   **수식으로 표현**:
    *   $Z = \{\theta, \phi_1, ..., \phi_M\}$ 입니다.
    *   이 변수들이 모두 독립이라고 가정하면, 결합 확률 $q(Z)$는 각 변수의 확률의 곱으로 나타낼 수 있습니다.

$$ q(Z) = q(\theta, \phi_1, ..., \phi_M) $$

평균장 가정을 적용하면,

$$ q(Z) \approx q(\theta) \cdot q(\phi_1) \cdot q(\phi_2) \cdot ... \cdot q(\phi_M) = q(\theta) \prod_{i=1}^{M} q(\phi_i) $$

이것이 4번 과정의 두 번째 줄 식입니다.

*   **왜 '평균장'인가?**: 이 용어는 물리학(통계 역학)에서 유래했습니다. 복잡한 상호작용을 하는 수많은 입자들의 시스템을 분석할 때, 특정 입자 하나에 초점을 맞추고, 그 입자에 영향을 미치는 주변의 다른 모든 입자들의 복잡한 상호작용을 무시하는 대신, 그들의 **'평균적인(mean)' 영향력(field)**만을 고려하여 문제를 단순화하는 기법을 '평균장 이론'이라고 합니다. 변분 추론에서 잠재 변수들이 서로 독립이라고 가정하는 것이 이와 유사한 아이디어이기 때문에 '평균장 가정'이라는 이름이 붙었습니다.

### 4번 과정 종합

이제 4번 과정의 전체 수식을 다시 보면 이해가 되실 겁니다.

$$ \ge \mathbb{E}_{q(\theta)\prod q(\phi_i)} \left[ \log \frac{p(\theta) \prod_{i=1}^M p(D_i|\phi_i)p(\phi_i|\theta)}{q(\theta)\prod_{i=1}^M q(\phi_i)} \right] $$

*   **기댓값 아래의 $q(\theta)\prod q(\phi_i)$**: 기댓값을 계산할 확률 분포가 바로 우리가 **평균장 가정**을 통해 단순화한 근사 분포 $q(Z)$임을 의미합니다.
*   **분자 $p(\theta) \prod ...$**: **확률의 연쇄 법칙**을 이용해 우리 모델의 구조에 맞게 $p(D,Z)$를 확장한 결과입니다.
*   **분모 $q(\theta)\prod ...$**: **평균장 가정**을 통해 $q(Z)$를 단순화한 결과입니다.

결론적으로, 4번 과정은 ELBO를 유도하기 위해 기댓값 내부의 복잡한 확률 분포들을 **(1) 모델의 구조적 가정**과 **(2) 계산의 편의를 위한 단순화 가정(평균장 가정)**을 사용해 구체적인 형태로 풀어 쓴 단계입니다.


----

5번에서 6번으로 넘어가는 과정. 이 과정은 기댓값의 선형성(linearity of expectation)과 KL 발산의 정의를 이용.

### 시작: 5번 수식

5번 수식은 기댓값 안에 여러 항의 합이 있는 형태입니다.

$$
\mathbb{E}_{q(\theta)\prod_{j=1}^M q(\phi_j)} \left[ \sum_{i=1}^M \log p(D_i|\phi_i) + \sum_{i=1}^M \log \frac{p(\phi_i|\theta)}{q(\phi_i; \lambda_i)} + \log \frac{p(\theta)}{q(\theta; \psi)} \right]
$$

(혼동을 피하기 위해 기댓값 아래의 곱셈 인덱스를 `j`로, 썸네이션 인덱스를 `i`로 표기했습니다. 본질은 같습니다.)

### 1단계: 기댓값의 선형성 적용

기댓값의 중요한 성질 중 하나는 **선형성**입니다. 즉, $\mathbb{E}[A + B] = \mathbb{E}[A] + \mathbb{E}[B]$가 성립합니다. 이 성질을 이용해 기댓값 안의 세 덩어리를 각각 분리할 수 있습니다.

**[덩어리 1]**

$$ \mathbb{E}_{q(\theta)\prod q(\phi_j)} \left[ \sum_{i=1}^M \log p(D_i|\phi_i) \right] $$

**[덩어리 2]**

$$ \mathbb{E}_{q(\theta)\prod q(\phi_j)} \left[ \sum_{i=1}^M \log \frac{p(\phi_i|\theta)}{q(\phi_i; \lambda_i)} \right] $$

**[덩어리 3]**

$$ \mathbb{E}_{q(\theta)\prod q(\phi_j)} \left[ \log \frac{p(\theta)}{q(\theta; \psi)} \right] $$

이제 각 덩어리를 하나씩 자세히 살펴보겠습니다.

---

### 2단계: 각 덩어리 정리하기

#### [덩어리 3] 분석 (가장 간단한 항)

$$ \mathbb{E}_{q(\theta)\prod q(\phi_j)} \left[ \log \frac{p(\theta)}{q(\theta; \psi)} \right] $$

이 기댓값은 $q(\theta)$와 모든 $q(\phi_j)$에 대해 계산됩니다. 하지만 기댓값 안의 표현식 $\log \frac{p(\theta)}{q(\theta; \psi)}$은 오직 $\theta$에만 의존하고, $\phi_j$와는 아무런 관련이 없습니다.

따라서, $\phi_j$에 대한 기댓값은 아무런 영향을 주지 않습니다 (마치 $\mathbb{E}_{Y}[f(X)] = f(X)$ 와 같습니다). 결국 이 항은 $q(\theta)$에 대한 기댓값만 남게 됩니다.

$$ = \mathbb{E}_{q(\theta)} \left[ \log \frac{p(\theta)}{q(\theta; \psi)} \right] $$

이제 KL 발산의 정의를 봅시다: $\text{KL}(q \Vert  p) = \mathbb{E}_q \left[ \log \frac{q}{p} \right] = -\mathbb{E}_q \left[ \log \frac{p}{q} \right]$
따라서 위 식은 다음과 같이 정리됩니다.

$$ = - \text{KL}(q(\theta; \psi) \Vert  p(\theta)) $$

이것으로 6번 수식의 마지막 항이 유도되었습니다.

---

#### [덩어리 1] 분석 (재구성 항)

$$ \mathbb{E}_{q(\theta)\prod q(\phi_j)} \left[ \sum_{i=1}^M \log p(D_i|\phi_i) \right] $$

기댓값과 썸네이션의 순서를 바꿀 수 있습니다 ($\mathbb{E}[\sum X_i] = \sum \mathbb{E}[X_i]$).

$$ = \sum_{i=1}^M \mathbb{E}_{q(\theta)\prod q(\phi_j)} \left[ \log p(D_i|\phi_i) \right] $$

이제 썸네이션 안의 기댓값을 봅시다. 기댓값 안의 표현식 $\log p(D_i|\phi_i)$는 오직 $\phi_i$ 하나에만 의존합니다. $\theta$나 다른 $\phi_j$ (단, $j \neq i$)와는 관련이 없습니다.

따라서, $\theta$와 다른 $\phi_j$에 대한 기댓값은 아무런 영향을 미치지 않고, 오직 $q(\phi_i)$에 대한 기댓값만 남습니다.

$$ = \sum_{i=1}^M \mathbb{E}_{q(\phi_i;\lambda_i)} [\log p(D_i|\phi_i)] $$

여기서 한 단계 더 나아가봅시다. $\lambda_i$는 $i$번째 태스크에만 해당하므로 괜찮지만, 논문의 최종 ELBO 형태를 보면 이 항도 $q(\theta)$에 대한 기댓값 안에 포함되어 있습니다. 이것은 논문의 최종 목표 함수가 $\theta$에 대한 기댓값으로 전체를 묶고 있기 때문입니다. 하지만 $\log p(D_i|\phi_i)$ 항은 $\theta$와 직접적인 관련이 없습니다. 왜 이런 표현이 나올까요?

사실, 엄밀히 말하면 $\lambda_i$ 자체가 $\theta$에 의존하는 모델 구조(Amortized VI)를 나중에 도입하기 때문에, 최종적으로는 $\theta$에 대한 의존성이 생깁니다. 하지만 현재 단계의 순수 계층 모델에서는 의존성이 없습니다. **이 부분에서 수식 유도 과정이 약간의 비약을 포함하고 있는 것으로 보입니다.**

일단 순수한 계층 모델로만 보면, $q(\theta)$와 독립인 것처럼 보입니다.
하지만 논문의 최종 형태에 맞추기 위해, "어차피 모든 항이 나중에는 $\theta$에 대한 기댓값으로 묶일 것이다"라고 생각하고, 억지로 $q(\theta)$에 대한 기댓값을 씌워 표현할 수 있습니다. (엄밀한 수학적 과정이라기 보단, 최종 목표식을 향한 정리 과정으로 이해하는 것이 좋습니다)

$$ = \sum_{i=1}^M \mathbb{E}_{q(\theta;\psi)} \left[ \mathbb{E}_{q(\phi_i;\lambda_i)} [\log p(D_i|\phi_i)] \right] $$

이것이 6번 수식의 첫 번째 항이 됩니다.

---

#### [덩어리 2] 분석 (지역 정규화 항)

$$ \mathbb{E}_{q(\theta)\prod q(\phi_j)} \left[ \sum_{i=1}^M \log \frac{p(\phi_i|\theta)}{q(\phi_i; \lambda_i)} \right] $$

마찬가지로 기댓값과 썸네이션 순서를 바꿉니다.

$$ = \sum_{i=1}^M \mathbb{E}_{q(\theta)\prod q(\phi_j)} \left[ \log \frac{p(\phi_i|\theta)}{q(\phi_i; \lambda_i)} \right] $$

썸네이션 안의 기댓값을 봅시다. 기댓값 안의 표현식 $\log \frac{p(\phi_i|\theta)}{q(\phi_i; \lambda_i)}$은 $\theta$와 $\phi_i$에 의존합니다. 다른 $\phi_j$ ($j \neq i$)와는 관련이 없습니다.

따라서 다른 $\phi_j$에 대한 기댓값은 사라지고, $q(\theta)$와 $q(\phi_i)$에 대한 기댓값만 남습니다.

$$ = \sum_{i=1}^M \mathbb{E}_{q(\theta)q(\phi_i)} \left[ \log \frac{p(\phi_i|\theta)}{q(\phi_i; \lambda_i)} \right] $$

기댓값을 분리해서 쓸 수 있습니다.

$$ = \sum_{i=1}^M \mathbb{E}_{q(\theta;\psi)} \left[ \mathbb{E}_{q(\phi_i;\lambda_i)} \left[ \log \frac{p(\phi_i|\theta)}{q(\phi_i; \lambda_i)} \right] \right] $$

안쪽 기댓값 $\mathbb{E}_{q(\phi_i;\lambda_i)} [ \dots ]$를 잘 보면, 특정 $\theta$ 값이 **고정되어 있을 때**의 KL 발산 형태와 매우 유사합니다.

$\mathbb{E}_{q(\phi_i)} [ \log \frac{p(\phi_i|\theta)}{q(\phi_i)} ]$는 $q(\phi_i)$와 $p(\phi_i|\theta)$ 사이의 `-KL 발산`입니다.

$$ = \sum_{i=1}^M \mathbb{E}_{q(\theta;\psi)} \left[ - \text{KL}(q(\phi_i;\lambda_i) \Vert  p(\phi_i|\theta)) \right] $$

기댓값 밖으로 음수 부호를 빼내면,

$$ = - \sum_{i=1}^M \mathbb{E}_{q(\theta;\psi)} \left[ \text{KL}(q(\phi_i;\lambda_i) \Vert  p(\phi_i|\theta)) \right] $$

이것이 6번 수식의 두 번째 항이 됩니다.

---

### 최종 결합

위에서 유도한 3개의 덩어리를 모두 합치면 다음과 같습니다.

$$ \text{[덩어리 1]} + \text{[덩어리 2]} + \text{[덩어리 3]} $$

$$ = \sum_{i=1}^M \mathbb{E}_{q(\theta;\psi)} \left[ \mathbb{E}_{q(\phi_i;\lambda_i)}[\log p(D_i|\phi_i)] \right] - \sum_{i=1}^M \mathbb{E}_{q(\theta;\psi)} \left[ \text{KL}(q(\phi_i;\lambda_i) \Vert  p(\phi_i|\theta)) \right] - \text{KL}(q(\theta;\psi) \Vert  p(\theta)) $$

이제 첫 번째와 두 번째 항을 $q(\theta)$에 대한 기댓값으로 묶고, $\sum$ 기호도 기댓값 안으로 넣으면 논문의 최종 ELBO 형태와 일치하게 됩니다.

$$ \mathcal{L} = \mathbb{E}_{q(\theta;\psi)} \left[ \sum_{i=1}^M \left( \mathbb{E}_{q(\phi_i;\lambda_i)}[\log p(D_i|\phi_i)] - \text{KL}(q(\phi_i;\lambda_i) \Vert  p(\phi_i|\theta)) \right) \right] - \text{KL}(q(\theta;\psi) \Vert  p(\theta)) $$

이렇게 5번에서 6번으로의 전개가 완료됩니다. 핵심은 **기댓값의 선형성**과 **관련 없는 변수에 대한 기댓값은 사라진다**는 점, 그리고 **KL 발산의 정의**를 정확히 적용하는 것입니다.
