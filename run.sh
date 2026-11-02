#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================================================"
echo "⚡ FRANKENCODE: The Chimera Code Modernizer & Invariant Verifier"
echo "   Kiroween 2026 Hackathon | Category: Frankenstein & Best Student Project"
echo "================================================================================"

# Python virtual environment setup
if [ ! -d "venv" ]; then
    echo "⚡ Initializing virtual environment..."
    python3 -m venv venv
    ./venv/bin/pip install --upgrade pip
    ./venv/bin/pip install -r requirements.txt
fi

case "${1:-server}" in
    test)
        echo "🔬 Running Pytest Suite..."
        ./venv/bin/pytest -v
        ;;
    benchmark)
        echo "⚡ Running Empirical Benchmark & PBT Invariant Verification..."
        ./venv/bin/python3 eval_benchmark.py
        ;;
    mcp)
        echo "🔌 Starting FrankenCode MCP Server (stdio mode)..."
        ./venv/bin/python3 mcp-server/frankencode_mcp.py
        ;;
    server|*)
        echo "🏰 Awakening the FrankenCode Victorian Laboratory Cockpit..."
        echo "   Access UI at: http://localhost:8000"
        echo "   API Docs at:  http://localhost:8000/docs"
        ./venv/bin/uvicorn app.backend.main:app --host 0.0.0.0 --port 8000 --reload
        ;;
esac
