import Qubit
import gates
import QuantumRegister

q1 = Qubit.Qubit(1, 0)
print(q1.__repr__())
print(q1.proba())
print(q1.measure())

q1 = gates.apply_gate(gates.H, q1)

q2 = Qubit.Qubit(0, 1)
print(q2.__repr__())
print(q2.proba())
print(q2.measure())

qr = QuantumRegister.QuantumRegister([q1, q2])
print(qr)
print(qr.proba())
print(qr.measure() + 1)