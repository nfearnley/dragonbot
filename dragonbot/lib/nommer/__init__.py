from pathlib import Path
from importlib import import_module

import parsimonious

# define the grammar
grammar = """
Parser                          = DragonCode Garbage
DragonCode                      = Header _ Species
Header                          = "DC2."
"""

for module_path in Path(__file__).parent.glob("*.py"):
    module_name = module_path.stem
    if module_name == "__init__":
        continue
    module = import_module(f"dragonbot.lib.nommer.{module_name}")
    grammar += module.grammar

grammar += """
Garbage   = ~".*"
_  = ~"[ \\t\\r\\n]*"   # optional whitespace
__ = ~"[ \\t\\r\\n]+"   # mandatory whitespace
"""


def nom(s):
    g = parsimonious.Grammar(grammar)
    return g.parse(s)
