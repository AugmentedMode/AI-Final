from environment import Environment
from agent import Agent
import visualize_cube as cube

from statistics import mean
import time

env = Environment()
agent = Agent()

EPISODES = 4000 # Number of episodes during training
MOVES_ALLOWED = 20 # Maxinum moves allowed

scramble = 14 # Number of moves to scramble

solve_count = 0

# Loop through episodes
for episode in range(0, EPISODES):
    env.reset()
    env.scramble(scramble)

    state = env.state()

    step_count = 0
    done = False
    solved = False

    all_states = []

    # Loop through steps within episode
    while not done:
        step_count += 1

        state = env.state()

        action = agent.learnedAction(state)

        next_state, reward, done = env.step(action)

        all_states.append(env.cube)

        if not done and step_count >= MOVES_ALLOWED:
            done = True
        elif done:
            solve_count += 1
            solved = True

            # SHOW CUBE VISUALIZATIONS WHEN SOLVED
            cube.main(all_states)


        agent.update_q_value(state, action, next_state, reward)
