### **1. 기본 로지스틱 회귀 모델 (Basic Logistic Regression Model)**

단일 예측 변수 $x$에 대한 성공 확률 $\pi(x)$를 모델링합니다.

*   **로짓 형태 (Logit Form)**: 로그 오즈가 $x$에 대해 선형 관계를 가집니다.

$$ \text{logit}[\pi(x)] = \log\left(\frac{\pi(x)}{1-\pi(x)}\right) = \alpha + \beta x $$

*   **확률 형태 (Probability Form)**: 위 식을 $\pi(x)$에 대해 정리한 것입니다.

$$ \pi(x) = \frac{\exp(\alpha + \beta x)}{1 + \exp(\alpha + \beta x)} = \frac{1}{1 + \exp(-(\alpha + \beta x))} $$

### **2. 모델 모수($\beta$) 및 관련 값 해석**

*   **오즈비 (Odds Ratio, OR)**: $x$가 1단위 증가할 때 성공의 오즈가 몇 배 변하는지를 나타냅니다.

$$ \text{OR} = e^\beta $$

*   **확률의 순간 변화율 (기울기)**: 특정 지점 $x$에서 $x$가 변할 때 $\pi(x)$가 변하는 속도입니다.

$$ \frac{d\pi(x)}{dx} = \beta \cdot \pi(x) \cdot [1-\pi(x)] $$

### **3. 추론 (Inference)**

#### **가설 검정 (Hypothesis Testing)**

*   **왈드 검정 통계량 (Wald Test Statistic)**: $H _0: \beta = 0$을 검정합니다.

$$ z = \frac{\hat{\beta}}{\text{SE}(\hat{\beta})} $$

$z^2$은 근사적으로 자유도 1인 $\chi^2$ 분포를 따릅니다.

*   **가능도비 검정 통계량 (Likelihood Ratio Test Statistic, LRT)**: 두 개의 포함(nested) 모델 $M _0$(축소)와 $M _1$(전체)을 비교합니다.

$$ G^2 = -2(L _0 - L _1) $$

여기서 $L _0$와 $L _1$은 각각 $M _0$와 $M _1$의 최대화된 로그가능도입니다. $G^2$은 두 모델의 모수 개수 차이를 자유도로 갖는 $\chi^2$ 분포를 근사적으로 따릅니다.

#### **신뢰구간 (Confidence Intervals)**

*   **$\beta$의 95% 왈드 신뢰구간**:

$$ \hat{\beta} \pm 1.96 \times \text{SE}(\hat{\beta}) $$

*   **오즈비($e^\beta$)의 95% 신뢰구간**: $\beta$의 신뢰구간 양 끝점에 지수 함수를 적용합니다.

$$ \exp\left( \hat{\beta} \pm 1.96 \times \text{SE}(\hat{\beta}) \right) $$

*   **특정 예측 확률($\pi(x _0)$)의 95% 신뢰구간**:
    1.  먼저 $\text{logit}[\pi(x _0)] = \alpha + \beta x _0$의 신뢰구간을 구합니다.
        *   **분산**: $\text{Var}(\hat{\alpha} + \hat{\beta}x _0) = \text{Var}(\hat{\alpha}) + x _0^2 \text{Var}(\hat{\beta}) + 2x _0 \text{Cov}(\hat{\alpha}, \hat{\beta})$
        *   **신뢰구간 (로짓 척도)**: $(\hat{\alpha} + \hat{\beta}x _0) \pm 1.96 \times \sqrt{\text{Var}(\hat{\alpha} + \hat{\beta}x _0)}$
    2.  이 구간의 하한($L$)과 상한($U$)을 확률 척도로 역변환합니다.

$$ \left( \frac{e^L}{1+e^L}, \frac{e^U}{1+e^U} \right) $$


### **4. 다중 로지스틱 회귀 모델 (Multiple Logistic Regression)**

여러 예측 변수($x _1, \dots, x _p$)를 포함하도록 모델을 확장합니다.

*   **주효과 모델 (Main-effects Model)**:

$$ \text{logit}[\pi(\mathbf{x})] = \alpha + \beta _1 x _1 + \beta _2 x _2 + \dots + \beta _p x _p $$

$\beta _j$는 다른 변수들이 고정되었을 때 $x _j$의 효과(로그 오즈비)를 나타냅니다.

*   **상호작용 모델 (Interaction Model)**: (문제 2번에서 사용됨)

$$ \text{logit}[\pi(x)] = \alpha + \beta _1 x + \beta _2 x^2 $$

$x^2$ 항은 $x$의 효과가 $x$의 수준에 따라 변하는 비선형 관계를 모델링합니다.

### **5. 범주형 예측 변수 처리 (Categorical Predictors)**

*   **ANOVA 형태 모델**: $I$개 범주를 갖는 변수에 대해 $I$개의 모수를 사용합니다. 중복성 문제가 발생합니다.

$$ \text{logit}(\pi _i) = \alpha + \beta _i $$

*   **지시 변수(Dummy Variable) 모델**: 하나의 기준 범주를 설정하고 $I-1$개의 지시 변수를 사용합니다.

$$ \text{logit}(\pi) = \alpha + \beta _1 x _1 + \dots + \beta _{I-1}x _{I-1} $$

여기서 $\beta _j = \text{logit}(\pi _j) - \text{logit}(\pi _I)$는 기준 범주($I$) 대비 범주 $j$의 로그 오즈비입니다.

### **6. 특수 상황에 대한 검정 (Special Cases)**

*   **코크란-맨텔-헨젤(CMH) 검정**: 층화된 $2 \times 2 \times K$ 표에서 조건부 독립성을 검정하는 비-모델 기반 방법입니다.

$$ \text{CMH} = \frac{\left[\sum _k (n _{11k} - E(n _{11k}))\right]^2}{\sum _k \text{Var}(n _{11k})} $$

이는 로지스틱 회귀에서 $H _0: \beta _{\text{효과}}=0$에 대한 스코어 검정과 점근적으로 동일합니다.

*   **정확 조건부 로지스틱 회귀**: 완전/준-완전 분리나 희소 데이터 문제로 MLE가 존재하지 않을 때 사용됩니다. 이는 조건부 우도(Conditional Likelihood)에 기반하여 정확한 P-값과 신뢰구간을 계산합니다. (수식이 복잡하여 개념적으로 이해)
