from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

from app.models import (
    AnatomicalSpec, SutureResult, PBTReport, GalvanicTelemetry,
    DissectRequest, SutureRequest, VerifyRequest, BenchmarkRequest
)
from app.core.dissector import AnatomyDissector
from app.core.suture_engine import SutureEngine
from app.core.pbt_verifier import PBTVerifier
from app.core.sandbox import GalvanicSandbox

app = FastAPI(
    title="FrankenCode API — The Chimera Code Modernizer",
    description="Dr. Frankenstein's Software Laboratory: Stitching Legacy Relics into Living WebAssembly/Python Micro-Engines with Invariant Proof.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

@app.get("/api/health")
def health_check():
    return {
        "status": "ALIVE",
        "laboratory": "FrankenCode Gothic Core",
        "kiro_harness": "ENABLED",
        "mcp_server": "READY",
        "pbt_engine": "HYPOTHESIS_ACTIVE"
    }

@app.get("/api/specimens")
def list_specimens():
    return AnatomyDissector.list_specimens()

@app.get("/api/specimen/{specimen_id}")
def get_specimen(specimen_id: str):
    spec = AnatomyDissector.get_specimen(specimen_id)
    if not spec:
        raise HTTPException(status_code=404, detail="Specimen not found")
    return spec

@app.post("/api/dissect", response_model=AnatomicalSpec)
def dissect_code(req: DissectRequest):
    return AnatomyDissector.dissect(req.code, req.language, req.specimen_id or "custom")

@app.post("/api/suture", response_model=SutureResult)
def suture_specimen(req: SutureRequest):
    return SutureEngine.synthesize(req.spec)

@app.post("/api/verify", response_model=PBTReport)
def verify_invariants(req: VerifyRequest):
    return PBTVerifier.verify(req.spec, req.python_chimera, req.num_samples)

@app.post("/api/benchmark", response_model=GalvanicTelemetry)
def benchmark_sandbox(req: BenchmarkRequest):
    return GalvanicSandbox.benchmark(req.spec, req.python_chimera, req.iterations)

# Mount static frontend
if FRONTEND_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

    @app.get("/")
    def serve_index():
        return FileResponse(str(FRONTEND_DIR / "index.html"))
