#!/usr/bin/env python3
"""
FrankenCode MCP Server (Model Context Protocol)
Exposes Dr. Frankenstein's code autopsy and suture tools to Kiro IDE, CLI, and custom agents.
"""
import sys
import json
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.core.dissector import AnatomyDissector
from app.core.suture_engine import SutureEngine
from app.core.pbt_verifier import PBTVerifier
from app.core.sandbox import GalvanicSandbox

def handle_request(req: dict) -> dict:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id", 1)

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "dissect_legacy_code",
                        "description": "Performs anatomical AST dissection of legacy procedural code (COBOL, Fortran, C89), extracting vital formulas and vulnerabilities.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "code": {"type": "string", "description": "Legacy source code to dissect"},
                                "language": {"type": "string", "description": "COBOL, FORTRAN, C89, or auto-detect"}
                            },
                            "required": ["code"]
                        }
                    },
                    {
                        "name": "suture_specimen",
                        "description": "Synthesizes modern, memory-safe chimeras in Python, TypeScript, and Rust preserving exact legacy invariants.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "specimen_id": {"type": "string", "description": "Built-in specimen id (cobol_banking, fortran_ballistics, c89_packet)"}
                            },
                            "required": ["specimen_id"]
                        }
                    },
                    {
                        "name": "verify_invariants",
                        "description": "Executes Property-Based Testing (Hypothesis) across 100+ randomized boundary inputs to prove mathematical equivalence.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "specimen_id": {"type": "string", "description": "Target specimen ID"},
                                "num_samples": {"type": "integer", "default": 100}
                            },
                            "required": ["specimen_id"]
                        }
                    },
                    {
                        "name": "benchmark_sandbox",
                        "description": "Runs isolated execution sandbox to measure microsecond latency, memory footprint, and galvanic vitality.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "specimen_id": {"type": "string", "description": "Target specimen ID"},
                                "iterations": {"type": "integer", "default": 500}
                            },
                            "required": ["specimen_id"]
                        }
                    }
                ]
            }
        }

    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})

        if tool_name == "dissect_legacy_code":
            code = args.get("code", "")
            lang = args.get("language")
            spec = AnatomyDissector.dissect(code, lang)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": spec.model_dump_json(indent=2)}]}}

        elif tool_name == "suture_specimen":
            spec_id = args.get("specimen_id")
            spec = AnatomyDissector.get_specimen(spec_id)
            if not spec:
                return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32602, "message": f"Specimen not found: {spec_id}"}}
            suture = SutureEngine.synthesize(spec)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": suture.model_dump_json(indent=2)}]}}

        elif tool_name == "verify_invariants":
            spec_id = args.get("specimen_id")
            num_samples = args.get("num_samples", 100)
            spec = AnatomyDissector.get_specimen(spec_id)
            if not spec:
                return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32602, "message": f"Specimen not found: {spec_id}"}}
            suture = SutureEngine.synthesize(spec)
            report = PBTVerifier.verify(spec, suture.python_chimera, num_samples)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": report.model_dump_json(indent=2)}]}}

        elif tool_name == "benchmark_sandbox":
            spec_id = args.get("specimen_id")
            iterations = args.get("iterations", 500)
            spec = AnatomyDissector.get_specimen(spec_id)
            if not spec:
                return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32602, "message": f"Specimen not found: {spec_id}"}}
            suture = SutureEngine.synthesize(spec)
            telemetry = GalvanicSandbox.benchmark(spec, suture.python_chimera, iterations)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": telemetry.model_dump_json(indent=2)}]}}

        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Unknown tool: {tool_name}"}}

    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid Request"}}

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        # Quick CLI smoke test
        print("⚡ [FrankenCode MCP] Running self-test...")
        req = {"method": "tools/list", "id": 1}
        print("Tools list result:", json.dumps(handle_request(req), indent=2)[:300] + "...")
        sys.exit(0)

    # Standard JSON-RPC stdin/stdout loop
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling MCP request: {e}\n")

if __name__ == "__main__":
    main()
