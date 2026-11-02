import pytest
from app.core.dissector import AnatomyDissector, BUILTIN_SPECIMENS

def test_builtin_specimens_exist():
    specimens = AnatomyDissector.list_specimens()
    assert len(specimens) >= 3
    ids = [s["id"] for s in specimens]
    assert "cobol_banking" in ids
    assert "fortran_ballistics" in ids
    assert "c89_packet" in ids

def test_cobol_specimen_organs_and_pathologies():
    spec = AnatomyDissector.get_specimen("cobol_banking")
    assert spec is not None
    assert spec.origin_language == "COBOL"
    assert len(spec.vital_organs) >= 2
    assert any(p.severity == "CRITICAL" for p in spec.pathologies)
    assert any("overflow" in p.title.lower() or "truncation" in p.title.lower() for p in spec.pathologies)

def test_fortran_specimen_physics():
    spec = AnatomyDissector.get_specimen("fortran_ballistics")
    assert spec is not None
    assert spec.origin_language == "FORTRAN"
    assert any("drag" in organ.organ_name.lower() for organ in spec.vital_organs)

def test_c89_specimen_memory_guards():
    spec = AnatomyDissector.get_specimen("c89_packet")
    assert spec is not None
    assert spec.origin_language == "C89"
    assert any("redundancy" in organ.organ_name.lower() or "crc" in organ.organ_name.lower() for organ in spec.vital_organs)

def test_custom_code_dissection():
    custom_cobol = """IDENTIFICATION DIVISION.
PROGRAM-ID. HELLO.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-VAL PIC 9(5) VALUE 100.
PROCEDURE DIVISION.
STOP RUN."""
    spec = AnatomyDissector.dissect(custom_cobol)
    assert spec.origin_language == "COBOL"
    assert len(spec.inputs) >= 1
