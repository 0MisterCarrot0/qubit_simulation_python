# Registre avec |0>|0>
from Qubit import Qubit
from QuantumRegister import QuantumRegister
import gates
import numpy as np

q1 = Qubit(0.5, 0.5)
print(q1.__repr__())
q1 = gates.apply_gate_single(gates.Rphi(np.pi/2), q1)
print(q1.__repr__(True))
print(q1.proba(round_values=True))