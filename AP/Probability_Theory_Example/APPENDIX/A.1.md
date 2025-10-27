### **A.1 카라테오도리 확장 정리 (Carathéodory's Extension Theorem)**

이 절은 다음 정리의 증명에 할애됩니다.

**정리 A.1.1.** $\mathcal{S}$를 반대수(semialgebra)라 하고, $\mathcal{S}$ 위에 정의된 $\mu$가 $\mu(\emptyset)=0$을 만족한다고 하자. 다음을 가정하자.

(i) 만약 $S \in \mathcal{S}$가 $S _i \in \mathcal{S}$인 집합들의 유한 서로소 합집합이면, $\mu(S) = \sum _i \mu(S _i)$이다 (유한 가법성).

(ii) 만약 $S _i, S \in \mathcal{S}$이고 $S = \text{+} _{i \ge 1} S _i$ (가산 서로소 합집합)이면, $\mu(S) \le \sum _{i \ge 1} \mu(S _i)$이다 (가산 준가법성).

그러면 $\mu$는 $\mathcal{S}$에 의해 생성된 대수(algebra) $\bar{\mathcal{S}}$ 위의 측도(measure)인 유일한 확장 $\bar{\mu}$를 갖는다. 만약 확장 $\bar{\mu}$가 $\sigma$-유한($\sigma$-finite)이면, $\sigma(\mathcal{S})$ 위의 측도인 유일한 확장 $\nu$가 존재한다.

**증명.**
보조정리 1.1.7은 $\bar{\mathcal{S}}$가 $\mathcal{S}$에 속한 집합들의 유한 서로소 합집합들의 모임임을 보여준다. 우리는 $A = \text{+} _i S _i$일 때마다 $\bar{\mu}(A) = \sum _i \mu(S _i)$로 둠으로써 $\bar{\mathcal{S}}$ 위에 $\bar{\mu}$를 정의한다. $\bar{\mu}$가 잘 정의되었는지 확인하기 위해, $A = \text{+} _j T _j$라고도 가정하고 $S _i = \text{+} _j (S _i \cap T _j)$ 그리고 $T _j = \text{+} _i (S _i \cap T _j)$임을 관찰하자. 그러면 (i)은 다음을 암시한다.

$$ \sum _i \mu(S _i) = \sum _{i,j} \mu(S _i \cap T _j) = \sum _j \mu(T _j) $$

1.1절에서 우리는 다음을 증명했다:

**보조정리 A.1.2.** (i)만 성립한다고 가정하자.

(a) 만약 $A, B _i \in \bar{\mathcal{S}}$이고 $A = \text{+} _{i=1}^n B _i$이면, $\bar{\mu}(A) = \sum _i \bar{\mu}(B _i)$이다.

(b) 만약 $A, B _i \in \bar{\mathcal{S}}$이고 $A \subset \cup _{i=1}^n B _i$이면, $\bar{\mu}(A) \le \sum _i \bar{\mu}(B _i)$이다.

가법성 속성을 $A \in \bar{\mathcal{S}}$가 가산 서로소 합집합 $A = \text{+} _{i \ge 1} B _i$ (여기서 $B _i \in \bar{\mathcal{S}}$)인 경우로 확장하기 위해, 우리는 각각의 $B _i = \text{+} _j S _{i,j}$ (여기서 $S _{i,j} \in \mathcal{S}$)이고 $\sum _{i \ge 1} \bar{\mu}(B _i) = \sum _{i \ge 1, j} \mu(S _{i,j})$임을 관찰한다. 따라서 $B _i$들을 $S _{i,j}$들로 대체함으로써, 우리는 일반성을 잃지 않고 $B _i \in \mathcal{S}$라고 가정할 수 있다. 이제 $A \in \bar{\mathcal{S}}$는 $A = \text{+} _j T _j$ (유한 서로소 합집합)이고 $T _j = \text{+} _{i \ge 1} T _j \cap B _i$임을 암시한다. 따라서 (ii)는 다음을 암시한다.

$$ \mu(T _j) \le \sum _{i \ge 1} \mu(T _j \cap B _i) $$

$j$에 대해 합하고, 비음수들은 어떤 순서로든 합할 수 있음을 관찰하면,

$$ \bar{\mu}(A) = \sum _j \mu(T _j) \le \sum _{j} \sum _{i \ge 1} \mu(T _j \cap B _i) = \sum _{i \ge 1} \sum _j \mu(T _j \cap B _i) = \sum _{i \ge 1} \mu(B _i) $$

마지막 등식은 (i)로부터 따라 나온다. 반대 방향의 부등식을 증명하기 위해, $A _n = B _1 + \dots + B _n$이라 하고 $C _n = A \cap A _n^c$라고 하자. $\bar{\mathcal{S}}$는 대수이므로 $C _n \in \bar{\mathcal{S}}$이다. 따라서 $\bar{\mu}$의 유한 가법성은 다음을 암시한다.

$$ \bar{\mu}(A) = \bar{\mu}(B _1) + \dots + \bar{\mu}(B _n) + \bar{\mu}(C _n) \ge \bar{\mu}(B _1) + \dots + \bar{\mu}(B _n) $$

$n \to \infty$로 보내면, $\bar{\mu}(A) \ge \sum _{i \ge 1} \bar{\mu}(B _i)$이다.


대수 $\bar{\mathcal{S}}$ 위에 측도를 정의했으므로, 이제 우리는 다음을 설정함으로써 증명을 완성한다.

**정리 A.1.3. 카라테오도리 확장 정리 (Carathéodory's Extension Theorem).** $\mu$를 대수 $\mathcal{A}$ 위의 $\sigma$-유한 측도라고 하자. 그러면 $\mu$는 $\mathcal{A}$를 포함하는 가장 작은 $\sigma$-대수인 $\sigma(\mathcal{A})$로의 유일한 확장을 갖는다.

**[해설 및 추가 설명]**
*   **정리 A.1.1의 증명 흐름**:
    1.  **대수 $\bar{\mathcal{S}}$로의 확장**: 반대수 $\mathcal{S}$에서 시작하여, 그것의 원소들의 유한 서로소 합집합으로 이루어진 대수 $\bar{\mathcal{S}}$를 만든다. 그리고 함수 $\bar{\mu}$를 자연스럽게 정의한다($\bar{\mu}(\text{+} _i S _i) = \sum _i \mu(S _i)$).
    2.  **$\bar{\mu}$의 가산 가법성 증명**: 이 단계가 증명의 핵심이다. $\bar{\mu}$가 $\bar{\mathcal{S}}$ 위에서 유한 가법성을 넘어 가산 가법성을 가짐을 보인다. 즉, $\bar{\mathcal{S}}$ 위의 측도임을 보인다. 이는 양쪽 부등식을 모두 보여줌으로써 증명된다.
*   **정리 A.1.3**: 이 정리가 바로 카라테오도리 확장 정리의 핵심 내용이다. 이 정리는 이미 대수 위에서 잘 정의된 $\sigma$-유한 측도가 있다면, 그것을 유일하게 그 대수가 생성하는 $\sigma$-대수로 확장할 수 있다는 것을 보장한다. 이 정리를 통해 우리는 측도론의 가장 중요한 구성 도구를 얻게 된다.

---

**유일성(Uniqueness).** 우리는 존재성을 증명하는 더 어려운 문제에 도전하기 전에 확장이 유일하다는 것을 증명할 것이다. 유일성 증명의 핵심은 **딘킨의 $\pi-\lambda$ 정리(Dynkin's $\pi-\lambda$ theorem)**이며, 이 책에서 여러 번 사용할 결과이다. 평소처럼, 결과를 기술하기 전에 몇 가지 정의가 필요하다.
$\mathcal{P}$가 교집합에 대해 닫혀 있을 때, 즉 $A,B \in \mathcal{P}$이면 $A \cap B \in \mathcal{P}$일 때, $\mathcal{P}$는 **$\pi$-시스템($\pi$-system)**이라고 한다. 예를 들어, 직사각형 $(a _1, b _1] \times \dots \times (a _d, b _d]$의 모임은 $\pi$-시스템이다.
$\mathcal{L}$이 다음을 만족할 때, **$\lambda$-시스템($\lambda$-system)**이라고 한다: (i) $\Omega \in \mathcal{L}$. (ii) 만약 $A, B \in \mathcal{L}$이고 $A \subset B$이면 $B-A \in \mathcal{L}$. (iii) 만약 $A _n \in \mathcal{L}$이고 $A _n \uparrow A$이면 $A \in \mathcal{L}$. 독자는 다음 결과가 확장의 유일성을 증명하는 데 필요한 바로 그것임을 곧 알게 될 것이다.

**정리 A.1.4. $\pi-\lambda$ 정리.** 만약 $\mathcal{P}$가 $\pi$-시스템이고 $\mathcal{L}$이 $\mathcal{P}$를 포함하는 $\lambda$-시스템이면, $\sigma(\mathcal{P}) \subset \mathcal{L}$이다.

**증명.** 우리는 다음을 보일 것이다.

(a) 만약 $\ell(\mathcal{P})$가 $\mathcal{P}$를 포함하는 가장 작은 $\lambda$-시스템이면, $\ell(\mathcal{P})$는 $\sigma$-필드이다.

원하는 결과는 (a)로부터 따라나온다. 이를 보기 위해, $\sigma(\mathcal{P})$는 가장 작은 $\sigma$-필드이고 $\ell(\mathcal{P})$는 $\mathcal{P}$를 포함하는 가장 작은 $\lambda$-시스템이므로 다음을 가짐에 주목하라.

$$ \sigma(\mathcal{P}) \subset \ell(\mathcal{P}) \subset \mathcal{L} $$

(a)를 증명하기 위해, 우리는 교집합에 닫혀 있는 $\lambda$-시스템이 $\sigma$-필드임을 주목하는 것으로 시작한다. 왜냐하면,

만약 $A \in \mathcal{L}$이면 $A^c = \Omega - A \in \mathcal{L}$

$A \cup B = (A^c \cap B^c)^c$

$\cup _{i=1}^n A _i \uparrow \cup _{i=1}^\infty A _i$ as $n \uparrow \infty$

따라서, 다음을 보이는 것으로 충분하다.

(b) $\ell(\mathcal{P})$는 교집합에 닫혀 있다.

(b)를 증명하기 위해, $\mathcal{G} _A = \{B : A \cap B \in \ell(\mathcal{P})\}$라 하고 다음을 증명한다.

(c) 만약 $A \in \ell(\mathcal{P})$이면 $\mathcal{G} _A$는 $\lambda$-시스템이다.

이를 확인하기 위해, 우리는 다음을 주목한다: (i) $A \in \ell(\mathcal{P})$이므로 $\Omega \in \mathcal{G} _A$. (ii) 만약 $B,C \in \mathcal{G} _A$이고 $B \supset C$이면 $A \cap (B-C) = (A \cap B) - (A \cap C) \in \ell(\mathcal{P})$ 이다. 왜냐하면 $A \cap B, A \cap C \in \ell(\mathcal{P})$이고 $\ell(\mathcal{P})$는 $\lambda$-시스템이기 때문이다. (iii) 만약 $B _n \in \mathcal{G} _A$이고 $B _n \uparrow B$이면 $A \cap B _n \uparrow A \cap B \in \ell(\mathcal{P})$이다. 왜냐하면 $A \cap B _n \in \ell(\mathcal{P})$이고 $\ell(\mathcal{P})$는 $\lambda$-시스템이기 때문이다.

(c)에서 (b)로 가기 위해, $\mathcal{P}$가 $\pi$-시스템이므로,
만약 $A \in \mathcal{P}$이면 $\mathcal{G} _A \supset \mathcal{P}$이고, 따라서 (c)는 $\mathcal{G} _A \supset \ell(\mathcal{P})$임을 암시한다.
즉, 만약 $A \in \mathcal{P}$이고 $B \in \ell(\mathcal{P})$이면 $A \cap B \in \ell(\mathcal{P})$이다. 마지막 문장에서 $A$와 $B$를 바꾸면: 만약 $A \in \ell(\mathcal{P})$이고 $B \in \mathcal{P}$이면 $A \cap B \in \ell(\mathcal{P})$이지만, 이것은 다음을 암시한다.
만약 $A \in \ell(\mathcal{P})$이면 $\mathcal{G} _A \supset \mathcal{P}$이고, 따라서 (c)는 $\mathcal{G} _A \supset \ell(\mathcal{P})$임을 암시한다.
이 결론은 만약 $A, B \in \ell(\mathcal{P})$이면 $A \cap B \in \ell(\mathcal{P})$임을 암시하며, 이것은 (b)를 증명하고 증명을 완성한다. ◻

정리 A.1.3의 확장이 유일함을 증명하기 위해, 우리는 다음을 보일 것이다:

**정리 A.1.5.** $\mathcal{P}$를 $\pi$-시스템이라고 하자. 만약 $\nu _1$과 $\nu _2$가 $\mathcal{P}$ 위에서 일치하는 ($\sigma$-필드 $\mathcal{F} _1$과 $\mathcal{F} _2$ 위의) 측도들이고, $A _n \in \mathcal{P}$이고 $A _n \uparrow \Omega$이며 $\nu _i(A _n) < \infty$인 수열 $A _n$이 존재한다면, $\nu _1$과 $\nu _2$는 $\sigma(\mathcal{P})$ 위에서 일치한다.

**증명.** $\nu _1(A) = \nu _2(A) < \infty$인 $A \in \mathcal{P}$를 잡자.

$$ \mathcal{L} = \{B \in \sigma(\mathcal{P}) : \nu _1(A \cap B) = \nu _2(A \cap B)\} $$

라고 하자. 우리는 이제 $\mathcal{L}$이 $\lambda$-시스템임을 보일 것이다. $A \in \mathcal{P}$이므로, $\nu _1(A)=\nu _2(A)$이고 $\Omega \in \mathcal{L}$이다. 만약 $B,C \in \mathcal{L}$이고 $C \subset B$이면,

$$ \nu _1(A \cap (B-C)) = \nu _1(A \cap B) - \nu _1(A \cap C) = \nu _2(A \cap B) - \nu _2(A \cap C) = \nu _2(A \cap (B-C)) $$

여기서 우리는 뺄셈을 정당화하기 위해 $\nu _i(A) < \infty$라는 사실을 사용했다. 마지막으로, 만약 $B _n \in \mathcal{L}$이고 $B _n \uparrow B$이면, 정리 1.1.1의 (iii)부는 다음을 암시한다.

$$ \nu _1(A \cap B) = \lim _{n \to \infty} \nu _1(A \cap B _n) = \lim _{n \to \infty} \nu _2(A \cap B _n) = \nu _2(A \cap B) $$

가정에 의해 $\mathcal{P}$는 교집합에 닫혀 있으므로, $\pi-\lambda$ 정리는 $\mathcal{L} \supset \sigma(\mathcal{P})$임을 암시한다. 즉, 만약 $A \in \mathcal{P}$이고 $\nu _1(A)=\nu _2(A) < \infty$이며 $B \in \sigma(\mathcal{P})$이면 $\nu _1(A \cap B) = \nu _2(A \cap B)$이다. $A _n \in \mathcal{P}$이고 $A _n \uparrow \Omega$, $\nu _1(A _n) = \nu _2(A _n) < \infty$라 하고, 마지막 결과와 정리 1.1.1의 (iii)부를 사용하면, 우리는 원하는 결론을 얻는다. ◻


**[해설 및 추가 설명]**
*   **$\pi-\lambda$ 정리의 역할**: 이 정리는 유일성을 증명하는 강력한 도구입니다. 아이디어는 다음과 같습니다:
    1.  두 측도 $\nu _1, \nu _2$가 일치하는 집합들의 모임 $\mathcal{L}$을 정의합니다.
    2.  $\mathcal{L}$이 $\lambda$-시스템의 조건을 만족함을 보입니다.
    3.  측도들이 일치한다고 알려진 원래의 집합 모임 $\mathcal{P}$가 $\pi$-시스템임을 보입니다.
    4.  $\pi-\lambda$ 정리에 의해, $\mathcal{P}$를 포함하는 가장 작은 $\sigma$-필드 $\sigma(\mathcal{P})$가 $\mathcal{L}$에 포함됩니다.
    5.  이는 곧, 두 측도가 $\sigma(\mathcal{P})$ 전체에서 일치함을 의미합니다.
*   **$\sigma$-유한 조건의 재등장**: 정리 A.1.5에서 "An ↑ Ω이고 νi(An) < ∞인 수열이 존재한다"는 조건이 바로 측도가 $\sigma$-유한이라는 것입니다. 이 조건은 뺄셈을 정당화하고 극한을 취하는 과정에서 결정적인 역할을 합니다.
*   

**연습문제 A.1.1.** $\mathcal{F}$가 $\{1,2,3,4\}$의 모든 부분집합들의 집합일 때, $\sigma(\mathcal{C}) = \mathcal{F}$ (즉, $\mathcal{C}$를 포함하는 가장 작은 $\sigma$-대수가 $\mathcal{F}$)인 집합들의 모임 $\mathcal{C}$ 위에서 일치하지만 $\mathcal{F}$ 위에서는 일치하지 않는 두 확률 측도 $\mu \neq \nu$의 예를 들어라.

**[해설 및 힌트]**
*   **문제의 의도**: 이 문제는 정리 A.1.5에서 $\mathcal{P}$가 단지 집합들의 모임이 아니라 **$\pi$-시스템**이어야 한다는 조건이 왜 중요한지를 보여줍니다. $\pi$-시스템이 아닌 모임 위에서 두 측도가 일치하더라도, 생성된 $\sigma$-필드 위에서는 일치하지 않을 수 있습니다.
*   **풀이 힌트**:
    1.  두 개의 다른 확률 측도 $\mu$와 $\nu$를 정의합니다. 예를 들어, 각 점에 다른 확률을 할당합니다.
        *   $\mu(\{1\})=1/4, \mu(\{2\})=1/4, \mu(\{3\})=1/4, \mu(\{4\})=1/4$ (균등 분포)
        *   $\nu(\{1\})=1/2, \nu(\{2\})=1/4, \nu(\{3\})=1/8, \nu(\{4\})=1/8$
    2.  $\mu$와 $\nu$가 일치하는 집합들의 모임 $\mathcal{C}$를 찾습니다. 이 $\mathcal{C}$는 $\sigma(\mathcal{C})=\mathcal{F}$를 만족해야 하지만, $\pi$-시스템이 아니어야 합니다.
    3.  예를 들어, $\mathcal{C} = \{\{1,2\}, \{1,3\}, \{1,4\}\}$를 생각해볼 수 있습니다. 이 모임은 교집합에 대해 닫혀 있지 않으므로 $\pi$-시스템이 아닙니다. (예: $\{1,2\} \cap \{1,3\} = \{1\} \notin \mathcal{C}$)
    4.  $\mu$와 $\nu$를 $\mu(\{1,2\})=\nu(\{1,2\})$ 등을 만족하도록 잘 조정하여 예시를 완성합니다.

---

**존재성(Existence).** 우리의 다음 단계는 대수 $\mathcal{A}$ 위에 정의된 ($\sigma$-유한일 필요는 없는) 측도가 그것이 생성하는 $\sigma$-대수로 확장을 가짐을 보이는 것이다.
만약 $E \subset \Omega$이면, 우리는 $\mu^{\ast}(E) = \inf \sum _i \mu(A _i)$로 둔다. 여기서 하한(infimum)은 $E \subset \cup _i A _i$인 $\mathcal{A}$로부터의 모든 수열들에 대해 취해진다. 직관적으로, 만약 $\nu$가 $\mathcal{A}$ 위에서 $\mu$와 일치하는 측도라면, 정리 1.1.1의 (ii)로부터 다음이 따라나온다.

$$ \nu(E) \le \nu(\cup _i A _i) \le \sum _i \nu(A _i) = \sum _i \mu(A _i) $$

따라서 $\mu^{\ast}(E)$는 $E$의 측도에 대한 상한(upper bound)이다. 직관적으로, 가측 집합들은 그 상한이 꽉 들어맞는(tight) 집합들이다. 형식적으로, 우리는 집합 $E$가 **가측(measurable)**이라고 말하는 것은, 모든 집합 $F \subset \Omega$에 대해 다음을 만족하는 경우이다.

$$ \mu^{\ast}(F) = \mu^{\ast}(F \cap E) + \mu^{\ast}(F \cap E^c) \quad \text{(A.1.1)} $$


**[해설 및 추가 설명]**
*   **외측도(Outer Measure) $\mu^{\ast}$**: 대수 $\mathcal{A}$ 위의 측도 $\mu$를 $\sigma$-대수 $\sigma(\mathcal{A})$로 확장하기 위한 첫 단계는, $\Omega$의 **모든** 부분집합에 대해 정의되는 **외측도** $\mu^{\ast}$를 구성하는 것입니다.
*   **$\mu^{\ast}$의 정의**: 어떤 집합 $E$의 외측도 $\mu^{\ast}(E)$는, $E$를 덮을 수 있는 대수 $\mathcal{A}$의 원소들(가산 개)의 측도 합들 중에서 가장 작은 값으로 정의됩니다. 이는 마치 $E$를 더 간단한 도형들($A _i$)로 덮고 그 도형들의 넓이 합으로 $E$의 넓이를 근사하려는 시도와 같습니다.
*   **카라테오도리의 가측성 조건 (A.1.1)**: 이 조건은 외측도 $\mu^{\ast}$를 사용하여 어떤 집합 $E$가 "진정으로 측정 가능한지"를 판별하는 기준입니다. 직관적으로, $E$가 가측이라는 것은 임의의 "테스트 집합" $F$를 $E$를 기준으로 안쪽($F \cap E$)과 바깥쪽($F \cap E^c$)으로 잘랐을 때, 원래 $F$의 크기가 두 조각의 크기의 합과 같다는 것을 의미합니다. 이는 마치 $E$가 $F$를 "깨끗하게" 자를 수 있다는 뜻입니다. 이 조건이 모든 $F$에 대해 성립하면, $E$는 좋은 측정의 대상이 될 자격이 있습니다.

---

마지막 정의는 그다지 직관적이지 않지만, 아래의 증명에서 보듯이 매우 잘 작동한다. 정의로부터 $\mu^{\ast}$가 다음 속성들을 가짐이 즉각적으로 따라나온다:

(i) **단조성(monotonicity).** 만약 $E \subset F$이면 $\mu^{\ast}(E) \le \mu^{\ast}(F)$.

(ii) **준가법성(subadditivity).** 만약 $F \subset \cup _i F _i$ (가산 합집합)이면, $\mu^{\ast}(F) \le \sum _i \mu^{\ast}(F _i)$.

$\mu^{\ast}(\emptyset)=0$이고 (i), (ii)를 만족하는 임의의 집합 함수는 **외측도(outer measure)**라고 불린다. (ii)를 $F _1 = F \cap E$와 $F _2 = F \cap E^c$ (그리고 그 외에는 $F _i = \emptyset$)에 적용함으로써, 집합이 가측임을 증명하기 위해서는 다음을 보이는 것으로 충분함을 알 수 있다.

$$ \mu^{\ast}(F) \ge \mu^{\ast}(F \cap E) + \mu^{\ast}(F \cap E^c) \quad \text{(A.1.2)} $$

우리는 우리의 새로운 정의가 옛 정의를 확장함을 보이는 것으로 시작한다.

**보조정리 A.1.6.** 만약 $A \in \mathcal{A}$이면 $\mu^{\ast}(A) = \mu(A)$이고 $A$는 가측이다.

**증명.** 정리 1.1.1의 (ii)부는 만약 $A \subset \cup _i A _i$이면 $\mu(A) \le \sum _i \mu(A _i)$임을 암시한다. 따라서 $\mu(A) \le \mu^{\ast}(A)$이다. 물론, 우리는 항상 $A _1=A$와 나머지 $A _i=\emptyset$으로 취할 수 있으므로 $\mu^{\ast}(A) \le \mu(A)$이다.

임의의 $A \in \mathcal{A}$가 가측임을 증명하기 위해, $\mu^{\ast}(F)=\infty$일 때는 부등식 (A.1.2)가 자명하므로, 일반성을 잃지 않고 $\mu^{\ast}(F) < \infty$라고 가정하는 것으로 시작한다. (A.1.2)가 $E=A$일 때 성립함을 증명하기 위해, $\mu^{\ast}(F)<\infty$이므로 $F \subset \cup _i B _i$이고 $\sum _i \mu(B _i) \le \mu^{\ast}(F) + \epsilon$인 수열 $B _i \in \mathcal{A}$가 존재함을 관찰한다.
$\mu$는 $\mathcal{A}$ 위에서 가법적이고, $\mu = \mu^{\ast}$가 $\mathcal{A}$ 위에서 성립하므로, 우리는 다음을 갖는다.

$$ \mu(B _i) = \mu^{\ast}(B _i \cap A) + \mu^{\ast}(B _i \cap A^c) $$

$i$에 대해 합하고 $\mu^{\ast}$의 준가법성을 사용하면,

$$ \mu^{\ast}(F) + \epsilon \ge \sum _i \mu^{\ast}(B _i \cap A) + \sum _i \mu^{\ast}(B _i \cap A^c) \ge \mu^{\ast}(F \cap A) + \mu^{\ast}(F \cap A^c) $$

$\epsilon$은 임의적이므로 원하는 결과가 증명된다. ◻

**보조정리 A.1.7.** 가측 집합들의 모임 $\mathcal{A}^*$는 $\sigma$-필드이고, $\mu^{\ast}$를 $\mathcal{A}^*$에 제한한 것은 측도이다.

**참고.** 이 결과는 임의의 외측도에 대해 참이다.

**증명.** 정의로부터 다음이 명백하다:

(a) 만약 $E$가 가측이면 $E^c$도 그렇다.

우리의 첫 번째 자명하지 않은 과제는 다음을 증명하는 것이다:

(b) 만약 $E _1$과 $E _2$가 가측이면 $E _1 \cup E _2$와 $E _1 \cap E _2$도 그렇다.

**(b)의 증명.** 첫 번째 결론을 증명하기 위해, $G$를 $\Omega$의 임의의 부분집합이라 하자. 준가법성, $E _2$의 가측성( (A.1.1)에서 $F=G \cap E _1^c$로 둠), 그리고 $E _1$의 가측성을 사용하면,

$$ \begin{aligned} \mu^{\ast}(G \cap (E _1 \cup E _2)) + \mu^{\ast}(G \cap (E _1^c \cap E _2^c)) &\le \mu^{\ast}(G \cap E _1) + \mu^{\ast}(G \cap E _1^c \cap E _2) + \mu^{\ast}(G \cap E _1^c \cap E _2^c) \\ &= \mu^{\ast}(G \cap E _1) + \mu^{\ast}(G \cap E _1^c) = \mu^{\ast}(G) \end{aligned} $$

$E _1 \cap E _2$가 가측임을 증명하기 위해, $E _1 \cap E _2 = (E _1^c \cup E _2^c)^c$임을 관찰하고 (a)를 사용한다. ◻

(c) $G \subset \Omega$이고 $E _1, \dots, E _n$이 서로소인 가측 집합들이라 하자. 그러면,

$$ \mu^{\ast}(G \cap \cup _{i=1}^n E _i) = \sum _{i=1}^n \mu^{\ast}(G \cap E _i) $$

**(c)의 증명.** $F _m = \cup _{i \le m} E _i$라 하자. $E _n$은 가측이고, $F _n \supset E _n$, 그리고 $F _{n-1} \cap E _n = \emptyset$ 이므로,

$$ \begin{aligned} \mu^{\ast}(G \cap F _n) &= \mu^{\ast}(G \cap F _n \cap E _n) + \mu^{\ast}(G \cap F _n \cap E _n^c) \\ &= \mu^{\ast}(G \cap E _n) + \mu^{\ast}(G \cap F _{n-1}) \end{aligned} $$

이로부터 귀납법에 의해 원하는 결과가 따라나온다. ◻

(d) 만약 집합 $E _i$들이 가측이면 $E = \cup _{i=1}^\infty E _i$도 가측이다.

**(d)의 증명.** $E' _i = E _i \cap (\cap _{j<i} E _j^c)$라 하자. (a)와 (b)는 $E' _i$가 가측임을 암시하므로, 우리는 일반성을 잃지 않고 $E _i$들이 서로소라고 가정할 수 있다. $F _n = E _1 \cup \dots \cup E _n$이라 하자. $F _n$은 (b)에 의해 가측이므로, 단조성과 (c)를 사용하면,

$$ \begin{aligned} \mu^{\ast}(G) &= \mu^{\ast}(G \cap F _n) + \mu^{\ast}(G \cap F _n^c) \ge \mu^{\ast}(G \cap F _n) + \mu^{\ast}(G \cap E^c) \\ &= \sum _{i=1}^n \mu^{\ast}(G \cap E _i) + \mu^{\ast}(G \cap E^c) \end{aligned} $$

$n \to \infty$로 보내고 준가법성을 사용하면,

$$ \mu^{\ast}(G) \ge \sum _{i=1}^\infty \mu^{\ast}(G \cap E _i) + \mu^{\ast}(G \cap E^c) \ge \mu^{\ast}(G \cap E) + \mu^{\ast}(G \cap E^c) $$

이것이 (A.1.2)이다. ◻

정리 A.1.7 증명의 마지막 단계는 다음과 같다.

(e) 만약 $E = \cup _i E _i$이고, 여기서 $E _1, E _2, \dots$는 서로소이고 가측이면,

$$ \mu^{\ast}(E) = \sum _{i=1}^\infty \mu^{\ast}(E _i) $$

**(e)의 증명.** $F _n = E _1 \cup \dots \cup E _n$이라 하자. 단조성과 (c)에 의해,

$$ \mu^{\ast}(E) \ge \mu^{\ast}(F _n) = \sum _{i=1}^n \mu^{\ast}(E _i) $$

이제 $n \to \infty$로 보내고 준가법성을 사용하면 원하는 결론을 얻는다. ◻
