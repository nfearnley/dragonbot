from decimal import Decimal
from typing import List, Literal, Optional, Tuple

GenderPreset = Literal['f', 'h', 'm', 'n', 'p', '?']
StandardModifiers = Literal['+++!', '+++', '++', '+', '', '-', '--', '---', '---!']


class Attribute:
    letter = None

    def __init__(self):
        pass

    @classmethod
    def parse(cls, code: str):
        if not code.startswith(cls.letter):
            raise ValueError(f"{cls.__name__} attribute doesn't start with {cls.letter}.")

    def __str__(self) -> str:
        raise NotImplementedError


class Appendage(Attribute):
    def __init__(self, name: str, number: Optional[int] = None,
                 webbed: Optional[bool] = None, many: Optional[bool] = None, variable: Optional[bool] = None):
        self.name = name
        self.number = number
        self.webbed = webbed
        self.many = many
        self.variable = variable

        if self.number is not None and (self.many is not None or self.variable is not None):
            raise ValueError("Specific number and vauge amount is mutually exclusive for Appendages.")
        if self.many is None and self.variable is None and self.number is None:
            raise ValueError("An amount of appendages must be specified.")
        if self.many is not None and self.variable is not None:
            raise ValueError("Many and Variable options are mutually exclusive for Appendages.")


class Color(Attribute):
    def __init__(self, color: str, *,
                 light: Optional[bool] = None,
                 dark: Optional[bool] = None,
                 metallic: Optional[bool] = None,
                 transparent: Optional[bool] = None,
                 luminescent: Optional[bool] = None,
                 pearlescent: Optional[bool] = None,
                 glittery: Optional[bool] = None):
        self.color = color
        self.light = light
        self.dark - dark
        self.metallic = metallic
        self.transparent = transparent
        self.luminescent = luminescent
        self.pearlescent = pearlescent
        self.glittery = glittery


class ColorSpec(Attribute):
    def __init__(self, bases: List[Color], *,
                 stripes: Optional[List[Color]] = None,
                 bands: Optional[List[Color]] = None,
                 spots: Optional[List[Color]] = None,
                 stars: Optional[List[Color]] = None,
                 mottled: Optional[List[Color]] = None,
                 iridesence: Optional[List[Color]] = None,
                 mix: Optional[List[Color]] = None,
                 plaid: Optional[List[Color]] = None,
                 patterned: Optional[List[Color]] = None,
                 marbled: Optional[List[Color]] = None,
                 transition: Optional[List[Color]] = None):
        self.bases = bases
        self.stripes = stripes
        self.bands = bands
        self.spots = spots
        self.stars = stars
        self.mottled = mottled
        self.iridesence = iridesence
        self.mix = mix
        self.plaid = plaid
        self.patterned = patterned
        self.marbled = marbled
        self.transition = transition


class Gender(Attribute):
    letter = "G"

    def __init__(self, preset_gender: Optional[GenderPreset] = None, custom_gender: Optional[str] = None,
                 variable: Optional[List[str]] = None, transition: Optional[Tuple[str, str]] = None,
                 discrepancy: Optional[Tuple[str, str]] = None):

        self.preset_gender = preset_gender
        self.custom_gender = custom_gender
        self.variable = variable
        self.transition = transition
        self.discrepancy = discrepancy

        self.options = (self.preset_gender, self.custom_gender, self.variable, self.transition, self.discrepancy)

        if sum(a is not None for a in self.options) != 1:
            raise TypeError("Didn't pass one type of gender in.")

    @property
    def active_type(self):
        if self.preset_gender:
            return "preset"
        if self.custom_gender:
            return "custom"
        if self.variable:
            return "variable"
        if self.transition:
            return "transition"
        if self.discrepancy:
            return "discrepancy"

    @property
    def active(self):
        return next((item for item in self.options if item is not None))


class Length(Attribute):
    letter = "L"

    def __init__(self, vauge: Optional[str] = None, specific: Optional[Decimal] = None,
                 arm: Optional[Decimal] = None,
                 leg: Optional[Decimal] = None,
                 neck: Optional[Decimal] = None,
                 tail: Optional[Decimal] = None,
                 wingspan: Optional[Decimal] = None):
        self.vauge = vauge
        self.specific = specific

        self.arm = arm
        self.leg = leg
        self.neck = neck
        self.tail = tail
        self.wingspan = wingspan

        if sum(a is not None for a in (self.vauge, self.specific)) != 1:
            raise TypeError("Vauge and specific lengths are mutually exculsive.")


class Width(Attribute):
    letter = "W"

    def __init__(self, value: Literal[StandardModifiers, "~"]):
        self.value = value


class Weight(Attribute):
    letter = "T"

    def __init__(self, vauge: Optional[str] = None, specific: Optional[Decimal] = None):
        self.vauge = vauge
        self.specific = specific

        if sum(a is not None for a in (self.vauge, self.specific)) != 1:
            raise TypeError("Vauge and specific lengths are mutually exculsive.")


class Appendages(Attribute):
    letter = "P"

    def __init__(self,
                 arms: Optional[Appendage] = None,
                 forelimbs: Optional[Appendage] = None,
                 heads: Optional[Appendage] = None,
                 crests: Optional[Appendage] = None,
                 legs: Optional[Appendage] = None,
                 paddles: Optional[Appendage] = None,
                 tails: Optional[Appendage] = None,
                 horns: Optional[Appendage] = None,
                 wings: Optional[Appendage] = None,
                 winglimbs: Optional[Appendage] = None):
        self.arms = arms
        self.forelimbs = forelimbs
        self.heads = heads
        self.crests = crests
        self.legs = legs
        self.paddles = paddles
        self.tails = tails
        self.horns = horns
        self.wings = wings
        self.winglimbs = winglimbs


class SkinType(Attribute):
    letter = "Sk"

    def __init__(self,
                 base: Optional[str] = None,
                 arms: Optional[str] = None,
                 belly: Optional[str] = None,
                 head: Optional[str] = None,
                 legs: Optional[str] = None,
                 neck: Optional[str] = None,
                 tail: Optional[str] = None,
                 wings: Optional[str] = None):
        self.base = base
        self.arms = arms
        self.belly = belly
        self.head = head
        self.legs = legs
        self.neck = neck
        self.tail = tail
        self.wings = wings


class Coloration(Attribute):
    letter = "C"

    def __init__(self,
                 base: Optional[ColorSpec] = None,
                 arms: Optional[ColorSpec] = None,
                 belly: Optional[ColorSpec] = None,
                 claws: Optional[ColorSpec] = None,
                 eyes: Optional[ColorSpec] = None,
                 fur: Optional[ColorSpec] = None,
                 head: Optional[ColorSpec] = None,
                 crest: Optional[ColorSpec] = None,
                 legs: Optional[ColorSpec] = None,
                 neck: Optional[ColorSpec] = None,
                 points: Optional[ColorSpec] = None,
                 spines: Optional[ColorSpec] = None,
                 tail: Optional[ColorSpec] = None,
                 aura: Optional[ColorSpec] = None,
                 horns: Optional[ColorSpec] = None,
                 wings: Optional[ColorSpec] = None):
        self.base = base
        self.arms = arms
        self.belly = belly
        self.claws = claws
        self.eyes = eyes
        self.fur = fur
        self.head = head
        self.crest = crest
        self.legs = legs
        self.neck = neck
        self.points = points
        self.spines = spines
        self.tail = tail
        self.aura = aura
        self.horns = horns
        self.wings = wings


class Age(Attribute):
    letter = "A"

    def __init__(self, value: Literal[StandardModifiers, '?']):
        self.value = value


class DragonAttributes:
    def __init__(self,
                 gender: Optional[Gender] = None,
                 length: Optional[Length] = None,
                 width: Optional[Width] = None,
                 weight: Optional[Weight] = None,
                 appendages: Optional[Appendages] = None,
                 skintype: Optional[SkinType] = None,
                 coloration: Optional[Coloration] = None,
                 age: Optional[Age] = None):
        self.gender = gender
        self.length = length
        self.width = width
        self.weight = weight
        self.appendages = appendages
        self.skintype = skintype
        self.coloration = coloration
        self.age = age

    def __str__(self) -> str:
        return "attrs"


class Species:
    def __init__(self, name: str, attributes: DragonAttributes = None, subtype: str = None):
        self.name = name
        self.subtype = subtype
        self.attributes = attributes

    def __str__(self) -> str:
        return self.name


class DragonCode:
    def __init__(self, species: Species, attributes: DragonAttributes,
                 multispecies: Optional[List[Species]] = None,
                 shaped_species: Optional[Species] = None, alternate_form: Optional[Species] = None):
        self.species = species
        self.multispecies = multispecies
        self.shaped_species = shaped_species
        self.alternate_form = alternate_form
        self.attributes = attributes

    @classmethod
    def parse(cls, code: str):
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
