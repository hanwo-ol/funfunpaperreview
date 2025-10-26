4.5.1절의 이탈도(Deviance) 공식이 어떻게 유도되고, 그것이 어떻게 척도화된 이탈도(Scaled Deviance) 공식 (4.33)으로 이어지는지

---

### 목표

우리의 목표는 이탈도의 정의로부터 시작하여,
$$ \text{이탈도} = -2[L(\hat{\boldsymbol{\mu}};\mathbf{y}) - L(\mathbf{y};\mathbf{y})] $$
지수 분산족(EDF)의 일반적인 로그우도 공식을 대입하여 다음 식을 유도하는 것입니다.
$$ = 2\sum_i \frac{y_i(\tilde{\theta}_i - \hat{\theta}_i) - [b(\tilde{\theta}_i)-b(\hat{\theta}_i)]}{a(\phi)} $$
그리고 최종적으로 이것이 척도화된 이탈도 (4.33)와 어떻게 연결되는지 보이는 것입니다.
$$ \text{척도화된 이탈도} = \frac{D(\mathbf{y};\hat{\boldsymbol{\mu}})}{\phi} = \frac{2\sum_i \omega_i \{y_i(\tilde{\theta}_i-\hat{\theta}_i) - [b(\tilde{\theta}_i)-b(\hat{\theta}_i)]\}}{\phi} $$

---

### 시작점: 로그우도 함수 (EDF 형태)

지수 분산족(EDF)에 속하는 N개의 독립적인 관측치에 대한 전체 로그우도 함수 $L$은 각 관측치의 로그우도 $L_i$의 합입니다 (식 4.22 참조).
$$ L(\boldsymbol{\theta}, \phi; \mathbf{y}) = \sum_{i=1}^N L_i = \sum_{i=1}^N \left[ \frac{y_i\theta_i - b(\theta_i)}{a(\phi)} + c(y_i, \phi) \right] $$

### 1단계: 이탈도의 두 구성 요소 계산하기

이탈도 공식은 두 가지 로그우도 값의 차이를 필요로 합니다.

**1a. $L(\hat{\boldsymbol{\mu}};\mathbf{y})$: 내가 만든 모델의 최대 로그우도**
*   이것은 내가 설정한 모델(예: $\text{logit}(\pi_i) = \alpha + \beta x_i$)을 데이터에 적합시켜 얻은 최대우도 추정치 $\hat{\boldsymbol{\beta}}$를 사용했을 때의 로그우도 값입니다.
*   이 $\hat{\boldsymbol{\beta}}$는 $\hat{\eta}_i$를 결정하고, 이는 다시 $\hat{\mu}_i$를, 그리고 최종적으로 $\hat{\theta}_i$를 결정합니다.
*   따라서, 이 로그우도 값은 다음과 같이 쓸 수 있습니다.
    $$ L(\hat{\boldsymbol{\mu}};\mathbf{y}) = \sum_{i=1}^N \left[ \frac{y_i\hat{\theta}_i - b(\hat{\theta}_i)}{a(\phi)} + c(y_i, \phi) \right] $$

**1b. $L(\mathbf{y};\mathbf{y})$: 포화 모델의 최대 로그우도**
*   포화 모델(Saturated Model)은 데이터를 완벽하게 설명하는 모델로, 각 관측치 $y_i$를 그 평균의 추정치로 사용합니다: $\tilde{\mu}_i = y_i$.
*   이 포화 모델의 적합에 해당하는 자연 모수를 $\tilde{\theta}_i$라고 합시다. (즉, $\tilde{\theta}_i$는 $b'(\tilde{\theta}_i) = y_i$를 만족하는 값입니다.)
*   따라서, 포화 모델의 최대 로그우도 값은 다음과 같습니다.
    $$ L(\mathbf{y};\mathbf{y}) = \sum_{i=1}^N \left[ \frac{y_i\tilde{\theta}_i - b(\tilde{\theta}_i)}{a(\phi)} + c(y_i, \phi) \right] $$

### 2단계: 이탈도 공식에 대입 및 전개

이제 이 두 로그우도 값을 이탈도 정의 $-2[L(\hat{\boldsymbol{\mu}};\mathbf{y}) - L(\mathbf{y};\mathbf{y})]$에 대입합니다.

$$ \text{이탈도} = -2 \left\{ \left( \sum_i \frac{y_i\hat{\theta}_i - b(\hat{\theta}_i)}{a(\phi)} + \sum_i c(y_i, \phi) \right) - \left( \sum_i \frac{y_i\tilde{\theta}_i - b(\tilde{\theta}_i)}{a(\phi)} + \sum_i c(y_i, \phi) \right) \right\} $$

*   **$c(y_i, \phi)$ 항 상쇄**: 괄호를 풀면, $\sum_i c(y_i, \phi)$ 항은 양쪽 모두에 있으므로 서로 상쇄되어 사라집니다.

$$ = -2 \left\{ \sum_i \frac{y_i\hat{\theta}_i - b(\hat{\theta}_i)}{a(\phi)} - \sum_i \frac{y_i\tilde{\theta}_i - b(\tilde{\theta}_i)}{a(\phi)} \right\} $$

*   **합계 기호($\sum$)로 묶기**: 두 합계를 하나로 합칩니다. 분모 $a(\phi)$는 공통입니다.

$$ = -2 \sum_i \frac{[y_i\hat{\theta}_i - b(\hat{\theta}_i)] - [y_i\tilde{\theta}_i - b(\tilde{\theta}_i)]}{a(\phi)} $$

*   **마이너스 부호 처리**: 괄호 앞의 $-2$에서 $-1$을 괄호 안으로 넣어 뺄셈의 순서를 바꿉니다.

$$ = 2 \sum_i \frac{[y_i\tilde{\theta}_i - b(\tilde{\theta}_i)] - [y_i\hat{\theta}_i - b(\hat{\theta}_i)]}{a(\phi)} $$

*   **항 재배열**: $y_i$를 포함하는 항과 $b(\theta)$를 포함하는 항으로 다시 묶습니다.

$$ = 2 \sum_i \frac{(y_i\tilde{\theta}_i - y_i\hat{\theta}_i) - (b(\tilde{\theta}_i) - b(\hat{\theta}_i))}{a(\phi)} $$
$$ = 2 \sum_i \frac{y_i(\tilde{\theta}_i - \hat{\theta}_i) - [b(\tilde{\theta}_i) - b(\hat{\theta}_i)]}{a(\phi)} $$

이것이 바로 본문의 첫 번째 목표 공식입니다. 이 공식은 어떤 지수 분산족에 속하는 GLM에 대해서도 성립하는 **이탈도(Deviance)의 일반적인 정의**입니다.

---

### 3단계: 척도화된 이탈도 (식 4.33)로의 연결

이제 이 일반 공식을, 분산 함수 $a(\phi)$가 특별한 형태를 갖는 경우에 적용합니다.

**가정**: $a(\phi) = \phi / \omega_i$
*   **$\phi$ (분산 모수, dispersion parameter)**: 분포의 전반적인 분산을 조절하는 상수. 푸아송, 이항에서는 $\phi=1$. 정규분포에서는 $\phi=\sigma^2$.
*   **$\omega_i$ (가중치, weight)**: 각 관측치 $i$에 대한 알려진 가중치.
    *   **이항 비율**: $Y_i$가 $n_i$번 시행의 비율일 때, $\omega_i = n_i$ 입니다. (그래서 $a(\phi) = 1/n_i$)
    *   **단일 관측치**: 각 관측치가 동등한 중요도를 가질 때, $\omega_i=1$ 입니다. (그래서 $a(\phi)=\phi$)

**유도 과정**:
1.  **$a(\phi)$ 대입**: 이탈도 공식의 $a(\phi)$ 자리에 $\phi/\omega_i$를 대입합니다.
    $$ \text{이탈도} = 2 \sum_i \frac{y_i(\tilde{\theta}_i - \hat{\theta}_i) - [b(\tilde{\theta}_i) - b(\hat{\theta}_i)]}{\phi / \omega_i} $$

2.  **식 정리**: 분모의 분수를 정리하면 $\omega_i$가 분자로 올라갑니다.
    $$ = \frac{2 \sum_i \omega_i \{ y_i(\tilde{\theta}_i - \hat{\theta}_i) - [b(\tilde{\theta}_i) - b(\hat{\theta}_i)] \}}{\phi} $$

3.  **척도화된 이탈도와 이탈도 정의**:
    *   본문에서는 이 전체 양을 **척도화된 이탈도(Scaled Deviance)**라고 부릅니다.
    *   그리고 이 식의 **분자 부분**, 즉 $\phi$를 제외한 부분을 **이탈도(Deviance)** $D(\mathbf{y};\hat{\boldsymbol{\mu}})$로 재정의합니다.
        $$ D(\mathbf{y};\hat{\boldsymbol{\mu}}) = 2 \sum_i \omega_i \{ y_i(\tilde{\theta}_i - \hat{\theta}_i) - [b(\tilde{\theta}_i) - b(\hat{\theta}_i)] \} $$
    *   따라서,
        $$ \text{척도화된 이탈도} = \frac{D(\mathbf{y};\hat{\boldsymbol{\mu}})}{\phi} $$

이것이 바로 식 (4.33)입니다.

**요약 및 결론**:
1.  **이탈도(Deviance)**는 본질적으로 (포화 모델의 로그우도)와 (내 모델의 로그우도)의 차이에 -2를 곱한 **우도비 통계량**입니다.
2.  이 정의를 지수 분산족의 일반 공식에 적용하면, 이탈도가 $\theta$와 $b(\theta)$ 함수들의 차이로 표현됨을 보일 수 있습니다.
3.  분산 함수 $a(\phi)$가 $\phi/\omega_i$ 형태를 가질 때, 전체 양은 $\phi$로 나누어진 형태가 됩니다.
4.  통계학자들은 편의상 $\phi$를 제외한 부분을 **이탈도($D$)**라고 부르고, 전체 양($D/\phi$)을 **척도화된 이탈도**라고 부르기로 약속했습니다.
5.  푸아송이나 이항 모델처럼 $\phi=1$인 경우, **이탈도와 척도화된 이탈도는 같습니다.** 정규분포 모델처럼 $\phi=\sigma^2$을 추정해야 하는 경우, 두 값은 달라집니다.
