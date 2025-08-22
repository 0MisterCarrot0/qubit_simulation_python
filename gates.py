import numpy as np
import QuantumRegister

#Different gates : X, Y, Z, H, S, T, Rphi (Single Qubit)
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
def Rphi(phi): # Phase gate
    return np.array([[1, 0],
                     [0, np.exp(1j * phi)]])

#Different gates : CNOT, CZ, SWAP, CU (2 Qubits)
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
def CU(u00, u01, u10, u11):
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, u10, u11],
                     [0, 0, u01, u00]])

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
    quantum_register.state = gate @ quantum_register.state
    return quantum_register

def apply_gate_multi(gate, quantum_register, target_qubit):
    '''
    Made for applying a single gate on one qubit from a register
    '''
    n = len(quantum_register.qubits)
    operator = 1
    for i in reversed(range(n)):  # <-- inverser l’ordre
        if i == target_qubit:
            operator = np.kron(gate, operator)
        else:
            operator = np.kron(np.eye(2), operator)
    quantum_register.state = operator @ quantum_register.state
    return quantum_register
