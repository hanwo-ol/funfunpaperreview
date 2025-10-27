### **2.1.1 독립을 위한 충분 조건 (Sufficient Conditions for Independence)**

우리의 주된 결과는 정리 2.1.7입니다. 그 결과를 기술하기 위해, 우리의 이전 모든 정의들을 일반화하는 정의가 필요합니다.

집합들의 모임(collections of sets) $\mathcal{A}_1, \mathcal{A}_2, \dots, \mathcal{A}_n \subset \mathcal{F}$가 **독립(independent)**이라고 하는 것은, $A_i \in \mathcal{A}_i$이고 $I \subset \{1, \dots, n\}$일 때마다 $P(\cap_{i \in I} A_i) = \prod_{i \in I} P(A_i)$가 성립하는 경우입니다.

만약 각 모임이 단일 집합, 즉 $\mathcal{A}_i = \{A_i\}$이면, 이 정의는 집합들에 대한 정의로 축소됩니다.

**보조정리 2.1.5.** 일반성을 잃지 않고 각 $\mathcal{A}_i$가 $\Omega$를 포함한다고 가정할 수 있다. 이 경우, 조건은 다음 문장과 동치이다.

$$ P(\cap_{i=1}^n A_i) = \prod_{i=1}^n P(A_i) \quad \text{whenever } A_i \in \mathcal{A}_i $$

왜냐하면 우리는 $i \notin I$인 경우에 $A_i = \Omega$로 둘 수 있기 때문이다.


**증명.** 만약 $\mathcal{A}_1, \mathcal{A}_2, \dots, \mathcal{A}_n$이 독립이고 $\bar{\mathcal{A}}_i = \mathcal{A}_i \cup \{\Omega\}$이면, $\bar{\mathcal{A}}_1, \bar{\mathcal{A}}_2, \dots, \bar{\mathcal{A}}_n$은 독립이다. 왜냐하면 만약 $A_i \in \bar{\mathcal{A}}_i$이고 $I=\{j: A_j \neq \Omega\}$이면 $\cap_{i \in I} A_i = \cap_{i \in I_0} A_i$ (여기서 $I_0$는 원래 $I$ 중 $\Omega$가 아닌 것들만 모은 인덱스)이기 때문이다. ◻ (원문 오타 수정: 원문의 $\cap_i A_i = \cap_{i \in I} A_i$는 $I_0$를 사용하는 것이 더 명확합니다.)

**[해설 및 추가 설명]**
*   **다수 모임의 독립성**: 이 정의는 두 사건의 독립성, 두 확률 변수의 독립성, 두 $\sigma$-필드의 독립성을 하나의 틀로 통합합니다. 예를 들어,
    *   **사건들의 독립**: $\mathcal{A}_i = \{A_i, A_i^c\}$
    *   **확률 변수들의 독립**: $\mathcal{A}_i = \sigma(X_i)$
*   **보조정리 2.1.5의 의미**: 부분집합 $I$에 대해 매번 확인할 필요 없이, 전체 곱에 대해서만 확인하면 된다는 것을 보여주어 증명을 간결하게 만듭니다. 전체 공간 $\Omega$는 확률이 1이므로 곱셈에 영향을 주지 않기 때문입니다.

---

정리 2.1.7의 증명은 **딘킨의 $\pi-\lambda$ 정리(Dynkin's $\pi-\lambda$ theorem)**에 기반합니다. 이 결과를 기술하기 위해, 두 가지 정의가 필요합니다.
$\mathcal{A}$가 교집합에 대해 닫혀 있을 때, 즉 $A, B \in \mathcal{A}$이면 $A \cap B \in \mathcal{A}$일 때, $\mathcal{A}$는 **$\pi$-시스템($\pi$-system)**이라고 합니다.
$\mathcal{L}$이 다음을 만족할 때 **$\lambda$-시스템($\lambda$-system)**이라고 합니다:

(i) $\Omega \in \mathcal{L}$.

(ii) 만약 $A, B \in \mathcal{L}$이고 $A \subset B$이면 $B-A \in \mathcal{L}$.

(iii) 만약 $A_n \in \mathcal{L}$이고 $A_n \uparrow A$이면 $A \in \mathcal{L}$.

**정리 2.1.6. $\pi-\lambda$ 정리.** 만약 $\mathcal{P}$가 $\pi$-시스템이고 $\mathcal{L}$이 $\mathcal{P}$를 포함하는 $\lambda$-시스템이면, $\sigma(\mathcal{P}) \subset \mathcal{L}$이다.

증명은 부록 A.1절에 숨겨져 있습니다.

**[해설 및 추가 설명]**
*   **$\pi-\lambda$ 정리의 강력함**: 이 정리는 측도론과 확률론에서 매우 강력한 도구입니다. 어떤 속성(이 경우엔 독립성)이 비교적 다루기 쉬운 집합들의 모임($\pi$-시스템) 위에서 성립하고, 그 속성을 가진 집합들의 모임이 $\lambda$-시스템의 조건을 만족한다면, 그 속성은 훨씬 더 복잡한, $\pi$-시스템이 생성하는 전체 $\sigma$-필드 위에서도 성립한다는 것을 보장해 줍니다. 즉, 간단한 경우에 성립함을 보이면 복잡한 경우로 자동 확장됩니다.

---

**정리 2.1.7.** $\mathcal{A}_1, \mathcal{A}_2, \dots, \mathcal{A}_n$이 독립이고 각각이 $\pi$-시스템이라고 가정하자. 그러면 $\sigma(\mathcal{A}_1), \sigma(\mathcal{A}_2), \dots, \sigma(\mathcal{A}_n)$은 독립이다.

**증명.** $A_i \in \mathcal{A}_i$인 집합 $A_2, \dots, A_n$을 잡고, $F = A_2 \cap \dots \cap A_n$이라 하고, $\mathcal{L} = \{A : P(A \cap F) = P(A)P(F)\}$라고 하자. $P(\Omega \cap F) = P(\Omega)P(F)$이므로, $\Omega \in \mathcal{L}$이다.
$\lambda$-시스템의 (ii)를 확인하기 위해, 만약 $A, B \in \mathcal{L}$이고 $A \subset B$이면 $(B-A) \cap F = (B \cap F) - (A \cap F)$임을 주목하자. 따라서 정리 1.1.1의 (i), $A, B \in \mathcal{L}$이라는 사실, 그리고 다시 정리 1.1.1의 (i)을 사용하여,

$$ \begin{aligned} P((B-A) \cap F) &= P(B \cap F) - P(A \cap F) = P(B)P(F) - P(A)P(F) \\ &= \{P(B) - P(A)\}P(F) = P(B-A)P(F) \end{aligned} $$

이고 우리는 $B-A \in \mathcal{L}$임을 얻는다.

(iii)을 확인하기 위해, $B_k \in \mathcal{L}$이고 $B_k \uparrow B$라 하고, $(B_k \cap F) \uparrow (B \cap F)$임을 주목하자. 따라서 정리 1.1.1의 (iii), $B_k \in \mathcal{L}$이라는 사실, 그리고 다시 정리 1.1.1의 (iii)을 사용하여,

$$ P(B \cap F) = \lim_k P(B_k \cap F) = \lim_k P(B_k)P(F) = P(B)P(F) $$

이제 $\pi-\lambda$ 정리를 적용하면 $\mathcal{L} \supset \sigma(\mathcal{A}_1)$을 얻는다. 이로부터 만약 $A_1 \in \sigma(\mathcal{A}_1)$이고 $2 \le i \le n$에 대해 $A_i \in \mathcal{A}_i$이면 다음이 성립한다.

$$ P(\cap_{i=1}^n A_i) = P(A_1)P(\cap_{i=2}^n A_i) = \prod_{i=1}^n P(A_i) $$

이제 보조정리 2.1.5를 사용하면, 다음을 얻는다:

($\star$) 만약 $\mathcal{A}_1, \mathcal{A}_2, \dots, \mathcal{A}_n$이 독립이면, $\sigma(\mathcal{A}_1), \mathcal{A}_2, \dots, \mathcal{A}_n$은 독립이다.

($\star$)를 $\mathcal{A}_2, \dots, \mathcal{A}_n, \sigma(\mathcal{A}_1)$에 적용하면 (정의는 순서를 바꿔도 변하지 않으므로 이들은 독립이다) $\sigma(\mathcal{A}_2), \mathcal{A}_3, \dots, \mathcal{A}_n, \sigma(\mathcal{A}_1)$이 독립임을 보이고, $n$ 번의 반복 후에 우리는 원하는 결과를 얻는다. ◻

**[해설 및 추가 설명]**
*   **증명의 핵심 전략**:
    1.  한 번에 하나의 모임만 $\sigma$-필드로 확장합니다. 먼저 $\mathcal{A}_1$이 $\sigma(\mathcal{A}_1)$으로 바뀌어도 독립성이 유지됨을 보입니다.
    2.  이를 위해 $\pi-\lambda$ 정리를 사용합니다. $\mathcal{L}$을 "독립성을 유지하는 좋은 집합들"의 모임으로 정의하고, 이것이 $\lambda$-시스템임을 보입니다.
    3.  $\mathcal{A}_1$은 $\pi$-시스템이고 $\mathcal{L}$에 포함되므로, $\sigma(\mathcal{A}_1)$ 전체가 $\mathcal{L}$에 포함됩니다. 즉, $\sigma(\mathcal{A}_1)$의 모든 원소들이 독립성을 유지합니다.
    4.  이 과정을 $\mathcal{A}_2, \mathcal{A}_3, \dots, \mathcal{A}_n$에 대해 반복하여 모든 모임을 $\sigma$-필드로 확장합니다.

---

정리 2.1.7을 확립하기 위해 노력한 결과, 우리는 몇 가지 중요한 따름정리들을 얻습니다.

**정리 2.1.8.** 확률 변수 $X_1, \dots, X_n$이 독립이기 위해서는, 모든 $x_1, \dots, x_n \in (-\infty, \infty]$에 대해 다음이 성립하는 것이 충분하다.

$$ P(X_1 \le x_1, \dots, X_n \le x_n) = \prod_{i=1}^n P(X_i \le x_i) $$

**증명.** $\mathcal{A}_i$를 $\{X_i \le x_i\}$ 형태의 집합들의 모임으로 하자.

$$ \{X_i \le x\} \cap \{X_i \le y\} = \{X_i \le x \wedge y\} $$

이므로 (여기서 $(x \wedge y)_i = x_i \wedge y_i = \min\{x_i, y_i\}$), $\mathcal{A}_i$는 $\pi$-시스템이다. 우리가 $x_i = \infty$를 허용했으므로, $\Omega \in \mathcal{A}_i$이다. 연습문제 1.3.1은 $\sigma(\mathcal{A}_i) = \sigma(X_i)$임을 암시하므로, 결과는 정리 2.1.7로부터 따라나온다. ◻

마지막 결과는 확률 변수들의 독립성을 그들의 분포 함수를 통해 표현합니다. 연습문제 2.1.1과 2.1.2는 밀도 함수와 이산 확률 변수들을 다룹니다.

**[해설 및 추가 설명]**
*   **정리 2.1.8의 실용성**: 이 정리는 확률 변수들의 독립성을 보이는 작업을 매우 단순하게 만들어줍니다. 모든 가능한 보렐 집합에 대해 $P(X_1 \in B_1, \dots) = \prod P(X_i \in B_i)$를 보이는 대신, 단순히 결합 누적 분포 함수(joint CDF)가 각 주변 누적 분포 함수(marginal CDF)의 곱으로 표현되는지만 확인하면 됩니다. 이는 실용적인 계산에서 독립성을 확인하는 가장 표준적인 방법입니다.

---

우리의 다음 목표는 독립 확률 변수들의 서로소 모임들의 함수들이 독립임을 증명하는 것입니다. 정확한 내용은 정리 2.1.10을 참조하십시오. 먼저 $\sigma$-필드에 대한 유사한 결과를 증명할 것입니다.

**정리 2.1.9.** $\mathcal{F}_{i,j}$, $1 \le i \le n$, $1 \le j \le m(i)$가 독립이고 $\mathcal{G}_i = \sigma(\cup_j \mathcal{F}_{i,j})$라고 하자. 그러면 $\mathcal{G}_1, \dots, \mathcal{G}_n$은 독립이다.

**증명.** $\mathcal{A}_i$를 $A_{i,j} \in \mathcal{F}_{i,j}$일 때 $\cap_j A_{i,j}$ 형태의 집합들의 모임으로 하자. $\mathcal{A}_i$는 $\Omega$를 포함하고 $\cup_j \mathcal{F}_{i,j}$를 포함하는 $\pi$-시스템이므로, 정리 2.1.7은 $\sigma(\mathcal{A}_i) = \mathcal{G}_i$가 독립임을 암시한다. ◻

**정리 2.1.10.** 만약 $1 \le i \le n, 1 \le j \le m(i)$에 대해 $X_{i,j}$들이 독립이고 $f_i: \mathbb{R}^{m(i)} \to \mathbb{R}$이 가측 함수이면, $f_i(X_{i,1}, \dots, X_{i, m(i)})$들은 독립이다.

**증명.** $\mathcal{F}_{i,j} = \sigma(X_{i,j})$이고 $\mathcal{G}_i = \sigma(\cup_j \mathcal{F}_{i,j})$라고 하자. $f_i(X_{i,1}, \dots, X_{i,m(i)}) \in \mathcal{G}_i$이므로, 원하는 결과는 정리 2.1.9와 연습문제 2.1.1로부터 따라나온다. ◻

정리 2.1.10의 구체적인 특별한 경우로서 우리가 곧 사용할 것은 다음과 같다: 만약 $X_1, \dots, X_n$이 독립이면, $X=X_1$과 $Y=X_2 \cdots X_n$은 독립이다. 나중에, 독립 확률 변수 $X_1, \dots, X_n$의 합 $S_m = X_1 + \dots + X_m$을 연구할 때, 우리는 정리 2.1.10을 사용하여 만약 $m<n$이면 $S_n - S_m$이 사건 $\{\max_{1 \le k \le m} S_k > x\}$의 지시 함수와 독립임을 결론지을 것이다.

**[해설 및 추가 설명]**
*   **정리 2.1.9 & 2.1.10 (독립성 묶기)**: 이 두 정리는 독립성의 매우 중요한 "묶기(grouping)" 속성을 보여줍니다.
    *   **직관적 설명**: 만약 우리가 서로 아무 관련이 없는 여러 개의 작은 정보 묶음들($\mathcal{F}_{i,j}$)을 가지고 있다면, 이들을 몇 개의 큰 덩어리($\mathcal{G}_i$)로 묶어도 그 큰 덩어리들끼리는 여전히 서로 아무 관련이 없습니다.
    *   **예시**: $X_1, X_2, X_3, X_4$가 모두 독립이라고 합시다. 정리 2.1.10에 따르면, $X_1+X_2$와 $X_3-X_4$는 독립입니다. 왜냐하면 첫 번째 함수는 $\{X_1, X_2\}$에만 의존하고 두 번째 함수는 $\{X_3, X_4\}$에만 의존하며, 이 두 그룹은 서로소이기 때문입니다. 이 속성은 확률 과정 이론, 특히 마팅게일이나 마르코프 연쇄를 다룰 때 매우 빈번하게 사용됩니다.
