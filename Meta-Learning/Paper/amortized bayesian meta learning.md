물론입니다. 페이지 2에 제시된 수식을 처음부터, 생략된 부분을 포함하여 상세하게 전개해 드리겠습니다.

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

$\text{KL}(q||p) = \mathbb{E}_q[\log \frac{q}{p}] = -\mathbb{E}_q[\log \frac{p}{q}]$

$$
= \sum_{i=1}^M \mathbb{E}_{q(\theta;\psi)} \left[ \mathbb{E}_{q(\phi_i;\lambda_i)}[\log p(D_i|\phi_i)] \right] - \sum_{i=1}^M \mathbb{E}_{q(\theta;\psi)} \left[ \text{KL}(q(\phi_i;\lambda_i) || p(\phi_i|\theta)) \right] - \text{KL}(q(\theta;\psi) || p(\theta))
$$

이 마지막 식이 바로 논문의 `\mathcal{L}(\psi, \lambda_1, ..., \lambda_M)`에 해당하는 **ELBO**입니다. 논문에서는 기댓값 순서를 조금 다르게 표현했을 뿐, 본질적으로 동일한 식입니다.

$$
\mathcal{L} = \mathbb{E}_{q(\theta;\psi)} \left[ \sum_{i=1}^M \mathbb{E}_{q(\phi_i;\lambda_i)}[\log p(D_i|\phi_i)] - \text{KL}(q(\phi_i;\lambda_i) || p(\phi_i|\theta)) \right] - \text{KL}(q(\theta;\psi) || p(\theta))
$$

### 3단계: 최적화 문제로의 전환 (수식 1, 2)

이제 우리의 목표는 이 ELBO($\mathcal{L}$)를 최대화하는 $\psi$와 $\lambda_i$를 찾는 것입니다. 이것이 바로 **수식 (1)** 입니다.

$$
\underset{\psi, \lambda_1, ..., \lambda_M}{\arg\max} \quad \mathbb{E}_{q(\theta;\psi)} \left[ \sum_{i=1}^M \mathbb{E}_{q(\phi_i;\lambda_i)}[\log p(D_i|\phi_i)] - \text{KL}(q(\phi_i;\lambda_i) || p(\phi_i|\theta)) \right] - \text{KL}(q(\theta;\psi) || p(\theta)) \quad (1)
$$

수식 (1)은 세 부분으로 해석할 수 있습니다.
1.  $\mathbb{E}[\log p(D_i|\phi_i)]$: **재구성 항(Reconstruction Term)**. 데이터 $D_i$를 얼마나 잘 설명하는지를 나타냅니다. (이 값을 최대화)
2.  $\text{KL}(q(\phi_i) || p(\phi_i|\theta))$: **지역 정규화 항(Local Regularizer)**. 태스크별 사후분포 $q(\phi_i)$가 사전분포 $p(\phi_i|\theta)$에서 너무 멀어지지 않도록 규제합니다. (KL은 거리와 유사하므로 최소화, 즉 `-KL`은 최대화)
3.  $\text{KL}(q(\theta) || p(\theta))$: **전역 정규화 항(Global Regularizer)**. 전역 사후분포 $q(\theta)$가 하이퍼파라미터 $p(\theta)$에서 너무 멀어지지 않도록 규제합니다. (마찬가지로 `-KL`은 최대화)

일반적으로 최적화 문제는 손실 함수를 '최소화'하는 것으로 표현합니다. 따라서 `argmax F(x)`는 `argmin -F(x)`와 같습니다. 수식 (1)의 모든 항에 음수 부호를 붙여 최소화 문제로 바꾸면 **수식 (2)**가 됩니다.

$$
\underset{\psi, \lambda_1, ..., \lambda_M}{\arg\min} \quad \mathbb{E}_{q(\theta;\psi)} \left[ \sum_{i=1}^M -\mathbb{E}_{q(\phi_i;\lambda_i)}[\log p(D_i|\phi_i)] + \text{KL}(q(\phi_i;\lambda_i) || p(\phi_i|\theta)) \right] + \text{KL}(q(\theta;\psi) || p(\theta)) \quad (2)
$$

이것이 바로 경사 하강법을 통해 우리가 실제로 최적화할 최종 손실 함수입니다.
