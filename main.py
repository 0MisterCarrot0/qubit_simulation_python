import Qubit
import gates
import QuantumRegister

q1 = Qubit.Qubit(1, 0)
q2 = Qubit.Qubit(1, 0)
q1 = gates.apply_gate_single(gates.H, q1)
qr = QuantumRegister.QuantumRegister([q1, q2])
print(qr.__repr__())
print(qr.proba(round_values=True))
gates.apply_gate_double(gates.CNOT, qr)
print(qr.__repr__())
print(qr.proba(round_values=True))
gates.apply_gate_double(gates.CNOT, qr)
print(qr.__repr__())
print(qr.proba(round_values=True))