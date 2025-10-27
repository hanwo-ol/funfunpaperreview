### 증명 1: 로짓 모델의 멱함수 형태 (과제 2, 문제 4.a)

목표: 로지스틱 회귀 모델 $\text{logit}(\pi) = \alpha + \beta \log(d)$ 로부터 $\frac{\pi}{1-\pi} = e^\alpha d^\beta$ 를 유도하는 것입니다.

전개 과정:

1.  로짓(logit)의 정의를 대입합니다.
    로짓 함수의 정의에 따라, 모델은 다음과 같이 쓸 수 있습니다.

$$ \log\left(\frac{\pi}{1-\pi}\right) = \alpha + \beta \log(d) $$

2.  양변에 지수 함수(exponential function)를 취합니다.
    좌변의 로그를 없애기 위해 양변에 밑이 $e$인 지수 함수를 적용합니다.

$$ \exp\left[\log\left(\frac{\pi}{1-\pi}\right)\right] = \exp[\alpha + \beta \log(d)] $$

지수 함수와 로그 함수는 서로 역함수 관계($e^{\log x} = x$)이므로 좌변은 다음과 같이 간단해집니다.

$$ \frac{\pi}{1-\pi} = \exp[\alpha + \beta \log(d)] $$

3.  우변에 지수 법칙을 적용합니다.
    지수 법칙($e^{A+B} = e^A \cdot e^B$)을 이용하여 우변을 두 항의 곱으로 분리합니다.

$$ \frac{\pi}{1-\pi} = e^\alpha \cdot e^{\beta \log(d)} $$

4.  로그와 지수의 성질을 이용하여 우변을 정리합니다.
    로그의 성질($k \log d = \log d^k$)을 이용하여 $e^{\beta \log(d)}$ 항을 변형합니다.

$$ e^{\beta \log(d)} = e^{\log(d^\beta)} $$

다시 지수 함수와 로그 함수의 역함수 관계를 적용하면,

$$ e^{\log(d^\beta)} = d^\beta $$

5.  최종 결과를 결합합니다.
    3단계와 4단계의 결과를 합치면 목표로 했던 식이 유도됩니다.

$$ \frac{\pi}{1-\pi} = e^\alpha d^\beta $$

증명 완료.

---

### 증명 2: 베이즈 정리와 진단 검사 (Textbook, Exercise 2.25)

목표: 진단 검사에서 양성 판정을 받은 환자가 실제로 질병을 가지고 있을 확률(양성 예측도, Positive Predictive Value)이 $P(D|+) = \frac{\pi _1 \rho}{\pi _1 \rho + \pi _2(1-\rho)}$ 임을 보이는 것입니다.

정의:
*   $D$: 질병이 있는 사건, $\bar{D}$: 질병이 없는 사건
*   $+$: 검사 결과가 양성인 사건
*   $\pi _1$: 민감도(Sensitivity) = $P(+|D)$
*   $\pi _2$: 위양성률(False Positive Rate) = $P(+|\bar{D})$
*   $\rho$: 유병률(Prevalence) = $P(D)$, 따라서 $P(\bar{D}) = 1-\rho$

전개 과정:

1.  조건부 확률의 정의를 적용합니다.
    우리가 구하고자 하는 확률은 $P(D|+)$ 입니다. 조건부 확률의 정의에 따라,

$$ P(D|+) = \frac{P(D \cap +)}{P(+)} $$

2.  분자($P(D \cap +)$)를 계산합니다.
    확률의 곱셈 법칙에 따라 $P(A \cap B) = P(A|B)P(B)$ 입니다.

$$ P(D \cap +) = P(+|D)P(D) $$

주어진 정의를 대입하면,

$$ P(D \cap +) = \pi _1 \rho $$

3.  분모($P(+)$)를 계산합니다.
    전체 확률의 법칙(Law of Total Probability)에 따라, 양성 결과가 나오는 경우는 '질병이 있으면서 양성'인 경우와 '질병이 없으면서 양성'인 두 가지 경우의 합입니다.

$$ P(+) = P(+ \cap D) + P(+ \cap \bar{D}) $$

각 항에 곱셈 법칙을 적용합니다.

$$ P(+) = P(+|D)P(D) + P(+|\bar{D})P(\bar{D}) $$

주어진 정의를 대입하면,

$$ P(+) = \pi _1 \rho + \pi _2 (1-\rho) $$

4.  분자와 분모를 결합합니다.
    2단계와 3단계에서 구한 결과를 1단계의 분수식에 대입합니다.

$$ P(D|+) = \frac{\pi _1 \rho}{\pi _1 \rho + \pi _2(1-\rho)} $$

증명 완료.

---

### 증명 3: 환자-대조군 연구의 한계 (과제 1, 문제 4.c)

목표: 환자-대조군 연구 자료를 사용하여 "흡연자와 비흡연자에서 폐암으로 고통받는 비율"($P(\text{폐암}|\text{흡연})$)을 직접 비교할 수 없는 이유를 설명하는 것입니다.

논리 전개:

1.  우리가 추정하고 싶은 목표: $P(\text{폐암}|\text{흡연})$는 모집단의 모든 흡연자 중 폐암에 걸린 사람의 비율입니다. 이를 추정하려면 모집단에서 무작위로 표본을 추출해야 합니다.

2.  환자-대조군 연구의 표집 방법: 이 연구는 모집단에서 무작위로 표본을 추출하지 않았습니다. 대신, 연구자는 결과(폐암 유무)를 기준으로 두 그룹을 의도적으로 선정했습니다.
    *   폐암 환자 709명 (환자군)
    *   폐암이 아닌 환자 709명 (대조군)
    이 과정에서 연구자는 표본 내 폐암 환자의 비율을 인위적으로 $709 / (709+709) = 50\%$로 고정시켰습니다.

3.  결론: 표본 내 폐암 비율(50%)은 실제 인구 집단의 폐암 유병률(prevalence, 매우 낮음)과 아무 관련이 없습니다. 표본이 모집단을 대표하지 않기 때문에, 이 표본의 흡연자 중 폐암 환자의 비율($688/1338$)을 계산하더라도, 이는 모집단의 실제 $P(\text{폐암}|\text{흡연})$에 대한 타당한 추정치가 될 수 없습니다. 따라서 이 자료로는 비율의 차이나 상대위험도를 직접 계산할 수 없습니다.

---

### 증명 4: 로지스틱 회귀 곡선의 도함수 (Textbook, Exercise 5.25)

목표: 로지스틱 회귀 모델 $\pi(x) = \frac{\exp(\alpha+\beta x)}{1+\exp(\alpha+\beta x)}$의 도함수가 $\frac{d\pi(x)}{dx} = \beta\pi(x)[1-\pi(x)]$ 임을 보이는 것입니다.

전개 과정:

1.  몫의 미분법(Quotient Rule)을 사용합니다.
    함수 $f(x) = \exp(\alpha+\beta x)$와 $g(x) = 1+\exp(\alpha+\beta x)$라고 두면, $\pi(x) = f(x)/g(x)$ 입니다. 몫의 미분법은 $(\frac{f}{g})' = \frac{f'g - fg'}{g^2}$ 입니다.

2.  $f'(x)$와 $g'(x)$를 계산합니다.
    연쇄 법칙에 의해,
    *   $f'(x) = \frac{d}{dx}\exp(\alpha+\beta x) = \exp(\alpha+\beta x) \cdot \beta = \beta f(x)$
    *   $g'(x) = \frac{d}{dx}(1+\exp(\alpha+\beta x)) = \exp(\alpha+\beta x) \cdot \beta = \beta f(x)$

3.  몫의 미분법 공식에 대입합니다.

$$ \frac{d\pi(x)}{dx} = \frac{[\beta f(x)] [g(x)] - [f(x)] [\beta f(x)]}{[g(x)]^2} $$

분자에서 공통 인수 $\beta f(x)$를 묶어냅니다.

$$ = \frac{\beta f(x) [g(x) - f(x)]}{[g(x)]^2} $$

4.  $f(x)$와 $g(x)$를 다시 대입하여 정리합니다.
    *   $g(x) - f(x) = [1+\exp(\alpha+\beta x)] - \exp(\alpha+\beta x) = 1$
    대입하면,

$$ \frac{d\pi(x)}{dx} = \frac{\beta f(x) \cdot 1}{[g(x)]^2} = \frac{\beta \exp(\alpha+\beta x)}{[1+\exp(\alpha+\beta x)]^2} $$

5.  $\pi(x)$와 $1-\pi(x)$로 표현합니다.
    위 식을 다음과 같이 두 부분으로 나눌 수 있습니다.

$$ \frac{d\pi(x)}{dx} = \beta \cdot \left[ \frac{\exp(\alpha+\beta x)}{1+\exp(\alpha+\beta x)} \right] \cdot \left[ \frac{1}{1+\exp(\alpha+\beta x)} \right] $$

첫 번째 대괄호 안의 항은 $\pi(x)$의 정의와 같습니다.
    두 번째 대괄호 안의 항은 $1-\pi(x)$와 같습니다. 왜냐하면,

$$ 1-\pi(x) = 1 - \frac{\exp(\alpha+\beta x)}{1+\exp(\alpha+\beta x)} = \frac{1+\exp(\alpha+\beta x) - \exp(\alpha+\beta x)}{1+\exp(\alpha+\beta x)} = \frac{1}{1+\exp(\alpha+\beta x)} $$

이기 때문입니다.

6.  최종 결과를 결합합니다.

$$ \frac{d\pi(x)}{dx} = \beta \cdot \pi(x) \cdot [1-\pi(x)] $$

증명 완료.

---

### 증명 5: 독립성 모델의 등가성 (Textbook, Exercise 5.32.b)

목표: $I \times 2$ 표에 대한 로지스틱 모델 $\text{logit}(\pi _i) = \alpha + \beta _i$ 에서, 독립성 모델($\beta _1=\beta _2=\dots=\beta _I$)과 비율이 동일한 조건($\pi _1=\pi _2=\dots=\pi _I$)이 서로 동등함을 증명하는 것입니다.

전개 과정:

방향 1: $(\beta _1 = \dots = \beta _I) \implies (\pi _1 = \dots = \pi _I)$

1.  독립성 모델을 가정합니다: 모든 $i$에 대해 $\beta _i$가 어떤 공통 상수 $\beta^*$와 같습니다.

$$ \beta _1 = \beta _2 = \dots = \beta _I = \beta^* $$

2.  이 가정을 로지스틱 모델에 대입합니다.

$$ \text{logit}(\pi _i) = \alpha + \beta^* $$

3.  이 식의 우변은 $i$와 관계없이 상수입니다. 따라서 모든 $i$에 대해 $\text{logit}(\pi _i)$ 값은 동일합니다.

$$ \text{logit}(\pi _1) = \text{logit}(\pi _2) = \dots = \text{logit}(\pi _I) $$

4.  로짓 함수 $g(\pi) = \log(\frac{\pi}{1-\pi})$는 $0 < \pi < 1$ 범위에서 일대일(one-to-one) 함수입니다 (엄격하게 증가하는 함수).

5.  일대일 함수의 성질에 따라, 만약 $g(\pi _a) = g(\pi _b)$이면, 반드시 $\pi _a = \pi _b$여야 합니다.
6.  따라서, 모든 $\text{logit}(\pi _i)$가 같으므로, 모든 $\pi _i$도 같아야 합니다.

$$ \pi _1 = \pi _2 = \dots = \pi _I $$

첫 번째 방향 증명 완료.

방향 2: $(\pi _1 = \dots = \pi _I) \implies (\beta _1 = \dots = \beta _I)$

1.  모든 비율이 동일하다고 가정합니다: 모든 $i$에 대해 $\pi _i$가 어떤 공통 상수 $\pi^*$와 같습니다.

$$ \pi _1 = \pi _2 = \dots = \pi _I = \pi^* $$

2.  양변에 로짓 함수를 취합니다.

$$ \text{logit}(\pi _1) = \text{logit}(\pi _2) = \dots = \text{logit}(\pi _I) = \text{logit}(\pi^*) $$

3.  로지스틱 모델의 정의 $\text{logit}(\pi _i) = \alpha + \beta _i$를 위 식에 대입합니다.

$$ \alpha + \beta _1 = \alpha + \beta _2 = \dots = \alpha + \beta _I = \text{logit}(\pi^*) $$

4.  각 등식에서 $\alpha$를 소거하면,

$$ \beta _1 = \beta _2 = \dots = \beta _I = \text{logit}(\pi^*) - \alpha $$

5.  우변 $\text{logit}(\pi^*) - \alpha$는 $i$와 관계없는 상수입니다. 따라서 모든 $\beta _i$는 동일한 상수 값과 같습니다.
    두 번째 방향 증명 완료.

결론: 양방향이 모두 증명되었으므로, 두 조건은 서로 동등합니다.
