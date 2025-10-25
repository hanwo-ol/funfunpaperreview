### 목표

우리의 목표는 PRE 구조

$$ \frac{V(Y) - E[V(Y|X)]}{V(Y)} \quad \cdots \text{(식 2.12)} $$

에서 변동(Variation)의 척도로 엔트로피(Entropy)를 사용하여, 불확실성 계수 $U$의 공식

$$ U = \frac{\sum_i\sum_j \pi _{ij}\log(\pi _{ij}/\pi _{i+}\pi _{+j})}{-\sum_j \pi _{+j}\log\pi _{+j}} \quad \cdots \text{(식 2.13)} $$

를 유도하는 것입니다.

### 1단계: 변동 척도 V(·)를 엔트로피로 정의하기

Theil(1970)은 명목형 변수의 변동성 또는 불확실성을 측정하는 척도로 정보 이론의 엔트로피를 제안했습니다. 어떤 확률분포 $\{\pi_j\}$에 대한 엔트로피는 다음과 같이 정의됩니다.

$$ H(\pi) = - \sum_j \pi_j \log(\pi_j) $$

*   엔트로피의 의미: 분포의 "무질서도" 또는 "불확실성"의 정도.
    *   최소 엔트로피 (0): 하나의 $\pi_j$가 1이고 나머지가 모두 0일 때. 결과가 무엇일지 100% 확신할 수 있는 상태. 불확실성이 전혀 없음.
    *   최대 엔트로피: 모든 $\pi_j$가 $1/J$로 동일할 때 (균등 분포). 결과를 전혀 예측할 수 없는 가장 불확실한 상태.

이제 PRE 공식의 각 부분에 엔트로피를 적용해 봅시다.

### 2단계: V(Y) 계산하기 (분모)

$V(Y)$는 반응 변수 Y의 주변분포(marginal distribution) $\{\pi _{+j}\}$의 변동성입니다. 따라서 엔트로피 공식을 Y의 주변분포에 적용합니다.

$$ V(Y) = H(\pi _{+j}) = - \sum_j \pi _{+j} \log(\pi _{+j}) $$

이것이 식 (2.13)의 분모 부분입니다.

### 3단계: E[V(Y|X)] 계산하기

이 부분은 두 단계로 나뉩니다.

3a. 조건부 변동 V(Y|X=i) 계산
$V(Y|X=i)$는 설명 변수 X가 특정 범주 $i$로 고정되었을 때, Y의 조건부 분포(conditional distribution) $\{\pi _{j|i}\}$의 변동성입니다. 따라서 엔트로피 공식을 Y의 조건부 분포에 적용합니다.

$$ V(Y|X=i) = H(\pi _{j|i}) = - \sum_j \pi _{j|i} \log(\pi _{j|i}) $$

3b. 조건부 변동의 기댓값 E[V(Y|X)] 계산
이제 각 하위 그룹($X=i$)의 변동성 $V(Y|X=i)$를, 해당 그룹이 나타날 확률($\pi _{i+}$)을 가중치로 사용하여 평균을 냅니다.

$$ E[V(Y|X)] = \sum_i \pi _{i+} V(Y|X=i) $$

$$ = \sum_i \pi _{i+} \left( - \sum_j \pi _{j|i} \log(\pi _{j|i}) \right) $$

$$ = - \sum_i \sum_j \pi _{i+} \pi _{j|i} \log(\pi _{j|i}) $$

여기서 조건부 확률의 정의($\pi _{ij} = \pi _{i+} \pi _{j|i}$)를 사용하여 $\pi _{i+}\pi _{j|i}$를 $\pi _{ij}$로 바꿀 수 있습니다.

$$ E[V(Y|X)] = - \sum_i \sum_j \pi _{ij} \log(\pi _{j|i}) $$

또한, $\pi _{j|i} = \pi _{ij} / \pi _{i+}$ 이므로 이를 대입하면 다음과 같이 쓸 수도 있습니다.

$$ E[V(Y|X)] = - \sum_i \sum_j \pi _{ij} \log(\pi _{ij} / \pi _{i+}) $$

### 4단계: V(Y) - E[V(Y|X)] 계산하기 (분자)

이제 2단계와 3단계에서 구한 결과를 <_blank>뺍니다.

$$ V(Y) - E[V(Y|X)] = \left( - \sum_j \pi _{+j} \log(\pi _{+j}) \right) - \left( - \sum_i \sum_j \pi _{ij} \log(\pi _{j|i}) \right) $$

$$ = \sum_i \sum_j \pi _{ij} \log(\pi _{j|i}) - \sum_j \pi _{+j} \log(\pi _{+j}) $$

여기서 주변 확률의 정의($\pi _{+j} = \sum_i \pi _{ij}$)를 사용하여 두 번째 항을 이중 합계로 바꿀 수 있습니다.

$$ = \sum_i \sum_j \pi _{ij} \log(\pi _{j|i}) - \sum_i \sum_j \pi _{ij} \log(\pi _{+j}) $$

합계 기호로 묶고 로그의 성질($\log a - \log b = \log(a/b)$)을 사용합니다.

$$ = \sum_i \sum_j \pi _{ij} \left( \log(\pi _{j|i}) - \log(\pi _{+j}) \right) $$

$$ = \sum_i \sum_j \pi _{ij} \log\left(\frac{\pi _{j|i}}{\pi _{+j}}\right) $$

마지막으로, 조건부 확률의 정의 $\pi _{j|i} = \pi _{ij}/\pi _{i+}$를 대입합니다.

$$ = \sum_i \sum_j \pi _{ij} \log\left(\frac{\pi _{ij}/\pi _{i+}}{\pi _{+j}}\right) = \sum_i \sum_j \pi _{ij} \log\left(\frac{\pi _{ij}}{\pi _{i+}\pi _{+j}}\right) $$

이것이 바로 식 (2.13)의 분자 부분입니다. 이 양은 정보 이론에서 상호 정보량(Mutual Information)이라고 불리며, X를 앎으로써 Y에 대해 얻게 되는 정보의 양을 의미합니다.

### 5단계: 최종 공식 조립

이제 4단계에서 구한 분자와 2단계에서 구한 분모를 합치면 불확실성 계수 $U$의 공식이 완성됩니다.
$$ U = \frac{V(Y) - E[V(Y|X)]}{V(Y)} = \frac{\sum_i\sum_j \pi _{ij}\log(\pi _{ij}/\pi _{i+}\pi _{+j})}{-\sum_j \pi _{+j}\log\pi _{+j}} $$

이것으로 식 (2.13)의 유도가 완료되었습니다. 이 과정은 PRE라는 일반적인 통계적 원리가, 변동성의 척도로 '엔트로피'라는 구체적인 도구를 만났을 때 어떻게 '불확실성 계수'라는 특정 연관성 측도로 구체화되는지를 보여줍니다.
