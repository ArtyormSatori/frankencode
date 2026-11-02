# FrankenCode — Task Breakdown & Implementation Waves
# Kiro Wave Dependency Graph & Execution Matrix

## Wave 1: Core Engine & Data Models (Independent Baseline)
- [x] **Task 1.1**: Define Pydantic models for `AnatomicalSpec`, `SutureResult`, `PBTReport`, `GalvanicTelemetry`.
- [x] **Task 1.2**: Implement `app/core/dissector.py` with AST & heuristic parsers for COBOL, Fortran, and C89 specimens.
- [x] **Task 1.3**: Implement curated legacy specimens:
  - `COBOL-BANK-01`: Compound interest, tier fee schedule & overdraft penalty calculation.
  - `FORTRAN-TRAJ-02`: Atmospheric projectile drag, Reynolds number & trajectory integration.
  - `C89-PACKET-03`: CRC32 checksum, byte unpacking & bounded string buffer extractor.

## Wave 2: Suture Engine & PBT Invariant Gate (Depends on Wave 1)
- [x] **Task 2.1**: Implement `app/core/suture_engine.py` generating modern type-safe Python and TypeScript modules.
- [x] **Task 2.2**: Implement `app/core/pbt_verifier.py` with Hypothesis test suites testing mathematical equivalence, boundary behavior, and invariant preservation.
- [x] **Task 2.3**: Implement `app/core/sandbox.py` with microsecond telemetry and memory measurement.

## Wave 3: MCP Server & Kiro Integration (Parallel with Wave 2)
- [x] **Task 3.1**: Create `mcp-server/frankencode_mcp.py` exposing MCP endpoints to Kiro IDE/CLI.
- [x] **Task 3.2**: Configure `.kiro/agents/` (Anatomist, Suture Craftsman, Galvanic Verifier).
- [x] **Task 3.3**: Configure `.kiro/hooks/` (pre-suture lint, PBT gate, post-benchmark).
- [x] **Task 3.4**: Write `.kiro/steering/` (system-steering, invariant-rules, security-guidelines).

## Wave 4: Gothic Web Cockpit & Interactive Visuals (Depends on Wave 1-2)
- [x] **Task 4.1**: Build FastAPI backend endpoints in `app/backend/main.py`.
- [x] **Task 4.2**: Build responsive Gothic Victorian Laboratory UI (`app/frontend/index.html`, `styles.css`, `app.js`):
  - Specimen Selector (COBOL, Fortran, C89 + Custom code input).
  - Multi-tab Anatomical Autopsy viewer.
  - Galvanic Lightning Chamber with canvas particle animations.
  - Dual Galvanometer meters (Equivalence Voltage & Latency Amperage).
  - Audio sound design with Web Audio synthesizer (galvanic spark hum & success chime).
  - 1-Click "Electrify & Suture" workflow.

## Wave 5: Verification, Benchmarks & Submission (Terminal Wave)
- [x] **Task 5.1**: Write automated pytest suite covering 100% of core components (`tests/`).
- [x] **Task 5.2**: Run empirical benchmark comparing legacy vs chimera execution across 1,000 iterations (`eval_benchmark.py` -> `BENCHMARK_RESULTS.json`).
- [x] **Task 5.3**: Write comprehensive `README.md`, `LICENSE` (MIT), `.gitignore` (safeguarding `/.kiro`).
- [x] **Task 5.4**: Create `SUBMISSION.md` and `DEMO_SCRIPT.md` tailored for Kiroween 2026 Devpost judges.
- [x] **Task 5.5**: Initialize Git repo, commit all assets, create public GitHub repository `ArtyormSatori/frankencode`, and push.
