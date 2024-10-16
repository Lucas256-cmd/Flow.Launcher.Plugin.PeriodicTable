from flowlauncher import FlowLauncher
from mendeleev import element


class Main(FlowLauncher):
    def query(self, param: str = '') -> list:
        try:
            param_element = element(param)
            atomic_number = str(param_element.atomic_number)
            atomic_weight = str(param_element.atomic_weight)
            boiling_point = str(param_element.boiling_point)
            melting_point = str(param_element.melting_point)
            discovery_year = str(param_element.discovery_year)
            return [
                {
                    "title": param_element.name,
                    "subTitle": param_element.symbol,
                    "icoPath": "Images/app.png",
                    "score": 0
                },
                {
                    "title": "Atomic Number: " + atomic_number,
                    "subTitle": "Atomic Mass: " + atomic_weight,
                    "icoPath": "Images/app.png",
                    "score": 0
                },
                {
                    "title": "Boiling Point: " + boiling_point,
                    "subTitle": "Melting Point: " + melting_point,
                    "icoPath": "Images/app.png",
                    "score": 0
                },
                {
                    "title": "Year Discovered: " + discovery_year,
                    "icoPath": "Images/app.png",
                    "score": 0
                }
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
