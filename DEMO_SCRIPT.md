# FrankenCode — Kiroween 2026 Video Demo Script & Storyboard
**Target Length**: 2 minutes 30 seconds (< 3 minutes mandatory limit)  
**Hackathon**: Kiroween 2026: Build something wicked and git commit to the darkness  
**Category**: Frankenstein (Stitching incompatible technologies) & Best Student Project  
**Platform**: YouTube Public Video Submission  

---

## Technical Setup Before Recording
1. Start FrankenCode API & UI:
   ```bash
   cd /home/adminis/hackathon-builds/frankencode
   source venv/bin/activate
   uvicorn app.backend.main:app --port 8000 --host 0.0.0.0
   ```
2. Open Browser at `http://localhost:8000/`.
3. Audio: Web Audio Galvanic Synthesizer ON (`🔊 Galvanic Audio: ON`).
4. Display resolution: 1080p (1920x1080) at 60 FPS.

---

## Detailed Storyboard & Scene Breakdown

### Scene 1: The Dark Prologue — Legacy Graveyard (0:00 - 0:25)
- **Visual**: Camera pans over the gothic header with purple lightning strikes flashing on the canvas background. Specimen shelf shows COBOL-74, FORTRAN-77, and C89 relics.
- **Screen Action**: Mouse hovers over the specimen jars; clicking on **COBOL-74 Core Ledger Suture**. The editor fills with real COBOL-74 fixed-point arithmetic code.
- **Audio**: Low atmospheric galvanic hum; crisp typewriter clicks.
- **Voiceover**:
  > "Trillion-dollar banking networks, aerospace guidance rockets, and critical infrastructure still run on ancient procedural relics from the 1970s and 80s: COBOL, Fortran, and C89. Modernizing them is terrifying because a single rounding drift or subtle arithmetic error can bankrupt an institution.  
  > Welcome to **FrankenCode** — our entry for Kiroween 2026. Dr. Frankenstein's software laboratory built natively using **Kiro's spec-driven development harness** to dissect legacy relics, suture them into modern chimeras, and mathematically prove behavioral invariants with property-based testing."

---

### Scene 2: Anatomical Autopsy — AST Extraction & Pathology Diagnoses (0:25 - 0:55)
- **Visual**: Focus zooms into Stage 2: Anatomical Autopsy panel.
- **Screen Action**: Highlight the diagnosed pathologies:
  - `[CRITICAL] PIC-Clause Fixed-Point Overflow Hazard`
  - `[WARNING] Banker's Rounding Discrepancy Risk`
  - Dissected Vital Organs: `Tiered Overdraft Penalty Valve` and `Bimetric Interest Heart`.
- **Audio**: Electric spark trigger sound (`playGalvanicSpark()`).
- **Voiceover**:
  > "Using Kiro's custom **Anatomist Agent** (`.kiro/agents/anatomist.json`), FrankenCode parses the AST of ancient procedural relics. It extracts vital formulas into formal mathematical contracts while diagnosing dangerous pathologies: fixed-width integer overflows, buffer boundaries, and floating-point singularities."

---

### Scene 3: The Suture — Multi-Era Polyglot Synthesis (0:55 - 1:25)
- **Visual**: Focus transitions to Stage 3: Synthesized Modern Chimera.
- **Screen Action**:
  - Show the Python 3.13 chimera utilizing Python's `decimal.Decimal` and `ROUND_HALF_EVEN`.
  - Click the **TypeScript** tab: show clean, strongly typed TS interface with bounds enforcement.
  - Click the **Rust Contract** tab: show safe Rust struct with fixed-point arithmetic.
- **Audio**: Suture mechanical stitching sound.
- **Voiceover**:
  > "Next, Kiro's **Suture Craftsman Agent** (`.kiro/agents/suture-craftsman.json`) synthesizes modern chimeras in Python, TypeScript, and Rust. Instead of risky manual rewrites or naive LLM hallucinations, each stitch adheres to strict steering directives (`.kiro/steering/invariant-rules.md`), encapsulating bounds-checking and defensive invariant guards."

---

### Scene 4: The Lightning Rod — Property-Based Testing Invariant Gate (1:25 - 2:05)
- **Visual**: Focus on the action bar and Stage 4 Lightning Chamber.
- **Screen Action**:
  - Click the **⚡ ELECTRIFY & SUTURE** button.
  - Canvas lightning bolts erupt across the screen.
  - Galvanic audio sparks.
  - The Property-Based Testing (Hypothesis) engine executes 100 randomized boundary cases.
  - The live result table populates: 100/100 Passed (100.0% Pass Rate).
  - The Galvanometer needle leaps to **100.0 Volts** and **11,165 Ops/sec**.
  - Triumphant four-note synthesizer chime plays.
  - Switch to Fortran Ballistics, click Electrify: watch drag vector ODEs verified.
  - Switch to C89 Telemetry Packet: watch CRC32 bit-exact unpacking verified.
- **Audio**: Dramatic thunder crash -> electric spark -> high-voltage hum -> melodic success chime.
- **Voiceover**:
  > "Now, the spark of life: **Galvanic Property-Based Verification**! We channel Hypothesis PBT through Kiro's automated hook (`.kiro/hooks/pbt-invariant-gate.py`).  
  > Across 100 randomized, adversarial boundary inputs — negative overdrafts, Mach 2.5 air resistance vectors, corrupted byteframes — FrankenCode evaluates both the legacy oracle and the modern chimera.  
  > Notice the Galvanic Vitality: **100.0 Volts**. Zero arithmetic divergence. The monster is alive — and mathematically proven identical!"

---

### Scene 5: Kiro Spec-Driven Architecture & Epilogue (2:05 - 2:30)
- **Visual**: Quick terminal cut-in showing `.kiro/` directory tree, the MCP server (`mcp-server/frankencode_mcp.py`), and `pytest` terminal run (16/16 tests passing).
- **Screen Action**: Run `./.kiro/hooks/pbt-invariant-gate.py` in terminal showing `[PBT Invariant Gate PASSED]`. Show GitHub repo with public Apache 2.0 license.
- **Voiceover**:
  > "FrankenCode is built completely on Kiro's architecture: formal specs in `.kiro/specs/`, invariant steering rules in `.kiro/steering/`, custom agent configurations, and automated CI lifecycle hooks.  
  > Don't fear legacy ghosts this Kiroween. Stitch them into living chimeras with FrankenCode.  
  > Built with pride by Huynh Le Tuan Kiet, Thai Nguyen University of Technology. Git commit to the darkness!"
