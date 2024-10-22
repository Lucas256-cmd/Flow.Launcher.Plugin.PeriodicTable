import json

# periodic-table-lookup.json first contains a list called "order" which contains the order of the elements in the periodic table
# Then it contains a dictionary for each element with the element name as the key.
with open('periodic-table-lookup.json', encoding="utf8") as f:
    periodic_table = json.load(f)


# For the structure of periodic_table, see the bottom of this file
# The first element in the dictionary is order which contains a list of all the elements in the json file in the order they appear in the file.
# This element is not used in this code

# Function to get the element name by its key
def get_element_name_by_symbol(symbol):
    for name, element in periodic_table.items():
        # name is the element name in lowercase
        # element is the dictionary containing the element data. The name in this dictionary is capitalized and not tho be confused with the name variable
        # this is true for every name, element found in this code
        if name != "order" and element['symbol'] == symbol.capitalize():
            # capitalize is needed because the symbol in the dictionary is capitalized
            return name.lower()  # return the element name in lowercase because the name will be used to search in the dictionary and the dictionary keys are lowercase
    return None


def get_element_symbol_by_name(name):
    if name.lower() in periodic_table:
        return periodic_table[name.lower()]['symbol']
    return None


class Element:
    def __init__(self, element_name_or_symbol):
        # try to get the element name and symbol from the dictionary
        self.name = get_element_name_by_symbol(element_name_or_symbol)
        self.symbol = get_element_symbol_by_name(element_name_or_symbol)
        # if the element name and symbol are not found, try to find a partial match
        if self.name is None and self.symbol is None:
            self.partial_match(element_name_or_symbol)
        if self.name is None:
            # This means that the user entered the element name
            self.name = element_name_or_symbol.lower()
        if self.symbol is None:
            # This means that the user entered the element symbol
            self.symbol = element_name_or_symbol.capitalize()
        # if the element name is found, set the element data
        if self.name:
            self.element_dict = periodic_table[self.name]
            self.name = self.name.capitalize()  # Capitalization done after name and symbol are set because it doesn't have to be lowercase anymore because there is no need to search in the dictionary anymor
            self.atomic_number = str(self.element_dict['number']) if self.element_dict[
                'number'] else "Unknown or not in database"
            self.atomic_mass = str(self.element_dict['atomic_mass']) if self.element_dict[
                'atomic_mass'] else "Unknown or not in database"
            self.boiling_point = (str(self.element_dict['boil']) + "K") if self.element_dict[
                'boil'] else "Unknown or not in database"
            self.melting_point = (str(self.element_dict['melt']) + "K") if self.element_dict[
                'melt'] else "Unknown or not in database"
            self.discoverer = self.element_dict['discovered_by'] if self.element_dict[
                'discovered_by'] else "Discovered by unknown or not in database"
            self.named_by = self.element_dict['named_by'] if self.element_dict[
                'named_by'] else "Named by unknown or not in database"

    def partial_match(self, element_name_or_symbol):
        if element_name_or_symbol != "":
            # First, try to find elements whose names or symbols start with the input string
            for name, element in periodic_table.items():
                if name != "order" and (name.startswith(element_name_or_symbol.lower()) or element['symbol'].startswith(
                        element_name_or_symbol.capitalize())):
                    self.name = name
                    self.symbol = element['symbol']
                    return

            # If no elements start with the input string, try to find partial matches within the string
            for name, element in periodic_table.items():
                if name != "order" and (
                        element_name_or_symbol.lower() in name or element_name_or_symbol.capitalize() in element[
                    'symbol']):
                    self.name = name
                    self.symbol = element['symbol']
                    return

            # If no matches are found, raise a ValueError
            raise ValueError("Element not found")
        else:
            raise ValueError("No element entered")


"""
This is a snippet of the JSON file periodic-table-lookup.json
{
    ...
    "hydrogen": {
        "name": "Hydrogen",
        "appearance": "colorless gas",
        "atomic_mass": 1.008,
        "boil": 20.271,
        "category": "diatomic nonmetal",
        "density": 0.08988,
        "discovered_by": "Henry Cavendish",
        "melt": 13.99,
        "molar_heat": 28.836,
        "named_by": "Antoine Lavoisier",
        "number": 1,
        "period": 1,
        "group": 1,
        "phase": "Gas",
        "source": "https://en.wikipedia.org/wiki/Hydrogen",
        "bohr_model_image": "https://storage.googleapis.com/search-ar-edu/periodic-table/element_001_hydrogen/element_001_hydrogen_srp_th.png",
        "bohr_model_3d": "https://storage.googleapis.com/search-ar-edu/periodic-table/element_001_hydrogen/element_001_hydrogen.glb",
        "spectral_img": "https://en.wikipedia.org/wiki/File:Hydrogen_Spectra.jpg",
        "summary": "Hydrogen is a chemical element with chemical symbol H and atomic number 1. With an atomic weight of 1.00794 u, hydrogen is the lightest element on the periodic table. Its monatomic form (H) is the most abundant chemical substance in the Universe, constituting roughly 75% of all baryonic mass.",
        "symbol": "H",
        "xpos": 1,
        "ypos": 1,
        "wxpos": 1,
        "wypos": 1,
        "shells": [
          1
        ],
        "electron_configuration": "1s1",
        "electron_configuration_semantic": "1s1",
        "electron_affinity": 72.769,
        "electronegativity_pauling": 2.2,
        "ionization_energies": [
          1312
        ],
        "cpk-hex": "ffffff",
        "image": {
          "title": "Vial of glowing ultrapure hydrogen, H2. Original size in cm: 1 x 5",
          "url": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Hydrogenglow.jpg",
          "attribution": "User:Jurii, CC BY 3.0 <https://creativecommons.org/licenses/by/3.0>, via Wikimedia Commons, source: https://images-of-elements.com/hydrogen.php"
        },
        "block": "s"
      },
      ...
}
"""
