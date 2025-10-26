### 식 (4.21)의 배경과 목표

목표: 이항 분포가 일반화 선형 모델(GLM)의 이론적 기반인 지수 분산족(Exponential Dispersion Family, EDF)의 형태를 만족함을 보이는 것입니다.

EDF의 일반 형태 (식 4.17):

$$
f(y_i; \theta_i, \phi)
= \exp\!\left( \frac{y_i\theta_i - b(\theta_i)}{a(\phi)} + c(y_i, \phi) \right)
$$


이항 분포의 확률 질량 함수를 조작하여 위와 같은 형태로 만드는 것이 목표입니다.

### $y _i$의 정의: 성공 횟수가 아닌 성공 비율

이 섹션(4.4.3)에서 가장 중요한 전제 조건 중 하나는 다음과 같습니다.

> "Next, suppose that $n _i Y _i$ has a $\text{bin}(n _i, \pi _i)$ distribution; that is, here $y _i$ is the sample proportion (rather than number) of successes, so $E(Y _i) = \pi _i$ does not depend on $n _i$."

이 문장을 해석하면 다음과 같습니다.

*   $n _i Y _i$: 이것이 우리가 흔히 아는 성공 횟수입니다. $n _i$번의 시행 중 성공한 횟수를 나타내며, 이항분포 $\text{bin}(n _i, \pi _i)$를 따릅니다.
*   $Y _i$: 이 섹션에서 사용하는 반응 변수 $Y _i$는 성공 횟수를 시행 횟수 $n _i$로 나눈 성공 비율(proportion of successes)입니다.

$$ Y _i = \frac{\text{성공 횟수}}{n _i} $$

*   $y _i$: $Y _i$의 관측된 값, 즉 관측된 성공 비율입니다.

왜 이렇게 정의하는가?
GLM의 일반 이론에서는 반응 변수 $Y _i$의 기댓값 $E(Y _i)=\mu _i$를 모델링합니다. 만약 $Y _i$를 성공 횟수로 정의하면 $E(Y _i) = n _i\pi _i$가 되어, 기댓값이 표본 크기 $n _i$에 의존하게 됩니다. 이론을 더 깔끔하게 전개하기 위해, 저자는 $E(Y _i)=\pi _i$가 되도록 $Y _i$를 성공 '비율'로 정의한 것입니다.

---

### 식 (4.21) 유도 과정

1.  시작점: 이항 분포 확률 질량 함수 (성공 횟수 기준)
    성공 횟수를 $k$라고 할 때, 확률 질량 함수는 다음과 같습니다.

$$ P(\text{성공 횟수}=k) = \binom{n _i}{k} \pi _i^k (1-\pi _i)^{n _i-k} $$

여기서 $k = n _i y _i$ (성공 횟수 = 총 시행 횟수 $\times$ 성공 비율) 이므로, $k$ 자리에 $n _i y _i$를 대입합니다.

$$ f(y _i; \pi _i, n _i) = \binom{n _i}{n _i y _i} \pi _i^{n _i y _i} (1-\pi _i)^{n _i - n _i y _i} $$

2.  지수 함수 형태로 변환: 전체 식을 $\exp[\log(\dots)]$ 형태로 바꿉니다.

$$ = \exp\left[ \log\left( \binom{n _i}{n _i y _i} \pi _i^{n _i y _i} (1-\pi _i)^{n _i(1 - y _i)} \right) \right] $$

로그의 성질을 이용하여 항들을 분리합니다.

$$ = \exp\left[ n _i y _i \log(\pi _i) + n _i(1-y _i)\log(1-\pi _i) + \log\binom{n _i}{n _i y _i} \right] $$

3.  자연 모수 $\theta _i$ 도입: 이항 분포의 자연 모수는 로짓(logit)입니다.

$$ \theta _i = \log\left(\frac{\pi _i}{1-\pi _i}\right) $$

이 식으로부터 $\pi _i$와 $(1-\pi _i)$를 $\theta _i$에 대한 식으로 표현해야 합니다.
    *   $e^{\theta _i} = \frac{\pi _i}{1-\pi _i} \implies (1-\pi _i)e^{\theta _i} = \pi _i \implies e^{\theta _i} = \pi _i(1+e^{\theta _i}) \implies \pi _i = \frac{e^{\theta _i}}{1+e^{\theta _i}}$
    *   $1-\pi _i = 1 - \frac{e^{\theta _i}}{1+e^{\theta _i}} = \frac{1}{1+e^{\theta _i}}$
    로그를 취하면,
    *   $\log(\pi _i) = \log\left(\frac{e^{\theta _i}}{1+e^{\theta _i}}\right) = \theta _i - \log(1+e^{\theta _i})$
    *   $\log(1-\pi _i) = \log\left(\frac{1}{1+e^{\theta _i}}\right) = -\log(1+e^{\theta _i})$

4.  대입 및 정리: 3단계에서 구한 식들을 2단계의 $\exp[\dots]$ 안에 대입합니다.

$$ \exp\left[ n _i y _i (\theta _i - \log(1+e^{\theta _i})) + n _i(1-y _i)(-\log(1+e^{\theta _i})) + \log\binom{n _i}{n _i y _i} \right] $$

괄호를 풀고 정리합니다.

$$ = \exp\left[ n _i y _i \theta _i - n _i y _i \log(1+e^{\theta _i}) - n _i \log(1+e^{\theta _i}) + n _i y _i \log(1+e^{\theta _i}) + \log\binom{n _i}{n _i y _i} \right] $$

$- n _i y _i \log(1+e^{\theta _i})$와 $+ n _i y _i \log(1+e^{\theta _i})$ 항이 서로 상쇄됩니다.

$$ = \exp\left[ n _i y _i \theta _i - n _i \log(1+e^{\theta _i}) + \log\binom{n _i}{n _i y _i} \right] $$

5.  EDF 형태로 맞추기: 최종 목표인 $\exp\left( \frac{y_i\theta_i - b(\theta_i)}{a(\phi)} + c(y_i, \phi) \right)
$ 형태와 비교합니다.
    위 식의 $\exp[\dots]$ 안의 모든 항을 $n _i$로 나누고 다시 $n _i$를 곱해줍니다. (형태를 맞추기 위한 트릭)

$$ = \exp\[ n _i \left( y _i \theta _i - \log(1+e^{\theta _i}) \right) + \log\binom{n _i}{n _i y _i} \] $$

$$ = \exp\left[ \frac{y _i \theta _i - \log(1+e^{\theta _i})}{1/n _i} + \log\binom{n _i}{n _i y _i} \right] $$

이것이 바로 식 (4.21)입니다.

### EDF 구성 요소 식별

이제 이 최종 형태를 EDF 일반 형태와 비교하여 각 "부품"을 식별할 수 있습니다.
*   $y _i$: 성공 비율
*   $\theta _i$: 자연 모수, $\log(\frac{\pi _i}{1-\pi _i})$ (로짓)
*   $b(\theta _i)$: $\log(1+e^{\theta _i})$
*   $a(\phi)$: $1/n _i$. 여기서 분산 모수 $\phi=1$이고, 가중치 $\omega _i=n _i$로 볼 수 있습니다.
*   $c(y _i, \phi)$: $\log\binom{n _i}{n _i y _i}$

결론: 이 과정을 통해, 이항 분포(반응 변수를 '비율'로 정의했을 때)가 지수 분산족의 형태를 완벽하게 만족함을 보였습니다. 여기서 $y _i$는 성공 비율이며, 성공 횟수가 아님을 명확히 이해하는 것이 중요합니다. 이 수학적 증명 덕분에, 우리는 이항 데이터를 다루는 로지스틱 회귀와 같은 모델들을 일반화 선형 모델이라는 통일된 프레임워크 안에서 체계적으로 다룰 수 있게 됩니다.
