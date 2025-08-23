import numpy as np
import Qubit
import QuantumRegister
import gates

def check_qubit(q, label=""):
    print(f"\n--- {label} ---")
    print(q.__repr__(round_values=True))
    print("probabilities =", q.proba(round_values=True))
    print("state valid?", q.is_state_valid())
    print("probabilities valid?", q.is_probabilities_valid())


def check_qr(qr, label=""):
    print(f"\n--- {label} ---")
    print("state =", qr.state)
    print("probabilities =", qr.proba(round_values=True))
    print("state valid?", qr.is_state_valid())
    print("probabilities valid?", qr.is_probabilities_valid())


def test_qubits():
    print("=== TEST QUBIT ===")
    q0 = Qubit.Qubit(1, 0)  # |0>
    check_qubit(q0, "q0 (|0>)")

    q1 = Qubit.Qubit(0, 1)  # |1>
    check_qubit(q1, "q1 (|1>)")

    q_plus = Qubit.Qubit(1/np.sqrt(2), 1/np.sqrt(2))  # |+>
    check_qubit(q_plus, "q+ (|+>)")  
    # expected: probabilities {0: 0.5, 1: 0.5}

    q_phase = gates.apply_gate_single(gates.Rphi(np.pi/2), q_plus)
    check_qubit(q_phase, "q+ after Rphi(pi/2)")
    # expected: |ψ> ≈ 0.71|0> + 0.71j|1>


def test_single_gates():
    print("\n=== TEST SINGLE-QUBIT GATES ===")
    q = Qubit.Qubit(1, 0)  # |0>
    check_qubit(q, "initial |0>")

    q = gates.apply_gate_single(gates.X, q)  # → |1>
    check_qubit(q, "after X")

    q = gates.apply_gate_single(gates.H, q)  
    # H|1> = (|0> - |1>)/√2
    check_qubit(q, "after H")
    # expected: probabilities {0: 0.5, 1: 0.5}


def test_quantum_register():
    print("\n=== TEST 2-QUBIT REGISTER ===")
    q0 = Qubit.Qubit(1, 0)  # |0>
    q1 = Qubit.Qubit(1, 0)  # |0>
    qr = QuantumRegister.QuantumRegister([q0, q1])
    check_qr(qr, "initial QR (|00>)")
    # expected: [1,0,0,0]

    qr = gates.apply_gate_multi(gates.H, qr, target_qubit=0)
    check_qr(qr, "after H on q0")
    # expected: (|00>+|10>)/√2 → [0.5, 0, 0.5, 0]

    qr = gates.apply_gate_multi(gates.H, qr, target_qubit=1)
    check_qr(qr, "after H on q1")
    # expected: |++> → [0.25, 0.25, 0.25, 0.25]

    qr = gates.apply_gate_double(gates.CNOT, qr)
    check_qr(qr, "after CNOT")
    # expected: Bell state (|00>+|11>)/√2 → [0.5, 0, 0, 0.5]


def test_three_qubits():
    print("\n=== TEST 3-QUBIT REGISTER ===")
    q0 = Qubit.Qubit(1, 0)  # |0>
    q1 = Qubit.Qubit(1/np.sqrt(2), 1/np.sqrt(2))  # |+>
    q2 = Qubit.Qubit(0, 1)  # |1>
    qr = QuantumRegister.QuantumRegister([q0, q1, q2])
    check_qr(qr, "initial QR (|0>|+>|1>)")
    # expected: (|001>+|011>)/√2 → probs [0,0.5,0,0.5,0,0,0,0]

    qr = gates.apply_gate_multi(gates.H, qr, target_qubit=0)
    check_qr(qr, "after H on q0")
    # expected: (|001>+|011>+|101>+|111>)/2 → probs [0,0.25,0,0.25,0,0.25,0,0.25]


if __name__ == "__main__":
    test_qubits()
    test_single_gates()
    test_quantum_register()
    test_three_qubits()
