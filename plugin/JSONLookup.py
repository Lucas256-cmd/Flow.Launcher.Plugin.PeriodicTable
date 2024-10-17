import json

# periodic-table-lookup.json first contains a list called "order" which contains the order of the elements in the periodic table
# Then it contains a dictionary for each element with the element name as the key.
with open('periodic-table-lookup.json', encoding="utf8") as f:
    periodic_table = json.load(f)

# Function to get the element name by its key
def get_element_name_by_symbol(symbol):
    for name, element in periodic_table.items():
        if name != "order" and element['symbol'] == symbol.capitalize():
            return name.lower()
    return None


def get_element_symbol_by_name(name):
    if name.lower() in periodic_table:
        return periodic_table[name.lower()]['symbol']
    return None

def get_element_dict(element_name):
    return periodic_table[element_name]


class Element:
    def __init__(self, element_name_or_symbol):
        self.name = get_element_name_by_symbol(element_name_or_symbol)
        self.symbol = get_element_symbol_by_name(element_name_or_symbol)
        if self.name is None and self.symbol is None:
            self.partial_match(element_name_or_symbol)
        if self.name is None:
            # This means that the user entered the element name
            self.name = element_name_or_symbol.lower()
        if self.symbol is None:
            # This means that the user entered the element symbol
            self.symbol = element_name_or_symbol.capitalize()

        if self.name:
            self.element_dict = get_element_dict(self.name)
            self.name = self.name.capitalize()  # Capitalization done after name and symbol are set because it doesn't have to be lowercase anymore because there is no need to search in the dictionary anymor
            self.atomic_number = str(self.element_dict['number']) if self.element_dict[
                'number'] else "Unknown or not in database"
            self.atomic_mass = str(self.element_dict['atomic_mass']) if self.element_dict[
                'atomic_mass'] else "Unknown or not in database"
            self.boiling_point = (str(self.element_dict['boil']) + " K") if self.element_dict[
                'boil'] else "Unknown or not in database"
            self.melting_point = (str(self.element_dict['melt']) + " K") if self.element_dict[
                'melt'] else "Unknown or not in database"
            self.discoverer = self.element_dict['discovered_by'] if self.element_dict[
                'discovered_by'] else "Discovered by unknown or not in database"
            self.named_by = self.element_dict['named_by'] if self.element_dict[
                'named_by'] else "Named by unknown or not in database"

    def partial_match(self, element_name_or_symbol):
        # only run this if element_name_or_symbol is not "" else every element will be matched and the last element will be returned
        if element_name_or_symbol != "":
            for name, element in periodic_table.items():
                if name != "order" and (element_name_or_symbol.lower() in name):
                    self.name = name
                    self.symbol = element['symbol']
                    break
            if self.name is None:
                for name, element in periodic_table.items():
                    if name != "order" and (element_name_or_symbol.lower() in element['symbol']):
                        self.name = name
                        self.symbol = element['symbol']
                        break
            if self.name is None:
                raise ValueError("Element not found")
        else:
            raise ValueError("No element entered")