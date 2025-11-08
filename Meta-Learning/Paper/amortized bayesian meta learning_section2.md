논문의 2장 "META-LEARNING VIA HIERARCHICAL VARIATIONAL INFERENCE"의 수식 전개

---

### 2장 : 계층적 변분 추론을 통한 메타-러닝

이 장의 목표는 베이지안 메타-러닝을 위한 수학적 프레임워크를 정립하는 것입니다. 
- 핵심 아이디어는 여러 개의 태스크(에피소드)에서 얻은 데이터를 사용하여, 태스크 전반에 걸친 공유 지식(global latent variable $\theta$)과 각 태스크에 특화된 지식(local latent variables $\phi_i$)을 동시에 추론하는 것입니다.

#### 1. 기본 설정 및 목표

먼저 용어를 정리하고 최종 목표를 설정하겠습니다.

*   데이터: 총 $M$개의 에피소드(태스크)가 있습니다. $i$번째 에피소드는 데이터셋 $D_i = \{(x_{i,j}, y_{i,j})\}_{j=1}^{N}$를 가집니다.
*   계층적 모델 (Hierarchical Model):
    *   $\theta$: 전역 잠재 변수(global latent variable). 모든 에피소드에 걸쳐 공유되는 지식(예: 좋은 특징을 추출하는 신경망 가중치의 사전 분포)을 나타냅니다. 파라미터 $\psi$를 갖는 근사 분포 $q(\theta; \psi)$로 추정됩니다.
    *   $\phi_i$: 지역 잠재 변수(local latent variable). $i$번째 에피소드에만 특화된 지식(예: 해당 태스크를 풀기 위해 미세 조정된 신경망 가중치)을 나타냅니다. 파라미터 $\lambda_i$를 갖는 근사 분포 $q(\phi_i; \lambda_i)$로 추정됩니다.
*   생성 과정 (Generative Process): 데이터가 생성되는 순서는 다음과 같습니다.
    1.  전역 지식 $\theta$가 사전분포 $p(\theta)$에서 샘플링됩니다.
    2.  각 에피소드 $i$에 대해, 지역 지식 $\phi_i$가 $\theta$에 의존하는 사전분포 $p(\phi_i|\theta)$에서 샘플링됩니다.
    3.  각 에피소드 $i$의 데이터 $D_i$는 해당 지역 지식 $\phi_i$를 조건으로 하는 $p(D_i|\phi_i)$로부터 생성됩니다.

*   최종 목표: 모든 관측된 데이터 $D_1, ..., D_M$의 로그 증거(log evidence) 또는 주변 로그 우도(marginal log likelihood)를 최대화하는 것입니다. 각 에피소드가 독립이라고 가정하면, 목표는 다음과 같습니다.

$$
\log p(D_1, \dots, D_M) = \log \prod_{i=1}^{M} p(D_i) = \sum_{i=1}^{M} \log p(D_i)
$$

여기서 $p(D_i)$는 잠재 변수 $\theta, \phi_i$에 대해 주변화(marginalize)하여 계산해야 합니다.

$$
p(D_i) = \int \int p(D_i|\phi_i) p(\phi_i|\theta) p(\theta) d\phi_i d\theta
$$

이 적분은 신경망과 같은 복잡한 모델에서는 계산이 불가능(intractable)합니다. 따라서 우리는 변분 추론(Variational Inference)을 사용하여 이 값의 하한(lower bound), 즉 증거 하한(Evidence Lower Bound, ELBO)을 구하고 이를 대신 최대화합니다.

#### 2. 증거 하한(ELBO) 유도 과정 (논문 수식 풀이)

이제 논문의 첫 번째 수식부터 마지막 `L` 수식까지 단계별로 유도해 보겠습니다.

[시작] 목표인 로그 증거
($\log p(D_1, \dots, D_M)$)부터 시작하겠습니다. 모든 태스크 데이터가 주어졌을 때의 로그 우도입니다.

$$
\log p(D_1, \dots, D_M) = \log \int p(D_1, \dots, D_M, \theta) d\theta = \log \int p(\theta) \prod_{i=1}^{M} p(D_i|\theta) d\theta
$$

여기서 $p(D_i|\theta) = \int p(D_i|\phi_i) p(\phi_i|\theta) d\phi_i$ 이므로, 전체 식은 다음과 같습니다.

$$
\log \left[ \int p(\theta) \left( \prod_{i=1}^{M} \int p(D_i|\phi_i) p(\phi_i|\theta) d\phi_i \right) d\theta \right]
$$

이것이 논문의 첫 수식 `log[∫ p(θ) [∏ ∫...dφ_i] dθ]`와 동일합니다.

---
[1단계] 첫 번째 변분 추론 근사: 전역 변수 $\theta$에 대한 ELBO

먼저 바깥쪽 적분(dθ)을 처리합니다. 근사 사후분포 $q(\theta; \psi)$를 도입하고, 적분 안의 항에 $q(\theta; \psi) / q(\theta; \psi)$를 곱해줍니다.

$$
\log \left[ \int q(\theta; \psi) \frac{p(\theta) \prod_{i=1}^{M} p(D_i|\theta)}{q(\theta; \psi)} d\theta \right]
$$

이 식은 $q(\theta; \psi)$에 대한 기댓값(Expectation) 형태로 볼 수 있습니다.

$$
\log \mathbb{E}_{q(\theta; \psi)} \left[ \frac{p(\theta) \prod_{i=1}^{M} p(D_i|\theta)}{q(\theta; \psi)} \right]
$$

이제 옌센 부등식(Jensen's Inequality)을 적용합니다. 볼록 함수(convex function) $f(x)$에 대해 $\mathbb{E}[f(X)] \ge f(\mathbb{E}[X])$가 성립하며, 오목 함수(concave function)인 로그 함수에 대해서는 $\log(\mathbb{E}[X]) \ge \mathbb{E}[\log(X)]$가 성립합니다.

$$
\begin{aligned}
\log \mathbb{E}_{q(\theta; \psi)} \left[ \dots \right] &\ge \mathbb{E}_{q(\theta; \psi)} \left[ \log \left( \frac{p(\theta) \prod_{i=1}^{M} p(D_i|\theta)}{q(\theta; \psi)} \right) \right] \\
&= \mathbb{E}_{q(\theta; \psi)} \left[ \log p(\theta) + \sum_{i=1}^{M} \log p(D_i|\theta) - \log q(\theta; \psi) \right] \\
&= \mathbb{E}_{q(\theta; \psi)} \left[ \sum_{i=1}^{M} \log p(D_i|\theta) \right] + \mathbb{E}_{q(\theta; \psi)} \left[ \log \frac{p(\theta)}{q(\theta; \psi)} \right] \\
&= \mathbb{E}_{q(\theta; \psi)} \left[ \sum_{i=1}^{M} \log \left( \int p(D_i|\phi_i)p(\phi_i|\theta) d\phi_i \right) \right] - \text{KL}(q(\theta; \psi) \Vert  p(\theta))
\end{aligned}
$$

마지막 항은 쿨백-라이블러 발산(KL Divergence)의 정의에 따라 정리되었습니다. $KL(q \Vert p)$ = $\int q(x) \log \frac{q(x)}{p(x)} dx = -\mathbb{E}_q[\log \frac{p(x)}{q(x)}]$. 이것이 논문의 두 번째 줄 `≥ E_q(θ;ψ)[...] - KL(...)`에 해당합니다.

---
[2단계] 두 번째 변분 추론 근사: 지역 변수 $\phi_i$에 대한 ELBO

이제 위에서 얻은 하한의 첫 번째 항 내부를 다시 한 번 변분 추론으로 근사합니다. 각 에피소드 $i$에 대해 근사 사후분포 $q(\phi_i; \lambda_i)$를 도입합니다.

$$
\log \left( \int p(D_i|\phi_i)p(\phi_i|\theta) d\phi_i \right)
$$

여기에 $q(\phi_i; \lambda_i) / q(\phi_i; \lambda_i)$를 곱해주고 옌센 부등식을 똑같이 적용합니다.

$$
\begin{aligned}
\log \left( \int q(\phi_i; \lambda_i) \frac{p(D_i|\phi_i)p(\phi_i|\theta)}{q(\phi_i; \lambda_i)} d\phi_i \right) &\ge \mathbb{E}_{q(\phi_i; \lambda_i)} \left[ \log \frac{p(D_i|\phi_i)p(\phi_i|\theta)}{q(\phi_i; \lambda_i)} \right] \\
&= \mathbb{E}_{q(\phi_i; \lambda_i)} [\log p(D_i|\phi_i)] + \mathbb{E}_{q(\phi_i; \lambda_i)} \left[ \log \frac{p(\phi_i|\theta)}{q(\phi_i; \lambda_i)} \right] \\
&= \mathbb{E}_{q(\phi_i; \lambda_i)} [\log p(D_i|\phi_i)] - \text{KL}(q(\phi_i; \lambda_i) \Vert  p(\phi_i|\theta))
\end{aligned}
$$

---
[3단계] 전체 ELBO 결합

이제 2단계에서 얻은 하한을 1단계의 결과에 대입합니다. 1단계의 하한은 다음과 같았습니다.

$$
\mathbb{E}_{q(\theta; \psi)} \left[ \sum_{i=1}^{M} \underbrace{\log \left( \int p(D_i|\phi_i)p(\phi_i|\theta) d\phi_i \right)}_{\text{이 부분을 대체}} \right] - \text{KL}(q(\theta; \psi) \Vert  p(\theta))
$$

대입하면,

$$
\ge \mathbb{E}_{q(\theta; \psi)} \left[ \sum_{i=1}^{M} \left( \mathbb{E}_{q(\phi_i; \lambda_i)} [\log p(D_i|\phi_i)] - \text{KL}(q(\phi_i; \lambda_i) \Vert  p(\phi_i|\theta)) \right) \right] - \text{KL}(q(\theta; \psi) \Vert  p(\theta))
$$

기댓값의 선형성(Linearity of Expectation)에 따라 정리하면,

$$
\ge \sum_{i=1}^{M} \mathbb{E}_{q(\theta; \psi)} \left[ \mathbb{E}_{q(\phi_i; \lambda_i)} [\log p(D_i|\phi_i)] - \text{KL}(q(\phi_i; \lambda_i) \Vert  p(\phi_i|\theta)) \right] - \text{KL}(q(\theta; \psi) \Vert  p(\theta))
$$

논문에서는 표기를 간결하게 하기 위해 기댓값을 합쳐서 표현했습니다. 최종적으로 논문에서 정의한 증거 하한(ELBO)인 $\mathcal{L}(\psi, \lambda_1, \dots, \lambda_M)$는 다음과 같습니다.

$$
\mathcal{L}(\psi, \lambda_1, \dots, \lambda_M) = \mathbb{E}_{q(\theta; \psi)} \left[ \sum_{i=1}^{M} \mathbb{E}_{q(\phi_i; \lambda_i)} [\log p(D_i|\phi_i)] - \text{KL}(q(\phi_i; \lambda_i) \Vert  p(\phi_i|\theta)) \right] - \text{KL}(q(\theta; \psi) \Vert  p(\theta))
$$

이것이 논문의 세 번째 `≥` 부등호 뒤의 식과 최종 `L`의 정의와 일치합니다.

#### 3. 최적화 문제 (Optimization Problem)

변분 추론의 목표는 ELBO를 최대화하여, 하한을 실제 로그 증거 값에 최대한 가깝게 만드는 것입니다. 따라서 최적화 문제는 다음과 같습니다.

수식 (1): ELBO 최대화

$$
\underset{\psi, \lambda_1, \dots, \lambda_M}{\arg\max} \quad \mathcal{L}(\psi, \lambda_1, \dots, \lambda_M)
$$

$$
\underset{\psi, \lambda_1, \dots, \lambda_M}{\arg\max} \quad \mathbb{E}_{q(\theta; \psi)} \left[ \sum_{i=1}^{M} \mathbb{E}_{q(\phi_i; \lambda_i)} [\log p(D_i|\phi_i)] - \text{KL}(q(\phi_i; \lambda_i) \Vert  p(\phi_i|\theta)) \right] - \text{KL}(q(\theta; \psi) \Vert  p(\theta))
$$

각 항의 의미를 해석하면 다음과 같습니다.
*   $\mathbb{E}_{q(\phi_i; \lambda_i)} [\log p(D_i|\phi_i)]$: 재구성 항(Reconstruction Term). $i$번째 태스크에 대한 근사 사후분포 $q(\phi_i; \lambda_i)$에서 샘플링된 파라미터 $\phi_i$가 데이터 $D_i$를 얼마나 잘 설명하는지를 나타냅니다. 이 항을 최대화해야 합니다.
*   $-\text{KL}(q(\phi_i; \lambda_i) \Vert  p(\phi_i|\theta))$: 지역 정규화 항(Local Regularization Term). 지역 사후분포 $q(\phi_i)$가 전역 지식 $\theta$로부터 파생된 사전분포 $p(\phi_i|\theta)$에서 너무 멀어지지 않도록 규제합니다. KL 발산을 최소화(즉, -KL을 최대화)해야 합니다.
*   $-\text{KL}(q(\theta; \psi) \Vert  p(\theta))$: 전역 정규화 항(Global Regularization Term). 전역 사후분포 $q(\theta)$가 초기 사전분포 $p(\theta)$에서 너무 멀어지지 않도록 규제합니다.

수식 (2): 음의 ELBO 최소화

일반적으로 최적화기는 손실 함수를 최소화하는 데 사용되므로, 위 최대화 문제를 음수 부호를 붙여 최소화 문제로 변환할 수 있습니다.

$$
\underset{\psi, \lambda_1, \dots, \lambda_M}{\arg\min} \quad -\mathcal{L}(\psi, \lambda_1, \dots, \lambda_M)
$$

$$
\underset{\psi, \lambda_1, \dots, \lambda_M}{\arg\min} \quad \mathbb{E}_{q(\theta; \psi)} \left[ \sum_{i=1}^{M} \left( -\mathbb{E}_{q(\phi_i; \lambda_i)} [\log p(D_i|\phi_i)] + \text{KL}(q(\phi_i; \lambda_i) \Vert  p(\phi_i|\theta)) \right) \right] + \text{KL}(q(\theta; \psi) \Vert  p(\theta))
$$

이것이 수식 (2)와 정확히 일치합니다. 이제 각 항은 손실(Loss)의 관점에서 해석할 수 있습니다.
*   $-\mathbb{E}_{q(\phi_i; \lambda_i)} [\log p(D_i|\phi_i)]$: 음의 로그 우도(Negative Log-Likelihood). 일반적인 지도 학습의 손실 함수와 같습니다.
*   $\text{KL}(...)$: KL 패널티 항. 근사 사후분포가 사전분포로부터 멀어지는 것에 대한 페널티입니다.

이로써 2장의 모든 수식에 대한 상세한 유도와 설명이 마무리되었습니다. 이 장은 변분 추론을 이용한 베이지안 메타-러닝의 이론적 토대를 마련하는 부분이며, 이후 3장에서는 이 최적화 문제를 어떻게 확장 가능하게(scalable) 풀 것인지에 대한 구체적인 방법을 제시합니다.
