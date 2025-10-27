## 제1장 측도론 (Measure Theory)

이 장에서는 측도론의 몇 가지 정의와 결과들을 다시 살펴볼 것입니다. 여기서의 목적은 이 개념들을 이전에 접해보지 못한 독자들에게 입문을 제공하고, 이미 본 적이 있는 독자들에게는 해당 내용을 복습하는 것입니다. 더 어려운 증명들, 특히 직관에 크게 기여하지 않는 것들은 부록에 숨겨져 있습니다. 측도론에 대한 탄탄한 배경 지식이 있는 독자들은 이전에 부록의 일부였던 1.4절, 1.5절, 1.7절을 건너뛰어도 좋습니다.

---

### **1.1 확률 공간 (Probability Spaces)**

여기서부터 책 전체에 걸쳐, 정의되는 용어는 **굵은 글씨체**로 표시됩니다. 우리는 가장 기본적인 양(quantity)부터 시작하겠습니다.

**확률 공간(probability space)** 은 삼중쌍(triple) $(\Omega, \mathcal{F}, P)$입니다. 여기서 $\Omega$는 "결과(outcomes)"의 집합이고, $\mathcal{F}$는 "사건(events)"의 집합이며, $P: \mathcal{F} \rightarrow [0, 1]$은 사건에 확률을 할당하는 함수입니다.

우리는 $\mathcal{F}$가 **$\sigma$-필드($\sigma$-field)** (또는 **$\sigma$-대수($\sigma$-algebra)**)라고 가정합니다. 즉, $\Omega$의 부분집합들로 이루어진 (공집합이 아닌) 모임(collection)으로서 다음을 만족합니다:

(i) 만약 $A \in \mathcal{F}$이면 $A^c \in \mathcal{F}$이다. (여집합에 대해 닫혀 있다)

(ii) 만약 $A_i \in \mathcal{F}$가 가산 개의(countable) 집합들의 열(sequence)이면, $\cup_i A_i \in \mathcal{F}$이다. (가산 합집합에 대해 닫혀 있다)

여기서 그리고 앞으로, **가산(countable)** 이라는 것은 유한(finite)이거나 가산 무한(countably infinite)임을 의미합니다. $\cap_i A_i = (\cup_i A_i^c)^c$ 이므로, $\sigma$-필드는 가산 교집합에 대해서도 닫혀 있다는 것을 알 수 있습니다. 우리는 정의를 확인하기 더 쉽게 만들기 위해 마지막 속성(가산 교집합)은 정의에서 생략합니다.

$P$가 없는 $(\Omega, \mathcal{F})$는 **가측 공간(measurable space)** 이라고 불립니다. 즉, 우리가 측도를 부여할 수 있는 공간입니다. **측도(measure)** 는 비음의 가산가법적인 집합 함수(nonnegative countably additive set function)입니다. 즉, 함수 $\mu: \mathcal{F} \rightarrow \mathbb{R}$이 다음을 만족합니다:

(i) 모든 $A \in \mathcal{F}$에 대해 $\mu(A) \ge \mu(\emptyset) = 0$이다.

(ii) 만약 $A_i \in \mathcal{F}$가 가산 개의 서로소인(disjoint) 집합들의 열이라면,

$$ \mu(\cup_i A_i) = \sum_i \mu(A_i) $$

**[해설 및 추가 설명]**

*   **확률 공간 $(\Omega, \mathcal{F}, P)$**: 현대 확률론의 근간을 이루는 가장 중요한 개념입니다.
    *   **$\Omega$ (표본 공간, Sample Space)**: 확률적 실험에서 나올 수 있는 모든 가능한 결과들의 집합입니다. 예를 들어, 동전 던지기에서는 {앞, 뒤}, 주사위 던지기에서는 {1, 2, 3, 4, 5, 6}이 됩니다.
    *   **$\mathcal{F}$ (사건 공간, Event Space, $\sigma$-field)**: 우리가 확률을 측정하고 싶은 대상인 '사건'들의 모임입니다. 사건은 표본 공간 $\Omega$의 부분집합입니다. 예를 들어, 주사위 던지기에서 '짝수가 나오는 사건'은 {2, 4, 6}입니다.
        *   **왜 그냥 부분집합의 모임이 아니라 $\sigma$-필드인가?** 우리가 사건들을 결합하거나(합집합), 여사건을 생각하거나, 사건들의 극한을 다룰 때에도 그 결과가 여전히 확률을 측정할 수 있는 '사건'이 되도록 보장하기 위함입니다. $\sigma$-필드의 두 가지 조건은 이를 수학적으로 보장해주는 최소한의 장치입니다.
        *   (i) $A$가 사건이면, '$A$가 일어나지 않는 사건'($A^c$)도 사건이어야 합니다.
        *   (ii) 셀 수 있는 만큼의 사건들 중 '적어도 하나가 일어나는 사건'(가산 합집합)도 사건이어야 합니다.
        *   이 두 조건과 드 모르간의 법칙을 이용하면, '모든 사건이 일어나는 사건'(가산 교집합)도 사건임을 보장할 수 있습니다.
    *   **$P$ (확률 측도, Probability Measure)**: 각각의 사건 $A \in \mathcal{F}$에 0과 1 사이의 숫자를 할당하는 함수입니다. 이 숫자가 바로 사건 A의 확률입니다.
*   **측도(Measure)와 확률 측도(Probability Measure)**:
    *   측도는 길이, 넓이, 부피와 같은 개념을 추상화한 것입니다. 집합의 "크기"를 재는 함수라고 생각할 수 있습니다.
    *   확률 측도는 전체 공간 $\Omega$의 크기가 1인 특별한 경우의 측도입니다. 즉, $\mu(\Omega)=1$이면, 우리는 그 측도 $\mu$를 **확률 측도(probability measure)**라고 부릅니다. 이 책에서는 확률 측도를 보통 $P$로 표기합니다.

---

다음 결과는 우리가 나중에 필요로 할, 측도의 정의로부터 나오는 몇 가지 귀결들을 보여줍니다. 모든 경우에, 우리가 언급하는 집합들은 $\mathcal{F}$에 속한다고 가정합니다.

**정리 1.1.1.** $\mu$를 $(\Omega, \mathcal{F})$ 상의 측도라고 하자.

(i) **단조성(monotonicity).** 만약 $A \subset B$이면 $\mu(A) \le \mu(B)$이다.

(ii) **준가법성(subadditivity).** 만약 $A \subset \cup_{m=1}^{\infty} A_m$이면 $\mu(A) \le \sum_{m=1}^{\infty} \mu(A_m)$이다.

(iii) **아래로부터의 연속성(continuity from below).** 만약 $A_i \uparrow A$ (즉, $A_1 \subset A_2 \subset \dots$이고 $\cup_i A_i = A$)이면 $\mu(A_i) \uparrow \mu(A)$이다.

(iv) **위로부터의 연속성(continuity from above).** 만약 $A_i \downarrow A$ (즉, $A_1 \supset A_2 \supset \dots$이고 $\cap_i A_i = A$)이고, $\mu(A_1) < \infty$이면 $\mu(A_i) \downarrow \mu(A)$이다.

**증명.**
(i) $B-A = B \cap A^c$를 두 집합의 차집합으로 두자. $+$를 서로소 합집합(disjoint union)을 나타내는 데 사용하면, $B = A + (B-A)$이므로

$$ \mu(B) = \mu(A) + \mu(B-A) \ge \mu(A) $$

(ii) $A'_n = A_n \cap A$라고 하자. $B_1 = A'_1$ 그리고 $n > 1$에 대해 $B_n = A'_n - \cup_{m=1}^{n-1} A'_m$이라고 하자. $B_n$들은 서로소이고 합집합이 $A$이므로, 측도의 정의 (ii), $B_m \subset A_m$, 그리고 이 정리의 (i)을 사용하여 다음을 얻는다.

$$ \mu(A) = \sum_{m=1}^{\infty} \mu(B_m) \le \sum_{m=1}^{\infty} \mu(A_m) $$

(iii) $B_n = A_n - A_{n-1}$이라고 하자. 그러면 $B_n$들은 서로소이고 $\cup_{m=1}^{\infty} B_m = A$, $\cup_{m=1}^{n} B_m = A_n$이므로

$$ \mu(A) = \sum_{m=1}^{\infty} \mu(B_m) = \lim_{n \to \infty} \sum_{m=1}^{n} \mu(B_m) = \lim_{n \to \infty} \mu(A_n) $$

(iv) $A_1 - A_n \uparrow A_1 - A$이므로, (iii)은 $\mu(A_1 - A_n) \uparrow \mu(A_1 - A)$임을 암시한다. $A_1 \supset A$이므로 $\mu(A_1 - A) = \mu(A_1) - \mu(A)$이고, 따라서 $\mu(A_n) \downarrow \mu(A)$가 성립한다. ◻

**[해설 및 추가 설명]**

*   **정리 1.1.1의 의미**: 이 정리는 측도(그리고 확률)가 우리가 직관적으로 기대하는 '크기'의 속성들을 가지고 있음을 보여줍니다.
    *   (i) **단조성**: 더 큰 집합은 더 큰 (혹은 같은) 크기를 가집니다. 당연해 보이지만, 측도의 기본 공리로부터 유도되는 중요한 성질입니다.
    *   (ii) **준가법성**: 여러 집합의 합집합의 크기는 각 집합의 크기의 합보다 작거나 같습니다. 등호는 집합들이 서로소일 때만 성립합니다. 겹치는 부분이 있으면 크기의 합이 더 커지기 때문입니다.
    *   (iii) & (iv) **연속성**: 이 두 성질은 측도론이 극한을 다룰 수 있게 해주는 핵심입니다.
        *   '점점 커지는' 사건들의 열($A_i \uparrow A$)의 확률은 그 극한 사건($A$)의 확률로 수렴합니다.
        *   '점점 작아지는' 사건들의 열($A_i \downarrow A$)의 확률도 그 극한 사건($A$)의 확률로 수렴합니다. 단, 여기에는 **$\mu(A_1) < \infty$** 라는 중요한 조건이 붙습니다. 이 조건이 없으면 성립하지 않을 수 있습니다. (예: 실수 전체에서 르벡 측도를 생각하고 $A_n = (n, \infty)$라 하면, $\mu(A_n)=\infty$이지만 $\cap_n A_n = \emptyset$이므로 $\mu(\cap_n A_n)=0$입니다. $\infty$가 0으로 수렴하지 않죠.)

---

가장 간단한 설정으로, 학부 확률론에서 친숙할 만한 것은 다음과 같다:

**예제 1.1.2. 이산 확률 공간 (Discrete probability spaces).** $\Omega$가 가산 집합(즉, 유한이거나 가산 무한)이라고 하자. $\mathcal{F}$를 $\Omega$의 모든 부분집합들의 집합으로 하자.

$$ P(A) = \sum_{\omega \in A} p(\omega) \quad \text{여기서 } p(\omega) \ge 0 \text{ 이고 } \sum_{\omega \in \Omega} p(\omega) = 1 $$

이라고 하자.
조금만 생각해보면 이것이 이 공간 위에서 가장 일반적인 확률 측도임을 알 수 있다. 많은 경우에 $\Omega$가 유한 집합일 때, 우리는 $p(\omega) = 1/|\Omega|$를 갖는다. 여기서 $|\Omega|$는 $\Omega$에 있는 점의 개수이다.

**[해설 및 추가 설명]**

*   이산 확률 공간은 각 결과(outcome) $\omega$에 개별적인 확률 $p(\omega)$를 부여할 수 있는 경우입니다. 이 경우, 어떤 사건 $A$의 확률은 그 사건에 속하는 모든 결과들의 확률을 단순히 더해서 구합니다.
*   여기서 $\mathcal{F}$는 $\Omega$의 **멱집합(power set)**이 됩니다. 즉, $\Omega$의 어떤 부분집합이든 '사건'으로 간주될 수 있습니다. 이는 표본 공간이 가산일 때만 가능하며, 비가산인 경우(예: $\Omega=[0,1]$)에는 모든 부분집합에 일관된 확률을 부여할 수 없는 문제가 발생합니다 (이에 대한 예시는 부록에서 다룹니다).

---

다음 정의를 준비하기 위해, 정의로부터 쉽게 따라나오는 사실을 주목할 필요가 있다. 만약 $\mathcal{F}_i, i \in I$가 $\sigma$-필드라면 $\cap_{i \in I} \mathcal{F}_i$도 그렇다. 여기서 $I \neq \emptyset$는 임의의 인덱스 집합(즉, 비가산일 수도 있다)이다. 이로부터 만약 우리가 집합 $\Omega$와 $\Omega$의 부분집합들의 모임 $\mathcal{A}$를 가지고 있다면, $\mathcal{A}$를 포함하는 가장 작은 $\sigma$-필드가 존재한다는 것을 알 수 있다. 우리는 이것을 $\mathcal{A}$에 의해 **생성된 $\sigma$-필드($\sigma$-field generated by $\mathcal{A}$)**라고 부르고 $\sigma(\mathcal{A})$로 표기할 것이다.

$\mathbb{R}^d$를 실수 벡터 $(x_1, \dots, x_d)$의 집합으로 하고, $\mathcal{R}^d$를 **보렐 집합(Borel sets)**, 즉 열린 집합(open sets)들을 포함하는 가장 작은 $\sigma$-필드로 하자. $d=1$일 때는 위첨자를 생략한다.

**예제 1.1.3. 실수 직선 상의 측도 (Measures on the real line).** $(\mathbb{R}, \mathcal{R})$ 상의 측도들은 다음과 같은 속성을 가진 **스틸체스 측도 함수(Stieltjes measure function)** $F$를 제공함으로써 정의된다:

(i) $F$는 비감소(nondecreasing) 함수이다.

(ii) $F$는 우연속(right continuous) 함수이다. 즉, $\lim_{y \downarrow x} F(y) = F(x)$.

**정리 1.1.4.** 각각의 스틸체스 측도 함수 $F$에 대해, $(\mathbb{R}, \mathcal{R})$ 상에 유일한 측도 $\mu$가 존재하며 다음을 만족한다.

$$ \mu((a, b]) = F(b) - F(a) \quad (1.1.1) $$

$F(x)=x$일 때, 결과로 나오는 측도는 **르벡 측도(Lebesgue measure)**라고 불린다.

정리 1.1.4의 증명은 길고 복잡한 길이므로, 이 절에서는 관련된 주요 아이디어들을 설명하고 나머지 세부 사항은 부록 A.1절에 숨기는 것으로 만족할 것이다. $(a, b]$에서 "오른쪽은 닫힌" 구간을 선택하는 것은 만약 $b_n \downarrow b$이면 $\cap_n(a, b_n] = (a, b]$라는 사실에 의해 결정된다. 다음 정의는 "왼쪽은 열린" 구간을 선택한 이유를 설명할 것이다.

집합들의 모임 $\mathcal{S}$가 **반대수(semialgebra)**라고 불리는 것은 (i) 교집합에 대해 닫혀 있고, 즉 $S, T \in \mathcal{S}$이면 $S \cap T \in \mathcal{S}$이고, (ii) 만약 $S \in \mathcal{S}$이면 $S^c$는 $\mathcal{S}$에 속한 집합들의 유한한 서로소 합집합(finite disjoint union)인 경우이다. 반대수의 중요한 예는 다음과 같다.

**예제 1.1.5.** $\mathcal{S}_d = $ 공집합과 다음 형태의 모든 집합들

$$ (a_1, b_1] \times \dots \times (a_d, b_d] \subset \mathbb{R}^d \quad \text{여기서 } -\infty \le a_i < b_i \le \infty $$

**[해설 및 추가 설명]**

*   **생성된 $\sigma$-필드 $\sigma(\mathcal{A})$**: $\mathcal{A}$라는 기본적인 벽돌들로 지을 수 있는 가장 작은 '튼튼한 집'($\sigma$-필드)이라고 생각할 수 있습니다. 예를 들어 $\mathcal{A} = \{\{1,2\}, \{3,4\}\}$이고 $\Omega=\{1,2,3,4\}$이면, $\sigma(\mathcal{A})$는 $\{\emptyset, \{1,2\}, \{3,4\}, \{1,2,3,4\}\}$가 됩니다.
*   **보렐 집합 $\mathcal{R}^d$**: 실수 공간 $\mathbb{R}^d$에서 다루는 거의 모든 '합리적인' 집합(열린 집합, 닫힌 집합, 구간, 이들의 가산 합집합/교집합 등)을 포함합니다. 확률론에서는 대부분 보렐 집합 위에서 정의된 확률 변수를 다룹니다.
*   **스틸체스 측도 함수 $F$와 정리 1.1.4**: 이 부분은 측도론의 핵심 아이디어 중 하나입니다.
    *   연속적인 공간에서는 각 점의 확률이 0이므로 이산 공간처럼 각 점에 확률을 부여하여 측도를 정의할 수 없습니다.
    *   대신, 누적 분포 함수(CDF)와 유사한 스틸체스 함수 $F$를 정의합니다. $F(x)$는 $(-\infty, x]$ 구간의 '크기'를 나타냅니다.
    *   정리 1.1.4는 이렇게 잘 정의된 함수 $F$가 있으면, 모든 보렐 집합에 대해 유일한 측도 $\mu$가 존재함을 보장합니다. 이는 마치 CDF가 확률 분포를 유일하게 결정하는 것과 같습니다.
    *   우연속 조건은 $\mu(\{x\}) = F(x) - F(x-)$ (점 x에서의 점프 크기)와 같은 관계를 깔끔하게 만들어주는 기술적인 조건입니다.
*   **반대수(Semialgebra)**: $\sigma$-필드를 구성하기 위한 가장 기본적인 집합들의 모임입니다. 반대수로부터 유한 합집합을 통해 대수(algebra)를 만들고, 다시 대수로부터 가산 합집합/교집합을 통해 $\sigma$-필드를 만드는 과정(카라테오도리 확장 정리)이 측도론의 표준적인 구성 방법입니다. 예제 1.1.5의 반열린 직사각형들이 바로 그 출발점입니다.


**예제 1.1.5.** $\mathcal{S}_d = $ 공집합과 다음 형태의 모든 집합들

$$ (a_1, b_1] \times \dots \times (a_d, b_d] \subset \mathbb{R}^d \quad \text{여기서 } -\infty \le a_i < b_i \le \infty $$

**(1.1.1)의 정의는 반대수(semialgebra) $\mathcal{S}_1$ 위에서 $\mu$의 값을 제공합니다.** 반대수에서 $\sigma$-대수로 나아가기 위해 우리는 중간 단계를 사용합니다. $\Omega$의 부분집합들의 모임 $\mathcal{A}$가 **대수(algebra)**(또는 **필드(field)**)라고 불리는 것은, $A, B \in \mathcal{A}$일 때 $A^c$와 $A \cup B$가 $\mathcal{A}$에 속하는 경우입니다. $A \cap B = (A^c \cup B^c)^c$이므로, $A \cap B \in \mathcal{A}$임이 따라나옵니다. 명백하게 $\sigma$-대수는 대수입니다. 역이 성립하지 않는 예는 다음과 같습니다:

**예제 1.1.6.** $\Omega = \mathbb{Z} = $ 정수들의 집합. $A \subset \mathbb{Z}$이면서 $A$ 또는 $A^c$가 유한 집합인 모임 $\mathcal{A}$는 대수입니다.

**[해설 및 추가 설명]**

*   **대수(Algebra) vs. $\sigma$-대수($\sigma$-Algebra)**: 이 둘의 유일한 차이점은 '닫혀 있는' 연산의 범위입니다.
    *   **대수**: **유한** 합집합과 여집합에 대해 닫혀 있습니다. 따라서 유한 교집합에 대해서도 닫혀 있습니다.
    *   **$\sigma$-대수**: **가산** 합집합과 여집합에 대해 닫혀 있습니다. 따라서 가산 교집합에 대해서도 닫혀 있습니다.
    *   모든 $\sigma$-대수는 대수이지만, 예제 1.1.6에서 보여주듯 모든 대수가 $\sigma$-대수인 것은 아닙니다. 예를 들어, $\mathbb{Z}$에서 각 짝수를 원소로 갖는 유한 집합들 $\{2\}, \{4\}, \{6\}, \dots$는 모두 $\mathcal{A}$에 속합니다. 하지만 이들의 가산 합집합인 '모든 짝수들의 집합' $E = \{2, 4, 6, \dots\}$는 $E$도 $E^c$(홀수 집합)도 유한 집합이 아니므로 $\mathcal{A}$에 속하지 않습니다. 따라서 $\mathcal{A}$는 가산 합집합에 대해 닫혀 있지 않으므로 $\sigma$-대수가 아닙니다.
*   **측도론의 구성 단계**: 측도론은 보통 가장 단순한 구조에서 시작하여 점점 더 복잡하고 강력한 구조로 확장하는 방식으로 이론을 전개합니다.
    1.  **반대수 (Semialgebra)**: 가장 기본적인 구성 요소 (예: 구간 $(a, b]$). 교집합에는 닫혀 있지만 합집합에는 그렇지 않을 수 있습니다.
    2.  **대수 (Algebra)**: 반대수의 원소들의 '유한' 합집합으로 만들어지는 구조.
    3.  **$\sigma$-대수 ($\sigma$-Algebra)**: 대수를 '가산' 연산에 대해 확장하여 극한을 다룰 수 있게 만든 최종 구조.

---

**보조정리 1.1.7.** 만약 $\mathcal{S}$가 반대수이면 $\bar{\mathcal{S}} = \{\mathcal{S} \text{에 있는 집합들의 유한 서로소 합집합}\}$은 대수이며, 이를 $\mathcal{S}$에 의해 **생성된 대수(algebra generated by $\mathcal{S}$)**라고 부른다.

**증명.** $A = +_i S_i$이고 $B = +_j T_j$라고 가정하자. 여기서 $+$는 서로소 합집합을 나타내고 인덱스 집합은 유한하다고 가정한다. 그러면 $A \cap B = +_{i,j} S_i \cap T_j \in \bar{\mathcal{S}}$이다. 여집합의 경우, $A = +_i S_i$이면 $A^c = \cap_i S_i^c$이다. 반대수 $\mathcal{S}$의 정의는 $S_i^c \in \bar{\mathcal{S}}$임을 암시한다. 우리는 $\bar{\mathcal{S}}$가 교집합에 닫혀 있음을 보였으므로, 귀납법에 의해 $A^c \in \bar{\mathcal{S}}$가 성립한다. ◻

**예제 1.1.8.** $\Omega = \mathbb{R}$이고 $\mathcal{S} = \mathcal{S}_1$이면, $\bar{\mathcal{S}}_1 = $ 공집합과 다음 형태의 모든 집합들이다.

$$ \cup_{i=1}^k (a_i, b_i] \quad \text{여기서 } -\infty \le a_i < b_i \le \infty $$

집합 함수 $\mu$가 $\mathcal{S}$ 위에서 주어졌을 때, 우리는 그것을 다음과 같이 $\bar{\mathcal{S}}$로 확장할 수 있다.

$$ \mu(\text{+}_{i=1}^n A_i) = \sum_{i=1}^n \mu(A_i) $$

**대수 $\mathcal{A}$ 위의 측도(measure on an algebra)**란, 다음을 만족하는 집합 함수 $\mu$를 의미한다.

(i) 모든 $A \in \mathcal{A}$에 대해 $\mu(A) \ge \mu(\emptyset) = 0$이다.
(ii) 만약 $A_i \in \mathcal{A}$가 서로소이고 그들의 합집합이 $\mathcal{A}$에 속하면,

$$ \mu(\cup_{i=1}^\infty A_i) = \sum_{i=1}^\infty \mu(A_i) $$

$\mu$가 **$\sigma$-유한($\sigma$-finite)**이라고 하는 것은, $\mu(A_n) < \infty$이고 $\cup_n A_n = \Omega$인 집합들의 열 $A_n \in \mathcal{A}$가 존재하는 경우이다. $A'_1 = A_1$이라 하고 $n \ge 2$에 대해 $A'_n = \cup_{m=1}^n A_m$ 또는 $A'_n = A_n \cap (\cap_{m=1}^{n-1} A_m^c) \in \mathcal{A}$로 두면, 우리는 일반성을 잃지 않고 $A_n \uparrow \Omega$이거나 $A_n$들이 서로소라고 가정할 수 있다.

다음 결과는 반대수 $\mathcal{S}$ 위에 정의된 측도를 그것이 생성하는 $\sigma$-대수 $\sigma(\mathcal{S})$로 확장하는 데 도움을 준다.

---

**정리 1.1.9.** $\mathcal{S}$를 반대수라 하고, $\mathcal{S}$ 위에 정의된 $\mu$가 $\mu(\emptyset)=0$을 만족한다고 하자. 다음을 가정하자.

(i) 만약 $S \in \mathcal{S}$가 $S_i \in \mathcal{S}$인 집합들의 유한 서로소 합집합이면, $\mu(S) = \sum_i \mu(S_i)$이다.

(ii) 만약 $S_i, S \in \mathcal{S}$이고 $S = \text{+}_{i \ge 1} S_i$이면, $\mu(S) \le \sum_{i \ge 1} \mu(S_i)$이다.

그러면 $\mu$는 $\mathcal{S}$에 의해 생성된 대수 $\bar{\mathcal{S}}$ 위의 측도인 유일한 확장 $\bar{\mu}$를 갖는다. 만약 $\bar{\mu}$가 시그마-유한이면, $\sigma(\mathcal{S})$ 위의 측도인 유일한 확장 $\nu$가 존재한다.

위의 (ii)에서, 그리고 앞으로 $i \ge 1$은 가산 합집합을 나타내고, 평범한 첨자 $i$ 또는 $j$는 유한 합집합을 나타낸다. 정리 1.1.9의 증명은 상당히 복잡하므로 부록 A.1절에서 다룬다. 정리의 조건 (ii)를 확인하기 위해 다음이 유용하다.

**보조정리 1.1.10.** (i)만 성립한다고 가정하자.
(a) 만약 $A, B_i \in \bar{\mathcal{S}}$이고 $A = \text{+}_{i=1}^n B_i$이면, $\bar{\mu}(A) = \sum_i \bar{\mu}(B_i)$이다.

(b) 만약 $A, B_i \in \bar{\mathcal{S}}$이고 $A \subset \cup_{i=1}^n B_i$이면, $\bar{\mu}(A) \le \sum_i \bar{\mu}(B_i)$이다.

**증명.** 정의에 따라, 만약 $A = \text{+}_i B_i$가 $\bar{\mathcal{S}}$에 속한 집합들의 유한 서로소 합집합이고 $B_i = \text{+}_j S_{i,j}$이면, 다음이 성립함이 따라나온다.

$$ \bar{\mu}(A) = \sum_{i,j} \mu(S_{i,j}) = \sum_i \bar{\mu}(B_i) $$

(b)를 증명하기 위해, $n=1, B_1=B$인 경우부터 시작하자. $B=A+(B \cap A^c)$이고 $B \cap A^c \in \bar{\mathcal{S}}$이므로,

$$ \bar{\mu}(A) \le \bar{\mu}(A) + \bar{\mu}(B \cap A^c) = \bar{\mu}(B) $$

이제 $n > 1$을 다루기 위해, $F_k = B_1^c \cap \dots \cap B_{k-1}^c \cap B_k$라 하고 다음을 주목하자.

$$ \cup_i B_i = F_1 + \dots + F_n $$

$$ A = A \cap (\cup_i B_i) = (A \cap F_1) + \dots + (A \cap F_n) $$

따라서 (a), $n=1$일 때의 (b), 그리고 다시 (a)를 사용하여,

$$ \bar{\mu}(A) = \sum_{k=1}^n \bar{\mu}(A \cap F_k) \le \sum_{k=1}^n \bar{\mu}(F_k) = \bar{\mu}(\cup_i B_i) $$

◻

**[해설 및 추가 설명]**

*   **정리 1.1.9 (카라테오도리 확장 정리)**: 이 정리는 측도론의 건설에서 가장 중요한 정리입니다. 매우 단순한 집합들(반대수) 위에서 잘 정의된 (즉, 유한 가법성과 가산 준가법성을 만족하는) 함수 $\mu$만 있으면, 이것을 우리가 원하는 복잡한 집합들($\sigma$-대수) 위에서의 완전한 측도로 유일하게 확장할 수 있다는 것을 보장합니다. "$\sigma$-유한" 조건은 대수에서 $\sigma$-대수로의 마지막 확장 단계에서 필요합니다.
*   **보조정리 1.1.10**: 확장 정리의 까다로운 조건인 '가산 준가법성'을 직접 보이는 대신, 이 보조정리는 '유한 준가법성'을 보이는 것으로 충분할 수 있는 길을 열어줍니다. 증명에 사용된 $F_k$를 구성하는 방법은, 겹치는 집합들의 합집합을 다룰 때 서로소인 집합들의 합집합으로 바꾸는 표준적인 기술입니다.

---

**정리 1.1.4의 증명.** $\mathcal{S}$를 $-\infty \le a < b \le \infty$인 반열린 구간 $(a,b]$들의 반대수로 하자. $\mathcal{S}$ 위에 $\mu$를 정의하기 위해, 먼저 다음을 관찰하는 것으로 시작한다.

$$ F(\infty) = \lim_{x \uparrow \infty} F(x) \quad \text{그리고} \quad F(-\infty) = \lim_{x \downarrow -\infty} F(x) \quad \text{가 존재한다.} $$

그리고 $\mu((a,b]) = F(b)-F(a)$는 $F(\infty) > -\infty$이고 $F(-\infty) < \infty$이므로 모든 $-\infty \le a < b \le \infty$에 대해 의미가 있다.

만약 $(a, b] = \text{+}_{i=1}^n (a_i, b_i]$이면, 구간들을 재배열한 후에 우리는 $a_1=a, b_n=b$ 그리고 $2 \le i \le n$에 대해 $a_i=b_{i-1}$을 가져야만 하므로, 정리 1.1.9의 조건 (i)이 성립한다.

조건 (ii)를 확인하기 위해, 먼저 $-\infty < a < b < \infty$이고, $(a, b] \subset \cup_{i \ge 1} (a_i, b_i]$ (일반성을 잃지 않고) $-\infty < a_i < b_i < \infty$라고 가정하자. $F(a+\delta) < F(a)+\epsilon$이 되도록 $\delta>0$을 선택하고, $F(b_i+\eta_i) < F(b_i) + \epsilon 2^{-i}$가 되도록 $\eta_i$를 선택하자.

열린 구간 $(a_i, b_i+\eta_i)$들은 $[a+\delta, b]$를 덮으므로, 유한 부분 덮개(finite subcover) $( \alpha_j, \beta_j ), 1 \le j \le J$가 존재한다. $(a+\delta, b] \subset \cup_{j=1}^J (\alpha_j, \beta_j]$ 이므로, 보조정리 1.1.10의 (b)는 다음을 암시한다.

$$ F(b) - F(a+\delta) \le \sum_{j=1}^J F(\beta_j) - F(\alpha_j) \le \sum_{i=1}^\infty (F(b_i+\eta_i)-F(a_i)) $$

따라서, $\delta$와 $\eta_i$의 선택에 의해,

$$ F(b) - F(a) \le 2\epsilon + \sum_{i=1}^\infty (F(b_i)-F(a_i)) $$

그리고 $\epsilon$은 임의적이므로, 우리는 $-\infty < a < b < \infty$ 경우에 대해 결과를 증명했다. 마지막 제한을 제거하기 위해, 만약 $(a, b] \subset \cup_i (a_i, b_i]$이고, $(A, B] \subset (a, b]$가 $-\infty < A < B < \infty$를 가지면, 우리는 다음을 얻는다.

$$ F(B) - F(A) \le \sum_{i=1}^\infty (F(b_i) - F(a_i)) $$

마지막 결과가 임의의 유한한 $(A,B] \subset (a,b]$에 대해 성립하므로, 원하는 결과가 따라나온다. ◻


### **$\mathbb{R}^d$ 상의 측도 (Measures on $\mathbb{R}^d$)**

우리의 다음 목표는 정리 1.1.4의 $\mathbb{R}^d$ 버전을 증명하는 것입니다. 첫 번째 단계는 정의 함수 $F$에 대한 가정을 도입하는 것입니다. $d=1$인 경우와의 유추를 통해 다음과 같이 가정하는 것이 자연스럽습니다:

(i) $F$는 **비감소(nondecreasing)** 함수이다. 즉, 만약 $x \le y$ (모든 $i$에 대해 $x_i \le y_i$를 의미)이면 $F(x) \le F(y)$이다.

(ii) $F$는 **우연속(right continuous)** 함수이다. 즉, $\lim_{y \downarrow x} F(y) = F(x)$이다 (여기서 $y \downarrow x$는 각 성분 $y_i$가 $x_i$로 감소하며 수렴함을 의미한다).

(iii) 만약 $x_n \downarrow -\infty$ (즉, 각 좌표 성분이 $-\infty$로 가면) $F(x_n) \downarrow 0$이다. 만약 $x_n \uparrow \infty$ (즉, 각 좌표 성분이 $\infty$로 가면) $F(x_n) \uparrow 1$이다. (이 부분은 오타 수정 및 내용 보강. 원문은 $x_n \uparrow -\infty$는 오타로 보임. 일반적으로 분포함수는 무한대에서 1, 음의 무한대에서 0으로 수렴. 이 책 5판에서는 이 부분이 빠지고 대신 `(iv) Δ_A F ≥ 0 for all rectangles A` 조건으로 통합됨.)

그러나 이번에는 이것만으로는 충분하지 않습니다. 다음 $F$를 고려해 봅시다.

$$ F(x_1, x_2) = \begin{cases} 1 & \text{if } x_1, x_2 \ge 1 \\ 2/3 & \text{if } x_1 \ge 1 \text{ and } 0 \le x_2 < 1 \\ 2/3 & \text{if } x_2 \ge 1 \text{ and } 0 \le x_1 < 1 \\ 0 & \text{otherwise} \end{cases} $$

**[해설 및 추가 설명]**

*   **$\mathbb{R}^d$에서의 함수 $F$**: $d=1$일 때, $F(x)$는 점 $x$까지의 누적된 '크기'를 나타냈습니다. $\mathbb{R}^d$에서는 $F(x_1, \dots, x_d)$가 $(-\infty, x_1] \times \dots \times (-\infty, x_d]$ 라는 '무한 직사각형'의 크기를 나타냅니다. (i), (ii), (iii)은 1차원 CDF의 성질을 자연스럽게 확장한 것입니다.
*   **왜 이 조건들만으로는 부족한가?**: 1차원에서는 구간 $(a, b]$의 측도를 $\mu((a,b]) = F(b)-F(a) \ge 0$ (비감소 성질 때문에)으로 간단히 정의할 수 있었습니다. 하지만 $d \ge 2$에서는 직사각형 $(a_1, b_1] \times (a_2, b_2]$의 측도를 정의하기 위해 포함-배제의 원리가 필요합니다.

---

그림 1.1은 반례에 대한 그림입니다. 약간의 생각으로 다음을 알 수 있습니다.

$$ \begin{aligned} \mu((a_1, b_1] \times (a_2, b_2]) = & \mu((-\infty, b_1] \times (-\infty, b_2]) - \mu((-\infty, a_1] \times (-\infty, b_2]) \\ & - \mu((-\infty, b_1] \times (-\infty, a_2]) + \mu((-\infty, a_1] \times (-\infty, a_2]) \\ = & F(b_1, b_2) - F(a_1, b_2) - F(b_1, a_2) + F(a_1, a_2) \end{aligned} $$


이것을 $a_1 = a_2 = 1 - \epsilon$ 그리고 $b_1 = b_2 = 1$로 사용하고 $\epsilon \rightarrow 0$으로 보내면 다음을 알 수 있습니다.

$$ \mu(\{1,1\}) = 1 - 2/3 - 2/3 + 0 = -1/3 $$

유사한 추론은 $\mu(\{1,0\}) = \mu(\{0,1\}) = \frac{2}{3}$임을 보여줍니다.

**[해설 및 추가 설명]**

*   위의 계산은 직사각형의 측도가 음수가 될 수 있음을 보여줍니다. 측도는 항상 0 이상이어야 하므로, (i), (ii), (iii)만으로는 $\mathbb{R}^d$에서 측도를 정의하기에 충분하지 않다는 것을 의미합니다. 이 문제를 해결하기 위해 추가적인 조건이 필요합니다.

---

$F$가 측도를 정의하기 위한 세 번째이자 마지막 조건을 공식화하기 위해, 다음을 정의합시다.

$$ A = (a_1, b_1] \times \dots \times (a_d, b_d] $$

$$ V = \{a_1, b_1\} \times \dots \times \{a_d, b_d\} $$

여기서 $-\infty < a_i < b_i < \infty$ 입니다. $\infty$가 허용되지 않음을 강조하기 위해, 우리는 $A$를 **유한 직사각형(finite rectangle)**이라고 부를 것입니다. 그러면 $V$는 직사각형 $A$의 꼭짓점들의 집합입니다. 만약 $v \in V$이면,

$$ \text{sgn}(v) = (-1)^{\text{# of } a\text{'s in } v} $$

$$ \Delta_A F = \sum_{v \in V} \text{sgn}(v)F(v) $$

우리는 $\mu(A) = \Delta_A F$로 둘 것이므로, 다음을 가정해야 합니다.

(iv) 모든 직사각형 $A$에 대해 $\Delta_A F \ge 0$이다.

**정리 1.1.11.** 함수 $F: \mathbb{R}^d \rightarrow [0,1]$이 위에서 주어진 (i)-(iv)를 만족한다고 가정하자. 그러면 $(\mathbb{R}^d, \mathcal{R}^d)$ 위에 유일한 확률 측도 $\mu$가 존재하여, 모든 유한 직사각형 $A$에 대해 $\mu(A) = \Delta_A F$를 만족한다.

**[해설 및 추가 설명]**

*   **$\Delta_A F$의 의미**: 이 연산자는 직사각형 $A$의 측도를 계산하는 일반화된 방법입니다. $d=2$일 때, $\Delta_A F = F(b_1, b_2) - F(a_1, b_2) - F(b_1, a_2) + F(a_1, a_2)$가 됩니다. 이것은 포함-배제의 원리를 적용하여 큰 직사각형의 넓이에서 작은 직사각형들의 넓이를 빼고 더하는 과정과 같습니다.
*   **조건 (iv)**: 이 조건은 모든 직사각형의 측도가 음수가 되지 않도록 보장하는 필수적인 조건입니다. 이 조건이 추가됨으로써 $F$는 $\mathbb{R}^d$ 상에서 유일한 확률 측도를 생성할 수 있게 됩니다.

---

**예제 1.1.12.** $F(x) = \prod_{i=1}^d F_i(x_i)$라고 가정하자. 여기서 $F_i$는 정리 1.1.4의 (i)과 (ii)를 만족한다. 이 경우,

$$ \Delta_A F = \prod_{i=1}^d (F_i(b_i) - F_i(a_i)) $$

모든 $i$에 대해 $F_i(x) = x$일 때, 결과로 나오는 측도는 $\mathbb{R}^d$ 위의 **르벡 측도(Lebesgue measure)**이다.

**증명.** 우리는 모든 유한 직사각형에 대해 $\mu(A) = \Delta_A F$로 두고, 그 정의를 $\mathcal{S}_d$로 확장하기 위해 단조성을 사용한다. 정리 1.1.9의 (i)을 확인하기 위해, $A = +_k B_k$가 $A$의 **정규 세분(regular subdivision)**이라고 부르는 경우를 생각하자. 이는 각 직사각형 $B_k$가

$$ (\alpha_{1, j_1-1}, \alpha_{1, j_1}] \times \dots \times (\alpha_{d, j_d-1}, \alpha_{d, j_d}] \quad \text{여기서 } 1 \le j_i \le n_i $$

형태를 갖는 수열 $a_i = \alpha_{i,0} < \alpha_{i,1} < \dots < \alpha_{i, n_i} = b_i$가 존재하는 경우이다.
정규 세분에 대해서는 $\lambda(A) = \sum_k \lambda(B_k)$임을 쉽게 알 수 있다. (먼저 모든 끝점들이 유한한 경우를 고려하고 그 다음 극한을 취하여 일반적인 경우를 얻는다.) 이 결과를 일반적인 유한 세분 $A = +_j A_j$로 확장하려면, 더 세분하여 정규 세분을 얻으면 된다.

(ii)의 증명은 정리 1.1.4의 증명과 거의 동일하다. 쓰기 쉽고 정리 1.1.4와의 유추를 끌어내기 위해, $x, y \in \mathbb{R}^d$에 대해 다음과 같이 표기하자.

$$ (x, y) = (x_1, y_1) \times \dots \times (x_d, y_d) $$

$$ (x, y] = (x_1, y_1] \times \dots \times (x_d, y_d] $$

$$ [x, y] = [x_1, y_1] \times \dots \times [x_d, y_d] $$

먼저 $-\infty < a < b < \infty$라고 가정하자. 부등식은 각 성분이 유한함을 의미한다. 그리고 $(a,b] \subset \cup_{i \ge 1} (a^i, b^i]$라고 가정하자.

*(이하 증명은 1차원의 경우와 거의 동일하게 진행됩니다. 간략히 요약하면,)*

1.  콤팩트 집합 $[a+\delta\bar{1}, b]$를 열린 직사각형들 $(a^i, b^i+\eta_i\bar{1})$로 덮는다. ($\bar{1}$은 모든 성분이 1인 벡터)
2.  하이네-보렐 정리에 의해 유한 부분 덮개를 찾는다.
3.  보조정리 1.1.10(b)를 적용하여 부등식을 유도한다.
4.  $\delta$와 $\eta_i$를 0으로 보내 원하는 결과를 얻는다.

---

### **연습문제 (Exercises)**

**1.1.1.** $\Omega = \mathbb{R}$, $\mathcal{F} = \{A \subset \mathbb{R} \mid A \text{ is countable or } A^c \text{ is countable}\}$ 이라 하자. $P(A) = 0$ (첫 번째 경우) 또는 $P(A)=1$ (두 번째 경우)로 정의하자. $(\Omega, \mathcal{F}, P)$가 확률 공간임을 보여라.

**1.1.2.** 예제 1.1.5의 $\mathcal{S}_d$의 정의를 상기하라. $\sigma(\mathcal{S}_d) = \mathcal{R}^d$, 즉 $\mathbb{R}^d$의 보렐 집합들과 같음을 보여라.

**1.1.3.** $\sigma$-필드 $\mathcal{F}$가 **가산 생성(countably generated)**되었다고 하는 것은, $\sigma(C) = \mathcal{F}$인 가산 모임 $C \subset \mathcal{F}$가 존재하는 경우이다. $\mathcal{R}^d$가 가산 생성됨을 보여라.

**1.1.4.** (i) 만약 $\mathcal{F}_1 \subset \mathcal{F}_2 \subset \dots$가 $\sigma$-대수들이면, $\cup_i \mathcal{F}_i$는 대수임을 보여라. (ii) $\cup_i \mathcal{F}_i$가 $\sigma$-대수일 필요는 없다는 것을 보여주는 예를 들어라.

**1.1.5.** 집합 $A \subset \{1, 2, \dots\}$가 **점근 밀도(asymptotic density)** $\theta$를 갖는다고 하는 것은 $\lim_{n \to \infty} |A \cap \{1, 2, \dots, n\}|/n = \theta$인 경우이다. 점근 밀도가 존재하는 집합들의 모임을 $\mathcal{A}$라 하자. $\mathcal{A}$는 $\sigma$-대수인가? 대수인가?
