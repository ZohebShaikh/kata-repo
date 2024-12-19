import subprocess
import sys

from kata_repo import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "kata_repo", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
