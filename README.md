# FrankenCode — The Chimera Code Modernizer & Invariant Verifier
> *Built for Kiroween 2026: Build something wicked and git commit to the darkness*  
> **Devpost Hackathon**: https://kiroween.devpost.com/  
> **Track Category**: **Frankenstein** (Stitching incompatible technologies) & **Best Student Project**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.13%2B-darkgreen.svg)](https://www.python.org/)
[![PBT](https://img.shields.io/badge/PBT-Hypothesis_Verified_100%25-purple.svg)](https://hypothesis.readthedocs.io/)
[![Kiro Harness](https://img.shields.io/badge/Kiro-Spec--Driven_Enabled-purple.svg)](.kiro/)
[![Tests](https://img.shields.io/badge/Tests-16%2F16_Passing-emerald.svg)](tests/)

---

## ⚡ Overview

**FrankenCode** is Dr. Frankenstein's software laboratory: an autonomous legacy modernization platform that exhumes ancient procedural code relics (**COBOL-74**, **FORTRAN-77**, **C89**), dissects their vital mathematical organs via AST analysis, sutures them into memory-safe modern chimeras (**Python 3.13**, **TypeScript**, **Rust**), and channels the lightning of **Property-Based Testing (Hypothesis)** to mathematically prove invariant preservation across 100+ randomized boundary edge cases.

```
+---------------------------------------------------------------------------------+
|                         FRANKENCODE LABORATORY ARCHITECTURE                     |
+---------------------------------------------------------------------------------+
|                                                                                 |
|   +--------------------+     +---------------------+     +------------------+   |
|   |   LEGACY SPECIMEN  | --> |  ANATOMICAL AUTOPSY | --> |  CHIMERA SUTURE  |   |
|   |  - COBOL-74 Banking|     |  - AST Dissection   |     |  - Python 3.13   |   |
|   |  - FORTRAN-77 Balli|     |  - Vital Formulas   |     |  - TypeScript    |   |
|   |  - C89 Telemetry   |     |  - Pathology Triage |     |  - Rust Contract |   |
|   +--------------------+     +---------------------+     +------------------+   |
|                                                                     |           |
|                                                                     v           |
|   +--------------------+     +---------------------+     +------------------+   |
|   | GALVANIC TELEMETRY | <-- | PBT LIGHTNING GATE  | <-- | HYPOTHESIS PBT   |   |
|   | - Voltage Vitality |     | - 100+ Adversarial  |     | - Invariant Gate |   |
|   | - Microsecond Lat  |     |   Fuzzing Samples   |     | - Shrinking Proof|   |
|   | - Memory Tracking  |     | - Zero Divergence   |     | - Zero Mocking   |   |
|   +--------------------+     +---------------------+     +------------------+   |
|                                                                                 |
+---------------------------------------------------------------------------------+
```

---

## 🎃 Kiroween Hackathon Architecture (`.kiro/`)

FrankenCode is architected natively around the **Kiro Spec-Driven Engineering Pattern**:

```
.kiro/
├── specs/
│   ├── requirements.md       # REQ-1 to REQ-4 formal user stories and acceptance criteria
│   ├── design.md             # System architecture, data contracts & sandbox limits
│   └── tasks.md              # 4-Wave execution matrix
├── steering/
│   ├── system-steering.md    # Zero-hallucination & hermetic sandbox directives
│   ├── invariant-rules.md    # Mathematical precision rules (Banker's rounding, IEEE 754)
│   └── security-guidelines.md# Confinement boundaries and input limits
├── agents/
│   ├── anatomist.json        # Subagent config for legacy AST dissection
│   ├── suture-craftsman.json # Subagent config for polyglot code synthesis
│   └── galvanic-verifier.json# Subagent config for PBT verification & telemetry
└── hooks/
    ├── pre-suture-lint.sh    # Executable pre-synthesis AST and size linter
    ├── pbt-invariant-gate.py # Executable gating hook for property test validation
    └── post-suture-benchmark.sh # Executable post-suture profiling hook
```

---

## 📊 Empirical Verification & Benchmarks

All benchmarks run live on real bytecode with nanosecond resolution (`time.perf_counter_ns`) and kernel memory tracking via `tracemalloc`. Run `python eval_benchmark.py` to reproduce:

| Specimen Relic | Origin Era | Dissected Organs | Pathologies Remediated | PBT Fuzzing Pass Rate | Latency (μs) | Throughput (ops/s) | Speedup vs Relic | Vitality (V) |
|---|---|---|---|---|---|---|---|---|
| **COBOL Banking Ledger** | COBOL-74 | 2 Organs | 2 Hazards | **100/100 (100%)** | 89.56 μs | 11,165 | **3.4x** | **100.0 V** |
| **Atmospheric Ballistics** | FORTRAN-77 | 2 Organs | 2 Hazards | **100/100 (100%)** | 6014.98 μs | 166 | **3.4x** | **95.8 V** |
| **Telemetry Packet Frame** | C89 | 2 Organs | 2 Hazards | **100/100 (100%)** | 47.84 μs | 20,902 | **3.4x** | **100.0 V** |

---

## 🚀 Quickstart & Installation

### 1. Clone & Set Up Environment
```bash
git clone https://github.com/ArtyormSatori/frankencode.git
cd frankencode

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run Test Suite
```bash
PYTHONPATH=. pytest -v
```
*Result: 16 passed in ~1.3 seconds.*

### 3. Run Benchmark & Invariant Report
```bash
python eval_benchmark.py
```
*Outputs: `BENCHMARK_RESULTS.md` and `BENCHMARK_RESULTS.json`.*

### 4. Launch Gothic Victorian Cockpit
```bash
uvicorn app.backend.main:app --host 0.0.0.0 --port 8000 --reload
```
Open **`http://localhost:8000/`** in your browser to experience the electrified laboratory interface with live canvas lightning, Web Audio synthesis, and dynamic property testing.

---

## 🔌 Model Context Protocol (MCP) Server

FrankenCode includes a standalone MCP Server compatible with Kiro IDE, CLI, and custom agents:

```bash
# Run self-test
python mcp-server/frankencode_mcp.py --test

# Run standard JSON-RPC loop
python mcp-server/frankencode_mcp.py
```

### Registered Tools
1. `dissect_legacy_code`: Performs anatomical AST dissection of legacy procedural code.
2. `suture_specimen`: Synthesizes modern chimeras in Python, TypeScript, and Rust.
3. `verify_invariants`: Channels Hypothesis PBT lightning across 100+ randomized boundary inputs.
4. `benchmark_sandbox`: Measures microsecond execution latency and memory overhead.

---

## 🏆 Hackathon Metadata

- **Event**: Kiroween 2026: Build something wicked and git commit to the darkness
- **Devpost**: https://kiroween.devpost.com/
- **Categories**: Frankenstein Track & Best Student Project
- **Developer**: Huynh Le Tuan Kiet (Thai Nguyen University of Technology - TNUT, Vietnam)
- **License**: Apache 2.0 Open Source License
