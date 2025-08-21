# qubit_simulation_python - Mini Qubit Simulator in Python 🧮⚛️

This project is a small educational library to manipulate **qubits**, apply **quantum gates**, and build **quantum registers** in Python.  
It allows you to visualize states, compute probabilities, and simulate measurements.

---

## 📂 Project Structure

├── main.py              # Example usage  
├── Qubit.py             # Qubit class  
├── gates.py             # Quantum gates definitions  
└── QuantumRegister.py   # QuantumRegister class (multi-qubits)  

---

## ⚡ Features

- **Qubit**
  - Define a qubit with complex amplitudes `alpha` and `beta`
  - Automatic state normalization
  - Probability calculation (`proba`)
  - Measurement simulation (`measure`)
  - Readable display (`__repr__`)

- **Quantum Gates (`gates.py`) for single qubit**
  - Pauli-X, Y, Z
  - Hadamard
  - Apply gates to a qubit with `apply_gate_single`
 
- **Quantum Gates (`gates.py`) for double qubit quantum register**
  - CNOT, CZ, SWAP
  - Apply gates do a double qubit QR with `apply_gate_double`

- **QuantumRegister**
  - Combine several qubits into a register (tensor product)
  - Compute probabilities of all basis states (`proba`)
  - Simulate a global measurement (`measure`)
  - Display of the global state
  - Set new state with `set_state`

---

## 🚀 Example Usage

### main.py
```python
from Qubit import Qubit
import gates
from QuantumRegister import QuantumRegister

#Simulation of Bell's state

q1 = Qubit.Qubit(1, 0)
q2 = Qubit.Qubit(1, 0)
q1 = gates.apply_gate_single(gates.H, q1) #Applying Hadamard on the first qubit
qr = QuantumRegister.QuantumRegister([q1, q2])
gates.apply_gate_double(gates.CNOT, qr)

#Bell's state
print(qr.__repr__())
print(qr.proba(round_values=True))

```
