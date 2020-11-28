import numpy as np
import operator
import random
import pickle

class Agent:
    def __init__(self):
        # was moves now actions keep comment for a day
        self.actions = ['U', 'U\'', 'D', 'D\'', 'R', 'R\'',  'L', 'L\'', 'F', 'F\'', 'B', 'B\'']
        self.action_dict = dict({'U':0, 'U\'':1,
                               'D':2, 'D\'':3,
                               'R':4, 'R\'':5,
                               'L':6, 'L\'':7,
                               'F':8, 'F\'':9,
                               'B':10, 'B\'':11})

        self.q_table = dict()

        with open('models/qtable-1566687218.pickle', 'rb') as pickle_file:
            self.q_table = pickle.load(pickle_file)

        self.alpha = 0.1 # alpha was at .1
        self.gamma = 0.01 # discount factor was 0.6

    def randomAction(self):
        action = random.choice(self.actions)
        return action

    def learnedAction(self, state):
        # the state will always be in the table. i need to move the block where these states are created and put it in here or another function
        if state in self.q_table:
            state_q_values = self.q_table.get(state)
            action = np.where(state_q_values == np.amax(state_q_values))
            action = int(action[0][0])

            action = self.actions[action]
        else:
            action = self.randomAction()

        return action

    def current_q_value(self, state, action_num):
        if state not in self.q_table:
            random_values = np.random.uniform(low = -2, high = 0, size = 12)

            self.q_table.update({state:random_values})
            return self.q_table.get(state)[action_num]
        else:
            return self.q_table.get(state)[action_num]

    def next_max_q_value(self, next_state):
        if next_state not in self.q_table:
            random_values = np.random.uniform(low = -2, high = 0, size = 12)

            self.q_table.update({next_state:random_values})

            next_state_values = self.q_table.get(next_state)
            return np.amax(next_state_values)
        else:
            next_state_values =  self.q_table.get(next_state)
            return np.amax(next_state_values)

    def update_q_value(self, state, action, next_state, reward):
        LEARNING_RATE = self.alpha
        DISCOUNT = self.gamma

        if isinstance(action, str):
            action_num = int(self.action_dict.get(action))
        else:
            action_num = action

        current_q_value = self.current_q_value(state, action_num)
        next_max_q_value = self.next_max_q_value(state)

        new_q_value = (1 - LEARNING_RATE) * (current_q_value) + LEARNING_RATE * (reward + DISCOUNT * next_max_q_value)

        state_values = self.q_table.get(state)
        state_values[action_num] = new_q_value

        self.q_table.update({state:state_values})
