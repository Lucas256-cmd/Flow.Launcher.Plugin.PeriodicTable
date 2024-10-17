from flowlauncher import FlowLauncher
import webbrowser
import JSONLookup


def open_url(url):
    webbrowser.open(url)


class Main(FlowLauncher):
    def query(self, param: str = '') -> list:
        result = []

        # easteregg
        if param.lower() == "blobfish":
            return [
                {
                    "title": "OOPS this is not an element",
                    "subTitle": "The Blobfish is a deep sea fish that inhabits the deep waters of the Atlantic and Pacific Ocean. The blobfish has a short, broad tongue and conical teeth that are slightly recurved and are arranged in bands in irregular rows along the premaxillaries (whatever this word may mean).",
                    "icoPath": "Images/b.png",
                    "score": 4,
                    "ContextData": {"title": "Blobfish"}
                },
                {
                    "title": "I don't even know why you searched for this.",
                    "subTitle": "But here is a picture of a Blobfish",
                    "icoPath": "Images/b.png",
                    "score": 3
                },
                {
                    "title": "If you want to see the full blobfish info use ctrl + ]",
                    "subTitle": "And ctrl + [ to set it back to normal, If the blobfish info is still too long go to the context menu of the first result.",
                    "icoPath": "Images/b.png",
                    "score": 2
                },
                {
                    "title": "More info",
                    "subTitle": "https://en.wikipedia.org/wiki/Psychrolutidae",
                    "jsonRPCAction": {
                        "method": "open_url",
                        "parameters": ["https://en.wikipedia.org/wiki/Psychrolutidae"]
                    },
                    "icoPath": "Images/b.png",
                    "score": 0
                },
            ]
        try:
            # try to get the element from the Element class
            param_element = JSONLookup.Element(param)
            atomic_number = param_element.atomic_number
            atomic_weight = param_element.atomic_mass
            boiling_point = param_element.boiling_point
            melting_point = param_element.melting_point
            discoverer = param_element.discoverer
            named_by = param_element.named_by
            # if the element is found, create a result list with the element information
            result = [
                {
                    "title": param_element.name,
                    "subTitle": param_element.symbol,
                    "icoPath": "Images/app.png",
                    "score": 3
                },
                {
                    "title": "Atomic Number: " + atomic_number,
                    "subTitle": "Atomic Mass: " + atomic_weight,
                    "icoPath": "Images/app.png",
                    "score": 2
                },
                {
                    "title": "Boiling Point: " + boiling_point,
                    "subTitle": "Melting Point: " + melting_point,
                    "icoPath": "Images/app.png",
                    "score": 1
                },
                {
                    "title": "Discovered by: " + discoverer,
                    "subTitle": "Named by: " + named_by,
                    "icoPath": "Images/app.png",
                    "score": 0
                }
            ]
        except ValueError as e:
            # if the Element class raises a ValueError, create a result list with a corresponding error message
            if str(e) == "Element not found":
                result = [
                    {
                        "title": "Element not found",
                        "subTitle": "Please enter a valid element name or symbol.",
                        "icoPath": "Images/app.png",
                        "score": 0,
                        "ContextData": {"title": "Element not found"}
                    }
                ]
            elif str(e) == "No element entered":
                result = [
                    {
                        "title": "No element entered",
                        "subTitle": "Please enter an element name or symbol.",
                        "icoPath": "Images/app.png",
                        "score": 0
                    }
                ]
        return result

    def context_menu(self, data):
        if data['title'] == "Blobfish":
            # hmm, what would this code do???
            return [
                {
                    "title": "The Blobfish is a deep sea fish that inhabits the deep waters of the Atlantic and Pacific Ocean.",
                    "subTitle": "The blobfish has a short, broad tongue and conical teeth that are slightly recurved and are arranged in bands in irregular rows along the premaxillaries (whatever this word may mean).",
                    "icoPath": "Images/b.png",
                    "score": 1
                },
                {
                    "title": "If the blobfish info is still too long,",
                    "subTitle": "try it making flow wider again now.",
                    "icoPath": "Images/b.png",
                    "score": 0
                }
            ]
