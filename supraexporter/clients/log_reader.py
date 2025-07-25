"""Utilities for reading and parsing Supra validator log files."""

import re
import subprocess  # nosec


def read_last_n_lines(filepath: str, n: int = 100000) -> str:
    """Read the last n lines from a log file using the tail command."""
    try:
        result = subprocess.run(  # nosec
            ["tail", "-n", str(n), filepath],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to read log file {filepath}: {e}")


def parse_block_height(log_data: str) -> int:
    """Extract the most recent block height from the log file.

    Expected pattern: "Block height: (12345678)".
    """
    pattern = re.compile(r"Block height: \((\d+)\)")
    for line in reversed(log_data.splitlines()):
        match = pattern.search(line)
        if match:
            return int(match.group(1))
    return 0


def calculate_keyword_abundance(log_data: str, keyword: str, pubkey: str) -> float:
    """Calculate how often the given keyword appears with the pubkey.

    Compared to total lines with the keyword.
    """
    lines = log_data.splitlines()

    keyword_lines = [line for line in lines if keyword.lower() in line.lower()]
    if not keyword_lines:
        return 0.0

    matching_lines = [line for line in keyword_lines if pubkey in line]
    return len(matching_lines) / len(keyword_lines)
