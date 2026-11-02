#!/usr/bin/env python3
"""
FrankenCode PBT Invariant Gate Hook
Triggered by Kiro after suture synthesis to enforce 100% invariant pass rate.
"""
import sys
import subprocess
from pathlib import Path

def main():
    print("⚡ [Kiro Hook: PBT Invariant Gate] Channeling lightning through test suite...")
    repo_root = Path(__file__).resolve().parent.parent.parent
    pytest_bin = repo_root / "venv" / "bin" / "pytest"
    
    if not pytest_bin.exists():
        pytest_bin = "pytest"
        
    cmd = [str(pytest_bin), "-q", str(repo_root / "tests" / "test_pbt.py")]
    proc = subprocess.run(cmd, cwd=str(repo_root), capture_output=True, text=True)
    
    if proc.returncode != 0:
        print("❌ [PBT Invariant Gate FAILED] Invariant broken under fuzzing!")
        print(proc.stdout)
        print(proc.stderr)
        sys.exit(1)
        
    print("✓ [PBT Invariant Gate PASSED] All property-based invariants verified 100%.")
    sys.exit(0)

if __name__ == "__main__":
    main()
