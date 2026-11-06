#!/usr/bin/env python3
"""Remove every hook whose command equals COMMAND from a Claude Code settings.json.

    strip-hook.py SETTINGS COMMAND

Backs the file up first when it changes; groups left empty are dropped, other hooks stay.
"""

import json
import shutil
import sys
import time
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    path, command = Path(sys.argv[1]).expanduser(), sys.argv[2].strip()
    settings = json.loads(path.read_text())
    hooks, removed = settings.get("hooks", {}), 0
    for event in list(hooks):
        groups = []
        for group in hooks[event]:
            kept = [h for h in group.get("hooks", []) if h.get("command", "").strip() != command]
            removed += len(group.get("hooks", [])) - len(kept)
            if kept:
                groups.append({**group, "hooks": kept})
        if groups:
            hooks[event] = groups
        else:
            del hooks[event]
    if not removed:
        print(f"  = no '{command}' hook in {path}")
        return 0
    shutil.copy2(path, path.with_name(f"{path.name}.bak.{time.strftime('%Y%m%d-%H%M%S')}"))
    path.write_text(json.dumps(settings, indent=2) + "\n")
    print(f"  ✓ removed {removed} '{command}' hook(s) from {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
