# FrankenCode — Technical Design Specification
# Architecture, Data Flow, and Invariant Engine

## 1. System Topology & Data Flow

```
┌────────────────────────────────────────────────────────────────────────┐
│                        FRANKENCODE COCKPIT UI                          │
│        (Gothic Victorian Laboratory • Galvanic Telemetry • Canvas)     │
└───────────────▲───────────────────────────────────────▲────────────────┘
                │ HTTP REST / SSE                       │ JSON Telemetry
┌───────────────▼───────────────────────────────────────▼────────────────┐
│                       FASTAPI BACKEND SERVICE                          │
│                                                                        │
│   ┌────────────────────┐   ┌───────────────────┐   ┌───────────────┐   │
│   │   Anatomy Parser   │──►│  Suture Synthesizer──►│  PBT Fuzzer   │   │
│   │ (AST & Specimen)   │   │ (Modern Generator)│   │ (Hypothesis)  │   │
│   └────────────────────┘   └───────────────────┘   └───────┬───────┘   │
│                                                            │           │
│                            ┌───────────────────┐           │           │
│                            │ Galvanic Sandbox  │◄──────────┘           │
│                            │ (Isolated Runner) │                       │
│                            └───────────────────┘                       │
└───────────────────────────────────▲────────────────────────────────────┘
                                    │ Model Context Protocol
┌───────────────────────────────────▼────────────────────────────────────┐
│                    FRANKENCODE MCP SERVER (KIRO TOOL)                  │
│  - dissect_legacy_code(code, lang)                                     │
│  - run_pbt_verification(spec, code)                                    │
│  - execute_chimera_sandbox(code, inputs)                               │
└────────────────────────────────────────────────────────────────────────┘
```

## 2. Core Modules

### 2.1 Anatomy Parser (`app/core/dissector.py`)
- Analyzes input source in supported dialects:
  - `COBOL`: Variable sections (`WORKING-STORAGE SECTION`), `COMPUTE`, `PERFORM`, financial picture clauses `PIC 9(7)V99`.
  - `FORTRAN`: Column-based or free-form equations, subroutines, `REAL*8`, math intrinsic calls (`SIN`, `EXP`, `SQRT`).
  - `C89`: Legacy structs, pointer arithmetic, memory bounds, function signatures.
- Output: `AnatomicalSpec` Pydantic model:
  - `specimen_name`: identifier.
  - `language`: COBOL / FORTRAN / C / PROCEDURAL.
  - `inputs`: list of `{name, type, min_val, max_val, precision}`.
  - `outputs`: list of `{name, type, description}`.
  - `vital_organs`: extracted logic formulas, conditional branches, boundary rules.
  - `diagnosed_pathologies`: known hazards (overflow risk, unsafe pointer, NaN hazard).

### 2.2 Suture Synthesizer (`app/core/suture_engine.py`)
- Takes `AnatomicalSpec` and produces clean modern Python and TypeScript equivalents.
- Enforces defensive invariants:
  - Strict type hints (`typing.TypedDict`, `decimal.Decimal` for COBOL currency).
  - Explicit divide-by-zero checks and domain clamping.
  - Zero external unsafe dependencies.

### 2.3 PBT Verifier (`app/core/pbt_verifier.py`)
- Implements Hypothesis Property-Based Testing strategy:
  - `hypothesis.strategies.floats()`, `integers()`, `text()`, `decimals()`.
  - Invariant 1: **Monotonicity / Mathematical Soundness** (outputs remain within defined physical/financial limits).
  - Invariant 2: **Equivalence with Legacy Oracle** (given valid input $X$, legacy calculation and sutured calculation match within tolerance $\epsilon = 10^{-6}$ or exact integer cents).
  - Invariant 3: **Total Exception Immunity** (no unhandled panics, segfaults, or overflow crashes on boundary inputs).

### 2.4 Galvanic Sandbox (`app/core/sandbox.py`)
- Executes Python and WebAssembly-ready logic in an isolated process.
- Captures wall-clock time in microseconds (`time.perf_counter_ns()`), peak memory allocation via `resource` / `tracemalloc`.
- Calculates Galvanic Vitality Score:
  $$V = 0.4 \times PBT_{pass\_rate} + 0.3 \times \min(100, \frac{1000}{\mu s}) + 0.3 \times Invariant_{score}$$

## 3. Kiro Steering & Hook Enforcement
- Hooks trigger before and after code stitching:
  - `pre-suture-lint.sh`: Scans AST for security violations (no `eval`, no arbitrary syscalls).
  - `pbt-invariant-gate.py`: Executes 100 test runs per specimen; blocks suture if pass rate < 100%.
  - `post-suture-benchmark.sh`: Verifies that modernized code achieves minimum 2x throughput vs simulated legacy interpreter.
