# |----------------------------------------- 120 character line length ------------------------------------------------|
grammar = """
Species = SpeciesForm / SpeciesShape / SpeciesCross / SpeciesShapechanger / SpeciesPart

SpeciesForm = SpeciesPart "[" SpeciesPart "]"

SpeciesShape = SpeciesPart "^" SpeciesPart

SpeciesCross = SpeciesPart "+" SpeciesPart

SpeciesShapechanger
    = (((SpeciesPart "~") / ("~" SpeciesPart)) ("/" SpeciesPart)*)
    / "~"

SpeciesPart = SpeciesType "?"?

SpeciesType = Species_Dragons / Species_Humanoids / Species_Amphibians / Species_Birds / Species_Crustaceans
        / Species_Dinosaurs / Species_Extraterrestrial / Species_Fish / Species_Insects / Species_Legendary
        / Species_Mammals / Species_Molluscs / Species_Mythical / Species_Plants / Species_Reptiles / Species_Spirits
        / Species_Undead

Species_Dragons                     = "D" Species_Dragons_Subspecies?
    Species_Dragons_Subspecies
        = Species_Dragons_Amphiteres / Species_Dragons_Draconids / Species_Dragons_Dragonettes
        / Species_Dragons_EasternDragons / Species_Dragons_FaerieDragons / Species_Dragons_Hydra
        / Species_Dragons_Dimar / Species_Dragons_Dracolich / Species_Dragons_PerneseDragons
        / Species_Dragons_TurtleDragons / Species_Dragons_Serpents / Species_Dragons_Tarrasques
        / Species_Dragons_Pseudodragons / Species_Dragons_Wyverns / Species_Dragons_WesternDragons
        / Species_Dragons_Wyrms
    Species_Dragons_Amphiteres      = "a"
    Species_Dragons_Draconids       = "c"
    Species_Dragons_Dragonettes     = "d"
    Species_Dragons_EasternDragons  = "e"
    Species_Dragons_FaerieDragons   = "f"
    Species_Dragons_Hydra           = "h"
    Species_Dragons_Dimar           = "i"
    Species_Dragons_Dracolich       = "l"
    Species_Dragons_PerneseDragons  = "p"
    Species_Dragons_TurtleDragons   = "r"
    Species_Dragons_Serpents        = "s" Species_Dragons_Serpents_Subspecies?
        Species_Dragons_Serpents_Subspecies
            = Species_Dragons_Serpents_SeaSerpents / Species_Dragons_Serpents_FireSerpents
        Species_Dragons_Serpents_SeaSerpents    = "s"
        Species_Dragons_Serpents_FireSerpents   = "f"
    Species_Dragons_Tarrasques      = "t"
    Species_Dragons_Pseudodragons   = "u"
    Species_Dragons_Wyverns         = "v"
    Species_Dragons_WesternDragons  = "w"
    Species_Dragons_Wyrms           = "y"

Species_Humanoids                       = "H" Species_Humanoids_Subspecies?
    Species_Humanoids_Subspecies
        = Species_Humanoids_Apes / Species_Humanoids_Dwarves / Species_Humanoids_Elves / Species_Humanoids_Fairies
        / Species_Humanoids_Giants / Species_Humanoids_Gnomes / Species_Humanoids_Hobbits / Species_Humanoids_Kender
        / Species_Humanoids_Nymphs / Species_Humanoids_Troll / Species_Humanoids_Wolfman
    Species_Humanoids_Apes              = "a"
    Species_Humanoids_Dwarves           = "d"
    Species_Humanoids_Elves             = "e" Species_Humanoids_Elves_Subspecies?
        Species_Humanoids_Elves_Subspecies
            = Species_Humanoids_Elves_WoodElves
        Species_Humanoids_Elves_WoodElves   = "w"
    Species_Humanoids_Fairies           = "f"
    Species_Humanoids_Giants            = "i"
    Species_Humanoids_Gnomes            = "g"
    Species_Humanoids_Hobbits           = "h"
    Species_Humanoids_Kender            = "k"
    Species_Humanoids_Nymphs            = "y"
    Species_Humanoids_Troll             = "t"
    Species_Humanoids_Wolfman           = "w"

Species_Amphibians                      = "A" Species_Amphibians_Subspecies?
    Species_Amphibians_Subspecies
        = Species_Amphibians_Frogs / Species_Amphibians_Newts / Species_Amphibians_Salamanders
        / Species_Amphibians_Toads
    Species_Amphibians_Frogs            = "f"
    Species_Amphibians_Newts            = "n"
    Species_Amphibians_Salamanders      = "s"
    Species_Amphibians_Toads            = "t"

Species_Birds               = "B" Species_Birds_Subspecies?
    Species_Birds_Subspecies
        = Species_Birds_Crows / Species_Birds_Eagles / Species_Birds_Hawks / Species_Birds_Phoenix
        / Species_Birds_Ravens
    Species_Birds_Crows     = "c"
    Species_Birds_Eagles    = "e"
    Species_Birds_Hawks     = "h"
    Species_Birds_Phoenix   = "p"
    Species_Birds_Ravens    = "r"

Species_Crustaceans                 = "C" Species_Crustaceans_Subspecies?
    Species_Crustaceans_Subspecies
        = Species_Crustaceans_Crabs / Species_Crustaceans_Lobsters / Species_Crustaceans_Shrimps
    Species_Crustaceans_Crabs       = "c"
    Species_Crustaceans_Lobsters    = "l"
    Species_Crustaceans_Shrimps     = "s"

Species_Dinosaurs                   = "S" Species_Dinosaurs_Subspecies?
    Species_Dinosaurs_Subspecies
        = Species_Dinosaurs_Allosaurs / Species_Dinosaurs_Triceratops / Species_Dinosaurs_Apatosaurs
        / Species_Dinosaurs_Stegosaurs / Species_Dinosaurs_Tyrannosaurs / Species_Dinosaurs_Velociraptors
    Species_Dinosaurs_Allosaurs     = "a"
    Species_Dinosaurs_Triceratops   = "c"
    Species_Dinosaurs_Apatosaurs    = "p"
    Species_Dinosaurs_Stegosaurs    = "s"
    Species_Dinosaurs_Tyrannosaurs  = "t"
    Species_Dinosaurs_Velociraptors = "v"

Species_Extraterrestrial                = "E" Species_Extraterrestrial_Subspecies?
    Species_Extraterrestrial_Subspecies
        = Species_Extraterrestrial_Daleks / Species_Extraterrestrial_Tribbles
    Species_Extraterrestrial_Daleks     = "d"
    Species_Extraterrestrial_Tribbles   = "t"

Species_Fish                    = "F" Species_Fish_Subspecies?
    Species_Fish_Subspecies
        = Species_Fish_SeaHorses / Species_Fish_FreshwaterFish / Species_Fish_Sharks
    Species_Fish_SeaHorses      = "h"
    Species_Fish_FreshwaterFish = "f"
        Species_Fish_FreshwaterFish_Subspecies
            = Species_Fish_FreshwaterFish_Goldfish / Species_Fish_FreshwaterFish_Trout
        Species_Fish_FreshwaterFish_Goldfish    = "g"
        Species_Fish_FreshwaterFish_Trout       = "t"
    Species_Fish_Sharks         = "s"

Species_Insects                 = "I" Species_Insects_Subspecies?
    Species_Insects_Subspecies
        = Species_Insects_Ants / Species_Insects_Beetles / Species_Insects_Flies / Species_Insects_Locusts
        / Species_Insects_Moths / Species_Insects_Butterflies
    Species_Insects_Ants        = "a"
    Species_Insects_Beetles     = "b"
    Species_Insects_Flies       = "f"
    Species_Insects_Locusts     = "l"
    Species_Insects_Moths       = "m"
    Species_Insects_Butterflies = "u"

Species_Legendary                   = "L" Species_Legendary_Subspecies?
    Species_Legendary_Subspecies
        = Species_Legendary_Gargoyles / Species_Legendary_Gremlins / Species_Legendary_Griffins
        / Species_Legendary_Manticores / Species_Legendary_Mermaids / Species_Legendary_Salamanders
        / Species_Legendary_Sprites / Species_Legendary_Treants / Species_Legendary_Unicorns
    Species_Legendary_Gargoyles     = "r"
    Species_Legendary_Gremlins      = "l"
    Species_Legendary_Griffins      = "g"
    Species_Legendary_Manticores    = "n"
    Species_Legendary_Mermaids      = "m"
    Species_Legendary_Salamanders   = "f"
    Species_Legendary_Sprites       = "s"
    Species_Legendary_Treants       = "t"
    Species_Legendary_Unicorns      = "u"

Species_Mammals                         = "M" Species_Mammals_Subspecies?
    Species_Mammals_Subspecies
        = Species_Mammals_Bats / Species_Mammals_Bears / Species_Mammals_Canines / Species_Mammals_Felines
        / Species_Mammals_Horses / Species_Mammals_Monkeys / Species_Mammals_Polecats / Species_Mammals_Rodents
        / Species_Mammals_Cetaceans
    Species_Mammals_Bats                = "a"
    Species_Mammals_Bears               = "b"
    Species_Mammals_Canines             = "c" Species_Mammals_Canines_Subspecies?
        Species_Mammals_Canines_Subspecies
            = Species_Mammals_Canines_DomesticDogs / Species_Mammals_Canines_Foxes / Species_Mammals_Canines_Wolves
        Species_Mammals_Canines_DomesticDogs    = "d"
        Species_Mammals_Canines_Foxes           = "f"
        Species_Mammals_Canines_Wolves          = "w"
    Species_Mammals_Felines             = "f" Species_Mammals_Felines_Subspecies?
        Species_Mammals_Felines_Subspecies
            = Species_Mammals_Felines_BlackPanthers / Species_Mammals_Felines_Cheetahs
            / Species_Mammals_Felines_DomesticCats / Species_Mammals_Felines_Leopard / Species_Mammals_Felines_Lions
            / Species_Mammals_Felines_Lynxs / Species_Mammals_Felines_Panthers / Species_Mammals_Felines_Pumas
            / Species_Mammals_Felines_Tigers
        Species_Mammals_Felines_BlackPanthers   = "b"
        Species_Mammals_Felines_Cheetahs        = "c"
        Species_Mammals_Felines_DomesticCats    = "d"
        Species_Mammals_Felines_Leopard         = "p" Species_Mammals_Felines_Leopard_Subspecies?
            Species_Mammals_Felines_Leopard_Subspecies
                = Species_Mammals_Felines_Leopard_SnowLeopard
            Species_Mammals_Felines_Leopard_SnowLeopard = "s"
        Species_Mammals_Felines_Lions           = "l"
        Species_Mammals_Felines_Lynxs           = "x"
        Species_Mammals_Felines_Panthers        = "a"
        Species_Mammals_Felines_Pumas           = "u"
        Species_Mammals_Felines_Tigers          = "t"
    Species_Mammals_Horses              = "h"
    Species_Mammals_Monkeys             = "m" Species_Mammals_Monkeys_Subspecies?
        Species_Mammals_Monkeys_Subspecies
            = Species_Mammals_Monkeys_Gibbons
        Species_Mammals_Monkeys_Gibbons         = "g"
    Species_Mammals_Polecats            = "p" Species_Mammals_Polecats_Subspecies?
        Species_Mammals_Polecats_Subspecies
            = Species_Mammals_Polecats_Ferrets / Species_Mammals_Polecats_Mink
        Species_Mammals_Polecats_Ferrets        = "f"
        Species_Mammals_Polecats_Mink           = "m"
    Species_Mammals_Rodents             = "r" Species_Mammals_Rodents_Subspecies?
        Species_Mammals_Rodents_Subspecies
            = Species_Mammals_Rodents_Gerbils / Species_Mammals_Rodents_Hamsters / Species_Mammals_Rodents_Mice
            / Species_Mammals_Rodents_Rats / Species_Mammals_Rodents_Squirrels
        Species_Mammals_Rodents_Gerbils         = "g"
        Species_Mammals_Rodents_Hamsters        = "h"
        Species_Mammals_Rodents_Mice            = "m"
        Species_Mammals_Rodents_Rats            = "r"
        Species_Mammals_Rodents_Squirrels       = "s"
    Species_Mammals_Cetaceans           = "w" Species_Mammals_Cetaceans_Subspecies?
        Species_Mammals_Cetaceans_Subspecies
            = Species_Mammals_Cetaceans_Dolphins / Species_Mammals_Cetaceans_KillerWhales
            / Species_Mammals_Cetaceans_Porpoises
        Species_Mammals_Cetaceans_Dolphins      = "d"
        Species_Mammals_Cetaceans_KillerWhales  = "k"
        Species_Mammals_Cetaceans_Porpoises     = "p"

Species_Molluscs = "O" Species_Molluscs_Subspecies?
    Species_Molluscs_Subspecies
        = Species_Molluscs_Cuttlefish / Species_Molluscs_Limpets / Species_Molluscs_Octopuses
        / Species_Molluscs_Oysters / Species_Molluscs_Snails
    Species_Molluscs_Cuttlefish     = "c"
    Species_Molluscs_Limpets        = "l"
    Species_Molluscs_Octopuses      = "o"
    Species_Molluscs_Oysters        = "y"
    Species_Molluscs_Snails         = "s"

Species_Mythical = "Y" Species_Mythical_Subspecies?
    Species_Mythical_Subspecies
        = Species_Mythical_Centaurs / Species_Mythical_Cyclopses / Species_Mythical_Golems / Species_Mythical_Hellhounds
        / Species_Mythical_Minotaurs / Species_Mythical_Pegasi / Species_Mythical_Satyrs / Species_Mythical_Sphinxes
    Species_Mythical_Centaurs       = "c"
    Species_Mythical_Cyclopses      = "y"
    Species_Mythical_Golems         = "g"
    Species_Mythical_Hellhounds     = "h"
    Species_Mythical_Minotaurs      = "m"
    Species_Mythical_Pegasi         = "p"
    Species_Mythical_Satyrs         = "t"
    Species_Mythical_Sphinxes       = "s"

Species_Plants = "P" Species_Plants_Subspecies?
    Species_Plants_Subspecies
        = Species_Plants_Cacti / Species_Plants_Fungii / Species_Plants_Trees
    Species_Plants_Cacti    = "c"
    Species_Plants_Fungii   = "f"
    Species_Plants_Trees    = "t"
        Species_Plants_Trees_Subspecies
            = Species_Plants_Trees_AshTrees / Species_Plants_Trees_ElmTrees / Species_Plants_Trees_OakTrees
        Species_Plants_Trees_AshTrees = "a"
        Species_Plants_Trees_ElmTrees = "e"
        Species_Plants_Trees_OakTrees = "o"

Species_Reptiles = "R" Species_Reptiles_Subspecies?
    Species_Reptiles_Subspecies
        = Species_Reptiles_AlligatorsAndCrocodiles / Species_Reptiles_Chameleons / Species_Reptiles_Geckos
        / Species_Reptiles_KomodoDragons / Species_Reptiles_Lizards / Species_Reptiles_Skinks / Species_Reptiles_Snakes
        / Species_Reptiles_Turtles
    Species_Reptiles_AlligatorsAndCrocodiles    = "a"
    Species_Reptiles_Chameleons                 = "c"
    Species_Reptiles_Geckos                     = "g"
    Species_Reptiles_KomodoDragons              = "k"
    Species_Reptiles_Lizards                    = "l"
    Species_Reptiles_Skinks                     = "n"
        Species_Reptiles_Skinks_Subspecies
            = Species_Reptiles_Skinks_FireSkinks
        Species_Reptiles_Skinks_FireSkinks          = "f"
    Species_Reptiles_Snakes                     = "s"
    Species_Reptiles_Turtles                    = "t"

Species_Spirits = "Q" Species_Spirits_Subspecies?
    Species_Spirits_Subspecies
        = Species_Spirits_Angels / Species_Spirits_DevilsAndDemons / Species_Spirits_Ghosts / Species_Spirits_Imps
        / Species_Spirits_Poltergeists / Species_Spirits_Spectres / Species_Spirits_WillOTheWisps
    Species_Spirits_Angels          = "a"
    Species_Spirits_DevilsAndDemons = "d"
    Species_Spirits_Ghosts          = "g"
    Species_Spirits_Imps            = "i"
    Species_Spirits_Poltergeists    = "p"
    Species_Spirits_Spectres        = "s"
    Species_Spirits_WillOTheWisps   = "w"

Species_Undead = "U" Species_Undead_Subspecies?
    Species_Undead_Subspecies
        = Species_Undead_Ghouls / Species_Undead_Vampires / Species_Undead_Zombies
    Species_Undead_Ghouls   = "g"
    Species_Undead_Vampires = "v"
    Species_Undead_Zombies  = "z"
"""
