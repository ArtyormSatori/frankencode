import pytest
from app.core.dissector import AnatomyDissector
from app.core.suture_engine import SutureEngine

def test_suture_cobol_banking():
    spec = AnatomyDissector.get_specimen("cobol_banking")
    assert spec is not None
    suture = SutureEngine.synthesize(spec)
    assert "Decimal" in suture.python_chimera
    assert "ROUND_HALF_EVEN" in suture.python_chimera
    assert "calculate_accfin" in suture.python_chimera
    assert "calculateAccfin" in suture.typescript_chimera
    assert "calculate_accfin" in suture.rust_contract
    assert len(suture.synthesized_invariants) >= 2

def test_suture_fortran_ballistics():
    spec = AnatomyDissector.get_specimen("fortran_ballistics")
    assert spec is not None
    suture = SutureEngine.synthesize(spec)
    assert "calculate_ballis" in suture.python_chimera
    assert "v_safe = max(v, 1e-9)" in suture.python_chimera
    assert len(suture.suture_notes) >= 2

def test_suture_c89_packet():
    spec = AnatomyDissector.get_specimen("c89_packet")
    assert spec is not None
    suture = SutureEngine.synthesize(spec)
    assert "parse_telemetry_frame" in suture.python_chimera
    assert "binascii.crc32" in suture.python_chimera
    assert "build_telemetry_frame" in suture.python_chimera
