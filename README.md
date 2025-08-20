# qubit_simulation_python - Mini Simulateur de Qubits en Python 🧮⚛️

Ce projet est une petite librairie éducative pour manipuler des **qubits**, appliquer des **portes quantiques** et créer des **registres quantiques** en Python.  
Il permet de visualiser les états, calculer les probabilités et simuler des mesures.

---

## 📂 Structure du projet

├── main.py # Exemple d'utilisation
├── Qubit.py # Classe Qubit
├── gates.py # Définitions des portes quantiques
└── QuantumRegister.py # Classe QuantumRegister (multi-qubits)

---

## ⚡ Fonctionnalités

- **Qubit**
  - Définir un qubit avec amplitudes complexes `alpha` et `beta`
  - Normalisation automatique de l'état
  - Calcul des probabilités (`proba`)
  - Simulation de mesure (`measure`)
  - Affichage lisible (`__repr__`)

- **Portes quantiques (`gates.py`)**
  - Pauli-X, Y, Z
  - Hadamard
  - Application de portes sur un qubit avec `apply_gate`

- **QuantumRegister**
  - Combiner plusieurs qubits en un registre (produit tensoriel)
  - Calculer les probabilités de tous les états de base (`proba`)
  - Simuler une mesure globale (`measure`)
  - Affichage de l’état global

---

## 🚀 Exemple d'utilisation

### main.py
```python
from Qubit import Qubit
import gates
from QuantumRegister import QuantumRegister

# Créer un qubit en |0>
q1 = Qubit(1, 0)
print(q1)
print(q1.proba())
print("Mesure qubit 1 :", q1.measure())

# Appliquer Hadamard -> superposition
q1 = gates.apply_gate(gates.H, q1)

# Créer un deuxième qubit en |1>
q2 = Qubit(0, 1)
print(q2)
print(q2.proba())
print("Mesure qubit 2 :", q2.measure())

# Construire un registre quantique avec 2 qubits
qr = QuantumRegister([q1, q2])
print(qr)
print("Probabilités :", qr.proba())
print("Mesure registre :", qr.measure())
