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

[시작] 목표인 로그 증거 $\log p(D _1,  \dots, D _M)$
부터 시작하겠습니다. 모든 태스크 데이터가 주어졌을 때의 로그 우도입니다.

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


---

일반적인 변분 추론(Variational Inference, VI)과 이 논문에서 사용된 계층적 변분 추론(Hierarchical Variational Inference)은 뭐가 다른가?

### **비교의 핵심: 모델의 구조와 추론의 목표**

가장 큰 차이점은 **추론하고자 하는 확률 모델의 구조**와 **추론의 목표**에 있습니다. 일반 VI는 단일 데이터셋에 대한 단일 잠재 변수를 다루는 반면, 계층적 VI는 여러 관련 그룹(태스크)에 걸쳐 공유되는 구조를 가진 잠-재 변수들을 다룹니다.

---

### **1. 일반 변분 추론 (Standard Variational Inference)**

#### **상황 (Scenario)**

*   하나의 데이터셋 $\mathcal{D} = \{x_1, \dots, x_N\}$가 주어집니다.
*   이 데이터를 설명하는 잠재 변수(latent variable) $\mathbf{z}$가 있습니다. 예를 들어, $\mathbf{z}$는 신경망의 모든 가중치(weights)가 될 수 있습니다.
*   우리는 데이터 $\mathcal{D}$가 주어졌을 때의 잠재 변수 $\mathbf{z}$의 사후분포(posterior) $p(\mathbf{z}|\mathcal{D})$를 알고 싶습니다.

#### **문제점 (Problem)**

베이즈 정리에 따라 사후분포는 다음과 같습니다.

$$ p(\mathbf{z}|\mathcal{D}) = \frac{p(\mathcal{D}|\mathbf{z}) p(\mathbf{z})}{p(\mathcal{D})} = \frac{p(\mathcal{D}|\mathbf{z}) p(\mathbf{z})}{\int p(\mathcal{D}|\mathbf{z}) p(\mathbf{z}) d\mathbf{z}} $$

여기서 분모에 있는 증거(evidence) $p(\mathcal{D})$의 적분 계산이 대부분의 경우 불가능(intractable)합니다.

#### **해결책 (Solution)**

*   다루기 쉬운 분포(예: 가우시안)인 **변분 분포(variational distribution) $q(\mathbf{z}; \lambda)$**를 도입하여 실제 사후분포 $p(\mathbf{z}|\mathcal{D})$를 근사합니다. 여기서 $\lambda$는 변분 파라미터입니다.

*   $q(\mathbf{z}; \lambda)$와 $p(\mathbf{z}|\mathcal{D})$ 사이의 **KL 발산(KL Divergence)을 최소화**하는 최적의 파라미터 $\lambda^*$를 찾습니다.

$$ \lambda^* = \underset{\lambda}{\arg\min} \quad \text{KL}(q(\mathbf{z}; \lambda) || p(\mathbf{z}|\mathcal{D})) $$

*   KL 발산을 직접 최소화하는 것은 $p(\mathbf{z}|\mathcal{D})$를 모르기 때문에 불가능합니다. 대신, 이와 동치인 **증거 하한(Evidence Lower Bound, ELBO)을 최대화**합니다.

$$ \mathcal{L}(\lambda) = \mathbb{E}_{q(\mathbf{z}; \lambda)}[\log p(\mathcal{D}|\mathbf{z})] - \text{KL}(q(\mathbf{z}; \lambda) || p(\mathbf{z})) $$

#### **그래프 모델 (Graphical Model)**
일반 VI의 모델 구조는 간단합니다.

```
   z (Latent Variable)
   |
   V
   x (Observed Data)
```

#### **요약 (Summary)**
*   **목표**: 단일 데이터셋에 대한 사후분포 $p(\mathbf{z}|\mathcal{D})$ 추론.
*   **구조**: 단일 계층 (잠재 변수 → 데이터).
*   **결과물**: 데이터셋 $\mathcal{D}$를 가장 잘 설명하는 **하나의** 근사 사후분포 $q(\mathbf{z}; \lambda^*)$.

---

### **2. 계층적 변분 추론 (Hierarchical Variational Inference) - 이 논문의 경우**

#### **상황 (Scenario)**

*   단일 데이터셋이 아니라, 서로 관련은 있지만 다른 **여러 개의 데이터셋(태스크)** $\mathcal{D}_1, \dots, \mathcal{D}_M$이 주어집니다. (예: 각 태스크는 다른 종류의 동물 이미지를 분류하는 문제)
*   **잠재 변수가 계층 구조**를 가집니다.
    *   **전역 잠재 변수 $\theta$**: 모든 태스크에 걸쳐 공유되는 정보. (예: 모든 동물 이미지 분류에 공통적으로 유용한 특징 추출기 가중치의 분포)
    *   **지역 잠재 변수 $\phi_i$**: 각 태스크 $\mathcal{D}_i$에만 특화된 정보. (예: $i$번째 동물 분류기를 위해 미세 조정된 가중치)
*   우리는 모든 태스크 데이터가 주어졌을 때의 전역 사후분포 $p(\theta|\mathcal{D}_1, \dots, \mathcal{D}_M)$와 각 태스크에 대한 지역 사후분포 $p(\phi_i|\mathcal{D}_i, \theta)$를 동시에 알고 싶습니다.

#### **문제점 (Problem)**
일반 VI보다 훨씬 더 복잡한 계층적 구조 때문에, 사후분포 $p(\theta, \phi_1, \dots, \phi_M | \mathcal{D}_1, \dots, \mathcal{D}_M)$를 계산하는 것은 더욱 어렵습니다.

#### **해결책 (Solution)**

*   계층 구조를 반영하여 **두 종류의 변분 분포**를 도입합니다.
    *   전역 변수 $\theta$를 근사하는 $q(\theta; \psi)$.
    *   각 지역 변수 $\phi_i$를 근사하는 $q(\phi_i; \lambda_i)$.
*   전체 데이터셋에 대한 **결합 증거 하한(Joint ELBO)을 최대화**합니다. 이 ELBO는 모든 변분 파라미터($\psi, \lambda_1, \dots, \lambda_M$)에 대해 최적화됩니다.

$$ \mathcal{L}(\psi, \{\lambda_i\}) = \mathbb{E}_{q(\theta;\psi)}\left[ \sum_{i=1}^M \mathbb{E}_{q(\phi_i;\lambda_i)}[\log p(\mathcal{D}_i|\phi_i)] - \text{KL}(q(\phi_i;\lambda_i)||p(\phi_i|\theta)) \right] - \text{KL}(q(\theta;\psi)||p(\theta)) $$

*   이 최적화 과정을 통해, **여러 태스크로부터 정보를 공유(information sharing)**하여 각 태스크를 더 잘 학습할 수 있습니다. 예를 들어, 데이터가 부족한 태스크 $\mathcal{D}_j$는 다른 태스크들로부터 학습된 강력한 전역 정보 $\theta$의 도움을 받아 더 나은 사후분포 $q(\phi_j)$를 추정할 수 있습니다.

#### **그래프 모델 (Graphical Model)**
계층적 모델은 여러 태스크가 전역 변수를 공유하는 구조를 가집니다. (논문의 Figure 1a 참조)
```
            θ (Global Variable)
           / | \
          /  |  \
         V   V   V
       φ_1 φ_2 ... φ_M (Local Variables)
        |   |       |
        V   V       V
       D_1 D_2 ... D_M (Observed Data)
```

#### **요약 (Summary)**
*   **목표**: 여러 관련 데이터셋(태스크)에 대한 계층적 사후분포 $p(\theta, \{\phi_i\} | \{\mathcal{D}_i\})$ 추론.
*   **구조**: 다중 계층 (전역 변수 → 지역 변수 → 데이터).
*   **결과물**:
    *   모든 태스크의 공통 정보를 담은 **하나의** 전역 근사 사후분포 $q(\theta; \psi^*)$.
    *   각 태스크에 특화된 **M개의** 지역 근사 사후분포 $q(\phi_i; \lambda_i^*)$.

---

### **핵심 차이점 표로 정리**

| 구분 | 일반 변분 추론 (Standard VI) | 계층적 변분 추론 (Hierarchical VI) |
| :--- | :--- | :--- |
| **적용 대상** | 단일 데이터셋 | 여러 개의 관련된 데이터셋 (태스크 그룹) |
| **모델 구조** | 단일 계층 | 다중 계층 (계층적) |
| **잠재 변수** | 단일 잠재 변수 $\mathbf{z}$ | 전역 변수 $\theta$와 다수의 지역 변수 $\phi_i$ |
| **추론 목표** | $p(\mathbf{z} \vert \mathcal{D})$ | $p(\theta, \{\phi_i\} \vert \{\mathcal{D}_i\})$ |
| **변분 분포** | $q(\mathbf{z})$ 하나 | $q(\theta)$와 다수의 $q(\phi_i)$ |
| **핵심 이점** | intractable한 사후분포의 근사 | **정보 공유 (Information Sharing)**를 통한 학습 효율 증대 |
| **메타-러닝**<br>**관점** | (해당 없음) | **전역 변수 $\theta$가 "학습하는 법"** 또는 "좋은 사전 지식"을 인코딩 |

이 논문에서 계층적 VI를 사용하는 이유는 메타-러닝의 본질, 즉 **"여러 태스크를 통해 얻은 경험으로 새로운 태스크를 더 빨리 배우는 것"**을 수학적으로 모델링하기에 완벽한 프레임워크이기 때문입니다. 전역 변수 $\theta$가 바로 여러 태스크에서 축적된 '경험' 또는 '사전 지식'의 역할을 수행합니다.
