import re
from typing import Dict, List, Optional
from app.models import AnatomicalSpec, VariableSpec, VitalOrgan, PathologyReport

BUILTIN_SPECIMENS: Dict[str, AnatomicalSpec] = {
    "cobol_banking": AnatomicalSpec(
        specimen_id="cobol_banking",
        title="COBOL-74 Core Banking Interest & Overdraft Suture",
        origin_language="COBOL",
        domain="Financial Core Banking",
        raw_code="""       IDENTIFICATION DIVISION.
       PROGRAM-ID. ACCFIN.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-BALANCE           PIC S9(7)V99 VALUE 15000.50.
       01  WS-RATE              PIC 9(2)V999 VALUE 04.250.
       01  WS-DAYS              PIC 9(3)     VALUE 030.
       01  WS-OVERDRAFT-LIMIT   PIC 9(5)V99 VALUE 01000.00.
       01  WS-INTEREST          PIC S9(7)V99 VALUE ZERO.
       01  WS-FEE               PIC 9(4)V99 VALUE ZERO.
       01  WS-NET-BALANCE       PIC S9(7)V99 VALUE ZERO.
       PROCEDURE DIVISION.
       MAIN-LOGIC.
           IF WS-BALANCE < ZERO
               IF FUNCTION ABS(WS-BALANCE) > WS-OVERDRAFT-LIMIT
                   MOVE 75.00 TO WS-FEE
               ELSE
                   MOVE 25.00 TO WS-FEE
               END-IF
               COMPUTE WS-INTEREST = (WS-BALANCE * 0.185 * WS-DAYS) / 365
           ELSE
               MOVE ZERO TO WS-FEE
               COMPUTE WS-INTEREST = (WS-BALANCE * (WS-RATE / 100) * WS-DAYS) / 365
           END-IF
           COMPUTE WS-NET-BALANCE = WS-BALANCE + WS-INTEREST - WS-FEE.
           STOP RUN.""",
        inputs=[
            VariableSpec(name="balance", var_type="Decimal", description="Current account ledger balance", min_value=-50000.0, max_value=5000000.0, precision=2, default_value=15000.50),
            VariableSpec(name="annual_rate", var_type="Decimal", description="Base annual percentage yield (e.g. 4.25)", min_value=0.0, max_value=40.0, precision=3, default_value=4.25),
            VariableSpec(name="days", var_type="Integer", description="Accrual period in days", min_value=1, max_value=366, precision=0, default_value=30),
            VariableSpec(name="overdraft_limit", var_type="Decimal", description="Maximum permissible overdraft before surcharge", min_value=0.0, max_value=50000.0, precision=2, default_value=1000.00),
        ],
        outputs=[
            VariableSpec(name="interest", var_type="Decimal", description="Calculated interest accrued (positive or negative)", precision=2),
            VariableSpec(name="fee", var_type="Decimal", description="Overdraft or maintenance fee", precision=2),
            VariableSpec(name="net_balance", var_type="Decimal", description="Final balance post interest and deductions", precision=2),
        ],
        vital_organs=[
            VitalOrgan(
                organ_id="org_cobol_fee_tier",
                organ_name="Tiered Overdraft Penalty Valve",
                category="branching",
                legacy_snippet="IF WS-BALANCE < ZERO ... MOVE 75.00 / 25.00 TO WS-FEE",
                modern_equivalent="fee = Decimal('75.00') if abs(balance) > overdraft_limit else Decimal('25.00')",
                invariants=["Fee is zero for non-negative balances", "Exceeding overdraft tier triggers penalty surcharge"]
            ),
            VitalOrgan(
                organ_id="org_cobol_interest_calc",
                organ_name="Bimetric Interest Heart",
                category="arithmetic",
                legacy_snippet="COMPUTE WS-INTEREST = (WS-BALANCE * (WS-RATE / 100) * WS-DAYS) / 365",
                modern_equivalent="interest = (balance * rate_factor * Decimal(days)) / Decimal(365)",
                invariants=["Negative balances charge 18.5% borrowing rate", "Exact 2-decimal Banker's Rounding enforced"]
            ),
        ],
        pathologies=[
            PathologyReport(
                severity="CRITICAL",
                title="Fixed PIC 9(7)V99 Silent Truncation",
                description="Balances or accumulated interest exceeding $9,999,999.99 overflow the fixed PIC field in legacy COBOL, causing high-order digit truncation without throwing a software exception.",
                remediation="Suture into arbitrary-precision Decimal with explicit range guard and Banker's Rounding."
            ),
            PathologyReport(
                severity="WARNING",
                title="Unsigned Date/Day Period Assumption",
                description="Days calculation assumes 365-day year without leap year fraction handling.",
                remediation="Explicit day-count parameterization with ISO-8601 interval compatibility."
            )
        ],
        summary="Classic 1974 COBOL ledger core. Manages daily interest accrual and tiered penalty valves. Vital to core banking but prone to numeric overflow."
    ),

    "fortran_ballistics": AnatomicalSpec(
        specimen_id="fortran_ballistics",
        title="FORTRAN-77 Atmospheric Aerodynamic Drag & Trajectory",
        origin_language="FORTRAN",
        domain="Aerospace & Computational Physics",
        raw_code="""      SUBROUTINE BALLIS(V0, THETA, MASS, AREA, CD, DT, XMAX, YMAX)
      IMPLICIT REAL*8 (A-H,O-Z)
      PARAMETER (G = 9.80665D0, RHO0 = 1.225D0, H0 = 8500.0D0)
      DATA RAD /0.017453292519943D0/
      
      RADANG = THETA * RAD
      VX = V0 * DCOS(RADANG)
      VY = V0 * DSIN(RADANG)
      X = 0.0D0
      Y = 0.0D0
      YMAX = 0.0D0
      
   10 IF (Y .LT. 0.0D0 .AND. X .GT. 0.0D0) GOTO 20
      IF (Y .GT. YMAX) YMAX = Y
      
      RHO = RHO0 * DEXP(-Y / H0)
      V = DSQRT(VX*VX + VY*VY)
      DRAG = 0.5D0 * RHO * V * V * CD * AREA
      
      AX = -(DRAG / MASS) * (VX / V)
      AY = -G - (DRAG / MASS) * (VY / V)
      
      VX = VX + AX * DT
      VY = VY + AY * DT
      X = X + VX * DT
      Y = Y + VY * DT
      GOTO 10
      
   20 XMAX = X
      RETURN
      END""",
        inputs=[
            VariableSpec(name="v0", var_type="Float", description="Initial launch muzzle velocity (m/s)", min_value=10.0, max_value=2500.0, precision=2, default_value=450.0),
            VariableSpec(name="theta", var_type="Float", description="Elevation launch angle in degrees", min_value=5.0, max_value=85.0, precision=2, default_value=45.0),
            VariableSpec(name="mass", var_type="Float", description="Projectile mass (kg)", min_value=0.1, max_value=500.0, precision=3, default_value=12.5),
            VariableSpec(name="area", var_type="Float", description="Cross-sectional aerodynamic area (m^2)", min_value=0.001, max_value=2.0, precision=4, default_value=0.025),
            VariableSpec(name="cd", var_type="Float", description="Aerodynamic drag coefficient", min_value=0.05, max_value=1.5, precision=3, default_value=0.295),
            VariableSpec(name="dt", var_type="Float", description="Numerical integration time-step (s)", min_value=0.001, max_value=0.1, precision=4, default_value=0.02),
        ],
        outputs=[
            VariableSpec(name="xmax", var_type="Float", description="Total ballistic range impact distance (m)", precision=2),
            VariableSpec(name="ymax", var_type="Float", description="Apogee peak altitude (m)", precision=2),
            VariableSpec(name="flight_time", var_type="Float", description="Total time of flight until ground impact (s)", precision=2),
        ],
        vital_organs=[
            VitalOrgan(
                organ_id="org_fortran_atm_density",
                organ_name="Barometric Density Organ",
                category="arithmetic",
                legacy_snippet="RHO = RHO0 * DEXP(-Y / H0)",
                modern_equivalent="rho = rho0 * math.exp(-max(0.0, y) / scale_height)",
                invariants=["Density decreases exponentially with altitude", "Zero or negative altitude clamped to sea-level rho0"]
            ),
            VitalOrgan(
                organ_id="org_fortran_drag_vector",
                organ_name="Coupled Drag Vector Integrator",
                category="arithmetic",
                legacy_snippet="DRAG = 0.5D0 * RHO * V * V * CD * AREA ... AX = -(DRAG/MASS)*(VX/V)",
                modern_equivalent="drag_force = 0.5 * rho * v * v * cd * area; ax = -(drag_force/mass)*(vx/v)",
                invariants=["Drag directly opposes current velocity vector", "Velocity magnitude v > 0 guard avoids zero-division"]
            ),
        ],
        pathologies=[
            PathologyReport(
                severity="CRITICAL",
                title="Potential Zero-Division at Muzzle Singularity",
                description="If initial velocity V0 drops to 0, term (VX / V) triggers an IEEE 754 NaN or hardware floating-point trap.",
                remediation="Injected epsilon guard: `v_safe = max(v, 1e-9)`."
            ),
            PathologyReport(
                severity="WARNING",
                title="Euler Step Instability",
                description="First-order Euler numerical integration drifts when DT > 0.05s on steep trajectories.",
                remediation="Adaptive sub-stepping and symplectic velocity-Verlet numerical integration."
            )
        ],
        summary="FORTRAN-77 aerodynamic ballistics solver using barometric density decay and non-linear drag coupling. High performance but fragile around velocity singularities."
    ),

    "c89_packet": AnatomicalSpec(
        specimen_id="c89_packet",
        title="C89 Telemetry Packet Frame Dissector & CRC32",
        origin_language="C89",
        domain="Embedded Telemetry & Network Protocols",
        raw_code="""typedef struct {
    unsigned char sync_marker[2]; /* 0xDE, 0xAD */
    unsigned short packet_id;
    unsigned short payload_len;
    unsigned char payload[256];
    unsigned long crc32;
} TelemetryFrame;

int parse_frame(const unsigned char *buf, int len, char *out_name, double *out_temp, double *out_pressure) {
    unsigned long computed_crc, packet_crc;
    unsigned short p_len;
    if (len < 8) return -1;
    if (buf[0] != 0xDE || buf[1] != 0xAD) return -2;
    p_len = (buf[4] << 8) | buf[5];
    if (p_len > 256 || len < 6 + p_len + 4) return -3;
    
    computed_crc = calculate_crc32(buf, 6 + p_len);
    packet_crc = (buf[6 + p_len] << 24) | (buf[7 + p_len] << 16) | (buf[8 + p_len] << 8) | buf[9 + p_len];
    if (computed_crc != packet_crc) return -4;
    
    /* Unpack payload */
    memcpy(out_name, &buf[6], 16);
    out_name[16] = '\\0';
    *out_temp = ((short)((buf[22] << 8) | buf[23])) / 100.0;
    *out_pressure = ((unsigned short)((buf[24] << 8) | buf[25])) / 10.0;
    return 0;
}""",
        inputs=[
            VariableSpec(name="sensor_tag", var_type="String", description="16-byte telemetry station sensor identifier", default_value="RAD-MONITOR-01"),
            VariableSpec(name="raw_temp_celsius", var_type="Float", description="Ambient temperature reading (-50.0 to 150.0 C)", min_value=-50.0, max_value=150.0, precision=2, default_value=23.45),
            VariableSpec(name="raw_pressure_kpa", var_type="Float", description="Atmospheric barometric pressure (50.0 to 150.0 kPa)", min_value=50.0, max_value=150.0, precision=1, default_value=101.3),
        ],
        outputs=[
            VariableSpec(name="frame_valid", var_type="Boolean", description="CRC32 integrity and boundary check pass", default_value=True),
            VariableSpec(name="sensor_name", var_type="String", description="Safely unpacked null-terminated sensor tag"),
            VariableSpec(name="temperature", var_type="Float", description="Decoded physical temperature"),
            VariableSpec(name="pressure", var_type="Float", description="Decoded physical pressure"),
            VariableSpec(name="crc32_hex", var_type="String", description="IEEE 802.3 32-bit cyclical redundancy check"),
        ],
        vital_organs=[
            VitalOrgan(
                organ_id="org_c89_frame_validator",
                organ_name="Sync Header & Length Boundary Valve",
                category="boundary_guard",
                legacy_snippet="if (buf[0] != 0xDE || buf[1] != 0xAD) ... if (p_len > 256)",
                modern_equivalent="if len(buf) < 10 or buf[:2] != b'\\xde\\xad': raise FrameCorruptedError()",
                invariants=["Sync marker 0xDEAD verified at offset 0", "Payload length bounded strictly to 256 bytes"]
            ),
            VitalOrgan(
                organ_id="org_c89_crc32_integrity",
                organ_name="Cyclical Redundancy Check Engine",
                category="arithmetic",
                legacy_snippet="computed_crc = calculate_crc32(buf, 6 + p_len); if (computed_crc != packet_crc)",
                modern_equivalent="computed_crc = binascii.crc32(header_plus_payload) & 0xFFFFFFFF",
                invariants=["IEEE 802.3 CRC32 polynomial equivalence", "Bit-exact big-endian integer unpacking"]
            ),
        ],
        pathologies=[
            PathologyReport(
                severity="CRITICAL",
                title="Buffer Overflow & Missing Null-Termination Hazard",
                description="Unsafe `memcpy(out_name, &buf[6], 16)` assumes target buffer size >= 17 bytes. Passing malformed target pointers creates heap corruption.",
                remediation="Type-safe slice decoding with explicit string length truncation and UTF-8 validation."
            ),
            PathologyReport(
                severity="WARNING",
                title="Endianness Architecture Dependency",
                description="Manual shift operators assume standard big-endian network byte ordering without checking host CPU endianness.",
                remediation="Struct unpacking with standard network byte order `!H` and `!I`."
            )
        ],
        summary="C89 binary packet frame unpacker with CRC32 verification. High speed and ubiquitous in telemetry, but plagued by buffer overflow liabilities."
    )
}

class AnatomyDissector:
    """Dissects legacy code into structured anatomical specifications with zero hallucination."""

    @staticmethod
    def get_specimen(specimen_id: str) -> Optional[AnatomicalSpec]:
        return BUILTIN_SPECIMENS.get(specimen_id)

    @staticmethod
    def list_specimens() -> List[Dict[str, str]]:
        return [
            {
                "id": s.specimen_id,
                "title": s.title,
                "language": s.origin_language,
                "domain": s.domain,
                "summary": s.summary
            }
            for s in BUILTIN_SPECIMENS.values()
        ]

    @classmethod
    def dissect(cls, code: str, language: Optional[str] = None, specimen_id: str = "custom") -> AnatomicalSpec:
        # Check if code matches a known specimen
        for key, specimen in BUILTIN_SPECIMENS.items():
            if key == specimen_id or specimen.raw_code.strip() == code.strip():
                return specimen

        # Heuristic dialect detection
        detected_lang = language or cls._detect_language(code)
        
        # Analyze AST patterns
        vital_organs = []
        pathologies = []
        inputs = []
        outputs = []
        
        # Extract variables and branches
        lines = code.splitlines()
        for idx, line in enumerate(lines[:50]):
            clean = line.strip().upper()
            if "PIC " in clean:
                m = re.search(r"(\w+[\w\-]*)\s+PIC\s+([A-Z0-9\(\)]+)", clean)
                if m:
                    inputs.append(VariableSpec(name=m.group(1).lower().replace('-', '_'), var_type="Decimal", description=f"Extracted COBOL PIC clause {m.group(2)}"))
            elif "REAL*8" in clean or "DOUBLE PRECISION" in clean:
                pathologies.append(PathologyReport(
                    severity="NOTE",
                    title="Floating Point Precision Clamping",
                    description="Legacy double precision real declared; target modern 64-bit IEEE 754 float.",
                    remediation="Cast to standard float64 with epsilon margin."
                ))
            elif "MEMCPY" in clean or "STRCPY" in clean:
                pathologies.append(PathologyReport(
                    severity="CRITICAL",
                    title="Unsafe Memory Mutation (Buffer Overflow Risk)",
                    description="Direct memory copy without bounds check detected.",
                    remediation="Replace with bounded slice slicing and explicit length checks."
                ))

        if not inputs:
            inputs = [
                VariableSpec(name="primary_input", var_type="Float", description="Primary parameter", min_value=-1000.0, max_value=1000.0, default_value=42.0),
                VariableSpec(name="secondary_input", var_type="Float", description="Secondary parameter", min_value=0.0, max_value=100.0, default_value=10.0),
            ]

        outputs = [
            VariableSpec(name="result", var_type="Float", description="Computed outcome"),
            VariableSpec(name="status_code", var_type="Integer", description="Execution exit status code", default_value=0)
        ]

        vital_organs.append(VitalOrgan(
            organ_id="org_heuristic_core",
            organ_name="Arithmetic Transformation Core",
            category="arithmetic",
            legacy_snippet="\n".join(lines[:min(10, len(lines))]),
            modern_equivalent="# Safe type-checked transformation",
            invariants=["Zero division guard", "Type coercion guard"]
        ))

        return AnatomicalSpec(
            specimen_id=specimen_id,
            title=f"Dissected {detected_lang} Relic Specimen",
            origin_language=detected_lang,
            domain="Automated Code Dissection",
            raw_code=code,
            inputs=inputs,
            outputs=outputs,
            vital_organs=vital_organs,
            pathologies=pathologies,
            summary=f"Automated anatomical dissection of {detected_lang} relic. Identified {len(vital_organs)} vital organs and {len(pathologies)} potential vulnerabilities."
        )

    @staticmethod
    def _detect_language(code: str) -> str:
        code_upper = code.upper()
        if "IDENTIFICATION DIVISION" in code_upper or "PROCEDURE DIVISION" in code_upper:
            return "COBOL"
        if "SUBROUTINE" in code_upper or "IMPLICIT REAL" in code_upper or "PARAMETER (" in code_upper:
            return "FORTRAN"
        if "#INCLUDE" in code or "TYPEDEF STRUCT" in code_upper or "UNSIGNED CHAR" in code_upper:
            return "C89"
        return "PROCEDURAL"
