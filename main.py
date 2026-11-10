
from pyscript import document

# Non-metal elements
# Dictionary with information about non-metals
# Element Symbol: (Element Name, Atomic Number, Atomic Mass)

elements = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.90),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222.0)
}

# function to search an element
def search_element(e):

    # Get the input from HTML
    # Remove unnecessary spaces at the beginning and end
    # Capitalize the first letter and make the remaining letters lowercase
    Element1 = document.getElementById("element1").value.strip().capitalize()

    # Retrieve the element information from the dictionary using the entered symbol
    # If the symbol is not found, display "Element not found" with dashes
    result = elements.get(Element1, ("Element not found", "-", "-"))

    # Display the results
    document.getElementById("symbol").innerText = Element1
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]
