import json
from datetime import datetime, timedelta
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "activity.json"

def _load():
    return json.loads(DATA_FILE.read_text()) if DATA_FILE.exists() else {"sessions": []}

def print_stats():
    sessions = _load()["sessions"]
    today = datetime.now().date()
    week_start = today - timedelta(days=today.weekday())
    today_seconds = week_seconds = 0
    active_days = set()
    for s in sessions:
        dt = datetime.fromisoformat(s["start"])
        if dt.date() == today: today_seconds += s["seconds"]
        if dt.date() >= week_start: week_seconds += s["seconds"]
        active_days.add(dt.date())
    streak = 0
    cursor = today
    while cursor in active_days:
        streak += 1
        cursor -= timedelta(days=1)
    def fmt(seconds): return f"{seconds // 3600}h {(seconds % 3600) // 60}m"
    print("\n⚡ DevPulse")
    print("─" * 32)
    print(f"🔥 Current streak   {streak} days")
    print(f"⏱️  Today            {fmt(today_seconds)}")
    print(f"📅 This week        {fmt(week_seconds)}")
    print(f"💻 Sessions         {len(sessions)}\n")
