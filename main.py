import sys
from pathlib import Path

plugindir = Path.absolute(Path(__file__).parent)
paths = (".", "lib", "plugin")
sys.path = [str(plugindir / p) for p in paths] + sys.path

from flowlauncher import FlowLauncher
from mendeleev import element


class PeriodicTable(FlowLauncher):
    def query(self, query: str):
        try:
            query_element = element(query)
            return [
                {
                    "title": query_element.name,
                    "subTitle": query_element.symbol,
                    "icoPath": "Images/app.png",
                    "jsonRPCAction": {
                        "method": "copy_to_clipboard",
                        "parameters": [query_element.name],
                        "dontHideAfterAction": False
                    },
                    "score": 0
                },

            ]
        except ValueError:
            return [
                {
                    "title": "Element not found",
                    "subTitle": "Element is case sensitive",
                    "icoPath": "Images/app.png",
                    "score": 0
                }
            ]


if __name__ == "__main__":
    PeriodicTable()
