from environment import Environment
from agent import Agent
import visualize_cube as cube

import matplotlib.pyplot as plt
from statistics import mean
import random
import pickle
import time

env = Environment()
agent = Agent()

EPSILON = 0.01 # The higher the epsilon the more exploration
EPISODES = 1000000 # Number of episodes during training
SHOW_EVERY = 2000 # Display metrics every
MOVES_ALLOWED = 8 # Maxinum moves allowed

scramble = 4 # Number of moves to scramble

solve_count = 0
last_100_solve_count = []

# Initalize rolling metrics
ep_rewards = []
aggr_ep_rewards = {'ep': [], 'avg': [], 'max': [], 'min': []}

# Loop through episodes
for episode in range(0, EPISODES):
    env.reset()
    env.scramble(scramble)

    state = env.state()

    step_count = 0
    done = False
    solved = False
    episode_reward = 0

    all_states = []

    # Loop through steps within episode
    while not done:
        step_count += 1

        state = env.state()

        if random.uniform(0, 1) < EPSILON:
            action = agent.randomAction()
        else:
            action = agent.learnedAction(state)

        next_state, reward, done = env.step(action)

        episode_reward += reward

        if episode % SHOW_EVERY == 0:

            print(f'Episode number: {episode}')
            print(f'Solved: {solve_count} times')
            print(f'Move count: {step_count}')
            print(f'State: {state}')
            print(f'Reward: {reward}')
            print(f'Episode reward total: {episode_reward}')

            if episode > 0:
                print(f'Percent Solved for last 100: {last_100_solve_count.count(1)} %')
                percent_solved = round(solve_count * 100 / (episode), 2)
                print(f'Percent of Cubes Solved: {percent_solved} %\n')

            #env.printCube()
            #time.sleep(0.3)

        all_states.append(env.cube)

        if not done and step_count >= MOVES_ALLOWED:
            done = True
        elif done:
            solve_count += 1
            solved = True
            last_100_solve_count.append(int(1))

            # SHOW CUBE VISUALIZATIONS WHEN SOLVED
            #cube.main(all_states)


        agent.update_q_value(state, action, next_state, reward)


    ep_rewards.append(episode_reward)

    if not episode % SHOW_EVERY:
        average_reward = sum(ep_rewards[-SHOW_EVERY:])/len(ep_rewards[-SHOW_EVERY:])
        aggr_ep_rewards['ep'].append(episode)
        aggr_ep_rewards['avg'].append(average_reward)
        aggr_ep_rewards['max'].append(max(ep_rewards[-SHOW_EVERY:]))
        aggr_ep_rewards['min'].append(min(ep_rewards[-SHOW_EVERY:]))

        print(f'Episode: {episode}, average reward: {average_reward}')


    if not solved:
        last_100_solve_count.append(int(0))

    if (len(last_100_solve_count) == 100):
        del last_100_solve_count[0]

# SHOW METRIC GRAPH

plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['avg'], label="average rewards")
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['max'], label="max rewards")
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['min'], label="min rewards")
plt.legend(loc=4)
plt.show()


with open(f'models/qtable-{int(time.time())}.pickle', 'wb') as f:
    pickle.dump(agent.q_table, f)
