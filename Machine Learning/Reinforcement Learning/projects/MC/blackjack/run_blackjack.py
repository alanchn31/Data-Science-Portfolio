import argparse
import numpy as np
import sys
from blackjack import BlackjackEnv


def print_observation(observation):
    score, dealer_score, usable_ace = observation
    print("Player Score: {} (Usable Ace: {}), Dealer Score: {}".format(
          score, usable_ace, dealer_score))


def strategy(observation, max_hand_points):
    score, dealer_score, usable_ace = observation
    # Stick (action 0) if the score is > max_hand_points, hit (action 1) otherwise
    return 0 if score >= max_hand_points else 1


def main(num_episodes, max_hand_points):
    env = BlackjackEnv()
    for i_episode in range(20):
        observation = env.reset()
        for t in range(num_episodes):
            print_observation(observation)
            action = strategy(observation, max_hand_points)
            print("Taking action: {}".format( ["Stick", "Hit"][action]))
            observation, reward, done, _ = env.step(action)
            if done:
                print_observation(observation)
                print("Game end. Reward: {}\n".format(float(reward)))
                break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script for playing Blackjack')
    parser.add_argument('--num_episodes', type=int, default=100,
                        help='Number of blackjack games to run')
    parser.add_argument('--max_hand_points', type=int, default=20,
                        help='Strategy for playing, number in which if not exceeded, \
                             player will continue to stick')
    args = parser.parse_args()
    main(args.num_episodes, args.max_hand_points)