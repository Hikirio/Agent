class QMemory:
    global stepX
    stepX = 3

    def __init__(self):
        self.listMemory = []

    def remember(self, q_state):
        if not self.isExist(q_state):
            self.listMemory.append(q_state)

    def isExist(self, q_state):
        for item in self.listMemory:
            if item.equals(q_state):
                return True
        return False

    def find(self, q_state):
        for item in self.listMemory:
            if item.equals(q_state):
                return item
        return None

    def getNextRightState(self, q_state):
        if q_state.getStateY() != 0:
            is_qstateR = QState([q_state.getStateX() + stepX, q_state.getStateY() + int(1), -1], 0)
            q_stateR = self.find(is_qstateR)
            if q_stateR:
                return q_stateR
            else:
                self.remember(is_qstateR)
                return is_qstateR
        return None

    def getNextLeftState(self, q_state):
        if q_state.getStateY() != 0:
            is_qstateL = QState([q_state.getStateX() - stepX, q_state.getStateY() + int(1), -1], 1)
            q_stateL = self.find(is_qstateL)
            if q_stateL:
                return q_stateL
            else:
                self.remember(is_qstateL)
                return is_qstateL
        return None

    def toString(self):
        strMemory = "count q_state=> " + str(len(self.listMemory)) + "\n"
        for item in self.listMemory:
            strMemory += item.toString() + '\n'
        return strMemory

class QState:
    def __init__(self, state, action, reward=0, nextWeightActionLeft=0, nextWeightActionRight=0):
        self.state = state
        self.nextWeightActionLeft = nextWeightActionLeft
        self.nextWeightActionRight = nextWeightActionRight
        self.reward = reward
        self.action = action

    def toString(self):
        return "state=> " + str(self.state) + " nextWeightActionLeft=> " + str(self.nextWeightActionLeft) \
               + " nextWeightActionRight=> " + str(self.nextWeightActionRight) + " reward=> " + str(self.reward) \
               + " action=>" + str(self.action)

    def setWeightActL(self, value):
        self.nextWeightActionLeft = value

    def setWeightActR(self, value):
        self.nextWeightActionRight = value

    def getWeightActL(self):
        return self.nextWeightActionLeft

    def getWeightActR(self):
        return self.nextWeightActionRight

    def getStateX(self):
        return self.state[0]

    def getStateY(self):
        return self.state[1]

    def equals(self, o):
        if (self.getStateX() == o.getStateX()) and (self.getStateY() == o.getStateY()):
            return True
        else:
            return False


__all__ = [QMemory, QState]
