# 🧠 Learning to Learn by Gradient Descent by Gradient Descent

이 문서는 Andrychowicz et al. (2016)의 논문 *“Learning to Learn by Gradient Descent by Gradient Descent”* 내용을 기반으로  
RNN 기반 메타 옵티마이저(meta-optimizer)의 구조와 수식적 해석을 정리한 것입니다.

---

## 1️⃣ 옵티마이저의 목표

기본 네트워크(Optimizee)의 파라미터를 $\theta$,  
RNN 옵티마이저의 파라미터를 $\phi$라고 하자.  

메타 옵티마이저의 목표는 기본 네트워크의 평균 손실을 최소화하는 것이다.

$$
L(\phi) = \mathbb{E} _f [f(\theta(f, \phi))]
$$

- $f$: base network (optimizee)의 손실 함수  
- $\theta(f, \phi)$: RNN 옵티마이저에 의해 업데이트된 파라미터  
- $L(\phi)$: 여러 태스크에 대한 기대 손실  

즉, RNN의 역할은 base network의 손실을 줄이는 학습 규칙을 학습하는 것이다.

---

## 2️⃣ RNN 옵티마이저의 입력과 출력

RNN 옵티마이저는 다음과 같이 정의된다:

$$
(g _t, h _{t+1}) = m(\nabla _t, h _t, \phi)
$$

| 기호 | 의미 |
|------|------|
| $\nabla _t = \nabla _\theta f(\theta _t)$ | Base network의 gradient (손실의 기울기) |
| $h _t$ | RNN의 hidden state (이전 단계 정보 저장) |
| $\phi$ | RNN 옵티마이저의 파라미터 |
| $g _t$ | RNN의 출력 (업데이트 벡터) |
| $h _{t+1}$ | RNN의 다음 hidden state |

즉, RNN은 gradient와 내부 상태를 입력으로 받아,  
다음 파라미터 업데이트 방향 $g _t$를 학습된 방식으로 예측한다.

---

## 3️⃣ 파라미터 업데이트 규칙

Base network의 파라미터는 다음과 같이 갱신된다:

$$
\theta _{t+1} = \theta _t + g _t
$$

여기서 $g _t$는 일반적인 경사 하강법의 $-\alpha \nabla _\theta L$ 대신  
RNN이 출력한 학습된 업데이트 벡터이다.  

즉, 업데이트 규칙이 고정된 수식이 아니라 학습된 함수 형태로 표현된다.

---

## 4️⃣ 메타 학습 과정 (Meta-Optimization Loop)

전체 학습은 두 개의 루프로 구성된다.

| 단계 | 설명 |
|------|------|
| Inner Loop | RNN 옵티마이저 $m _\phi$를 이용해 base network $f _\theta$의 파라미터를 반복적으로 업데이트 |
| Outer Loop | Inner loop 수행 후, 최종 손실을 기반으로 RNN의 파라미터 $\phi$를 gradient descent로 업데이트 |

즉, RNN은 gradient를 입력으로 받아 업데이트 규칙을 학습하며,  
그 RNN 자체는 gradient descent로 학습된다.

---

## 5️⃣ 핵심 요약

- RNN은 경사 하강법을 완전히 대체하지 않는다.  
  대신 gradient와 내부 state를 함께 입력받아, 학습된 방식으로 업데이트 함수를 구성한다.

- 파라미터 업데이트는 다음과 같다:

$$
\theta _{t+1} = \theta _t + g _t, \quad (g _t, h _{t+1}) = m(\nabla _t, h _t, \phi)
$$

- Outer loop에서 $\phi$를 gradient descent로 학습시키므로,  
  이 과정을 “경사 하강법으로 경사 하강법을 학습한다”라고 부른다.

---

> 요약하자면:  
> - RNN은 gradient descent의 수식을 학습 가능한 함수로 일반화한다.  
> - gradient와 hidden state를 입력으로 받아,  
>   경험적으로 더 나은 업데이트 규칙을 생성한다.  
> - 결과적으로, “learning to learn by gradient descent by gradient descent”가 실현된다.
