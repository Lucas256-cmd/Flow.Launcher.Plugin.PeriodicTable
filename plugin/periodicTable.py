from flowlauncher import FlowLauncher
import webbrowser
import JSONLookup

class Main(FlowLauncher):
    def query(self, param: str = '') -> list:
        # easteregg
        if param.lower() == "blobfish":
            return [
                {
                    "title": "OOPS THIS IS NOT A PERIODIC ELEMENT",
                    "subTitle": "The Blobfish is a deep sea fish that inhabits the deep waters of the Atlantic and Pacific Ocean. The blobfish has a short, broad tongue and conical teeth that are slightly recurved and are arranged in bands in irregular rows along the premaxillaries (whatever this word may mean).",
                    "icoPath": "Images/b.png",
                    "score": 4
                },
                {
                    "title": "I don't even know why you searched for this",
                    "subTitle": "But here is a picture of a Blobfish",
                    "icoPath": "Images/b.png",
                    "score": 3
                },
                {
                    "title": "If you want to see the full message of the first result use ctrl + ]",
                    "subTitle": "And ctrl + [ to set it back to normal",
                    "icoPath": "Images/b.png",
                    "score": 2
                },
                {
                    "title": "more info",
                    "subTitle": "https://en.wikipedia.org/wiki/Psychrolutidae",
                    "jsonRPCAction": {
                        "method": "open_url",
                        "parameters": ["https://en.wikipedia.org/wiki/Psychrolutidae"]
                    },
                    "icoPath": "Images/b.png",
                    "score": 1
                },
            ]
        try:
            param_element = JSONLookup.Element(param)
            atomic_number = param_element.atomic_number
            atomic_weight = param_element.atomic_mass
            boiling_point = param_element.boiling_point
            melting_point = param_element.melting_point
            result = [
                {
                    "title": param_element.name.capitalize(),
                    "subTitle": param_element.symbol,
                    "icoPath": "Images/app.png",
                    "score": 2
                },
                {
                    "title": "Atomic Number: " + atomic_number,
                    "subTitle": "Atomic Mass: " + atomic_weight,
                    "icoPath": "Images/app.png",
                    "score": 1
                },
                {
                    "title": "Boiling Point: " + boiling_point + " K",
                    "subTitle": "Melting Point: " + melting_point + " K",
                    "icoPath": "Images/app.png",
                    "score": 0
                }
            ]
        except ValueError:
            result = [
                {
                    "title": "Element not found",
                    "icoPath": "Images/app.png",
                    "score": 0
                }
            ]
        return result

    def open_url(self, url):
        webbrowser.open(url)
