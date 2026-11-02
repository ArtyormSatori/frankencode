# FrankenCode — Security Guidelines & Sandbox Directives

## 1. Input Sanitization
- Input legacy source code must not exceed 2MB per payload.
- Arbitrary code execution prevention: The sandbox runs in an isolated sub-process with restricted globals, strict timeouts (maximum 2.0s per run), and memory limits (maximum 128MB).
- No system shell escape, no file descriptor leakage, no network egress during sandbox execution.

## 2. AST Extraction Safety
- Parsers inspect token streams and AST nodes without invoking dynamic `eval` or unsafe native loaders.
- Any attempt to pass binary payloads targeting host architecture vulnerabilities is quarantined as a malformed specimen.
