from flowlauncher import FlowLauncher
import periodictable

class Main(FlowLauncher):
    def query(self, param: str = '') -> list:
        # easteregg
        if param == "Blobfish":
            return [
                {
                    "title": "OOPS THIS IS NOT A PERIODIC ELEMENT",
                    "subTitle": "The Blobfish is a deep sea fish that inhabits the deep waters of the Atlantic and Pacific Ocean. The blobfish has a short, broad tongue and conical teeth that are slightly recurved and are arranged in bands in irregular rows along the premaxillaries (whatever this word may mean).",
                    "icoPath": "Images/app.png",
                    "score": 0
                },
                {
                    "title": "I don't even know why you searched for this",
                    "subTitle": "But here is a picture of a Blobfish",
                    "icoPath": "Images/b.png",
                },
                {
                    "title": "If you want to see the full message use ctrl + ]",
                    "subTitle": "And ctrl + [ to set it back to normal",
                    "icoPath": "Images/app.png",
                    "score": 0
                },
                {
                    "title": "more info",
                    "subTitle": "https://en.wikipedia.org/wiki/Psychrolutidae",
                    "jsonRPCAction": {
                        "method": "open_url",
                        "parameters": ["https://en.wikipedia.org/wiki/Psychrolutidae"]
                    },
                    "icoPath": "Images/app.png",
                    "score": 0
                },
            ]
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
