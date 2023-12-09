The combination of RL and high-capacity function approximators such as neural networks holds the promise of automating a wide range of decision making and control tasks, but widespread adoption of these methods in real-world domains has been hampered by two major challenges.

RL과 신경망과 같은 고용량 function approximators의 결합은 다양한 의사결정 및 control 작업을 자동화하는 데 있어 큰 가능성을 가지고 있지만, 이러한 방법들이 실제 세계 영역에서 널리 채택되는 것은 두 가지 주요한 challenges에 의해 방해받고 있습니다.

First, model-free deep RL methods are notoriously expensive in terms of their sample complexity.

첫째, model-free deep RL methods는 그들의 sample complexity 측면에서 악명 높게 비용이 많이 듭니다.

This quickly becomes extravagantly expensive, as the number of gradient steps and samples per step needed to learn an effective policy increases with task complexity.

이는 과제의 복잡성이 증가함에 따라 효과적인 정책을 학습하는 데 필요한 gradient steps의 수와 각 step당 샘플 수가 빠르게 증가함에 따라 지나치게 비싸게 됩니다.

To that end, we draw on the maximum entropy framework, which augments the standard maximum reward reinforcement learning objective with an entropy maximization term.

이를 위해, 우리는 표준 최대 보상 강화 학습 목표에 엔트로피 최대화 term을 추가하는 최대 엔트로피 framework를 활용합니다.

Maximum entropy reinforcement learning alters the RL objective, though the original objective can be recovered using a temperature parameter.

최대 엔트로피 강화 학습은 RL 목표를 변경하지만, 원래의 목표는 temperature parameter를 사용하여 회복될 수 있습니다.

On-policy training tends to improve stability but results in poor sample complexity.

On-policy 훈련은 안정성을 향상시키는 경향이 있지만, 샘플 복잡성이 낮은 결과를 초래합니다.

A similar method can be derived as a zero-step special case of stochastic value gradients (SVG(0)).

비슷한 방법은 확률적 가치 gradients(SVG(0))의 제로-스텝 특수 사례로 유도될 수 있습니다.

the Q-function is estimating the optimal Q-function, and the actor does not directly affect the Q-function except through the data distribution.

Q-function은 최적의 Q-function을 추정하고, actor는 데이터 분포를 통해서가 아니면 Q-function에 직접적인 영향을 미치지 않습니다.

Crucially, the convergence of this method hinges on how well this sampler approximates the true posterior.

중요하게도, 이 방법의 수렴은 이 샘플러가 실제 사후 확률을 얼마나 잘 근사하는지에 달려 있습니다.

In our experiments, we demonstrate that our soft actor-critic algorithm does in fact exceed the performance of prior state-of-the-art off-policy deep RL methods by a wide margin.

우리의 실험에서, 우리는 soft actor-critic 알고리즘이 실제로 이전의 최신 off-policy deep RL 방법들의 성능을 큰 차이로 능가함을 입증합니다.

