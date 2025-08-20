import Qubit
import gates
import QuantumRegister

q1 = Qubit.Qubit(0.1, 0.9)
q2 = Qubit.Qubit(0.1, 0.9)
q3 = Qubit.Qubit(0.1, 0.9)
q4 = Qubit.Qubit(0.1, 0.9)
q5 = Qubit.Qubit(0.1, 0.9)
q6 = Qubit.Qubit(0.1, 0.9)
q7 = Qubit.Qubit(0.1, 0.9)

qr = QuantumRegister.QuantumRegister([q1, q2, q3, q4, q5, q6, q7])
print(qr.__repr__())
print(qr.proba())
print(qr.measure())