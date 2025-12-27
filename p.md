
---

### [Step 0] 사전 준비: Context 및 Reference 설정

이 프롬프트는 AI에게 페르소나를 부여하고, 거짓 정보를 생성하지 않도록 제약 조건을 거는 단계입니다.

**프롬프트:**
```markdown
당신은 통계물리학(Statistical Physics)과 딥러닝 최적화(Deep Learning Optimization), 그리고 MCMC(Markov Chain Monte Carlo) 이론에 정통한 AI 연구자입니다. 우리는 지금부터 NeurIPS나 ICML 등 Top-tier 컨퍼런스에 제출할 수준의 논문을 작성할 것입니다.

**논문 주제:** 
"Lévy-Bayes Foraging (LBF): A Thermodynamics-based Active Data Sampling Strategy via Adaptive Lévy Noise and SVGD Repulsion"
(파이토치 데이터로더의 샘플링을 SDE 기반의 Multi-agent 탐색 문제로 재해석하여 학습 효율을 높이는 방법)

**핵심 제약 사항:**
1. 모든 주장은 수학적/논리적 근거가 있어야 합니다.
2. 인용(Citation)은 내가 아래에 제공하는 **[Reference List]**에 있는 실제 논문들만 사용해야 합니다. 만약 추가적인 인용이 필요하다면 가상의 논문을 만들지 말고, "[Need Citation for: 주제]"라고 표시해 주세요.
3. 수식은 LaTeX 포맷으로 작성해 주세요.

**[Reference List]** (이 리스트를 기반으로 인용하세요):
1. [SGLD] Welling, M., & Teh, Y. W. (2011). Bayesian learning via stochastic gradient Langevin dynamics. ICML.
2. [Lévy SGD] Simsekli, U., et al. (2019). The Heavy-Tailed Costs of Optimal Transport. (Or related: Tail-index analysis of stochastic gradient noise in deep neural networks, ICML 2019).
3. [SVGD] Liu, Q., & Wang, D. (2016). Stein Variational Gradient Descent: A General Purpose Bayesian Inference Algorithm. NeurIPS.
4. [Importance Sampling] Katharopoulos, A., & Fleuret, F. (2018). Not All Samples Are Created Equal: Deep Learning with Importance Sampling. ICML.
5. [Zeroth-Order] Liu, S., et al. (2018). Zeroth-Order Stochastic Variance Reduction for Nonconvex Optimization. NeurIPS.
6. [Curriculum Learning] Bengio, Y., et al. (2009). Curriculum learning. ICML.

이 내용을 숙지했다면 "준비 완료"라고 대답해 주세요.
```

---

### [Step 1] Introduction 작성

Introduction은 독자를 설득하는 단계입니다. "왜 기존 SGD(Uniform Sampling)는 문제인가?"를 물리적 관점에서 비판해야 합니다.

**프롬프트:**
```markdown
**Section 1: Introduction** 초안을 작성해 주세요.

**포함해야 할 핵심 흐름:**
1. **Motivation:** 딥러닝 학습은 거대한 데이터 랜드스케이프를 탐색하는 과정이다. 하지만 기존의 Uniform Random Sampling (SGD의 기본 데이터로더)은 모든 데이터를 동등하게 취급하므로, 학습 후반부에는 '쉬운 데이터(Low Information)'에 계산 자원을 낭비한다 [Citation: Curriculum Learning, Importance Sampling].
2. **Problem:** 기존의 Importance Sampling 방법들은 Gradient 편향을 줄이기 위해 복잡한 가중치 계산이 필요하거나, 단순히 Loss가 큰 데이터만 뽑다가 Outlier에 취약해지고 Mode Collapse(비슷한 하드 샘플만 반복)가 발생한다.
3. **Analogy:** 우리는 데이터 샘플링을 "Multi-agent가 먹이(정보, Loss)가 풍부한 곳을 찾아다니는 Foraging Process"로 재정의한다.
4. **Proposal (LBF):** 
    - Brownian Motion 대신 **Lévy Flight**를 도입하여 Local Minima(Redundant Data trap)를 빠르게 탈출 [Citation: Lévy SGD].
    - Loss가 높으면 Gaussian(Exploitation), 낮으면 Lévy(Exploration)로 변하는 **Adaptive $\alpha$**.
    - **SVGD Repulsion**을 도입하여 샘플 간의 다양성을 확보(Mode Collapse 방지) [Citation: SVGD].
5. **Contributions:** 요약된 3가지 기여점 (Fast Mixing, Robustness, Variance Reduction).

*톤 앤 매너: 학술적이고 설득력 있게, 문단 간 연결을 매끄럽게 작성해 줘.*
```

---

### [Step 2] Related Work 작성

여기서는 너의 제안이 기존 연구들과 어떻게 다른지 명확히 선을 그어야 합니다.

**프롬프트:**
```markdown
**Section 2: Related Work**를 작성해 주세요. 아래 세 가지 카테고리로 나누어 기술하고, 우리 모델(LBF)과의 차별점을 강조하세요.

1. **Importance Sampling & Curriculum Learning:**
    - 기존 방법: Loss 기반의 중요도 샘플링 [Katharopoulos et al.].
    - 한계: 매 Epoch마다 전수 Loss 계산이 필요하거나, 근사 오차가 큼. 우리는 이를 물리적 입자의 이동(Dynamics)으로 해결함.
2. **Langevin Dynamics in MCMC:**
    - SGLD [Welling & Teh]는 파라미터 공간($\theta$)에서의 탐색을 다룸.
    - 차별점: 우리는 파라미터가 아니라 **데이터 인덱스 공간($z$)**에서 Langevin Dynamics를 적용한다는 점이 핵심 Novelty임.
3. **Heavy-tailed Noise & Lévy Processes:**
    - SGD의 노이즈가 Heavy-tail이라는 연구들 [Simsekli et al.].
    - 차별점: 기존 연구는 현상의 '분석'에 그쳤다면, 우리는 이를 능동적으로 제어(Control)하여 데이터 탐색 알고리즘으로 승화시킴.

*각 문단 끝에 우리 방식이 왜 더 우수한지(예: 별도의 전수 조사 없이 Sampling 과정 자체로 분포를 찾아냄) 한 문장으로 요약해 줘.*
```

---

### [Step 3] Methodology (SDE 및 알고리즘)

여기가 가장 중요합니다. 앞서 우리가 정의한 수식을 체계적으로 배치합니다.

**프롬프트:**
```markdown
**Section 3: Methodology**를 작성해 주세요.
이 섹션은 우리가 앞서 논의한 수식들을 정식으로 정의하는 곳입니다.

**3.1 Problem Formulation:**
- 데이터 인덱스 공간을 연속적인 Potential Energy Landscape $U(\mathbf{z}) \propto -\log \mathcal{L}$로 정의.
- 목표 분포 $\pi(\mathbf{z}) \propto \mathcal{L}(\mathbf{z})$ (Boltzmann distribution).

**3.2 Adaptive Lévy-Langevin Dynamics:**
- Underdamped SDE 수식 제시 (Friction, Drift, Adaptive Lévy Noise).
- $\alpha(\mathcal{L})$ 함수 정의 (Sigmoid 기반 적응형 지수).
- **Zeroth-Order Gradient Estimator:** 데이터가 불연속적이므로 $\nabla U$를 과거 Loss 차이로 근사하는 수식 [Reference: Zeroth-Order Liu et al.].

**3.3 Multi-Agent Interaction (SVGD):**
- Mode Collapse 방지를 위한 Repulsion Force 수식.
- Kernel $k(\cdot, \cdot)$를 이용한 상호작용 항 추가.

**3.4 Algorithm:**
- Euler-Maruyama Discretization을 적용한 최종 알고리즘(Algorithm 1)을 슈도코드(Pseudocode) 스타일 텍스트로 기술.

*수식 번호를 매기고, 변수(Variable)의 의미를 명확히 정의해 줘.*
```

---

### [Step 4] Theoretical Analysis (증명 및 분석)

이전에 네가 요청해서 내가 답변해 준 심층 분석 내용을 여기에 넣습니다.

**프롬프트:**
```markdown
**Section 4: Theoretical Analysis**를 작성해 주세요.
이 부분은 리뷰어들에게 우리 방법론의 수학적 타당성을 증명하는 핵심 파트입니다. 앞서 우리가 토의한 내용을 바탕으로 작성하세요.

1. **Fractional Fokker-Planck Equation & Stationary Distribution:**
    - SDE에 대응하는 FFPE 제시.
    - Lévy Motion으로 인해 Stationary Distribution이 Boltzmann 분포가 아닌 **Heavy-tailed Distribution (Polynomial decay)**을 가짐을 명시.
    - 이것이 "Hard Example Mining" 관점에서 오히려 Bias가 이득이 됨을 논리적으로 설명.
2. **First Exit Time Analysis:**
    - Brownian Motion(SGD) vs Lévy Motion(LBF)의 Deep Local Minima 탈출 시간 비교.
    - Kramer’s Rate(Exponential) vs Polynomial Rate 비교 수식 제시.
    - $\alpha \to 0$일 때 탈출 확률이 급격히 높아짐을 강조.
3. **Convergence & H-Theorem:**
    - Free Energy $F = E - TH$의 시간 변화율.
    - SVGD Repulsion 항이 엔트로피 $H$를 증가시켜 $F$를 감소시키고, 다양성을 보장함을 수식적으로 설명.

*복잡한 증명은 Appendix로 뺀다고 언급하고, 본문에서는 핵심 결과(Theorem)와 직관적 해석(Remark) 위주로 서술해 줘.*
```

---

### [Step 5] Experiments (Setup) & Conclusion & Abstract

실험 결과는 아직 없으므로, 실험 설계(Design) 위주로 작성하고 논문을 마무리합니다.

**프롬프트:**
```markdown
**Section 5: Experimental Setup, Conclusion, and Abstract**를 작성해 주세요.

**5.1 Experimental Setup (Plan):**
- **Datasets:** CIFAR-100 (Imbalanced), ImageNet (Large scale).
- **Baselines:** Random Sampling (SGD), Loss-based Sampling (Fixed), SGLD Data Sampler.
- **Metrics:** Top-1 Accuracy, Convergence Speed (Wall-clock time), Loss Landscape Visualization.

**Section 6: Conclusion:**
- LBF가 데이터 로딩을 수동적인 과정에서 능동적인 물리적 탐색 과정으로 격상시켰음을 요약.
- 이론적(Fast Mixing) 및 실용적(No extra forward pass) 이점 강조.

**Abstract (마지막 작성):**
- 전체 내용을 200~250 단어로 요약.
- "Data Sampling as a Thermodynamics Problem" -> "Lévy Noise for Exploration" -> "SVGD for Diversity" -> "Theoretical Guarantee" 흐름으로 작성.

*마지막으로, 논문의 제목을 3개 정도 제안해 줘.*
```

---

### 팁 (Tip)

이 과정을 통해 초안이 나오면, 각 섹션의 내용을 **Overleaf(LaTeX 에디터)**나 워드 프로세서로 옮기면서 수식의 오류를 점검하고, 문장을 다듬으면 됩니다. 특히 **Step 4**의 이론 파트는 제가 앞서 드린 답변의 수식을 그대로 LaTeX로 옮기는 것이 가장 정확할 것입니다.
