import hashlib
import json
from pathlib import Path

CACHE_FILE = Path(".build_cache.json")


def fingerprint(inputs):
    """Create a short ID from the build inputs."""
    text = json.dumps(inputs, sort_keys=True)
    return hashlib.sha256(text.encode()).hexdigest()


def build(inputs):
    """Reuse the build if its inputs have not changed."""
    current_id = fingerprint(inputs)

    if CACHE_FILE.exists():
        saved = json.loads(CACHE_FILE.read_text())
        if saved["fingerprint"] == current_id:
            print("CACHE HIT: inputs are unchanged; reusing the build.")
            return

    print("CACHE MISS: inputs changed; running the build.")
    print(f"Building app version {inputs['version']}...")
    CACHE_FILE.write_text(json.dumps({"fingerprint": current_id}, indent=2))
    print("Build complete. Cache updated.")


build({"source": "hello world", "version": 2})