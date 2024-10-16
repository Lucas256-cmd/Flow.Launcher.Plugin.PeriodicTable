from flowlauncher import FlowLauncher
import periodictable

class Main(FlowLauncher):
    def query(self, param: str = '') -> list:
        try:
            param_element = periodictable.elements.symbol(param)
            atomic_number = str(param_element.number)
            atomic_weight = str(param_element.mass)
            result = [
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
            ]
        except ValueError:
            result = [
                {
                    "title": "Element not found",
                    "subTitle": "Element is case sensitive",
                    "icoPath": "Images/app.png",
                    "score": 0
                }
            ]
        return result
