part1 에서는 강화학습 알고리즘의 대부분의 핵심 아이디어들을 가장 단순한 형태로 소개할거임.
- state, action space가 근사 action-value함수를 배열,표로 표현할 수 있을만큼 충분히 작은 형태로 소개할 것
- approximate action-value function?
  - 복잡한 문제에서 action-value함수를 추정 및 근사하기 위해 사용하는 함수임.

- action-value 함수
  - 강화학습의 기본개념. 특정 상태 $s$에서 특정 행동$a$을 했을 때, 앞으로 받을 보상의 총합에 대한 기댓값을 나타내는 함수임.

이렇게 단순한 경우에 이 방법들은 최적 가치함수와 최적 정책을 정확하게 찾아낼 수 있음. 
+ 이 파트의 첫번째 장에서는 단일 상태만 존재하는 bandit problems의 해법을 설명할 것
+ 두번째 장에서는 finite markov decision process 및 bellman equation, value function 등 중요 개념을 설명할 것.


---

2025-07-29: part 1의 4 Dynamic Programming ~ 8 Planning and Learning with Tabular Methods에 대한 intro에서의 설명은 후에 진행하겠음.

