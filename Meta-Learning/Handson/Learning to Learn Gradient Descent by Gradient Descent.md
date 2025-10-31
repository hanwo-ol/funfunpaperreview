## Gradient Descent를 통한 Gradient Descent 학습 (Learning to Learn Gradient Descent by Gradient Descent)

본 자료는 표준적인 Gradient Descent 최적화 기법을 학습 가능한 모델(RNN)로 대체하고, 이 모델 자체를 다시 Gradient Descent로 학습시키는 Meta-Learning 기법에 대해 설명합니다.

---

### Part 1: 기본 개념 - Gradient Descent

Meta-Learning 모델을 이해하기에 앞서, 최적화의 기본이 되는 Gradient Descent의 작동 방식을 먼저 정의합니다.

#### 1.1. 용어 및 표기법 정의

*   **모델 (Model)**: $f$
*   **모델 파라미터 (Parameters)**: $\theta$
    *   모델 $f$의 동작을 결정하는 학습 가능한 변수들의 집합입니다.
*   **손실 함수 (Loss Function)**: $L(\theta)$
    *   모델의 예측이 실제 정답과 얼마나 차이 나는지를 측정하는 함수입니다. 이 함수의 값을 최소화하는 것이 학습의 목표입니다.
*   **학습률 (Learning Rate)**: $\alpha$
    *   파라미터를 업데이트할 때, 손실 함수의 기울기(gradient)를 얼마나 반영할지 결정하는 상수(hyperparameter)입니다.
*   **손실 함수의 기울기 (Gradient)**: $\nabla L(\theta)$
    *   손실 함수 $L$을 파라미터 $\theta$에 대해 편미분한 벡터입니다. 이 벡터는 손실 함수 값이 가장 가파르게 증가하는 방향을 가리킵니다.
*   **타임 스텝 (Time Step)**: $t$
    *   학습 과정에서의 반복(iteration) 단계를 나타냅니다.

#### 1.2. Gradient Descent 업데이트 공식

Gradient Descent는 손실 함수 $L(\theta)$의 값을 최소화하는 파라미터 $\theta$를 찾기 위해 다음의 업데이트 규칙을 반복적으로 적용합니다.

$$
\theta _{t+1} = \theta _t - \alpha \nabla L(\theta _t)
$$

#### 1.3. 공식의 연산 설명

*   $\theta _t$: 타임 스텝 $t$에서의 현재 모델 파라미터입니다.
*   $\nabla L(\theta _t)$: 현재 파라미터 $\theta _t$ 위치에서 계산된 손실 함수의 기울기입니다.
*   $\alpha \nabla L(\theta _t)$: 기울기 벡터 $\nabla L(\theta _t)$에 학습률 $\alpha$만큼 스케일을 조정한 값입니다. 이는 파라미터를 업데이트할 보폭(step size)과 방향을 결정합니다.
*   $\theta _t - \alpha \nabla L(\theta _t)$: 현재 파라미터 $\theta _t$에서, 손실 함수가 가장 가파르게 증가하는 방향($\nabla L(\theta _t)$)의 **반대 방향**으로 $\alpha$만큼 이동합니다. 이 연산을 통해 파라미터는 손실 값이 더 낮은 지점으로 이동하게 됩니다.
*   $\theta _{t+1}$: 위 연산을 통해 업데이트된, 다음 타임 스텝 $t+1$에서의 새로운 파라미터입니다.

이 과정을 손실 함수 값이 충분히 낮아질 때까지 반복하여 모델을 최적화합니다.

---

### Part 2: Gradient Descent를 통한 Gradient Descent 학습

이제 고정된 규칙($\theta _{t+1} = \theta _t - \alpha \nabla L(\theta _t)$)을 사용하는 대신, 이 업데이트 규칙 자체를 학습하는 모델을 설계합니다.

#### 2.1. 역할 정의

이 알고리즘은 두 개의 주체를 가집니다.

*   **Optimizee**: 최적화의 대상이 되는 기본 네트워크(Base Network). 우리가 최종적으로 학습시키고 싶은 모델입니다.
*   **Optimizer**: Optimizee의 파라미터를 어떻게 업데이트할지 학습하는 모델. 이 역할은 **Recurrent Neural Network(RNN)**가 수행합니다.

#### 2.2. 용어 및 표기법 정의

*   **Optimizee 모델**: $f$, 이 모델의 파라미터는 $\theta$입니다.
*   **Optimizer 모델**: $m$, 이 모델은 RNN이며, 파라미터는 $\phi$입니다.
*   **Optimizee의 손실 함수 기울기**: $\nabla _t = \nabla _{\theta _t} L(f(\theta _t))$
    *   타임 스텝 $t$에서 Optimizee의 파라미터 $\theta _t$에 대한 손실 함수의 기울기입니다.
*   **Optimizer(RNN)의 은닉 상태 (Hidden State)**: $h _t$
    *   타임 스텝 $t$까지의 과거 업데이트 정보를 요약하여 저장하는 RNN의 내부 상태 벡터입니다.
*   **Optimizer가 생성한 업데이트 값**: $g _t$
    *   Optimizer 모델 $m$이 타임 스텝 $t$에서 Optimizee의 파라미터 $\theta$를 어떻게 업데이트할지 제안하는 값(벡터)입니다.

#### 2.3. 학습 프로세스 및 공식

##### **프로세스 개요**
1.  **Optimizee**는 현재 파라미터 $\theta _t$에 대한 손실 기울기 $\nabla _t$를 계산합니다.
2.  이 기울기 $\nabla _t$는 **Optimizer(RNN)**의 입력으로 들어갑니다.
3.  **Optimizer**는 입력받은 기울기 $\nabla _t$와 자신의 이전 은닉 상태 $h _t$를 사용하여, Optimizee를 위한 파라미터 업데이트 값 $g _t$와 다음 은닉 상태 $h _{t+1}$을 출력합니다.
4.  **Optimizee**는 Optimizer가 생성한 $g _t$를 이용해 자신의 파라미터를 업데이트합니다.

##### **1) Optimizer의 연산**

Optimizer 모델 $m$은 입력으로 $\nabla _t$와 $h _t$를 받아, 출력으로 $g _t$와 $h _{t+1}$을 생성합니다.

$$
(g _t, h _{t+1}) = m(\nabla _t, h _t; \phi)
$$

*   **연산 설명**:
    *   $m(\cdot; \phi)$: 파라미터 $\phi$로 정의된 RNN 함수입니다.
    *   $(\nabla _t, h _t)$: 타임 스텝 $t$에서의 입력. Optimizee의 기울기 정보와 Optimizer의 과거 상태 정보입니다.
    *   $(g _t, h _{t+1})$: 타임 스텝 $t$에서의 출력. Optimizee를 위한 업데이트 값과 Optimizer의 다음 상태입니다.

##### **2) Optimizee의 파라미터 업데이트**

Optimizee는 표준 Gradient Descent 규칙 대신, Optimizer가 생성한 $g _t$를 사용하여 파라미터를 업데이트합니다.

$$
\theta _{t+1} = \theta _t + g _t
$$

*   **연산 설명**:
    *   $\theta _t$: 타임 스텝 $t$에서의 Optimizee 파라미터입니다.
    *   $g _t$: Optimizer $m$이 생성한 업데이트 벡터입니다. 이 벡터는 방향과 크기 정보를 모두 포함하며, 표준 GD의 `- \alpha \nabla L` 부분을 대체합니다.
    *   $\theta _{t+1}$: Optimizer의 제안에 따라 업데이트된 Optimizee의 새로운 파라미터입니다.

#### 2.4. Optimizer는 어떻게 학습되는가? (Meta-Optimization)

핵심 질문은 "어떻게 Optimizer 모델 $m$의 파라미터 $\phi$를 학습시키는가?" 입니다. Optimizer의 목표는 **Optimizee의 최종 손실을 최소화**하는 것입니다.

##### **1) Optimizer의 손실 함수 (Meta-Loss)**

Optimizer의 성능은 자신이 최적화시킨 Optimizee가 얼마나 낮은 손실 값을 갖는지에 따라 평가됩니다. 따라서 Optimizer의 손실 함수 $L(\phi)$는 여러 학습 과정(task)에 대한 Optimizee의 최종 손실의 기댓값으로 정의됩니다.

$$
L(\phi) = \mathbb{E} _{f} [L _f(\theta(f, \phi))]
$$

*   **연산 설명**:
    *   $\theta(f, \phi)$: 파라미터 $\phi$를 가진 Optimizer $m$에 의해 최적화된 Optimizee $f$의 최종 파라미터입니다.
    *   $L _f(\cdot)$: Optimizee $f$의 손실 함수입니다.
    *   $\mathbb{E} _{f}[\cdot]$: 다양한 Optimizee 모델(또는 태스크) $f$에 대한 기댓값을 의미합니다. 이는 Optimizer가 특정 모델 하나에만 과적합되지 않고, 범용적인 최적화 능력을 학습하도록 만듭니다.

##### **2) Optimizer의 파라미터 업데이트**

이 Meta-Loss $L(\phi)$를 최소화하기 위해, 우리는 표준적인 **Gradient Descent**를 사용합니다.

$$
\phi _{new} = \phi _{old} - \beta \nabla _{\phi} L(\phi)
$$

*   **연산 설명**:
    *   $\phi _{old}$: 현재 Optimizer의 파라미터입니다.
    *   $\nabla _{\phi} L(\phi)$: Meta-Loss를 Optimizer의 파라미터 $\phi$에 대해 미분한 기울기입니다. 이 기울기를 계산하기 위해서는, Optimizee의 전체 학습 과정(unrolled optimization trajectory)에 대해 Backpropagation을 수행해야 합니다.
    *   $\beta$: Optimizer를 학습시키기 위한 학습률 (Meta-Learning Rate)입니다.
    *   $\phi _{new}$: 업데이트된 Optimizer의 새로운 파라미터입니다.

---

### 결론

"Learning to learn gradient descent by gradient descent"는 두 단계의 최적화 과정으로 요약할 수 있습니다.

1.  **내부 루프 (Inner-loop)**: RNN 기반의 **Optimizer**($m$)가 **Optimizee**($f$)의 파라미터($\theta$)를 업데이트하는 과정.
2.  **외부 루프 (Outer-loop / Meta-loop)**: **Gradient Descent**를 사용하여, 내부 루프의 최종 결과 (Optimizee의 손실)를 최소화하도록 **Optimizer**($m$)의 파라미터($\phi$)를 업데이트하는 과정.

이처럼 고정된 최적화 규칙을 사용하는 대신, 데이터로부터 더 효율적인 최적화 전략 자체를 학습하는 것이 이 알고리즘의 핵심입니다.
