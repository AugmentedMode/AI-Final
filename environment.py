import pandas as pd
import random
import py222

class Environment:
    def __init__(self):
        # creates Rubik's cube object
        self.cube = py222.initState()

    def step(self, action):
        state = self.state()

        self.executeAction(str(action))

        nextState = self.state()

        done = self.is_done()

        reward = self.reward(done)


        return nextState, reward, done

    def executeAction(self, action):
        self.cube = py222.doAlgStr(self.cube, action)

    def randomMove(self):
        moves = ['U', 'F', 'R', 'U\'', 'F\'', 'R\'', 'D', 'L', 'B', 'D\'', 'L', 'B\'']
        move = random.choice(moves)

        return move

    def reward(self, done):
        if done:
            return 100 #+ reward
        else:
            return 0 #+ reward

    def scramble(self, n):
        moves = ['U', 'F', 'R', 'U\'', 'F\'', 'R\'', 'D', 'L', 'B', 'D\'', 'L', 'B\'']

        alg = []
        for i in range(n):
            action = random.choice(moves)
            self.executeAction(action)

        return alg

    def state(self):
        temp = list(self.cube)
        state = ''.join(str(s) for s in temp)

        return str(state)

    def reset(self):
        self.cube = py222.initState()

    def is_done(self):
        return py222.isSolved(self.cube)

    def printCube(self):
        py222.printCube(self.cube)



        '''
        reward = 0

        side_1 = self.cube[0] == self.cube[1] == self.cube[2] == self.cube[3]
        side_2 = self.cube[4] == self.cube[5] == self.cube[6] == self.cube[7]
        side_3 = self.cube[8] == self.cube[9] == self.cube[10] == self.cube[11]
        side_4 = self.cube[12] == self.cube[13] == self.cube[14] == self.cube[15]
        side_5 = self.cube[16] == self.cube[17] == self.cube[18] == self.cube[19]
        side_6 = self.cube[20] == self.cube[21] == self.cube[22] == self.cube[23]

        if side_1:
            if self.cube[8] == self.cube[9] and self.cube[4] == self.cube[5] and self.cube[20] == self.cube[21] and self.cube[16] == self.cube[17]:
                reward += 30
                return reward
            else:
                reward += 10
                return reward
        elif side_2:
            if self.cube[1] == self.cube[3] and self.cube[9] == self.cube[11] and self.cube[13] == self.cube[15] and self.cube[20] == self.cube[22]:
                reward += 30
                return reward
            else:
                reward += 10
                return reward
        elif side_3:
            if self.cube[2] == self.cube[3] and self.cube[4] == self.cube[6] and self.cube[12] == self.cube[13] and self.cube[17] == self.cube[19]:
                reward += 30
                return reward
            else:
                reward += 10
                return reward
        elif side_4:
            if self.cube[10] == self.cube[11] and self.cube[6] == self.cube[7] and self.cube[18] == self.cube[19] and self.cube[22] == self.cube[23]:
                reward += 30
                return reward
            else:
                reward += 10
                return reward
        elif side_5:
            if self.cube[0] == self.cube[2] and self.cube[12] == self.cube[8] and self.cube[10] == self.cube[13] and self.cube[21] == self.cube[23]:
                reward += 30
                return reward
            else:
                reward += 10
                return reward
        elif side_6:
            if self.cube[5] == self.cube[7] and self.cube[0] == self.cube[1] and self.cube[14] == self.cube[15] and self.cube[16] == self.cube[18]:
                reward += 30
                return reward
            else:
                reward += 10
                return reward
        '''
