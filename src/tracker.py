import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "activity.json"

def _load():
    return json.loads(DATA_FILE.read_text()) if DATA_FILE.exists() else {"sessions": [], "active": None}

def _save(data):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(data, indent=2))

def start_session():
    data = _load()
    if data["active"]: return "A session is already running."
    data["active"] = datetime.now().isoformat()
    _save(data)
    return f"Session started at {data['active']}"

def stop_session():
    data = _load()
    if not data["active"]: return "No active session."
    start = datetime.fromisoformat(data["active"])
    end = datetime.now()
    seconds = int((end - start).total_seconds())
    data["sessions"].append({"start": start.isoformat(), "end": end.isoformat(), "seconds": seconds})
    data["active"] = None
    _save(data)
    return f"Session stopped — {seconds // 60} minutes recorded."
