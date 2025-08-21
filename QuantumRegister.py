#QuantumRegister
import numpy as np
import Qubit

class QuantumRegister:
    def __init__(self, qubits):
        self.qubits = qubits
        state = qubits[0].state()
        for q in qubits[1:]:
            state = np.kron(state, q.state())
        self.state = state

    def proba(self, round_values=False):
        probs = np.abs(self.state)**2
        if round_values:
            return [round(float(probs[i]), 2) for i in range(len(self.state))]
        return [float(probs[i]) for i in range(len(self.state))]

    def __repr__(self):
        return f"État global = {self.state}"
    
    def measure(self):
        probs = self.proba()
        outcome = np.random.choice(len(probs), p=probs)
        return outcome

    def set_state(self, new_state):
        self.state = new_state