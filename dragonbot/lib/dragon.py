from typing import List


class DragonAttributes:
    def __init__(self):
        pass

    def __str__(self) -> str:
        return "attr"


class Species:
    def __init__(self, name: str, attributes: DragonAttributes = None):
        self.name = name
        self.attributes = attributes

    def __str__(self) -> str:
        return self.name


class DragonCode:
    def __init__(self, species: List[Species], attributes: DragonAttributes, shapeshifter: bool):
        self.species = species
        self.attributes = attributes
        self.shapeshifter = shapeshifter

    @classmethod
    def parse(cls, code):
        if not code.startswith("DC2."):
            raise ValueError("Code does not begin with DC2.")

        speciesmap = {
            "D": "dragon",
            "H": "humanoid",
            "A": "amphibian",
            "B": "bird",
            "C": "crustacean",
            "S": "dinosaur",
            "E": "extraterrestrial",
            "F": "fish",
            "I": "insect",
            "L": "legendary",
            "M": "mammal",
            "O": "mollusc",
            "Y": "mythical",
            "P": "plant",
            "R": "reptile",
            "Q": "spirit",
            "U": "undead",
            "~": "shapechanger"
        }

        species = speciesmap[code[4]]
        return DragonCode(species = [Species(species)], attributes = DragonAttributes(), shapeshifter = False)

    def __str__(self) -> str:
        return self.species[0].name
