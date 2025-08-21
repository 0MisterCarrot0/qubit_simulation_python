import numpy as np
import QuantumRegister

#Different gates : X, Y, Z, H, S, T (Single Qubit)
X = np.array([[0, 1],
              [1, 0]])
Y = np.array([[0, -1j],
              [1j, 0]])
Z = np.array([[1, 0],
              [0, -1]])
H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])
S = np.array([[1, 0],
              [0, 1j]])
T = np.array([[1, 0],
              [0, np.exp(1j * np.pi / 4)]])

#Different gates : CNOT, CZ, SWAP (2 Qubits)
CNOT = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]])
CZ = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, -1]])
SWAP = np.array([[1, 0, 0, 0],
                 [0, 0, 1, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1]])

def apply_gate_single(gate, qubit):
    '''
    Made for a single qubit
    '''
    state = np.array([[qubit.alpha], [qubit.beta]])
    new_state = gate @ state
    qubit.alpha, qubit.beta = new_state[0, 0], new_state[1, 0]
    return qubit

def apply_gate_double(gate, quantum_register):
    '''
    Made for a double QR
    '''
    state = quantum_register.state
    new_state = gate @ state
    quantum_register.set_state(new_state)