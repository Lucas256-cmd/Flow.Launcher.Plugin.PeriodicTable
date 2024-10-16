import sys
from pathlib import Path

plugindir = Path(__file__).parent.resolve()
paths = (".", "lib", "plugin")
sys.path = [str(plugindir / p) for p in paths] + sys.path

from plugin import Main

if __name__ == "__main__":
    Main()
