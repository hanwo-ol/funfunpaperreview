# 🧠 Learning to Learn by Gradient Descent by Gradient Descent

이 문서는 Andrychowicz et al. (2016)의 논문 *“Learning to Learn by Gradient Descent by Gradient Descent”* 내용을 기반으로  
RNN 기반 메타 옵티마이저(meta-optimizer)의 구조와 수식적 해석을 정리한 것입니다.

---

## 1️⃣ 옵티마이저의 목표

기본 네트워크(Optimizee)의 파라미터를 $\theta$,  
RNN 옵티마이저의 파라미터를 $\phi$라고 하자.  

메타 옵티마이저의 목표는 기본 네트워크의 평균 손실을 최소화하는 것이다.

$$
L(\phi) = \mathbb{E}_f [f(\theta(f, \phi))]
$$

- $f$: base network (optimizee)의 손실 함수  
- $\theta(f, \phi)$: RNN 옵티마이저에 의해 업데이트된 파라미터  
- $L(\phi)$: 여러 태스크에 대한 기대 손실  

즉, RNN의 역할은 base network의 손실을 줄이는 학습 규칙을 학습하는 것이다.

---

## 2️⃣ RNN 옵티마이저의 입력과 출력

RNN 옵티마이저는 다음과 같이 정의된다:

$$
(g_t, h_{t+1}) = m(\nabla_t, h_t, \phi)
$$

| 기호 | 의미 |
|------|------|
| $\nabla_t = \nabla_\theta f(\theta_t)$ | Base network의 gradient (손실의 기울기) |
| $h_t$ | RNN의 hidden state (이전 단계 정보 저장) |
| $\phi$ | RNN 옵티마이저의 파라미터 |
| $g_t$ | RNN의 출력 (업데이트 벡터) |
| $h_{t+1}$ | RNN의 다음 hidden state |

즉, RNN은 gradient와 내부 상태를 입력으로 받아,  
다음 파라미터 업데이트 방향 $g_t$를 학습된 방식으로 예측한다.

---

## 3️⃣ 파라미터 업데이트 규칙

Base network의 파라미터는 다음과 같이 갱신된다:

$$
\theta_{t+1} = \theta_t + g_t
$$

여기서 $g_t$는 일반적인 경사 하강법의 $-\alpha \nabla_\theta L$ 대신  
RNN이 출력한 학습된 업데이트 벡터이다.  

즉, 업데이트 규칙이 고정된 수식이 아니라 학습된 함수 형태로 표현된다.

---

## 4️⃣ 메타 학습 과정 (Meta-Optimization Loop)

전체 학습은 두 개의 루프로 구성된다.

| 단계 | 설명 |
|------|------|
| Inner Loop | RNN 옵티마이저 $m_\phi$를 이용해 base network $f_\theta$의 파라미터를 반복적으로 업데이트 |
| Outer Loop | Inner loop 수행 후, 최종 손실을 기반으로 RNN의 파라미터 $\phi$를 gradient descent로 업데이트 |

즉, RNN은 gradient를 입력으로 받아 업데이트 규칙을 학습하며,  
그 RNN 자체는 gradient descent로 학습된다.

---

## 5️⃣ 핵심 요약

- RNN은 경사 하강법을 완전히 대체하지 않는다.  
  대신 gradient와 내부 state를 함께 입력받아, 학습된 방식으로 업데이트 함수를 구성한다.

- 파라미터 업데이트는 다음과 같다:

$$
\theta_{t+1} = \theta_t + g_t, \quad (g_t, h_{t+1}) = m(\nabla_t, h_t, \phi)
$$

- Outer loop에서 $\phi$를 gradient descent로 학습시키므로,  
  이 과정을 “경사 하강법으로 경사 하강법을 학습한다”라고 부른다.

---

## 6️⃣ 함수 $m$의 정의와 수식적 구조

위 식에서 $m$은 단순한 기호가 아니라, RNN 기반 옵티마이저를 나타내는 파라미터화된 함수이다.  
즉, $m$은 모델(model)이자, 업데이트 규칙을 학습하는 함수로 정의된다.

$$
m_\phi : (\nabla_t, h_t) \mapsto (g_t, h_{t+1})
$$

- 입력(Input):  
  - $\nabla_t$: optimizee의 gradient  
  - $h_t$: 이전 RNN hidden state  
- 출력(Output):  
  - $g_t$: 파라미터 업데이트 벡터  
  - $h_{t+1}$: 다음 hidden state  
- 파라미터(Parameter):  
  - $\phi$: RNN 옵티마이저의 가중치 (메타 수준에서 학습됨)

---

### 💡 LSTM 기반 구현 예시

실제로는 $m_\phi$를 LSTM이나 GRU 셀로 구현할 수 있다.  
예를 들어, LSTM 형태라면 다음과 같은 내부 연산으로 표현된다:

$$
\begin{aligned}
i_t &= \sigma(W_i \nabla_t + U_i h_t + b_i) \\
f_t &= \sigma(W_f \nabla_t + U_f h_t + b_f) \\
o_t &= \sigma(W_o \nabla_t + U_o h_t + b_o) \\
\tilde{c}_t &= \tanh(W_c \nabla_t + U_c h_t + b_c) \\
c_{t+1} &= f_t \odot c_t + i_t \odot \tilde{c}_t \\
h_{t+1} &= o_t \odot \tanh(c_{t+1}) \\
g_t &= W_g h_{t+1} + b_g
\end{aligned}
$$

이때,  
- $(c_t, h_t)$는 RNN의 내부 상태(state),  
- $g_t$는 base network의 파라미터 업데이트 벡터이다.  

즉, $m_\phi$는 “gradient를 업데이트로 변환하는 학습된 RNN 함수”로서 동작한다.

---

## 🧩 결론

> RNN 옵티마이저 $m_\phi$는 gradient descent의 고정된 규칙을 학습 가능한 함수로 일반화한 것이다.  
>  
> 이 함수는 gradient와 내부 상태를 입력받아,  
> 학습된 방식으로 파라미터 업데이트 벡터를 생성하며,  
> 메타 수준에서는 gradient descent를 통해 스스로 학습된다.  
>  
> 따라서, 전체 구조는 “learning to learn by gradient descent by gradient descent”로 요약된다.
