
### **최종 실험 계획 요약 테이블 (Comprehensive Experiment Plan Summary)**

| 단계 | 실험 ID | 실험명 (Experiment Name) | 목적 | 방법론 | 주요 스크립트 | 핵심 결과물/지표 | 가설 (기대 결과) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Phase 1: Foundational Validation** | E1.1 | Cross-Regime Gradient Alignment | MAML의 필요성 입증 | 레짐 간 Gradient Cosine Sim. 계산 | `exp1_gradient_alignment.py` | Heatmap | 비대각 성분 < 0.2 (낮은 상관관계) |
| | E1.2 | HRP Structural Stability | HRP의 구조적 안정성 입증 | Local Condition Number 분포 비교 | `exp2_covariance_stability.py` | KDE Plot | HRP < Random (안정적) |
| | E1.3 | HRP Learning Efficiency | HRP의 학습 효율성 입증 | Learning Curve 비교 | `exp2b_learning_efficiency.py` | MSE Loss Curve | HRP가 더 빠르게 낮은 Loss 도달 |
| | E1.4 | Prop 2: Covariance Sensitivity | Prop 2: Cov. 민감도 검증 | Shrinkage 강도별 민감도 회귀분석 | `020_dominance_ratio.py` | Log-Log Plot, Slope | Slope ≈ -1.0 |
| **Phase 2: Main Performance** | E2.1 | Comprehensive Backtest | 전체 모델 성과 비교 | 종합 백테스트 실행 | `012b_backtester_ablation.py` | 수익률/회전율 시계열 | - |
| | E2.2 | Financial Performance Metrics | 금융 성과 지표 산출 | CAGR, Sharpe, MDD 등 계산 | `013_performance_analysis.py` | 성과 지표 테이블, 그래프 | Meta > Pooled > Baselines |
| | E2.3 | Statistical Significance Test | 통계적 유의성 검증 | Bootstrap Sharpe Difference | `018_significance_test.py` | P-value | Meta vs. Others, p < 0.05 |
| **Phase 3: Ablation & Sensitivity** | E3.1 | Architecture Ablation | 아키텍처 요소 기여도 분석 | Attention/Skip-Connection 제거 후 성능 비교 | `012b_...`, `022_...` | Test MSE, Sharpe | Full Model > Ablated Model |
| | E3.2 | Meta-Learning Effect | Meta-Learning 효과 검증 | Adaptation 전/후 Loss 개선율 측정 | `013_diagnostics.py` | 개선율 분포 Histogram | 평균 개선율 > 0 |
| | E3.3 | Sensitivity to K (Regime Count) | K(Regime 개수) 민감도 분석 | K별 BIC 점수 및 백테스트 성과 비교 | `024_bic_for_k.py`, `012b_...` | BIC Score, Sharpe Table | K=4 근방에서 최적, 타 K값도 강건 |
| | E3.4 | Sensitivity to `tau` (Purity) | `tau` 민감도 분석 | `tau` 값 변경하며 백테스트 반복 | `005_...`, `011_...`, `012_...` | Sharpe vs. `tau` 그래프 | 합리적 범위 내에서 성능 안정적 |
| | E3.5 | Sensitivity to `kappa` (Cost) | `kappa` 민감도 분석 | `kappa` 값 변경하며 백테스트 반복 | `012b_backtester_ablation.py` | Sharpe vs. `kappa` 테이블 | 합리적 비용 수준에서 우위 유지 |
| | E3.6 | Stress Testing (Crisis Periods) | 위기 구간 방어 능력 평가 | 특정 위기 기간 성과 슬라이싱 분석 | `013_performance_analysis.py` | 위기 구간 MDD, 수익률 | Meta 모델의 하락 방어 우위 |
| **Phase 4: Deep Dives** | E4.1 | Thm 3: Chebyshev Geometry | Thm 3: 기하학적 검증 | 파라미터 공간 PCA 시각화 | `019_chebyshev_geometry.py` | 2D Scatter Plot | `theta_0`가 `theta_s*`들의 중앙에 위치 |
| | E4.2 | Thm 4: Robustness to Noise | Thm 4: 오탐지 강건성 검증 | Posterior 노이즈 주입 후 Loss 비교 | `021_posterior_noise.py` | Noise vs. Loss 그래프 | Soft-MAML의 성능 저하가 더 완만 |
| | E4.3 | Uncertainty Quantification | 모델 불확실성 정량화 | Regime별 Conformal Prediction Interval 계산 | `026_conformal_prediction_adaptive.py`| Regime별 Interval Width | 변동성 높은 Regime에서 Width 증가 |
| | E4.4 | Qualitative Case Study | 정성적 사례 연구 | 특정 위기 구간 시각화 | `006_...`, `021_..._2.py` | 시계열 그래프 (Posterior, Turnover) | Soft-MAML이 더 부드럽게 반응 |
| **Phase 5: Advanced Topics** | E5.1 | Post-Cost & Capacity Analysis | 실용성 검증 (퀀트) | 거래비용 차감 후 성과 및 AUM 한계 추정 | `013_...`, (추가 분석) | Cost-adjusted Sharpe | 실거래 비용 고려 시에도 우위 유지 |
| | E5.2 | Factor Exposure Analysis | 수익원 규명 (퀀트) | Fama-French 5-Factor 회귀분석 | (추가 분석) | Alpha, Beta 시계열 | 유의미한 Alpha 존재, 레짐별 Beta 변화 |
| | E5.3 | Bayesian Uncertainty | 불확실성 분해 (베이지안) | Deep Ensemble 구성 후 분산 분석 | (추가 학습/분석) | Epistemic Uncertainty 시계열 | 불확실성 지표와 미래 변동성 간 양의 상관관계 |
| | E5.4 | Architecture Comparison | 아키텍처 선택 타당성 (모델링) | U-Net vs. Transformer 성능 비교 | (추가 학습/백테스트) | 4개 조합(Arch x Order) 성과 테이블 | U-Net+HRP 조합이 가장 우수 |
| | E5.5 | Loss Function Ablation | 손실 함수 영향 분석 (모델링) | MSE vs. Differential Sharpe Ratio 학습/비교 | (추가 학습/백테스트) | 최종 Sharpe Ratio | 금융 목적 함수가 더 나은 성과를 보일 수 있음 |
| | E5.6 | Feature Set Ablation | 피처 엔지니어링 중요도 (학생) | Minimal vs. Full 피처셋 성능 비교 | (추가 학습/백테스트) | Sharpe Ratio | Full > Minimal, 그러나 Minimal도 준수한 성능 |
| | E5.7 | Lookback Window Sensitivity | 과거 정보 길이 영향 (학생) | `T_hist` 변경하며 백테스트 반복 | (데이터셋 재구성/재학습) | Sharpe vs. `T_hist` 그래프 | 60~120일 근방에서 최적점 존재 |
| | E5.8 | Regime Definition Sensitivity | 레짐 정의 방식 강건성 (학생) | VIX 기반 단순 레짐으로 재학습/비교 | (데이터셋 재구성/재학습) | Sharpe Ratio | 성능 소폭 하락하나, 프레임워크의 우위는 유지 |
