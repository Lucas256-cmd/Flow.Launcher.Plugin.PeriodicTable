from flowlauncher import FlowLauncher
import periodictable
import webbrowser

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
            param_element = periodictable.elements.symbol(param)
            atomic_number = str(param_element.number)
            atomic_weight = str(param_element.mass)
            result = [
                {
                    "title": param_element.name,
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

    def open_url(self, url):
        webbrowser.open(url)
