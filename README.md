# ⚡ DevPulse

> A lightweight developer productivity tracker for coders who want to measure consistency.

DevPulse is a terminal-based productivity dashboard built with Python. It tracks coding sessions locally, calculates streaks and weekly statistics, and can optionally pull public GitHub activity.

## ✨ Features

- ⏱️ Start and stop coding sessions
- 📊 Daily and weekly productivity statistics
- 🔥 Current coding streak
- 💾 Local JSON storage — no database required
- 🐙 Optional GitHub activity lookup
- 🖥️ Clean terminal dashboard with Rich

## 🚀 Quick Start

```bash
git clone https://github.com/mradulx/devpulse.git
cd devpulse
pip install -r requirements.txt
python -m src.main stats
```

## 💻 Usage

```bash
python -m src.main start
python -m src.main stop
python -m src.main stats
```

Example dashboard:

```text
⚡ DevPulse
────────────────────────────────
🔥 Current streak   3 days
⏱️  Today            2h 15m
📅 This week        8h 40m
💻 Sessions         12
```

## 🗂️ Structure

```text
devpulse/
├── src/
│   ├── main.py
│   ├── tracker.py
│   ├── stats.py
│   └── github.py
├── data/
│   └── activity.json
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## 🛠️ Stack

`Python` · `Rich` · `JSON` · `GitHub API`

## 🔮 Roadmap

- [ ] GitHub contribution heatmap
- [ ] LeetCode statistics
- [ ] Export reports
- [ ] SQLite storage
- [ ] Web dashboard

## 📄 License

MIT
