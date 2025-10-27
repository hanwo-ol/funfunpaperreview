## **제4장 마팅게일 (Martingales)**

마팅게일 $X_n$은 공정한 게임에 돈을 거는 플레이어의 시간 $n$에서의 재산으로 생각할 수 있습니다. 서브마팅게일(submartingales) (또는 슈퍼마팅게일(supermartingales))은 유리한 (또는 불리한) 게임에 돈을 거는 결과입니다. 마팅게일에 관한 두 가지 기본 사실이 있습니다. 첫 번째는 그것에 돈을 걸어서 돈을 벌 수 없다는 것입니다 (정리 4.2.8 참조). 특히, 어떤 유계 시간(bounded time) $N$에 게임을 멈추기로 선택한다면, 당신의 기대 상금 $EX_N$은 당신의 초기 재산 $X_0$과 같습니다. (우리는 현재 $X_0$가 확률적이지 않다고 가정하고 있습니다.) 우리의 두 번째 사실, 정리 4.2.11은 서브마팅게일에 관한 것입니다. Mike Brennan에게서 배운 발견적 방법을 사용하자면, "그것들은 비감소 수열의 확률론적 유사물이며, 따라서 만약 위로 유계이면 (정확히는, $\sup_n EX_n^+ < \infty$이면) 거의 확실하게 수렴한다"는 것입니다. 4.3절의 내용이 보여주듯이, 이 결과는 다양한 응용을 가집니다. 이후의 절들은 마팅게일이 $L^p, p > 1$ (4.4절)와 $L^1$ (4.6절)에서 수렴하기 위한 충분조건을 제공하고, 제곱 적분 가능한 마팅게일(square integrable martingales)의 특별한 경우를 연구하며 (4.5절), $n \le 0$으로 인덱싱된 마팅게일을 고려합니다 (4.7절). 우리는 유계가 아닌 멈춤 시간(unbounded stopping times)에 대해 $EX_N = EX_0$가 성립하기 위한 충분조건을 제공합니다 (4.8절). 이 결과들은 확률 보행(random walks)의 행동을 연구하는 데 매우 유용합니다. 4.9절은 4.8.1절에서 마팅게일 논증으로부터 유도된 확률 보행 결과들을 조합론적 논증을 제공함으로써 보완합니다.

---

### **4.1 조건부 기댓값 (Conditional Expectation)**

우리는 이 장과 다음 장에서 중요한 정의로 시작합니다. 정의를 내린 후, 그것을 설명하기 위해 몇 가지 예시를 고려할 것입니다. 확률 공간 $(\Omega, \mathcal{F}_o, P)$, $\sigma$-필드 $\mathcal{F} \subset \mathcal{F}_o$, 그리고 $E|X| < \infty$인 확률 변수 $X \in \mathcal{F}_o$가 주어졌다고 합시다. 우리는 **$\mathcal{F}$가 주어졌을 때 $X$의 조건부 기댓값(conditional expectation of $X$ given $\mathcal{F}$)**, $E(X|\mathcal{F})$를, 다음을 만족하는 임의의 확률 변수 $Y$로 정의합니다.

(i) $Y \in \mathcal{F}$, 즉, $Y$는 $\mathcal{F}$-가측이다.

(ii) 모든 $A \in \mathcal{F}$에 대해, $\int_A X dP = \int_A Y dP$

**[해설 및 추가 설명]**

*   **조건부 기댓값의 직관**: 고전적인 조건부 기댓값 $E[X|Y=y]$는 특정 값 $y$가 주어졌을 때의 $X$의 평균입니다. 반면, 현대 확률론에서의 조건부 기댓값 $E(X|\mathcal{F})$는 **확률 변수**입니다.
    *   $\mathcal{F}$는 우리가 "알고 있는 정보"를 나타내는 $\sigma$-필드입니다. 즉, $\mathcal{F}$에 속한 모든 사건 $A$에 대해, 우리는 사건 $A$가 일어났는지 아닌지를 알 수 있습니다.
    *   $E(X|\mathcal{F})$는 이러한 정보 $\mathcal{F}$를 바탕으로 한 $X$의 "최선의 추정치(best guess)"입니다.
*   **정의의 의미**:
    *   **(i) $Y \in \mathcal{F}$ (가측성)**: 우리의 추정치 $Y$는 우리가 가진 정보 $\mathcal{F}$만으로 그 값을 알 수 있어야 합니다. $Y$의 값이 $\mathcal{F}$에 속하지 않은 정보에 의존한다면 그것은 $\mathcal{F}$를 이용한 추정치라고 할 수 없습니다.
    *   **(ii) $\int_A X dP = \int_A Y dP$ (평균 일치)**: 우리가 알고 있는 어떤 정보(사건 $A \in \mathcal{F}$) 위에서든, 원래 값 $X$의 평균과 우리의 추정치 $Y$의 평균은 같아야 합니다. 이는 우리의 추정치가 편향되지 않았음을 보장합니다.

---

(i)과 (ii)를 만족하는 모든 $Y$는 $E(X|\mathcal{F})$의 **버전(version)**이라고 합니다. 가장 먼저 해결해야 할 것은 조건부 기댓값이 존재하고 유일하다는 것입니다. 우리는 두 번째 주장부터 다루되, 기술적인 사항부터 시작하겠습니다.

**보조정리 4.1.1.** 만약 $Y$가 (i)과 (ii)를 만족한다면, 그것은 적분 가능하다(integrable).

**증명.** $A=\{Y>0\} \in \mathcal{F}$로 두면, (ii)를 두 번 사용하고 더함으로써,

$$ \int_A Y dP = \int_A X dP \le \int_A |X| dP $$

$$ \int_{A^c} -Y dP = \int_{A^c} -X dP \le \int_{A^c} |X| dP $$

따라서 우리는 $E|Y| \le E|X|$를 얻습니다. ◻

**유일성(Uniqueness).** 만약 $Y'$ 또한 (i)과 (ii)를 만족한다면,

$$ \int_A Y dP = \int_A Y' dP \quad \text{for all } A \in \mathcal{F} $$

$A = \{Y-Y' \ge \epsilon > 0\}$로 두면, 우리는 다음을 봅니다.

$$ 0 = \int_A X - X dP = \int_A Y - Y' dP \ge \epsilon P(A) $$

따라서 $P(A)=0$입니다. 이것이 모든 $\epsilon$에 대해 성립하므로 우리는 $Y \le Y'$ a.s.(almost surely)를 얻고, $Y$와 $Y'$의 역할을 바꾸면 $Y=Y'$ a.s.를 얻습니다. 기술적으로, $Y=E(X|\mathcal{F})$와 같은 모든 등식은 $Y=E(X|\mathcal{F})$ a.s.로 쓰여야 하지만, 우리는 이전 장들에서도 이 점을 무시해왔고 앞으로도 계속 그럴 것입니다.
마지막 논증을 반복하면 다음을 얻습니다.

**정리 4.1.2.** 만약 $X_1 = X_2$가 $B \in \mathcal{F}$ 위에서 성립하면, $E(X_1|\mathcal{F}) = E(X_2|\mathcal{F})$가 $B$ 위에서 a.s. 성립한다.

**증명.** $Y_1 = E(X_1|\mathcal{F})$이고 $Y_2 = E(X_2|\mathcal{F})$라고 하자. $A = \{Y_1-Y_2 \ge \epsilon > 0\}$으로 두면, 우리는 다음을 본다.

$$ 0 = \int_{A \cap B} X_1-X_2 dP = \int_{A \cap B} Y_1-Y_2 dP \ge \epsilon P(A) $$

따라서 $P(A)=0$이고, 이전과 같이 결론이 따라나온다. ◻

**존재성(Existence).** 시작하기 위해, $\nu$가 $\mu$에 대해 **절대적으로 연속(absolutely continuous)** (줄여서 $\nu \ll \mu$)이라고 하는 것은 $\mu(A)=0$이면 $\nu(A)=0$임을 의미함을 상기하고, 우리는 정리 A.4.8을 사용합니다:

**[해설 및 추가 설명]**

*   **버전(Version)과 유일성**: 조건부 기댓값은 '거의 확실하게(a.s.)' 유일합니다. 즉, $Y$와 $Y'$이 둘 다 $E(X|\mathcal{F})$의 조건을 만족한다면, $P(Y \neq Y')=0$입니다. 측도가 0인 집합 위에서는 값이 달라도 상관없다는 의미입니다. 확률론에서는 a.s. 같은 함수는 보통 같은 것으로 취급합니다.
*   **존재성 증명으로의 길**: 존재성은 **라돈-니코딤 정리**라는 측도론의 깊은 결과를 이용하여 증명됩니다.

---

**라돈-니코딤 정리 (Radon-Nikodym Theorem).** $\mu$와 $\nu$를 $(\Omega, \mathcal{F})$ 위의 $\sigma$-유한 측도라고 하자. 만약 $\nu \ll \mu$이면, 모든 $A \in \mathcal{F}$에 대해 다음을 만족하는 함수 $f \in \mathcal{F}$가 존재한다.

$$ \int_A f d\mu = \nu(A) $$

$f$는 보통 $d\nu/d\mu$로 표기되며 **라돈-니코딤 도함수(Radon-Nikodym derivative)**라고 불린다.


마지막 정리는 조건부 기댓값의 존재성을 쉽게 보여줍니다. 먼저 $X \ge 0$이라고 가정합시다. $\mu = P|_{\mathcal{F}}$ (즉, $P$를 $\mathcal{F}$에 제한한 측도) 그리고 $A \in \mathcal{F}$에 대해

$$ \nu(A) = \int_A X dP $$

라고 합시다. 지배 수렴 정리는 $\nu$가 측도임을 암시하고(연습문제 1.5.4 참조), 적분의 정의는 $\nu \ll \mu$임을 암시합니다. 라돈-니코딤 도함수 $d\nu/d\mu \in \mathcal{F}$이고 임의의 $A \in \mathcal{F}$에 대해 다음을 만족합니다.

$$ \int_A X dP = \nu(A) = \int_A \frac{d\nu}{d\mu} dP $$

$A=\Omega$로 두면, 우리는 $d\nu/d\mu \ge 0$이 적분 가능함을 알 수 있고, $d\nu/d\mu$가 $E(X|\mathcal{F})$의 버전임을 보였습니다.

이제 일반적인 경우를 다루기 위해, $X=X^+ - X^-$로 쓰고, $Y_1=E(X^+|\mathcal{F})$와 $Y_2=E(X^-|\mathcal{F})$라고 합시다. 이제 $Y_1-Y_2 \in \mathcal{F}$는 적분 가능하며, 모든 $A \in \mathcal{F}$에 대해,

$$ \int_A X dP = \int_A X^+ dP - \int_A X^- dP = \int_A Y_1 dP - \int_A Y_2 dP = \int_A (Y_1 - Y_2) dP $$

이것은 $Y_1-Y_2$가 $E(X|\mathcal{F})$의 버전임을 보여주며 증명을 마칩니다. ◻

**[해설 및 추가 설명]**

*   **존재성 증명의 핵심 아이디어**:
    1.  새로운 측도 $\nu$를 $\nu(A) = \int_A X dP$로 정의합니다. 이 측도는 '사건 A 위에서 X를 적분한 값'을 A의 크기로 삼습니다.
    2.  이 측도 $\nu$는 원래 확률 측도 $P$에 대해 절대적으로 연속입니다. ($P(A)=0$이면 적분 영역의 크기가 0이므로 $\nu(A)=0$이 됩니다.)
    3.  라돈-니코딤 정리에 의해, $\nu$를 $P$에 대한 '밀도 함수'처럼 표현할 수 있는 함수 $f=d\nu/dP$가 존재합니다. 즉, $\nu(A) = \int_A f dP$ 입니다.
    4.  정의를 결합하면 $\int_A X dP = \int_A f dP$가 모든 $A \in \mathcal{F}$에 대해 성립합니다. 이 함수 $f$가 바로 우리가 찾던 $E(X|\mathcal{F})$입니다. $f$는 $\mathcal{F}$-가측이고 정의의 (ii)를 만족합니다.

---

### **4.1.1 예제 (Examples)**

직관적으로, 우리는 $\mathcal{F}$를 우리가 마음대로 사용할 수 있는 정보를 기술하는 것으로 생각합니다 - 각각의 $A \in \mathcal{F}$에 대해, 우리는 $A$가 일어났는지 아닌지를 압니다. 그러면 $E(X|\mathcal{F})$는 우리가 가진 정보를 바탕으로 한 $X$의 값에 대한 "최선의 추정치"입니다. 몇 가지 예제는 이를 명확히 하고 $E(X|\mathcal{F})$를 다른 조건부 기댓값의 정의와 연결하는 데 도움이 될 것입니다.

**예제 4.1.3.** 만약 $X \in \mathcal{F}$이면, $E(X|\mathcal{F})=X$이다. 즉, 만약 우리가 $X$를 안다면, 우리의 "최선의 추정치"는 $X$ 그 자체입니다. $X$는 항상 (ii)를 만족하므로, $X$가 $E(X|\mathcal{F})$가 되는 것을 막을 수 있는 유일한 것은 조건 (i)입니다. 이 예제의 특별한 경우는 $X=c$ (c는 상수)입니다.

**예제 4.1.4.** 완벽한 정보의 다른 극단에는 정보가 없는 경우가 있습니다. $X$가 $\mathcal{F}$와 독립이라고 가정합시다. 즉, 모든 $B \in \mathcal{R}$과 $A \in \mathcal{F}$에 대해

$$ P(\{X \in B\} \cap A) = P(X \in B) P(A) $$

이 경우, 우리는 $E(X|\mathcal{F}) = EX$라고 주장합니다. 즉, 만약 당신이 $X$에 대해 아무것도 모른다면, 최선의 추정치는 평균 $EX$입니다. 정의를 확인하기 위해, $EX \in \mathcal{F}$이므로 (i)이 성립함을 주목합시다 (상수는 모든 $\sigma$-필드에 대해 가측). (ii)를 확인하기 위해, 만약 $A \in \mathcal{F}$이면 $X$와 $1_A \in \mathcal{F}$는 독립이므로, 정리 2.1.13은 다음을 암시합니다.

$$ \int_A X dP = E(X 1_A) = (EX)(E 1_A) = \int_A EX dP $$

독자는 여기서 그리고 앞으로 게임은 "추측하고 검증하는(guess and verify)" 것임을 주목해야 합니다. 우리는 조건부 기댓값에 대한 공식을 내놓고 그것이 (i)과 (ii)를 만족하는지 확인합니다.

**예제 4.1.5.** 이 예제에서, 우리는 새로운 조건부 기댓값의 정의를 학부 확률 과정에서 처음 배운 것과 연관시킵니다. $\Omega_1, \Omega_2, \dots$가 $\Omega$의 유한 또는 무한 분할(partition)로, 각각 양의 확률을 갖는 서로소 집합들이고, $\mathcal{F} = \sigma(\Omega_1, \Omega_2, \dots)$가 이 집합들에 의해 생성된 $\sigma$-필드라고 합시다. 그러면,

$$ E(X|\mathcal{F}) = \frac{E(X;\Omega_i)}{P(\Omega_i)} \quad \text{on } \Omega_i $$

(여기서 $E(X; A) = \int_A X dP$ 입니다.) 말로 표현하면, $\Omega_i$의 정보는 우리 결과가 분할의 어느 요소에 속하는지 알려주고, 이 정보가 주어졌을 때 $X$에 대한 최선의 추정치는 $\Omega_i$ 위에서의 $X$의 평균값입니다. 우리의 추측이 맞는지 증명하기 위해, 제안된 공식이 각 $\Omega_i$ 위에서 상수이므로 $\mathcal{F}$에 대해 가측임을 관찰합니다. (ii)를 확인하기 위해, $A=\Omega_i$에 대해 등식을 확인하는 것으로 충분하지만, 이것은 자명합니다:

$$ \int_{\Omega_i} \frac{E(X; \Omega_i)}{P(\Omega_i)} dP = E(X; \Omega_i) = \int_{\Omega_i} X dP $$

퇴화되었지만 중요한 특별한 경우는 $\mathcal{F} = \{\emptyset, \Omega\}$인 자명한 $\sigma$-필드입니다. 이 경우, $E(X|\mathcal{F}) = EX$입니다.

학부 개념과의 연결을 계속하기 위해,

$$ P(A|\mathcal{G}) = E(1_A|\mathcal{G}) $$

$$ P(A|B) = P(A \cap B) / P(B) $$

라고 하고, 마지막 예제에서 $P(A|\mathcal{F}) = P(A|\Omega_i)$가 $\Omega_i$ 위에서 성립함을 관찰합니다. $\sigma$-필드가 주어진 조건부 기댓값의 정의는 확률 변수에 대한 조건부를 특별한 경우로 포함합니다. 우리는 다음과 같이 정의합니다.

$$ E(X|Y) = E(X|\sigma(Y)) $$

여기서 $\sigma(Y)$는 $Y$에 의해 생성된 $\sigma$-필드입니다.


**[해설 및 추가 설명]**

*   **예제 요약**:
    *   **완벽한 정보 (4.1.3)**: $X$의 값을 이미 알고 있다면($X \in \mathcal{F}$), 최선의 추정은 $X$ 자신이다.
    *   **정보 없음 (4.1.4)**: $X$에 대한 정보가 전혀 없다면($X$가 $\mathcal{F}$와 독립), 최선의 추정은 $X$의 평균 $EX$이다.
    *   **부분적 정보 (4.1.5)**: "결과가 $\Omega_i$에 속한다"는 정보만 있다면, 최선의 추정은 그 부분 공간 $\Omega_i$ 위에서의 $X$의 평균이다.
*   **$E(X|Y)$**: $Y$라는 확률 변수가 주어졌을 때의 조건부 기댓값은 $Y$의 값에 따라 결정되는 모든 사건들의 모임($\sigma(Y)$)이 주어졌을 때의 조건부 기댓값으로 정의됩니다. 이 결과 $E(X|Y)$는 $Y$의 함수가 됩니다. 예를 들어 $E(X|Y) = g(Y)$ 형태로 표현될 수 있습니다.

---

**예제 4.1.6.** 학부 확률론의 조건부 기댓값 정의와의 연결을 계속하기 위해, $X$와 $Y$가 결합 밀도 함수 $f(x,y)$를 갖는다고 가정합시다. 즉,

$$ P((X,Y) \in B) = \iint_B f(x,y) dx dy \quad \text{for } B \in \mathcal{R}^2 $$

그리고 단순화를 위해 모든 $y$에 대해 $\int f(x,y) dx > 0$이라고 가정합시다. 이 경우, 만약 $E|g(X)| < \infty$이면, $E(g(X)|Y) = h(Y)$라고 주장합니다. 여기서,

$$ h(y) = \frac{\int g(x)f(x,y) dx}{\int f(x,y) dx} $$

이 공식을 "추측"하기 위해, 확률 밀도 $P(Y=y)$를 마치 실제 확률인 것처럼 다루면,

$$ P(X=x|Y=y) = \frac{P(X=x, Y=y)}{P(Y=y)} = \frac{f(x,y)}{\int f(x,y) dx} $$

이므로, 조건부 확률 밀도에 대해 적분하면,

$$ E(g(X)|Y=y) = \int g(x) P(X=x|Y=y) dx $$

이제 제안된 공식을 "검증"하기 위해, $h(Y) \in \sigma(Y)$이므로 (i)이 성립함을 관찰합니다. (ii)를 확인하기 위해, 만약 $A \in \sigma(Y)$이면 어떤 $B \in \mathcal{R}$에 대해 $A=\{\omega: Y(\omega) \in B\}$이므로,

$$ \begin{aligned} E(h(Y); A) &= \int_B \left( \int h(y)f(x,y) dx \right) dy = \int_B \left( \int g(x)f(x,y) dx \right) dy \\ &= E(g(X)1_B(Y)) = E(g(X); A) \end{aligned} $$

**참고.** $\int f(x,y)dx > 0$이라는 가정을 없애기 위해, $h$를 다음과 같이 정의합니다.

$$ h(y) \int f(x,y) dx = \int g(x)f(x,y) dx $$

(즉, $\int f(x,y)dx=0$인 곳에서는 $h$는 아무 값이나 될 수 있음), 그리고 이것이 증명에 충분함을 관찰합니다.

**예제 4.1.7.** $X$와 $Y$가 독립이라고 가정합시다. $E|\phi(X,Y)| < \infty$인 함수 $\phi$와 $g(x) = E(\phi(x,Y))$를 생각합시다. 우리는 이제 다음을 보일 것입니다.

$$ E(\phi(X,Y)|X) = g(X) $$

**증명.** $g(X) \in \sigma(X)$임은 명백합니다. (ii)를 확인하기 위해, $A \in \sigma(X)$이면 $A=\{X \in C\}$임을 주목하고, 변수 변환 공식(정리 1.6.9)과 $(X,Y)$의 분포가 곱측도라는 사실(정리 2.1.11), 그리고 $g$의 정의, 그리고 다시 변수 변환을 사용하면,

$$ \begin{aligned} \int_A \phi(X,Y) dP &= E\{\phi(X,Y) 1_C(X)\} \\ &= \iint \phi(x,y) 1_C(x) \nu(dy) \mu(dx) \\ &= \int 1_C(x) g(x) \mu(dx) = \int_A g(X) dP \end{aligned} $$

이것이 원하는 결과를 증명합니다. ◻


**예제 4.1.8. 보렐의 역설 (Borel's paradox).** $X$를 지구 위에서 무작위로 선택된 점이라 하고, $\theta$를 경도, $\phi$를 위도라고 합시다. $\theta \in [0, 2\pi)$와 $\phi \in (-\pi/2, \pi/2]$로 잡는 것이 일반적이지만, 우리는 똑같이 $\theta \in [0, \pi)$와 $\phi \in (-\pi, \pi]$로 잡을 수도 있습니다. 말로 표현하면, 새로운 경도는 점이 놓여 있는 대원(great circle)을 명시하고, $\phi$는 그 각도를 제공합니다.
언뜻 보기에, 만약 $X$가 구 위에서 균등하다면 $\theta$와 대원 위의 각도 $\phi$ 모두 그들의 가능한 값들 위에서 균등해야 할 것처럼 보일 수 있습니다. $\theta$는 균등하지만 $\phi$는 그렇지 않습니다. 이 역설은 새로운 공식이나 전통적인 공식에서 $\phi$가 $\theta$와 독립이라는 것을 깨닫는 순간 완전히 사라집니다. 따라서 조건부 분포는 비조건부 분포와 같으며, 이는 북극 근처보다 적도 근처에 더 많은 땅이 있기 때문에 균등하지 않습니다.

**[해설 및 추가 설명]**
예제 4.1.7은 조건부 기댓값 계산의 중요한 원리를 보여줍니다: **조건부에 있는 변수는 상수로 취급하여 밖으로 빼낼 수 있고, 조건부에 없는 독립 변수는 평균을 취하여 없앨 수 있습니다.** 즉, $E(\phi(X,Y)|X)$를 계산할 때, $X$는 이미 주어진 정보이므로 상수 $x$처럼 취급하고, $Y$는 $X$와 독립이므로 $Y$에 대해서만 기댓값을 취하여 $E(\phi(x,Y))$를 계산한 후, $x$를 다시 $X$로 바꾸어 $g(X)$를 얻는 것입니다.

### **4.1.2 속성 (Properties)**

조건부 기댓값은 일반적인 기댓값이 갖는 속성들과 동일한 많은 속성들을 가집니다.

**정리 4.1.9.** 처음 두 부분에서는 $E|X|, E|Y| < \infty$라고 가정한다.

(a) **조건부 기댓값은 선형이다(Conditional expectation is linear):**

$$ E(aX+Y|\mathcal{F}) = aE(X|\mathcal{F}) + E(Y|\mathcal{F}) \quad (4.1.1) $$

(b) **만약 $X \le Y$이면,**

$$ E(X|\mathcal{F}) \le E(Y|\mathcal{F}) \quad (4.1.2) $$

(c) **만약 $X_n \ge 0$이고 $X_n \uparrow X$이며 $EX < \infty$이면,**

$$ E(X_n|\mathcal{F}) \uparrow E(X|\mathcal{F}) \quad (4.1.3) $$


**참고.** 마지막 결과를 $Y_1 - Y_n$에 적용함으로써, 만약 $Y_n \downarrow Y$이고 $E|Y_1|, E|Y| < \infty$이면, $E(Y_n|\mathcal{F}) \downarrow E(Y|\mathcal{F})$임을 알 수 있다.

**증명.**

(a)를 증명하기 위해, 우리는 우변이 좌변의 버전(version)임을 확인할 필요가 있다. 우변이 $\mathcal{F}$-가측인 것은 명백하다. (ii)를 확인하기 위해, 만약 $A \in \mathcal{F}$이면 적분의 선형성과 $E(X|\mathcal{F})$, $E(Y|\mathcal{F})$의 정의 속성에 의해 다음을 관찰한다.

$$ \begin{aligned} \int_A \{aE(X|\mathcal{F}) + E(Y|\mathcal{F})\} dP &= a \int_A E(X|\mathcal{F}) dP + \int_A E(Y|\mathcal{F}) dP \\ &= a \int_A X dP + \int_A Y dP = \int_A (aX+Y) dP \end{aligned} $$

이것이 (4.1.1)을 증명한다.

정의를 사용하면,

$$ \int_A E(X|\mathcal{F}) dP = \int_A X dP \le \int_A Y dP = \int_A E(Y|\mathcal{F}) dP $$

$A = \{E(X|\mathcal{F}) - E(Y|\mathcal{F}) \ge \epsilon > 0\}$로 두면, 표시된 집합의 확률이 모든 $\epsilon > 0$에 대해 0임을 알 수 있고, 따라서 (4.1.2)를 증명했다.

(c)를 증명하기 위해, $Y_n = X - X_n$이라고 하자. $E(Y_n|\mathcal{F}) \downarrow 0$임을 보이는 것으로 충분하다. $Y_n \downarrow$이므로, (4.1.2)는 $Z_n \equiv E(Y_n|\mathcal{F}) \downarrow$이 극한 $Z_\infty$로 수렴함을 암시한다. 만약 $A \in \mathcal{F}$이면,

$$ \int_A Z_n dP = \int_A Y_n dP $$

$n \to \infty$로 보내고, $Y_n \downarrow 0$임을 주목하고, 지배 수렴 정리를 사용하면 모든 $A \in \mathcal{F}$에 대해 $\int_A Z_\infty dP = 0$임을 얻고, 따라서 $Z_\infty \equiv 0$이다. ◻

**[해설 및 추가 설명]**

*   **정리 4.1.9의 의미**: 이 정리는 조건부 기댓값이 일반 기댓값처럼 행동한다는 것을 보여줍니다.
    *   (a) **선형성**: "평균의 합은 합의 평균"이라는 성질이 조건부 기댓값에서도 그대로 유지됩니다.
    *   (b) **단조성(Monotonicity)**: 거의 확실하게 한 확률 변수가 다른 것보다 작거나 같으면, 그들의 조건부 기댓값도 같은 순서를 유지합니다.
    *   (c) **단조 수렴 정리(Monotone Convergence Theorem)**: 0 이상의 값으로 증가하며 수렴하는 확률 변수열이 있을 때, 조건부 기댓값의 극한과 극한의 조건부 기댓값을 교환할 수 있습니다. 이는 일반 기댓값에 대한 단조 수렴 정리의 자연스러운 확장입니다.

---

**정리 4.1.10.** 만약 $\phi$가 볼록 함수(convex function)이고 $E|X|, E|\phi(X)| < \infty$이면,

$$ \phi(E(X|\mathcal{F})) \le E(\phi(X)|\mathcal{F}) \quad (4.1.4) $$

**증명.** 만약 $\phi$가 선형이면, 결과는 자명하므로, $\phi$가 선형이 아니라고 가정할 것이다. 만약 $S = \{(a,b) : a,b \in \mathbb{Q}, ax+b \le \phi(x) \text{ for all } x\}$ 이면, $\phi(x) = \sup\{ax+b : (a,b) \in S\}$이기 때문에 이렇게 한다. 자세한 내용은 정리 1.6.2의 증명을 참조하라. 만약 $\phi(x) \ge ax+b$이면 (4.1.2)와 (4.1.1)은 다음을 암시한다.

$$ E(\phi(X)|\mathcal{F}) \ge aE(X|\mathcal{F}) + b \quad \text{a.s.} $$

$(a,b) \in S$에 대해 상한(supremum)을 취하면 다음을 얻는다.

$$ E(\phi(X)|\mathcal{F}) \ge \phi(E(X|\mathcal{F})) \quad \text{a.s.} $$

이것이 원하는 결과를 증명한다. ◻

**참고.** 여기서 우리는 부등식 옆에 a.s.를 썼는데, 이는 각 $a,b$에 대해 예외적인 집합(exceptional set)이 존재하므로, 가산 집합에 대해 상한을 취해야 함을 강조하기 위함이다.

**[해설 및 추가 설명]**

*   **조건부 젠센 부등식(Conditional Jensen's Inequality)**: 이 정리는 일반 젠센 부등식 $\phi(EX) \le E(\phi(X))$의 조건부 버전입니다. 이 부등식은 확률론 전반에 걸쳐 매우 중요하게 사용됩니다. 예를 들어, $\phi(x)=|x|^p$ ($p \ge 1$)는 볼록 함수이므로, $|E(X|\mathcal{F})|^p \le E(|X|^p|\mathcal{F})$가 성립합니다.

---

**정리 4.1.11.** 조건부 기댓값은 $L^p$($p \ge 1$)에서의 축소 사상(contraction)이다.

**증명.** (4.1.4)는 $|E(X|\mathcal{F})|^p \le E(|X|^p|\mathcal{F})$임을 암시한다. 기댓값을 취하면 다음을 얻는다.

$$ E(|E(X|\mathcal{F})|^p) \le E(E(|X|^p|\mathcal{F})) = E|X|^p $$

마지막 등식에서, 우리는 정의의 (ii) 속성을 $A=\Omega$와 함께 사용한, 정의의 즉각적인 귀결인 항등식을 사용했다.

$$ E(E(Y|\mathcal{F})) = E(Y) \quad (4.1.5) $$

◻

**[해설 및 추가 설명]**

*   **$L^p$ 축소 사상**: 이 정리는 조건부 기댓값을 취하면 함수의 "$L^p$ 노름(norm)"이 줄어들거나 같아진다는 것을 의미합니다. $L^p$ 노름은 $||X||_p = (E|X|^p)^{1/p}$로 정의됩니다. 따라서 정리 4.1.11은 $||E(X|\mathcal{F})||_p \le ||X||_p$ 임을 말해줍니다. 정보를 잃어버림으로써 (더 작은 $\sigma$-필드 $\mathcal{F}$에 대한 기댓값을 취함으로써) 변동성(variability)이 줄어든다는 직관과 일치합니다.
*   **(4.1.5) 반복 기댓값의 법칙(Law of Iterated Expectations) / 타워 속성(Tower Property)**: $E(E(Y|\mathcal{F})) = E(Y)$는 매우 중요한 속성입니다. 전체 평균은 조건부 평균의 평균과 같다는 의미입니다.

---

조건부 기댓값은 (4.1.5)와 같이 "일반적인" 기댓값에서는 유사한 것이 없는 속성들도 가지고 있다.

**정리 4.1.12.** 만약 $\mathcal{F} \subset \mathcal{G}$이고 $E(X|\mathcal{G}) \in \mathcal{F}$이면, $E(X|\mathcal{F}) = E(X|\mathcal{G})$이다.

**증명.** 가정에 의해 $E(X|\mathcal{G}) \in \mathcal{F}$이다. 정의의 다른 부분을 확인하기 위해, 만약 $A \in \mathcal{F} \subset \mathcal{G}$이면 다음을 주목한다.

$$ \int_A X dP = \int_A E(X|\mathcal{G}) dP $$

◻

**정리 4.1.13.** 만약 $\mathcal{F}_1 \subset \mathcal{F}_2$이면, (i) $E(E(X|\mathcal{F}_1)|\mathcal{F}_2) = E(X|\mathcal{F}_1)$ (ii) $E(E(X|\mathcal{F}_2)|\mathcal{F}_1) = E(X|\mathcal{F}_1)$ 이다.

말로 표현하면, **더 작은 $\sigma$-필드가 항상 이긴다**. 증명이 보여주듯이, 첫 번째 등식은 자명하다. 두 번째는 증명하기 쉽지만, 정리 4.1.14와 결합하면 조건부 기댓값을 계산하는 강력한 도구가 된다. 나는 그것이 거짓인 결과를 증명하는 데 여러 번 사용되는 것을 보았다.

**증명.** $E(X|\mathcal{F}_1) \in \mathcal{F}_2$임을 알아차리면 (i)은 예제 4.1.3으로부터 따라나온다. (ii)를 증명하기 위해, $E(X|\mathcal{F}_1) \in \mathcal{F}_1$임을 주목하고, 만약 $A \in \mathcal{F}_1 \subset \mathcal{F}_2$이면

$$ \int_A E(X|\mathcal{F}_1) dP = \int_A X dP = \int_A E(X|\mathcal{F}_2) dP $$

◻

**[해설 및 추가 설명]**

*   **정리 4.1.12와 4.1.13 (타워 속성 확장)**: 이 정리들은 반복 기댓값의 법칙을 더 일반화한 것입니다.
    *   정리 4.1.13(ii)가 핵심입니다. $E[E(X|\mathcal{F}_2)|\mathcal{F}_1] = E(X|\mathcal{F}_1)$
    *   **직관적 설명**: $\mathcal{F}_2$는 $\mathcal{F}_1$보다 더 많은 정보를 가지고 있습니다. 먼저 $\mathcal{F}_2$ 정보로 최선의 추정치($E(X|\mathcal{F}_2)$)를 구한 다음, 그 추정치를 가지고 더 적은 정보인 $\mathcal{F}_1$로 다시 최선의 추정치를 구하면, 이는 처음부터 $\mathcal{F}_1$ 정보만 가지고 최선의 추정치를 구한 것과 같다는 의미입니다. 즉, 더 많은 정보로 계산했다가 다시 정보를 줄이면, 처음부터 적은 정보로 계산한 것과 같아집니다. "더 작은 $\sigma$-필드가 이긴다"는 말은 이 때문입니다.

---

다음 결과는 $\mathcal{F}$에 대한 조건부 기댓값에 대해, 확률 변수 $X \in \mathcal{F}$는 상수와 같다는 것을 보여준다. 그것들은 "적분" 밖으로 나올 수 있다.

**정리 4.1.14.** 만약 $X \in \mathcal{F}$이고 $E|Y|, E|XY| < \infty$이면,

$$ E(XY|\mathcal{F}) = X E(Y|\mathcal{F}) $$

**증명.** 우변 $\in \mathcal{F}$이므로, 우리는 (ii)를 확인해야 한다. 이를 위해, 우리는 통상적인 4단계 절차를 사용한다. 먼저, $X=1_B$ (여기서 $B \in \mathcal{F}$)라고 가정하자. 이 경우, 만약 $A \in \mathcal{F}$이면

$$ \int_A 1_B E(Y|\mathcal{F}) dP = \int_{A \cap B} E(Y|\mathcal{F}) dP = \int_{A \cap B} Y dP = \int_A 1_B Y dP $$

따라서 (ii)가 성립한다. 이 결과는 선형성에 의해 단순(simple) $X$로 확장된다. 만약 $X, Y \ge 0$이면, $X_n$을 $X_n \uparrow X$인 단순 확률 변수라 하고, 단조 수렴 정리를 사용하여 다음을 결론짓는다.

$$ \int_A X E(Y|\mathcal{F}) dP = \int_A XY dP $$

일반적인 결과를 증명하기 위해, $X$와 $Y$를 그들의 양수 부분과 음수 부분으로 나눈다. ◻


**[해설 및 추가 설명]**

*   **알려진 정보는 밖으로 빼내기**: 이 정리는 조건부 기댓값 계산에서 매우 유용한 도구입니다. **조건을 거는 정보($\mathcal{F}$)에 대해 이미 그 값을 알고 있는 변수($X$)는 상수처럼 취급하여 기댓값 밖으로 빼낼 수 있다**는 의미입니다. 이것은 $E(XY|\mathcal{F}) = X E(Y|\mathcal{F})$ 라는 공식으로 표현됩니다.

---

**정리 4.1.15.** $EX^2 < \infty$라고 가정하자. $E(X|\mathcal{F})$는 "평균 제곱 오차(mean square error)" $E(X-Y)^2$를 최소화하는 $Y \in \mathcal{F}$ 변수이다.

**참고.** 이 결과는 $E(X|\mathcal{F})$의 "기하학적 해석"을 제공한다. $L^2(\mathcal{F}_o) = \{Y \in \mathcal{F}_o : EY^2 < \infty\}$는 힐베르트 공간이고, $L^2(\mathcal{F})$는 닫힌 부분 공간이다. 이 경우, $E(X|\mathcal{F})$는 $X$를 $L^2(\mathcal{F})$ 위로의 **사영(projection)**한 것이다. 즉, 부분 공간에서 $X$에 가장 가까운 점이다.

**증명.** 만약 $Z \in L^2(\mathcal{F})$이면, 정리 4.1.14는 $Z E(X|\mathcal{F}) = E(ZX|\mathcal{F})$임을 암시한다. ($E|XZ| < \infty$는 코시-슈바르츠 부등식에 의해 성립한다.) 기댓값을 취하면,

$$ E(Z E(X|\mathcal{F})) = E(E(ZX|\mathcal{F})) = E(ZX) $$

또는, 재배열하면,

$$ E[Z(X-E(X|\mathcal{F}))] = 0 \quad \text{for } Z \in L^2(\mathcal{F}) $$

만약 $Y \in L^2(\mathcal{F})$이고 $Z = E(X|\mathcal{F}) - Y$이면,

$$ E(X-Y)^2 = E\{X - E(X|\mathcal{F}) + Z\}^2 = E\{X-E(X|\mathcal{F})\}^2 + E Z^2 $$

교차 곱 항(cross-product term)이 사라지기 때문이다. 마지막 공식으로부터, $E(X-Y)^2$는 $Z=0$일 때 최소화됨을 쉽게 알 수 있다. ◻

**[해설 및 추가 설명]**
$Z = E(X|\mathcal{F}) - Y$는 $\mathcal{F}$-가측이므로 $L^2(\mathcal{F})$에 속합니다. 따라서 $E[Z(X-E(X|\mathcal{F}))]=0$ 이 성립합니다.
교차 곱 항은 $2E[Z(X-E(X|\mathcal{F}))]$ 이며, 위에서 보였듯이 0이 됩니다.
따라서, $E(X-Y)^2$는 오차항 $E Z^2 = E(E(X|\mathcal{F})-Y)^2$를 포함하는데, 이 항은 $Y$를 $E(X|\mathcal{F})$로 선택했을 때 0이 되어 최소화됩니다. 이는 $E(X|\mathcal{F})$가 $L^2$ 공간에서 $X$의 최적의 근사치임을 의미합니다.

### **연습문제 (Exercises)**

**4.1.1. 베이즈 공식 (Bayes' formula).** $G \in \mathcal{G}$라 하고 다음을 보여라.

$$ P(G|A) = \frac{\int_G P(A|\mathcal{G}) dP}{\int_\Omega P(A|\mathcal{G}) dP} $$

$\mathcal{G}$가 분할(partition)에 의해 생성된 $\sigma$-필드일 때, 이것은 통상적인 베이즈 공식으로 환원된다.

$$ P(G_i|A) = \frac{P(A|G_i)P(G_i)}{\sum_j P(A|G_j)P(G_j)} $$

**[해설 및 힌트]**
*   **문제의 의도**: 현대적인 조건부 기댓값의 정의가 고전적인 베이즈 공식을 어떻게 포함하는지 이해하는 문제입니다.
*   **풀이 힌트**:
    1.  고전적인 베이즈 공식 $P(G|A) = P(G \cap A) / P(A)$ 에서 시작합니다.
    2.  $P(G \cap A)$를 조건부 기댓값의 정의 (ii)를 이용하여 적분 형태로 표현합니다. 즉, $P(G \cap A) = E[1_{G \cap A}] = E[1_G \cdot 1_A] = E[E[1_G \cdot 1_A | \mathcal{G}]]$ 입니다. $1_G$는 $\mathcal{G}$-가측이므로 밖으로 나올 수 있습니다(정리 4.1.14).
    3.  $P(G \cap A) = \int_G 1_A dP = \int_G E[1_A|\mathcal{G}] dP = \int_G P(A|\mathcal{G}) dP$ 임을 보입니다.
    4.  $P(A)$에 대해서도 분모를 같은 방식으로 유도합니다 ($G=\Omega$인 경우).
    5.  만약 $\mathcal{G}$가 분할 $\{G_j\}$에 의해 생성되었다면, $P(A|\mathcal{G})$는 각 $G_j$ 위에서 상수 값 $P(A|G_j)$를 갖는 확률 변수임을 이용하면 고전적인 공식이 나옵니다.

---

**4.1.2. 체비셰프 부등식 (Chebyshev's inequality)을 증명하라.** 만약 $a>0$ 이면,

$$ P(|X| \ge a | \mathcal{F}) \le a^{-2} E(X^2|\mathcal{F}) $$

**[해설 및 힌트]**
*   **문제의 의도**: 일반적인 체비셰프 부등식 $P(|X| \ge a) \le a^{-2}EX^2$의 조건부 버전을 증명하는 문제입니다.
*   **풀이 힌트**:
    1.  지시 함수를 이용한 부등식 $a^2 1_{\{|X| \ge a\}} \le X^2$ 에서 시작합니다. 이 부등식은 항상 성립합니다.
    2.  양변에 조건부 기댓값 $E(\cdot|\mathcal{F})$를 취합니다.
    3.  조건부 기댓값의 단조성(정리 4.1.9(b))을 이용합니다: $E(a^2 1_{\{|X| \ge a\}} | \mathcal{F}) \le E(X^2|\mathcal{F})$.
    4.  좌변에서 상수 $a^2$는 밖으로 나오고, $1_{\{|X| \ge a\}}$는 $\sigma(X, \mathcal{F})$에 대해 가측이므로, $E(1_{\{|X| \ge a\}}|\mathcal{F})$가 $P(|X|\ge a|\mathcal{F})$가 됨을 이용합니다 (엄밀하게는, $X$가 $\mathcal{F}$에 대해 가측이 아닐 수 있으므로 $1_{\{|X| \ge a\}}$를 상수처럼 밖으로 뺄 수는 없습니다. 하지만 부등식 $Y=a^2 1_{\{|X|\ge a\}}, Z=X^2$ 에서 $Y \le Z$ 이므로 $E[Y|\mathcal{F}] \le E[Z|\mathcal{F}]$ 를 바로 적용하면 됩니다).

---

**4.1.3.** 정리 1.5.2 다음의 참고 사항에 있는 증명을 모방하여 **조건부 코시-슈바르츠 부등식(conditional Cauchy-Schwarz inequality)**을 증명하라.

$$ E(XY|\mathcal{G})^2 \le E(X^2|\mathcal{G}) E(Y^2|\mathcal{G}) $$

**[해설 및 힌트]**
*   **문제의 의도**: 코시-슈바르츠 부등식 $|EXY|^2 \le EX^2 EY^2$의 조건부 버전을 증명하는 문제입니다.
*   **풀이 힌트**:
    1.  임의의 실수 $t$에 대해 $(X+tY)^2 \ge 0$ 이라는 사실에서 시작합니다.
    2.  $X^2 + 2tXY + t^2Y^2 \ge 0$ 입니다.
    3.  양변에 조건부 기댓값 $E(\cdot|\mathcal{G})$를 취하고 선형성을 이용합니다.
        $E(X^2|\mathcal{G}) + 2tE(XY|\mathcal{G}) + t^2E(Y^2|\mathcal{G}) \ge 0$.
    4.  이 부등식은 $t$에 대한 2차식이며, 거의 모든 $\omega$에 대해 항상 0 이상입니다. 따라서 이 2차식의 판별식(discriminant)은 0보다 작거나 같아야 합니다.
    5.  판별식/4 = $(E(XY|\mathcal{G}))^2 - E(X^2|\mathcal{G})E(Y^2|\mathcal{G}) \le 0$. 이로부터 원하는 결과를 얻습니다.

---

**4.1.4.** 정규 조건부 확률을 사용하여 비조건부 횔더 부등식으로부터 **조건부 횔더 부등식(conditional Hölder inequality)**을 얻어라. 즉, 만약 $p, q \in (1, \infty)$이고 $1/p + 1/q = 1$이면 다음을 보여라.

$$ E(|XY||\mathcal{G}) \le (E(|X|^p|\mathcal{G}))^{1/p} (E(|Y|^q|\mathcal{G}))^{1/q} $$

**[해설 및 힌트]**
*   **문제의 의도**: 횔더 부등식을 조건부 기댓값으로 확장하는 문제입니다. 정규 조건부 확률의 존재를 가정하면 증명이 간단해집니다.
*   **풀이 힌트**:
    1.  $X, Y$와 $\mathcal{G}$가 주어졌을 때의 정규 조건부 확률 측도 $P(\omega, \cdot)$가 존재한다고 가정합니다. 즉, $E(Z|\mathcal{G})(\omega) = \int Z(\omega') P(\omega, d\omega')$ 입니다.
    2.  각 $\omega$에 대해, $P(\omega, \cdot)$는 일반적인 확률 측도입니다. 이 측도에 대한 기댓값을 $E_\omega$라고 씁시다.
    3.  일반 횔더 부등식은 $E_\omega|XY| \le (E_\omega|X|^p)^{1/p} (E_\omega|Y|^q)^{1/q}$ 를 암시합니다.
    4.  좌변은 $E(|XY||\mathcal{G})(\omega)$이고, 우변은 $(E(|X|^p|\mathcal{G})(\omega))^{1/p} (E(|Y|^q|\mathcal{G})(\omega))^{1/q}$ 입니다. 이것이 거의 모든 $\omega$에 대해 성립합니다.

---

**4.1.5.** $\Omega = \{a,b,c\}$에서 $E(E(X|\mathcal{F}_1)|\mathcal{F}_2) \neq E(E(X|\mathcal{F}_2)|\mathcal{F}_1)$인 예를 들어라.

**[해설 및 힌트]**
*   **문제의 의도**: 정리 4.1.13(ii)의 타워 속성($\mathcal{F}_1 \subset \mathcal{F}_2$ 이면 성립)이 $\sigma$-필드들 사이에 포함 관계가 없을 때 일반적으로 성립하지 않음을 보여주는 반례를 만드는 문제입니다.
*   **풀이 힌트**:
    1.  $\Omega = \{a,b,c\}$에 확률을 부여합니다. 예를 들어, $P(\{a\})=P(\{b\})=P(\{c\})=1/3$.
    2.  $\mathcal{F}_1$과 $\mathcal{F}_2$를 서로 포함 관계가 없는 $\sigma$-필드로 잡습니다. 예를 들어, $\mathcal{F}_1 = \sigma(\{\{a,b\}, \{c\}\})$ 그리고 $\mathcal{F}_2 = \sigma(\{\{a\}, \{b,c\}\})$.
    3.  $X$를 적절한 확률 변수로 정의합니다. 예를 들어, $X(a)=1, X(b)=2, X(c)=3$.
    4.  $E(X|\mathcal{F}_1)$과 $E(X|\mathcal{F}_2)$를 계산합니다. 이들은 각 $\sigma$-필드의 생성원 위에서 상수 값을 갖는 계단 함수가 됩니다. (예: $E(X|\mathcal{F}_1)$는 $\{a,b\}$ 위에서 상수, $\{c\}$ 위에서 상수).
    5.  $E(E(X|\mathcal{F}_1)|\mathcal{F}_2)$와 $E(E(X|\mathcal{F}_2)|\mathcal{F}_1)$를 계산하여 두 결과가 다름을 보입니다.

---

**4.1.6.** 만약 $\mathcal{G} \subset \mathcal{F}$이고 $EX^2 < \infty$이면 다음을 보여라.

$$ E(\{X - E(X|\mathcal{F})\}^2) + E(\{E(X|\mathcal{F}) - E(X|\mathcal{G})\}^2) = E(\{X - E(X|\mathcal{G})\}^2) $$

왼쪽의 두 번째 항을 버리면, 기하학적으로는 부분 공간이 클수록 사영이 더 가깝다는 것을, 통계적으로는 정보가 많을수록 평균 제곱 오차가 작아진다는 것을 의미하는 부등식을 얻는다.

**[해설 및 힌트]**
*   **문제의 의도**: 이 등식은 분산 분석(ANOVA)과 유사한 아이디어를 담고 있으며, 조건부 기댓값의 사영(projection)으로서의 기하학적 의미를 보여주는 중요한 결과입니다.
*   **풀이 힌트**:
    1.  우변을 $E[(X - E(X|\mathcal{F})) + (E(X|\mathcal{F}) - E(X|\mathcal{G}))]^2$ 로 씁니다.
    2.  이것을 전개하면 $E(\{X - E(X|\mathcal{F})\}^2) + E(\{E(X|\mathcal{F}) - E(X|\mathcal{G})\}^2) + 2E[(X - E(X|\mathcal{F}))(E(X|\mathcal{F}) - E(X|\mathcal{G}))]$ 가 됩니다.
    3.  교차 곱 항(cross-product term)이 0임을 보이면 됩니다. 타워 속성을 이용합니다.
        $E[(X - E(X|\mathcal{F}))(E(X|\mathcal{F}) - E(X|\mathcal{G}))] = E[E[(X - E(X|\mathcal{F}))(E(X|\mathcal{F}) - E(X|\mathcal{G})) | \mathcal{F}]]$.
    4.  $E(X|\mathcal{F}) - E(X|\mathcal{G})$는 $\mathcal{F}$-가측이므로, $E[ (E(X|\mathcal{F}) - E(X|\mathcal{G})) \cdot E[(X - E(X|\mathcal{F})) | \mathcal{F}] ]$ 입니다.
    5.  $E[X - E(X|\mathcal{F}) | \mathcal{F}] = E(X|\mathcal{F}) - E(E(X|\mathcal{F})|\mathcal{F}) = E(X|\mathcal{F}) - E(X|\mathcal{F}) = 0$ 이므로 교차 곱 항은 0이 됩니다.

---

**4.1.7.** 이전 결과의 중요한 특별한 경우는 $\mathcal{G}=\{\emptyset, \Omega\}$일 때 발생한다. $\text{var}(X|\mathcal{F}) = E(X^2|\mathcal{F}) - E(X|\mathcal{F})^2$라고 하자. 다음을 보여라.

$$ \text{var}(X) = E(\text{var}(X|\mathcal{F})) + \text{var}(E(X|\mathcal{F})) $$

**[해설 및 힌트]**
*   **문제의 의도**: **분산 분해 공식(Variance Decomposition Formula)** 또는 **총 분산의 법칙(Law of Total Variance)**으로 알려진 매우 중요한 공식을 증명하는 문제입니다. 전체 분산은 조건부 분산의 평균과 조건부 평균의 분산의 합과 같다는 의미입니다.
*   **풀이 힌트**:
    1.  연습문제 4.1.6의 등식에서 $\mathcal{G}=\{\emptyset, \Omega\}$로 둡니다.
    2.  $E(X|\mathcal{G}) = E(X|\{\emptyset, \Omega\}) = EX$ 입니다.
    3.  등식을 다시 쓰면, $E[(X-E(X|\mathcal{F}))^2] + E[(E(X|\mathcal{F}) - EX)^2] = E[(X-EX)^2]$ 입니다.
    4.  좌변의 첫 번째 항은 $E[E[(X-E(X|\mathcal{F}))^2|\mathcal{F}]] = E[\text{var}(X|\mathcal{F})]$ 입니다. (타워 속성 사용)
    5.  좌변의 두 번째 항은 정의에 의해 $\text{var}(E(X|\mathcal{F}))$ 입니다. ($E[E(X|\mathcal{F})]=EX$ 이므로)
    6.  우변은 정의에 의해 $\text{var}(X)$ 입니다.

---

**4.1.8.** $Y_1, Y_2, \dots$는 평균 $\mu$와 분산 $\sigma^2$을 갖는 i.i.d.이고, $N$은 $EN^2 < \infty$인 독립적인 양의 정수 값 확률 변수이며, $X = Y_1+\dots+Y_N$이라고 하자. $\text{var}(X) = \sigma^2 EN + \mu^2 \text{var}(N)$임을 보여라. 공식을 이해하고 기억하는 데 도움이 되도록, $N$ 또는 $Y_i$가 상수인 두 가지 특별한 경우를 생각해보라.

**[해설 및 힌트]**
*   **문제의 의도**: 분산 분해 공식을 구체적인 예(확률 개수의 합)에 적용해보는 문제입니다.
*   **풀이 힌트**:
    1.  이전 문제의 공식 $\text{var}(X) = E(\text{var}(X|N)) + \text{var}(E(X|N))$을 사용합니다.
    2.  **$E(X|N)$ 계산**: $N=n$으로 주어지면, $X=Y_1+\dots+Y_n$ 입니다. 따라서 $E(X|N=n) = E[Y_1+\dots+Y_n] = n\mu$ 입니다. 즉, $E(X|N) = N\mu$ 입니다.
    3.  **$\text{var}(E(X|N))$ 계산**: $\text{var}(N\mu) = \mu^2 \text{var}(N)$.
    4.  **$\text{var}(X|N)$ 계산**: $N=n$으로 주어지면, $Y_i$들이 i.i.d.이므로 $\text{var}(X|N=n) = \text{var}(Y_1+\dots+Y_n) = n\sigma^2$ 입니다. 즉, $\text{var}(X|N) = N\sigma^2$ 입니다.
    5.  **$E(\text{var}(X|N))$ 계산**: $E(N\sigma^2) = \sigma^2 EN$.
    6.  두 결과를 더하면 원하는 공식을 얻습니다.
