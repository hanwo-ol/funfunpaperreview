### 1. 기본 로지스틱 회귀 모델 (Basic Logistic Regression Model)

단일 예측 변수 $x$에 대한 성공 확률 $\pi(x)$를 모델링합니다.

*   로짓 형태 (Logit Form): 로그 오즈가 $x$에 대해 선형 관계를 가집니다.

$$ \text{logit}[\pi(x)] = \log\left(\frac{\pi(x)}{1-\pi(x)}\right) = \alpha + \beta x $$

*   확률 형태 (Probability Form): 위 식을 $\pi(x)$에 대해 정리한 것입니다.

$$ \pi(x) = \frac{\exp(\alpha + \beta x)}{1 + \exp(\alpha + \beta x)} = \frac{1}{1 + \exp(-(\alpha + \beta x))} $$

### 2. 모델 모수($\beta$) 및 관련 값 해석

*   오즈비 (Odds Ratio, OR): $x$가 1단위 증가할 때 성공의 오즈가 몇 배 변하는지를 나타냅니다.

$$ \text{OR} = e^\beta $$

*   확률의 순간 변화율 (기울기): 특정 지점 $x$에서 $x$가 변할 때 $\pi(x)$가 변하는 속도입니다.

$$ \frac{d\pi(x)}{dx} = \beta \cdot \pi(x) \cdot [1-\pi(x)] $$

### 3. 추론 (Inference)

#### 가설 검정 (Hypothesis Testing)

*   왈드 검정 통계량 (Wald Test Statistic): $H  _0: \beta = 0$을 검정합니다.

$$ z = \frac{\hat{\beta}}{\text{SE}(\hat{\beta})} $$

$z^2$은 근사적으로 자유도 1인 $\chi^2$ 분포를 따릅니다.

*   가능도비 검정 통계량 (Likelihood Ratio Test Statistic, LRT): 두 개의 포함(nested) 모델 $M  _0$(축소)와 $M  _1$(전체)을 비교합니다.

$$ G^2 = -2(L  _0 - L  _1) $$

여기서 $L  _0$와 $L  _1$은 각각 $M  _0$와 $M  _1$의 최대화된 로그가능도입니다. $G^2$은 두 모델의 모수 개수 차이를 자유도로 갖는 $\chi^2$ 분포를 근사적으로 따릅니다.

#### 신뢰구간 (Confidence Intervals)

*   $\beta$의 95% 왈드 신뢰구간:

$$ \hat{\beta} \pm 1.96 \times \text{SE}(\hat{\beta}) $$

*   오즈비($e^\beta$)의 95% 신뢰구간: $\beta$의 신뢰구간 양 끝점에 지수 함수를 적용합니다.

$$ \exp\left( \hat{\beta} \pm 1.96 \times \text{SE}(\hat{\beta}) \right) $$

*   특정 예측 확률($\pi(x  _0)$)의 95% 신뢰구간:
    1.  먼저 $\text{logit}[\pi(x  _0)] = \alpha + \beta x  _0$의 신뢰구간을 구합니다.
        *   분산: $\text{Var}(\hat{\alpha} + \hat{\beta}x  _0) = \text{Var}(\hat{\alpha}) + x  _0^2 \text{Var}(\hat{\beta}) + 2x  _0 \text{Cov}(\hat{\alpha}, \hat{\beta})$
        *   신뢰구간 (로짓 척도): $(\hat{\alpha} + \hat{\beta}x  _0) \pm 1.96 \times \sqrt{\text{Var}(\hat{\alpha} + \hat{\beta}x  _0)}$
    2.  이 구간의 하한($L$)과 상한($U$)을 확률 척도로 역변환합니다.

$$ \left( \frac{e^L}{1+e^L}, \frac{e^U}{1+e^U} \right) $$


### 4. 다중 로지스틱 회귀 모델 (Multiple Logistic Regression)

여러 예측 변수($x  _1, \dots, x  _p$)를 포함하도록 모델을 확장합니다.

*   주효과 모델 (Main-effects Model):

$$ \text{logit}[\pi(\mathbf{x})] = \alpha + \beta  _1 x  _1 + \beta  _2 x  _2 + \dots + \beta  _p x  _p $$

$\beta  _j$는 다른 변수들이 고정되었을 때 $x  _j$의 효과(로그 오즈비)를 나타냅니다.

*   상호작용 모델 (Interaction Model): (문제 2번에서 사용됨)

$$ \text{logit}[\pi(x)] = \alpha + \beta  _1 x + \beta  _2 x^2 $$

$x^2$ 항은 $x$의 효과가 $x$의 수준에 따라 변하는 비선형 관계를 모델링합니다.

### 5. 범주형 예측 변수 처리 (Categorical Predictors)

*   ANOVA 형태 모델: $I$개 범주를 갖는 변수에 대해 $I$개의 모수를 사용합니다. 중복성 문제가 발생합니다.

$$ \text{logit}(\pi  _i) = \alpha + \beta  _i $$

*   지시 변수(Dummy Variable) 모델: 하나의 기준 범주를 설정하고 $I-1$개의 지시 변수를 사용합니다.

$$ \text{logit}(\pi) = \alpha + \beta  _1 x  _1 + \dots + \beta  _{I-1}x  _{I-1} $$

여기서 $\beta  _j = \text{logit}(\pi  _j) - \text{logit}(\pi  _I)$는 기준 범주($I$) 대비 범주 $j$의 로그 오즈비입니다.

### 6. 특수 상황에 대한 검정 (Special Cases)

*   코크란-맨텔-헨젤(CMH) 검정: 층화된 $2 \times 2 \times K$ 표에서 조건부 독립성을 검정하는 비-모델 기반 방법입니다.

$$ \text{CMH} = \frac{\left[\sum  _k (n  _{11k} - E(n  _{11k}))\right]^2}{\sum  _k \text{Var}(n  _{11k})} $$

이는 로지스틱 회귀에서 $H  _0: \beta  _{\text{효과}}=0$에 대한 스코어 검정과 점근적으로 동일합니다.

*   정확 조건부 로지스틱 회귀: 완전/준-완전 분리나 희소 데이터 문제로 MLE가 존재하지 않을 때 사용됩니다. 이는 조건부 우도(Conditional Likelihood)에 기반하여 정확한 P-값과 신뢰구간을 계산합니다. (수식이 복잡하여 개념적으로 이해)


---

### 1. 모델 구축 및 평가 관련 개념

1.  과적합 (Overfitting) vs. 과소적합 (Underfitting)
    *   과적합: 모델이 너무 복잡하여(예측 변수가 너무 많음) 실제 데이터의 근본적인 패턴뿐만 아니라 무작위적인 노이즈까지 학습하는 현상. 학습 데이터에 대한 성능은 매우 높지만, 새로운 데이터에 대한 예측력은 떨어집니다.
    *   과소적합: 모델이 너무 단순하여(중요한 예측 변수 누락) 데이터의 근본적인 패턴조차 제대로 포착하지 못하는 현상.

2.  편향-분산 상충관계 (Bias-Variance Trade-off)
    *   모델의 예측 오차는 편향(Bias)과 분산(Variance) 두 요소로 분해될 수 있습니다.
    *   편향: 모델의 예측값이 실제 값과 평균적으로 얼마나 떨어져 있는가. 단순한 모델(과소적합)일수록 편향이 큰 경향이 있습니다.
    *   분산: 데이터를 바꿀 때마다 모델의 예측값이 얼마나 많이 변동하는가. 복잡한 모델(과적합)일수록 분산이 큰 경향이 있습니다.
    *   상충관계: 편향을 줄이기 위해 모델을 복잡하게 만들면 분산이 커지고, 분산을 줄이기 위해 모델을 단순하게 만들면 편향이 커지는 관계. 좋은 모델은 이 둘 사이의 최적의 균형점을 찾는 모델입니다.

3.  정보 기준 (Information Criteria): AIC & BIC
    *   AIC (Akaike Information Criterion): $\text{AIC} = -2(\text{로그가능도}) + 2p$
    *   BIC (Bayesian Information Criterion): $\text{BIC} = -2(\text{로그가능도}) + p \log(n)$
    *   역할: 모델의 적합도(로그가능도)와 복잡성(모수 개수 $p$)을 동시에 고려하여 모델을 평가하는 지표. 값이 작을수록 더 좋은 모델로 간주됩니다.
    *   차이점: BIC는 표본 크기 $n$이 커질수록 복잡성에 더 강한 페널티를 부과하여, AIC보다 더 단순한 모델을 선택하는 경향이 있습니다.

### 2. 로지스틱 회귀의 심화 개념

1.  상호작용 효과 (Interaction Effect)
    *   정의: 한 예측 변수의 효과가 다른 예측 변수의 수준에 따라 달라지는 현상.
    *   모델: $\text{logit}(\pi) = \alpha + \beta _1 x _1 + \beta _2 x _2 + \beta _3 (x _1 x _2)$
    *   $\beta _3$가 상호작용 항의 계수입니다. 이 값이 0과 유의하게 다르면 상호작용이 존재한다고 봅니다.
    *   해석: "남성에게는 약물 A의 효과가 크지만, 여성에게는 효과가 작거나 없다"와 같이 효과가 조건에 따라 달라짐을 의미합니다.

2.  완전 분리 & 준-완전 분리 (Complete & Quasi-complete Separation)
    *   정의: 예측 변수(또는 그 조합)가 반응 변수의 결과를 완벽하게 또는 거의 완벽하게 예측하는 데이터 패턴. (6번 문제 b에서 발생)
    *   문제점: 이 경우, 특정 계수의 최대우도추정량(MLE)이 무한대($\pm\infty$)로 발산하여 존재하지 않게 됩니다. 소프트웨어는 보통 매우 큰 계수값과 거대한 표준오차를 출력하며 경고합니다.
    *   해결책: 정확 조건부 로지스틱 회귀 또는 벌점화 회귀(Penalized Regression) (예:リッジ(Ridge), 라쏘(Lasso))를 사용해야 합니다.

### 3. 가설 검정의 심화 개념

1.  검정력 (Power)
    *   정의: 대립가설이 사실일 때, 귀무가설을 올바르게 기각할 확률 ($1 - \beta$, 여기서 $\beta$는 2종 오류).
    *   의미: "실제로 효과가 있을 때, 내 연구가 그 효과를 '유의미하다'고 탐지해낼 능력"을 의미합니다. 검정력이 높은 연구 설계가 좋은 설계입니다.
    *   영향 요인: 효과 크기(Effect Size)가 클수록, 표본 크기($n$)가 클수록, 유의수준($\alpha$)이 클수록 검정력은 높아집니다.

2.  P-값 (P-value)
    *   정확한 정의: 귀무가설이 참이라고 가정했을 때, 현재 관측된 데이터와 같거나 그보다 더 극단적인 데이터가 관찰될 확률.
    *   흔한 오해: "P-값이 귀무가설이 참일 확률이다" (X), "P-값이 0.03이면 대립가설이 참일 확률이 97%다" (X). P-값은 가설 자체의 확률을 말해주지 않습니다.
    *   해석: P-값은 귀무가설에 반하는 증거의 강도를 나타내는 연속적인 척도입니다. 값이 작을수록 귀무가설에 불리한 강력한 증거가 됩니다.

3.  신뢰구간 (Confidence Interval)
    *   정확한 정의: "같은 모집단에서 표본을 무한히 반복 추출하여 매번 신뢰구간을 계산한다면, 그 구간들 중 95%는 실제 모수 값을 포함할 것이다."
    *   실용적 해석: "우리가 계산한 이 하나의 구간이 실제 모수 값을 포함할 것이라고 95% 수준으로 신뢰한다." (약간의 비약이 있지만 통용됨)
    *   P-값과의 관계: 95% 신뢰구간은 유의수준 5%의 양측 가설검정을 기각하지 못하는 모든 모수 값들의 집합입니다. 따라서 신뢰구간은 가설검정보다 더 많은 정보(효과의 크기와 불확실성)를 제공합니다.

---

### 1. 기본 연관성 측도 (2x2 표)

주어진 확률 $\pi _1$ (그룹 1의 성공 확률)과 $\pi _2$ (그룹 2의 성공 확률)에 대해:

*   비율의 차이 (Difference of Proportions): 두 확률의 절대적인 차이.

$$ \Delta\pi = \pi _1 - \pi _2 $$

*   상대위험도 (Relative Risk, RR): 한 그룹의 위험(확률)이 다른 그룹 위험의 몇 배인지.

$$ \text{RR} = \frac{\pi _1}{\pi _2} $$

*   오즈 (Odds): 성공 확률 대 실패 확률의 비.

$$ \Omega = \frac{\pi}{1-\pi} \quad \iff \quad \pi = \frac{\Omega}{1+\Omega} $$

*   오즈비 (Odds Ratio, OR): 한 그룹의 오즈가 다른 그룹 오즈의 몇 배인지.

$$ \theta = \frac{\Omega _1}{\Omega _2} = \frac{\pi _1 / (1-\pi _1)}{\pi _2 / (1-\pi _2)} $$

*   표본 오즈비 (Sample OR): $2 \times 2$ 표의 셀 빈도($n _{ij}$)를 이용한 교차곱비.

$$ \hat{\theta} = \frac{n _{11} n _{22}}{n _{12} n _{21}} $$

### 2. 분할표 분석 (I x J 표)

*   기대도수 (Expected Count): 독립성 가정 하에서.

$$ \hat{\mu} _{ij} = \frac{(i\text{행의 합계}) \times (j\text{열의 합계})}{\text{전체 합계}} = \frac{n _{i+} n _{+j}}{n} $$

*   피어슨 카이제곱 통계량 ($X^2$): 관측값과 기대값의 차이를 측정.

$$ X^2 = \sum _{i,j} \frac{(\text{관측도수} - \text{기대도수})^2}{\text{기대도수}} = \sum _{i,j} \frac{(n _{ij} - \hat{\mu} _{ij})^2}{\hat{\mu} _{ij}} $$

*   독립성 검정의 자유도 (df):

$$ \text{df} = (\text{행의 개수} - 1) \times (\text{열의 개수} - 1) $$

*   표준화 잔차 (Standardized Residual): 각 셀이 독립성에서 벗어난 정도를 $N(0,1)$ 척도로 표준화.

$$ r _{ij} = \frac{n _{ij} - \hat{\mu} _{ij}}{\sqrt{\hat{\mu} _{ij}(1 - p _{i+})(1 - p _{+j})}} \quad \text{ (여기서 } p _{i+} = \frac{n _{i+}}{n}, p _{+j} = \frac{n _{+j}}{n} \text{)} $$

### 3. 로지스틱 회귀 모델 (Logistic Regression)

*   기본 모델 (단일 예측변수):

$$ \text{logit}[\pi(x)] = \log\left(\frac{\pi(x)}{1-\pi(x)}\right) = \alpha + \beta x $$

*   확률 예측: 모델로부터 로그-오즈를 확률로 역변환.

$$ \hat{\pi}(x) = \frac{\exp(\hat{\alpha} + \hat{\beta}x)}{1 + \exp(\hat{\alpha} + \hat{\beta}x)} $$

*   계수($\beta$)와 오즈비의 관계:

$$ \text{OR} = e^\beta $$

(x가 1단위 증가할 때 오즈가 변하는 배수)

*   다중 로지스틱 회귀 모델 (주효과):

$$ \text{logit}[\pi(\mathbf{x})] = \alpha + \beta _1 x _1 + \beta _2 x _2 + \dots + \beta _p x _p $$

*   이차(Quadratic) 모델: $x$와 로그-오즈 간의 비선형 관계를 모델링.

$$ \text{logit}[\pi(x)] = \alpha + \beta _1 x + \beta _2 x^2 $$

### 4. 로지스틱 회귀의 추론 (Inference)

*   오즈비($e^\beta$)의 95% 신뢰구간 (Wald 방법):
    1.  $\beta$의 신뢰구간 계산: $\hat{\beta} \pm 1.96 \times \text{SE}(\hat{\beta})$
    2.  구간의 양 끝점에 지수 변환: $\exp(\hat{\beta} \pm 1.96 \times \text{SE}(\hat{\beta}))$

*   특정 예측 확률($\pi(x _0)$)의 95% 신뢰구간:
    1.  특정 값 $x _0$에서 로그-오즈($\eta(x _0) = \alpha + \beta x _0$)의 분산 계산:

$$ \text{Var}(\hat{\eta}(x _0)) = \text{Var}(\hat{\alpha}) + x _0^2 \text{Var}(\hat{\beta}) + 2x _0 \text{Cov}(\hat{\alpha}, \hat{\beta}) $$

    2.  로그-오즈의 신뢰구간 계산: $\hat{\eta}(x _0) \pm 1.96 \times \sqrt{\text{Var}(\hat{\eta}(x _0))}$
    3.  구간의 양 끝점($L, U$)을 확률로 역변환: $(\frac{e^L}{1+e^L}, \frac{e^U}{1+e^U})$

*   확률의 순간 변화율 (기울기): 특정 $x$ 값에서 $x$의 미세한 변화에 대한 $\pi(x)$의 변화율.

$$ \frac{d\pi(x)}{dx} = \beta \cdot \pi(x) \cdot [1-\pi(x)] $$

*   가능도비(우도비) 검정 통계량 ($G^2$): 두 포함(nested) 모델(축소 모델 $M _0$, 전체 모델 $M _1$) 비교.

$$ G^2 = -2(L _0 - L _1) = D(M _0) - D(M _1) $$

($L$: 로그가능도, $D$: 이탈도). 자유도는 두 모델의 모수 개수 차이. $\chi^2$ 분포를 따름.

### 5. 층화된 $2 \times 2$ 표 분석 (Stratified $2 \times 2$ Tables)

*   조건부 오즈비 (Conditional OR): 각 층($k$) 내에서의 오즈비.

$$ \hat{\theta} _{XY(k)} = \frac{n _{11k} n _{22k}}{n _{12k} n _{21k}} $$

*   Cochran-Mantel-Haenszel (CMH) 검정 통계량: 조건부 독립성 검정 ($H _0$: 공통 오즈비=1).

$$ \text{CMH} = \frac{\left[ \sum _k (n _{11k} - E(n _{11k})) \right]^2}{\sum _k \text{Var}(n _{11k})} $$

*   기대값: $E(n _{11k}) = \frac{n _{1+k}n _{+1k}}{n _{++k}}$
*   분산: $\text{Var}(n _{11k}) = \frac{n _{1+k}n _{2+k}n _{+1k}n _{+2k}}{n _{++k}^2(n _{++k}-1)}$
    *   이 통계량은 자유도 1인 $\chi^2$ 분포를 따릅니다.

*   Breslow-Day 검정 통계량: 오즈비의 동질성 검정 ($H _0: \theta _1 = \theta _2 = \dots = \theta _K$).

$$ X^2 _{BD} = \sum _{k=1}^{K} \frac{[n _{11k} - E(n _{11k} | \hat{\theta} _{MH})]^2}{\text{Var}(n _{11k} | \hat{\theta} _{MH})} $$

*   이 검정은 계산이 복잡하며, 보통 통계 소프트웨어를 통해 수행합니다. 여기서 기대값과 분산은 Mantel-Haenszel 공통 오즈비($\hat{\theta} _{MH}$)가 주어졌을 때의 비중심 초기하분포로부터 계산됩니다.
    *   이 통계량은 자유도가 $K-1$ (층의 개수 - 1)인 $\chi^2$ 분포를 따릅니다.

*   Mantel-Haenszel 공통 오즈비 추정량:

$$ \hat{\theta} _{MH} = \frac{\sum _k (n _{11k}n _{22k}/n _{++k})}{\sum _k (n _{12k}n _{21k}/n _{++k})} $$

($n _{++k}$는 $k$번째 층의 총합)

