import json

with open('periodic-table-lookup.json', encoding="utf8") as f:
    periodic_table = json.load(f)


# Function to get the element name by its key
def get_element_name(symbol):
    for element in periodic_table['elements']:
        if element['symbol'] == symbol:
            return element['name']
    raise ValueError


def get_element_dict(element_name):
    raise


class Element:
    def __init__(self, symbol):
        self.symbol = symbol
        self.name = get_element_name(symbol)
        self.element_dict = get_element_dict(self.name)
        self.atomic_number = self.get_atomic_number()
        self.atomic_mass = self.get_atomic_mass()
        self.boiling_point = self.get_boiling_point()
        self.melting_point = self.get_melting_point()
