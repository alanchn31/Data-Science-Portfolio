import argparse
import gym
import numpy as np
import random
import math
import argparse


def example_mode(env):
    env.reset()
    # Randomly select an action for 1000 steps
    for _ in range(1000):
        env.render()
        env.step(env.action_space.sample())


def policy_mode(env):
    # Define number of buckets
    num_buckets = (1, 1, 6, 3)
    num_actions = env.action_space.n

    state_value_bounds = list(zip(env.observation_space.low, env.observation_space.high))

    # Specify cart's velocity bounds:
    state_value_bounds[1] = [-0.5, 0.5]

    # Specify cart's pole angle bounds:
    state_value_bounds[1] = [-math.radians(50), math.radians(50)]

    action_index = len(num_buckets)
    q_value_table = np.zeros(num_buckets + (num_actions,))

    min_explore_rate = 0.01
    min_learning_rate = 0.1
    max_episodes = 1000
    max_time_steps = 250
    streak_to_end = 120
    solved_time = 199
    discount = 0.99
    num_streaks = 0

    # Define function to selection action based on criteria (exploration/exploitation)
    def select_action(state_value, explore_rate):
        if random.random() < explore_rate:
            action = environment.action_space.sample()
        else:
            action = np.argmax(q_value_table[state_value])
        return action

    
    def select_explore_rate(x):
        return max(min_explore_rate, min(1, 1.0 - math.log10((x + 1) /25)))
    

    def select_learning_rate(x):
        return max(min_learning_rate, min(0.5, 1.0 - math.log10((x + 1) / 25)))


    def bucketize_state_value(state_value):
        bucket_indexes = []
        for i in range(len(state_value)):
            if state_value[i] <= state_value_bounds[i][0]:
                bucket_index = 0
            elif state_value[i] >= state_value_bounds[i][1]:
                bucket_index = num_buckets[i] - 1
            else:
                bound_width = state_value_bounds[i][1] - state_value_bounds[i][0]
                offset = (num_buckets[i] - 1) * state_value_bounds[i][0] / bound_width
                scaling = (num_buckets[i] - 1) / bound_width
                bucket_index = int(round(scaling * state_value[i] - offset))
            bucket_indexes.append(bucket_index)
        return tuple(bucket_indexes)
    
    # Train the episodes:
    for episode_num in range(max_episodes):
        explore_rate = select_explore_rate(episode_num)
        learning_rate = select_learning_rate(episode_num)

        observation = env.reset()

        start_state_value = bucketize_state_value(observation)
        previous_state_value = start_state_value

        for time_step in range(max_time_steps):
            env.render()
            selected_action = select_action(previous_state_value, explore_rate)
            observation, reward_gain, completed, _ = env.step(selected_action)
            state_value = bucketize_state_value(observation)
            best_q_value = np.amax(q_value_table[state_value])
            q_value_table[previous_state_value + (selected_action,)] += learning_rate * (
                                                                                         reward_gain + discount * (best_q_value) - q_value_table[previous_state_value + (selected_action,)])
            print('episode number: %d' % episode_no)
            print('time sterp: %d' % time_step)
            print('selected action: %d' % selected_action)
            print('current state: %s' % str(state_value))
            print('reward obtained: %f' % reward_gain)
            print('best Q value: %f' % best_q_value)
            print('learning rate: %f' % learning_rate)
            print('explore rate: %f' % explore_rate)
            print('streak number: %d' % num_streaks)

            if completed:
                print('Episode %d finished after %f time steps' % (episode_num, time_step))
                if time_step >= solved_time:
                    num_streaks += 1
                else:
                    num_streaks = 0
                break
            
            previous_state_value = state_value
        
        if num_streaks > streak_to_end:
            break

def main(mode):
    # Create environment for playing Cartpole
    env = gym.make('CartPole-v0')

    if mode == 'example_mode':
        example_mode(env)
    else:
        policy_mode(env)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script for playing CartPole-v0')
    parser.add_argument('mode', type=str, const='policy',
                        help='Mode for running cartpole, \
                              either example_mode (without optimization) \
                              or policy (with optimization)')
    args = parser.parse_args()

    assert args.mode in ['example_mode', 'policy']
    main(args.mode)