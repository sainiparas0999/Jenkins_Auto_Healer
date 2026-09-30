from pathlib import Path
from analyzer import analyze_log
from log_reader import read_log


def main():
    project_root = Path(__file__).resolve().parents[2]
    log_path = project_root / "logs" / "sample_jenkins.log"
    log = read_log(str(log_path))

    print(str(log_path))
    analysis = analyze_log(log)
    print("===== ANALYSIS =====")
    print(analysis)

if __name__ == "__main__":
    main()