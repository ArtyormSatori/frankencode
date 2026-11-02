import pytest
from decimal import Decimal
from hypothesis import given, strategies as st, settings
from app.core.dissector import AnatomyDissector
from app.core.suture_engine import SutureEngine
from app.core.pbt_verifier import PBTVerifier

# 1. PBT for COBOL Banking Specimen
@settings(max_examples=50, deadline=None)
@given(
    bal=st.decimals(min_value=-50000, max_value=500000, places=2),
    rate=st.decimals(min_value=Decimal("0.1"), max_value=Decimal("30.0"), places=3),
    days=st.integers(min_value=1, max_value=365)
)
def test_pbt_cobol_banking_invariants(bal, rate, days):
    spec = AnatomyDissector.get_specimen("cobol_banking")
    assert spec is not None
    suture = SutureEngine.synthesize(spec)
    
    ns = {}
    exec(suture.python_chimera, ns)
    calc = ns["calculate_accfin"]
    
    out = calc(bal, rate, days, Decimal("1000.00"))
    
    # Invariant 1: Fee monotonicity and tier
    if bal < Decimal("0.00"):
        if abs(bal) > Decimal("1000.00"):
            assert out["fee"] == Decimal("75.00")
        else:
            assert out["fee"] == Decimal("25.00")
    else:
        assert out["fee"] == Decimal("0.00")

    # Invariant 2: Net balance formula balance + interest - fee
    assert out["net_balance"] == bal + out["interest"] - out["fee"]


# 2. PBT for Fortran Ballistics Specimen
@settings(max_examples=40, deadline=None)
@given(
    v0=st.floats(min_value=20.0, max_value=800.0),
    theta=st.floats(min_value=15.0, max_value=75.0),
    mass=st.floats(min_value=1.0, max_value=50.0)
)
def test_pbt_fortran_ballistics_invariants(v0, theta, mass):
    spec = AnatomyDissector.get_specimen("fortran_ballistics")
    assert spec is not None
    suture = SutureEngine.synthesize(spec)
    
    ns = {}
    exec(suture.python_chimera, ns)
    calc = ns["calculate_ballis"]
    
    out = calc(v0, theta, mass=mass, dt=0.02)
    
    # Invariant 1: Physical domain bounds
    assert out["xmax"] > 0.0
    assert out["ymax"] > 0.0
    assert out["flight_time"] > 0.0


# 3. PBT for C89 Telemetry Packet
@settings(max_examples=50, deadline=None)
@given(
    tag=st.text(min_size=1, max_size=16, alphabet=st.characters(blacklist_categories=('Cs', 'Cc'))),
    temp=st.floats(min_value=-40.0, max_value=120.0),
    press=st.floats(min_value=70.0, max_value=130.0)
)
def test_pbt_c89_packet_invariants(tag, temp, press):
    spec = AnatomyDissector.get_specimen("c89_packet")
    assert spec is not None
    suture = SutureEngine.synthesize(spec)
    
    ns = {}
    exec(suture.python_chimera, ns)
    parse = ns["parse_telemetry_frame"]
    build = ns["build_telemetry_frame"]
    
    frame = build(tag, temp, press)
    decoded = parse(frame)
    
    # Invariant 1: Frame integrity verified
    assert decoded["frame_valid"] is True
    assert abs(decoded["temperature"] - temp) <= 0.05
    assert abs(decoded["pressure"] - press) <= 0.1

    # Invariant 2: Corrupted frame must fail
    corrupted = bytearray(frame)
    corrupted[-1] ^= 0x01
    with pytest.raises(ValueError):
        parse(bytes(corrupted))


# 4. Engine PBT Suite Verification (100 samples per specimen)
def test_full_verifier_suite_execution():
    for spec_id in ["cobol_banking", "fortran_ballistics", "c89_packet"]:
        spec = AnatomyDissector.get_specimen(spec_id)
        assert spec is not None
        suture = SutureEngine.synthesize(spec)
        report = PBTVerifier.verify(spec, suture.python_chimera, num_samples=100)
        assert report.total_samples == 100
        assert report.passed_samples == 100
        assert report.pass_rate == 1.0
        assert len(report.tested_invariants) >= 3
