"""
Quantum-Neoclassical Computing — Research Toolkit
==================================================
"""
from .quantum_simulator import (
    QuantumSimulator,
    bell_state,
    grovers_search_v2,
    shors_algorithm,
    shors_full_quantum,
    quantum_teleportation,
    push_limits,
    qft_inverse,
)
from .anti_physics import (
    deutsch_ctc,
    reverse_thermodynamics,
    causal_paradox,
    quantum_fluctuation,
)

__version__ = "0.1.0"
