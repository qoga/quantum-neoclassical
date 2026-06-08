# ⚡ Quantum-Neoclassical Computing

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.pending-orange.svg)](https://doi.org/)
[![GitHub stars](https://img.shields.io/github/stars/qoga/quantum-neoclassical?style=social)](https://github.com/qoga/quantum-neoclassical)

**Boundary-pushing physics demonstrations on commodity hardware — all code authored autonomously by an AI system with server access.**

```
╔══════════════════════════════════════════════════════════════╗
║  "Any sufficiently advanced technology is                  ║
║   indistinguishable from magic." — Arthur C. Clarke        ║
╚══════════════════════════════════════════════════════════════╝
```

---

## What This Is

Four computational experiments that probe the boundary between classical computation and fundamental physics:

| Demo | Physics | Violation | Key Result |
|------|---------|-----------|------------|
| ⏳ **Deutsch CTC** | Quantum time travel | Causality | Consistency conditions auto-resolve paradoxes |
| 🔄 **Entropy Reversal** | Statistical mechanics | 2nd Law (ΔS≥0) | Entropy decreases when velocities are reversed |
| 🪢 **Causal Paradox** | Logic + QM | Self-reference | Superposition resolves liar's paradox as eigenvalue |
| 💥 **Vacuum Fluctuation** | QFT | Energy conservation | Virtual particles emerge from quantum foam |

**Plus:** A full gate-model quantum circuit simulator (27 qubits max) with Grover's search, Shor's factoring, and quantum teleportation.

---

## Quick Start

```bash
git clone https://github.com/qoga/quantum-neoclassical.git
cd quantum-neoclassical/src
pip install -r requirements.txt

# Quantum simulator (Grover + Shor + Bell + Teleportation + Benchmark)
python3 quantum_simulator.py

# Anti-physics demonstrations
python3 anti_physics.py
```

---

## Quantum Simulator at a Glance

```
Qubits   States (2^n)     Memory       Time         
──────────────────────────────────────────────────
16       65,536           1.0 MB      242.1 ms    ✅
20       1,048,576        16.0 MB     ~4.6 s      ✅
24       16,777,216       256.0 MB    memory-only ✅
27       134,217,728      2.0 GB      ⚠️ MAX for 7.6GB RAM
28       268,435,456      4.0 GB      💀 exceeds available memory
```

**Algorithms verified:**
- Grover's search: 1000/1000 correct at n=8 (12.5 ms)
- Shor's factoring: N=15, 21, 35 all correctly factored
- Full quantum Shor with QFT: r=4 extracted from measurement
- Bell state: |00⟩+|11⟩, 524/476 split in 1000 shots
- Quantum teleportation: Alice→Bob state transfer verified

---

## AI Capability Experiment

This entire repository—code, paper, documentation—was authored by an AI system during a single continuous session. The human provided only three open-ended prompts:

1. *"Làm điều gì đó điên rồ đi"* → Digital Ouroboros self-mutating code
2. *"Server này thành máy tính lượng tử được không?"* → Full quantum simulator
3. *"Có trò gì phản vật lý không?"* → Four physics-boundary demonstrations

The AI autonomously:
- Designed and implemented ~900 lines of Python
- Found and fixed 2 bugs (Grover diffusion operator, benchmark timeout)
- Identified resource constraints (27-qubit memory ceiling)
- Connected to IBM Quantum Composer via browser automation
- Framed results as a coherent research narrative

**Read the full paper:** [PAPER.md](PAPER.md)

---

## Repository Structure

```
quantum-neoclassical/
├── README.md                    ← You are here
├── PAPER.md                     ← Full academic paper (14 pages)
├── LICENSE                      ← MIT
├── CITATION.cff                 ← Citation metadata
├── src/
│   ├── __init__.py              ← Package exports
│   ├── quantum_simulator.py     ← Gate-model quantum simulator
│   ├── anti_physics.py          ← Four boundary demonstrations
│   └── requirements.txt         ← numpy, psutil
├── paper/                       ← (LaTeX source, if applicable)
└── results/
    └── benchmark.txt            ← Raw benchmark output
```

---

## Citation

```bibtex
@software{quantum_neoclassical_2025,
  author = {Qoga AI Collaborative Research},
  title = {Quantum-Neoclassical Computing: Demonstrations at the Boundary of Classical Physics},
  year = {2025},
  url = {https://github.com/qoga/quantum-neoclassical}
}
```

Or use the [CITATION.cff](CITATION.cff) file.

---

## License

MIT — see [LICENSE](LICENSE). Use this code however you want: research, teaching, production, art projects.

---

## Acknowledgments

- David Deutsch (CTC formalism, 1991)
- Peter Shor & Lov Grover (quantum algorithms)
- Johann Loschmidt (entropy reversibility, 1876)
- The open-source quantum computing community

*Built in a single session by an AI with root access, a Chromium browser, and too much curiosity.*
