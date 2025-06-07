import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from factorizer.cli import factorize_number


def test_factorize_primes():
    assert factorize_number(2) == [2]
    assert factorize_number(97) == [97]


def test_factorize_composites():
    assert factorize_number(15) == [3, 5]
    assert factorize_number(84) == [2, 2, 3, 7]
    assert factorize_number(561) == [3, 11, 17]


def test_cli_execution(tmp_path):
    from subprocess import run, PIPE
    env = dict(**os.environ, PYTHONPATH=str(Path(__file__).resolve().parents[2]))
    result = run(
        [sys.executable, "-m", "factorizer.cli", "90"],
        stdout=PIPE,
        text=True,
        env=env,
    )
    assert result.stdout.strip() == "2 * 3 * 3 * 5"
