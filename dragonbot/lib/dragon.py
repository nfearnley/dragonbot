from typing import List, Literal, Optional, Tuple

GenderPreset = Literal['f', 'h', 'm', 'n', 'p', '?']


class Length:
    def __init__(self) -> None:
        pass


class Gender:
    def __init__(self, preset_gender: GenderPreset, custom_gender: str, variable: List[str],
                 transition: Tuple[str, str], discrepancy: Tuple[str, str]) -> None:

        if sum(a is not None for a in (preset_gender, custom_gender, variable, transition, discrepancy)) != 1:
            raise TypeError("Didn't pass one type of gender in.")

        self.preset_gender = preset_gender
        self.custom_gender = custom_gender
        self.variable = variable
        self.transition = transition
        self.discrepancy = discrepancy

    @property
    def active(self):
        return self.preset_gender or self.custom_gender or self.variable or self.transition or self.discrepancy


class DragonAttributes:
    def __init__(self, gender = Optional[str]):
        pass

    def __str__(self) -> str:
        return "attr"


class Species:
    def __init__(self, name: str, attributes: DragonAttributes = None, subtype: str = None):
        self.name = name
        self.subtype = subtype
        self.attributes = attributes

    def __str__(self) -> str:
        return self.name


class DragonCode:
    def __init__(self, species: Species, attributes: DragonAttributes,
                 shapeshifter: bool, multispecies: Optional[List[Species]] = None,
                 shaped_species: Optional[Species] = None, alternate_form: Optional[Species] = None):
        self.species = species
        self.multispecies = multispecies
        self.shaped_species = shaped_species
        self.alternate_form = alternate_form
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
