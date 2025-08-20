import numpy as np

#Different gates : X, Y, Z, H
X = np.array([[0, 1],
              [1, 0]])
Y = np.array([[0, -1j],
              [1j, 0]])
Z = np.array([[1, 0],
              [0, -1]])
H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])

def apply_gate(gate, qubit):
    state = np.array([[qubit.alpha], [qubit.beta]])
    new_state = gate @ state
    qubit.alpha, qubit.beta = new_state[0, 0], new_state[1, 0]
    return qubit