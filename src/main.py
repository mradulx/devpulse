import argparse
from .tracker import start_session, stop_session
from .stats import print_stats

def main():
    parser = argparse.ArgumentParser(description="DevPulse developer productivity tracker")
    parser.add_argument("command", choices=["start", "stop", "stats"])
    args = parser.parse_args()
    if args.command == "start": print(start_session())
    elif args.command == "stop": print(stop_session())
    else: print_stats()

if __name__ == "__main__":
    main()
