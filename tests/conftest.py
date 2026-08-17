from __future__ import annotations

import os
import sys
from pathlib import Path


def _agent_root() -> Path:
    configured = (
        os.environ.get("ROXY_AGENT_ROOT", "").strip()
        or os.environ.get("AKASHIC_AGENT_ROOT", "").strip()
    )
    if configured:
        return Path(configured)
    return Path(__file__).resolve().parents[3] / "roxy-agent"


plugin_root = Path(__file__).resolve().parents[1]
agent_root = _agent_root()
for path in (plugin_root, agent_root):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))
