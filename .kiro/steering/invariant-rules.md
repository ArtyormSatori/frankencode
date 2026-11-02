# FrankenCode — Invariant Rules
# Rules for Equivalence Verification across Dialects

## Invariant 1: Financial & Arithmetic Precision (COBOL)
- Currency calculations MUST use exact fixed-point or `decimal.Decimal` with Banker's Rounding (`ROUND_HALF_EVEN`).
- Overflow protection: Any input exceeding the legacy PIC clause (e.g. `PIC 9(7)V99` -> 9,999,999.99) MUST raise a structured `ArithmeticDomainError` rather than silently wrapping or truncating.

## Invariant 2: Physical Continuity & Bounded Dynamics (Fortran)
- Floating-point calculations MUST maintain relative error within $\epsilon \le 10^{-6}$ of double-precision IEEE 754 reference.
- Domain guard: Divisors with $|\text{denominator}| < 10^{-12}$ or square roots of negative numbers MUST be clamped or handled via explicit domain guards.

## Invariant 3: Memory & Buffer Safety (C89)
- Buffer boundary: String extraction MUST enforce strict bounds checking with zero possibility of buffer overrun or null-byte omission.
- Checksums: CRC32 calculations MUST match standard IEEE 802.3 polynomial `0xEDB88320` across arbitrary binary payloads.
