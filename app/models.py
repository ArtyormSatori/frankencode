from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class VariableSpec(BaseModel):
    name: str
    var_type: str
    description: str = ""
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    precision: Optional[int] = None
    default_value: Optional[Any] = None

class VitalOrgan(BaseModel):
    organ_id: str
    organ_name: str
    category: str  # "arithmetic", "branching", "memory_io", "boundary_guard"
    legacy_snippet: str
    modern_equivalent: str
    invariants: List[str]

class PathologyReport(BaseModel):
    severity: str  # "CRITICAL", "WARNING", "NOTE"
    title: str
    description: str
    remediation: str

class AnatomicalSpec(BaseModel):
    specimen_id: str
    title: str
    origin_language: str  # "COBOL", "FORTRAN", "C89", "PROCEDURAL"
    domain: str
    raw_code: str
    inputs: List[VariableSpec]
    outputs: List[VariableSpec]
    vital_organs: List[VitalOrgan]
    pathologies: List[PathologyReport]
    summary: str

class SutureResult(BaseModel):
    specimen_id: str
    python_chimera: str
    typescript_chimera: str
    rust_contract: str
    synthesized_invariants: List[str]
    suture_notes: List[str]

class PBTTestResult(BaseModel):
    input_sample: Dict[str, Any]
    legacy_oracle_output: Any
    chimera_output: Any
    matched: bool
    deviation: float = 0.0

class PBTReport(BaseModel):
    specimen_id: str
    total_samples: int
    passed_samples: int
    failed_samples: int
    pass_rate: float
    tested_invariants: List[str]
    sample_runs: List[PBTTestResult]
    fuzzing_duration_ms: float
    shrink_counterexample: Optional[Dict[str, Any]] = None

class GalvanicTelemetry(BaseModel):
    specimen_id: str
    voltage_vitality: float  # 0 - 100 score
    amperage_throughput_ops_sec: float
    latency_microseconds: float
    memory_bytes: int
    speedup_factor: float
    status: str  # "ALIVE", "MUTATING", "STABLE"

class DissectRequest(BaseModel):
    code: str
    language: Optional[str] = None
    specimen_id: Optional[str] = "custom_specimen"

class SutureRequest(BaseModel):
    spec: AnatomicalSpec

class VerifyRequest(BaseModel):
    spec: AnatomicalSpec
    python_chimera: str
    num_samples: int = 100

class BenchmarkRequest(BaseModel):
    spec: AnatomicalSpec
    python_chimera: str
    iterations: int = 500
