Given current policy parameters φ, let φ_approx define the parameters from the actor update induced by the maximization of the approximate critic Q_θ(s, a) and φ_true the parameters from the hypothetical actor update with respect to the true underlying value function Qπ (s, a) (which is not known during learning):

현재 policy 파라미터 φ가 주어졌을 때, φ_approx는 근사 critic Q_θ(s, a)의 최대화에 의해 유도된 actor 업데이트의 파라미터를 정의하고, φ_true는 학습 중에는 알려지지 않은 진정한 기저 가치 함수 Qπ (s, a)에 대한 가상의 actor 업데이트의 파라미터를 정의합니다.

Firstly, the overestimation may develop into a more significant bias over many updates if left unchecked.

첫째, 과대추정은 검사하지 않고 방치할 경우 많은 업데이트에 걸쳐 더 중요한 편향으로 발전할 수 있습니다.

A very clear overestimation bias occurs from the learning procedure.

학습 절차로부터 매우 명확한 과대추정 편향이 발생합니다.

We further show this reduction is not sufficient experimentally in Section 6.1.

우리는 추가적으로 이 감소가 실험적으로 충분하지 않음을 섹션 6.1에서 보여줍니다.

However, the critics are not entirely independent due to the use of the opposite critic in the learning targets and the same replay buffer.

그러나, learning targets에서 opposite critic의 사용과 같은 replay buffer 때문에, critics는 완전히 독립적이지 않습니다.

It can then be shown that rather than learning an estimate of the expected return, the value estimate approximates the expected return minus the expected discounted sum of future TD-errors:

따라서 expected return의 추정을 학습하는 것보다는, 가치 추정이 expected return에서 미래 TD-errors의 expected 할인된 합을 뺀 값에 근사한다는 것을 보여줄 수 있습니다.

While a larger d would result in a larger benefit with respect to accumulating errors, for fair comparison, the critics are only trained once per time step, and training the actor for too few iterations would cripple learning. Both target networks are updated with τ = 0.005.

더 큰 d는 누적 오류에 대한 더 큰 이점을 가져올 것이지만, 공정한 비교를 위해 critics는 타임 스텝마다 한 번만 훈련되며, actor를 너무 적은 반복으로 훈련하는 것은 학습을 저해할 것입니다. 두 target 네트워크는 τ = 0.005로 업데이트됩니다.

To remove the dependency on the initial parameters of the policy, we use a purely exploratory policy for the first 10,000 time steps of stable length environments (HalfCheetah-v1 and Ant-v1) and the first 1,000 time steps for the remaining environments.

policy의 초기 파라미터에 대한 의존성을 제거하기 위해, 우리는 안정적인 길이 환경(HalfCheetah-v1 및 Ant-v1)의 처음 10,000 타임 스텝과 나머지 환경들에 대한 처음 1,000 타임 스텝 동안 순수하게 탐색적인 policy를 사용합니다.

Unlike the original implementation of DDPG, we used uncorrelated noise for exploration as we found noise drawn from the Ornstein-Uhlenbeck (Uhlenbeck & Ornstein, 1930) process offered no performance benefits.

원래 DDPG 구현과 달리, 우리는 Ornstein-Uhlenbeck (Uhlenbeck & Ornstein, 1930) 과정에서 추출된 noise가 성능 이점을 제공하지 않는다는 것을 발견하여 탐색을 위해 상관관계가 없는 noise를 사용했습니다.

Additionally, we compare our method with our re-tuned version of DDPG, which includes all architecture and hyper-parameter modifications to DDPG without any of our proposed adjustments.

또한, 우리는 제안된 조정 없이 DDPG에 대한 모든 아키텍처 및 하이퍼-파라미터 수정을 포함하는 DDPG의 재조정된 버전과 우리의 방법을 비교합니다.

This is reflected empirically, as both methods result in insignificant improvements over TD3 - CDQ, with an exception in the Ant-v1 environment, which appears to benefit greatly from any overestimation reduction.

이것은 경험적으로 반영되어 있으며, Ant-v1 환경에서의 예외를 제외하고, 두 방법 모두 TD3 - CDQ에 비해 미미한 개선을 가져옵니다. Ant-v1 환경은 어떤 과대추정 감소에서도 큰 이익을 얻는 것으로 보입니다.

As the inclusion of Clipped Double Q-learning into our full method outperforms both prior methods, this suggests that subduing the overestimations from the unbiased estimator is an effective measure to improve performance.

Clipped Double Q-learning을 우리의 전체 방법에 포함시키는 것이 이전 두 방법보다 더 우수한 성능을 보이는 것으로 나타나, 비편향 추정기에서의 과대추정을 억제하는 것이 성능 향상을 위한 효과적인 조치임을 시사합니다.

Our work investigates the importance of a standard technique in deep RL, target networks, and examines their role in limiting errors from imprecise function approximation and stochastic optimization.

우리의 연구는 deep RL에서의 표준 기술인 target 네트워크의 중요성을 조사하고, 부정확한 함수 근사와 확률적 최적화로부터 오류를 제한하는 그들의 역할을 검토합니다.

Finally, we introduce a SARSA-style regularization technique which modifies the temporal difference target to bootstrap off similar state-action pairs.

마지막으로, 우리는 비슷한 상태-행동 쌍으로부터 부트스트랩하기 위해 temporal difference target을 수정하는 SARSA 스타일의 정규화 기법을 도입합니다.

Without any lookahead search, the neural networks play Go at the level of state-of-the-art Monte Carlo tree search programs that simulate thousands of random games of self-play.

어떠한 선행 탐색 없이도, 신경망은 수천 개의 무작위 self-play 게임을 시뮬레이션하는 최신 몬테카를로 트리 탐색 프로그램 수준에서 바둑을 둡니다.

Using this search algorithm, our program AlphaGo achieved a 99.8% winning rate against other Go programs, and defeated the European Go champion by 5 games to 0.

이 탐색 알고리즘을 사용하여, 우리의 프로그램 AlphaGo는 다른 바둑 프로그램들에 대해 99.8%의 승률을 달성했으며, 유럽 바둑 챔피언을 5대 0으로 이겼습니다.

This is the first time that a computer program has defeated a human professional player in the full-sized game of Go, a feat previously thought to be at least a decade away.

이것은 컴퓨터 프로그램이 전체 크기의 바둑 게임에서 인간 프로 선수를 처음으로 이긴 사건으로, 이전에는 적어도 10년은 더 걸릴 것으로 생각되었던 업적입니다.

These policies are used to narrow the search to a beam of high probability actions, and to sample actions during rollouts.

이러한 정책들은 탐색을 높은 확률의 행동들로 좁히는 빔으로 제한하고, 롤아웃하는 동안 행동들을 샘플링하기 위해 사용됩니다.

We use these neural networks to reduce the effective depth and breadth of the search tree: evaluating positions using a value network, and sampling actions using a policy network.

우리는 이러한 신경망을 사용하여 탐색 트리의 효과적인 깊이와 너비를 줄입니다: 가치 네트워크를 사용하여 위치를 평가하고, 정책 네트워크를 사용하여 행동을 샘플링합니다.

Next, we train a reinforcement learning (RL) policy network, p_ρ, that improves the SL policy network by optimizing the final outcome of games of self-play. This adjusts the policy towards the correct goal of winning games, rather than maximizing predictive accuracy.

다음으로, 자체 플레이 게임의 최종 결과를 최적화함으로써 SL 정책 네트워크를 개선하는 강화 학습(RL) 정책 네트워크, p_ρ을 훈련합니다. 이는 예측 정확성을 최대화하기보다는 게임을 이기는 것이 올바른 목표로 정책을 조정합니다.

We play games between the current policy network p_ρ and a randomly selected previous iteration of the policy network.

우리는 현재 정책 네트워크 p_ρ와 무작위로 선택된 이전 반복의 정책 네트워크 사이에서 게임을 진행합니다.

The mean squared error between the predicted value and the actual game outcome is plotted against the stage of the game (how many moves had been played in the given position).

예측된 값과 실제 게임 결과 사이의 평균 제곱 오차는 게임의 단계(주어진 위치에서 얼마나 많은 수가 놓여졌는지)에 대해 플롯됩니다.

Figure 2,b shows the position evaluation accuracy of the value network, compared to Monte-Carlo rollouts using the fast rollout policy pπ; the value function was consistently more accurate. A single evaluation of vθ(s) also approached the accuracy of Monte-Carlo rollouts using the RL policy network pρ, but using 15,000 times less computation.

그림 2,b는 빠른 롤아웃 정책 pπ를 사용하는 몬테카를로 롤아웃과 비교하여 가치 네트워크의 위치 평가 정확도를 보여줍니다; 가치 함수는 일관되게 더 정확했습니다. 단일 vθ(s) 평가는 RL 정책 네트워크 pρ를 사용하는 몬테카를로 롤아웃의 정확도에도 접근했지만, 15,000배 적은 계산을 사용했습니다.

The tree is traversed by simulation (i.e., descending the tree in complete games without backup), starting from the root state.

트리는 루트 상태에서 시작하여 시뮬레이션(즉, 백업 없이 완전한 게임에서 트리를 내려가며)을 통해 탐색됩니다.

Evaluating policy and value networks requires several orders of magnitude more computation than traditional search heuristics.

정책 및 가치 네트워크를 평가하는 데는 전통적인 탐색 휴리스틱보다 몇 차수 더 많은 계산이 필요합니다.

In addition, we included the open source program GnuGo, a Go program using state-of-the-art search methods that preceded MCTS.

또한, MCTS보다 앞선 최첨단 검색 방법을 사용하는 바둑 프로그램인 오픈 소스 프로그램 GnuGo를 포함했습니다.

In addition, we included the open source program GnuGo, a Go program using state-of-the-art search methods that preceded MCTS.

또한, MCTS보다 앞선 최첨단 검색 방법을 사용하는 바둑 프로그램인 오픈 소스 프로그램 GnuGo를 포함했습니다.

Programs were evaluated on an Elo scale: a 230 point gap corresponds to a 79% probability of winning, which roughly corresponds to one amateur dan rank advantage on KGS;

프로그램들은 Elo 척도로 평가되었습니다: 230점의 차이는 승리 확률 79%에 해당하며, 이는 대략 KGS에서 한 아마추어 단급의 우위와 대응됩니다;

Games against the human European champion Fan Hui were also included; these games used longer time controls. 95% confidence intervals are shown.

인간 유럽 챔피언 판 후이와의 게임도 포함되었습니다; 이 게임들은 더 긴 시간 제어를 사용했습니다. 95% 신뢰 구간이 표시되어 있습니다.

Our program AlphaGo integrates these components together, at scale, in a high-performance tree search engine.

우리의 프로그램 AlphaGo는 이러한 구성 요소들을 대규모로 고성능 트리 검색 엔진에 통합합니다.

It is natural to wonder whether the same approach can be followed as for stochastic policies: adjusting the policy parameters in the direction of the policy gradient.

확률적 정책에 대해 취해진 것과 같은 접근 방식을 따를 수 있는지 궁금해하는 것은 자연스러운 일입니다: 정책 그라디언트 방향으로 정책 파라미터를 조정하는 것입니다.

We apply our deterministic actor-critic algorithms to several benchmark problems: a high-dimensional bandit; several standard benchmark reinforcement learning tasks with low dimensional action spaces; and a high-dimensional task for controlling an octopus arm.

우리는 결정론적 actor-critic 알고리즘을 여러 벤치마크 문제에 적용합니다: 고차원 밴딧; 낮은 차원의 행동 공간을 가진 여러 표준 벤치마크 강화 학습 작업; 그리고 문어 팔을 제어하는 고차원 작업입니다.

Finally, there are many applications (for example in robotics) where a differentiable control policy is provided, but where there is no functionality to inject noise into the controller.

마지막으로, (예를 들어 로봇 공학에서) 미분 가능한 제어 정책이 제공되지만 컨트롤러에 잡음을 주입하는 기능이 없는 많은 응용 분야가 있습니다.
