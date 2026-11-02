import pytest
from starlette.testclient import TestClient
from app.backend.main import app

client = TestClient(app)

def test_api_health():
    res = client.get("/api/health")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "ALIVE"
    assert data["kiro_harness"] == "ENABLED"

def test_api_specimens():
    res = client.get("/api/specimens")
    assert res.status_code == 200
    specimens = res.json()
    assert len(specimens) >= 3

def test_api_get_cobol_specimen():
    res = client.get("/api/specimen/cobol_banking")
    assert res.status_code == 200
    spec = res.json()
    assert spec["specimen_id"] == "cobol_banking"
    assert spec["origin_language"] == "COBOL"

def test_api_suture_and_verify():
    # 1. Fetch specimen
    res_spec = client.get("/api/specimen/cobol_banking")
    spec = res_spec.json()

    # 2. Suture
    res_suture = client.post("/api/suture", json={"spec": spec})
    assert res_suture.status_code == 200
    suture = res_suture.json()
    assert "calculate_accfin" in suture["python_chimera"]

    # 3. Verify
    res_verify = client.post("/api/verify", json={
        "spec": spec,
        "python_chimera": suture["python_chimera"],
        "num_samples": 50
    })
    assert res_verify.status_code == 200
    report = res_verify.json()
    assert report["pass_rate"] == 1.0
    assert report["passed_samples"] == 50

    # 4. Benchmark
    res_bench = client.post("/api/benchmark", json={
        "spec": spec,
        "python_chimera": suture["python_chimera"],
        "iterations": 100
    })
    assert res_bench.status_code == 200
    telemetry = res_bench.json()
    assert telemetry["voltage_vitality"] > 50.0
    assert telemetry["amperage_throughput_ops_sec"] > 0
