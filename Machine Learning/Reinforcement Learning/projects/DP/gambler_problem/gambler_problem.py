'''
This is Example 4.3. Gambler’s Problem from Sutton's book.
A gambler has the opportunity to make bets on the outcomes of a sequence of coin flips. 
If the coin comes up heads, he wins as many dollars as he has staked on that flip; 
if it is tails, he loses his stake. 
The game ends when the gambler wins by reaching his goal of $100, or loses by running out of money.

On each flip, the gambler must decide what portion of his capital to stake, in integer numbers of dollars. 
This problem can be formulated as an undiscounted, episodic, finite MDP.

The state is the gambler’s capital, s ∈ {1, 2, . . . , 99}. 
The actions are stakes, a ∈ {0, 1, . . . , min(s, 100 − s)}. 
The reward is zero on all transitions except those on which the gambler reaches his goal, when it is +1.

The state-value function then gives the probability of winning from each state. 
A policy is a mapping from levels of capital to stakes. 
The optimal policy maximizes the probability of reaching the goal. 
Let p_h denote the probability of the coin coming up heads.
If p_h is known, then the entire problem is known and it can be solved, for instance, by value iteration.

Note that this problem is a deterministic policy problem, not stochastic
'''

import numpy as np
import sys
import matplotlib.pyplot as plt
if "../" not in sys.path:
  sys.path.append("../")


def value_iteration_for_gamblers(p_h, goal=100, theta=0.0001, discount_factor=1.0):
    """
    Args:
        p_h: Probability of the coin coming up heads

    Returns:
        V (np.array): state values, shape (goal+1,)
        policy (np.array): policy with each element being the stake, shape: (goal+1,)
    """


    def one_step_lookahead(s, V, rewards):
        """
        Helper function to calculate the value for all action in a given state.
        
        Args:
            state: The gambler’s capital. Integer.
            V: The vector that contains values at each state. 
            rewards: The reward vector.
                        
        Returns:
            A vector containing the expected value of each action. 
            Its length equals to the number of actions.
        """

        A = np.zeros(goal + 1)
        actions = range(1, min(s, 100 - s) + 1)    # min bet is 1, maximum is 100-state+1
        for a in actions:
            A[a] = p_h * (rewards[s+a] + discount_factor * V[s+a]) + (1-p_h) * (rewards[s-a] + discount_factor * V[s-a])
        return A

    delta = float('inf')
    # Initialize 0s as initial policy and state values:
    V = np.zeros(goal + 1)
    policy = np.zeros((goal + 1,))
    rewards = np.zeros(goal + 1)
    rewards[goal] = 1

    while delta > theta:
        delta = 0
        for state in range(1, goal):
            A = one_step_lookahead(state, V, rewards)
            best_action_value = np.max(A)
            best_action = np.argmax(A)
            delta = max(delta, abs(best_action_value - V[state]))
            V[state] = best_action_value
            policy[state] = best_action

    return policy, V


policy, v = value_iteration_for_gamblers(0.25)

print("******Optimized Policy:******")
print(f"policy dimensions: {policy.shape}")
# x axis values
x = range(101)
# corresponding y axis values
y = policy
 
# plotting the bars
plt.bar(x, y, align='center', alpha=0.5)
# naming the x axis
plt.xlabel('Capital')
# naming the y axis
plt.ylabel('Final policy (stake)')
# giving a title to the graph
plt.title('Capital vs Final Policy')
# function to show the plot
plt.show()
print("")

print("******Optimized Value Function:******")
# x axis values
x = range(100)
# corresponding y axis values
y = v[:100]

# plotting the points 
plt.plot(x, y)

# naming the x axis
plt.xlabel('Capital')
# naming the y axis
plt.ylabel('Value Estimates')
 
# giving a title to the graph
plt.title('Final Policy (action stake) vs State (Capital)')

plt.show()
print("")