"""
The Revised Dragon Code V2.5

What is the Dragon Code?
  The Dragon Code is a short form way for those in the Dragon community to describe exactly what they are. It is used primarilly in Usenet post or e-mail signatures to reduce the amount of text one would need for a proper description.
  The code itself consists of a number of 'tags' that represent various characteristics. These tags start with a symbol that indicates what the tag represents, and are followed by other symbols that indicate the strength of (or otherwise modify) that characteristic. The most common modifiers are the + and - symbols, the number of which determines how strong (or weak) that characteristic is.
  You can easily identify the Dragon Code from all the other codes that are present because it always starts with the letters DC. Because the Original Dragon Code started with DC and this revised code is somewhat different (and not compatible with the old code), all Revised Dragon Codes should start DC2.
  The Revised Dragon Code's tags are presented in an arbitrary order below, however you may put them in your code in any order you wish (though keeping them in the order they are presented helps others to decode them). You do not even have to include all of the tags - none of the tags are mandatory including the Species tag. When presenting your own Dragon Code you may want to put spaces between the tags to aid others in reading it, but this is not mandatory either as you can omit spaces if there is not enough room; the only time a space is required is when you omit your Species in which case a space is required after the initial DC2. .
  Still confused? Well scroll down and have a read through the tags. You'll soon get the hang of it!

The Tags:
  Central to the whole code are the various tags. When you are first presented with a Dragon Code, it can be quite daunting to decode (especially when the tags are in a strange order). However with a bit of practice you should soon be able to get the hang of it. Of course no one is expected to know the whole code off by heart, or even to be able to decode the more complicated codes, but there are various programs around that allow you to construct your own code and decode others.
  To date, there are tags that describe almost every aspect of Draconity, both in real and virtual life. Of course there will be many areas that will not be represented here, and in these cases you are free to include "free text" in any part of the code. The only requirement is that you put "double quotes" around any text to distinguish them from other tags.
  Common to all the tags are two modifiers, ? and ~. The ? modifier indicates that you are unsure or do not know what you are - this is often different from omitting the tag as that can indicate that you don't have that characteristic. The ~ modifier indicates that you do not have a fixed value for the tag, or that you vary. Some of the tags will have these modifiers described, but whether they are or not, they apply to all.
  The Dragon Code tags are case sensitive. All the initial tag letters must be in upper case whereas any modifying letters are in lower case. This is to prevent tags being confused.
  There are those who want to represent differences between their virtual lives (on the Internet) and their real lives. The original Dragon Code allowed this for specific codes, but that was felt to be too limiting especially as many are a different species in real life to virtual life. It is now recommended that you have a different code for each life you lead.
  Lastly, please treat the Dragon Code with an open mind and as nothing more than a bit of fun. If you are not represented here it is purely because it is not possible to think of every possible species or characteristic. That said, you can always e-mail your suggestions to Wyrm <wyrm@dragoncode.org> who promises not to eat them!

The Revised Dragon Code (DC2) is maintained by Wyrm <wyrm@dragoncode.org>.
This file was last updated on 28th August 2001.
"""

from pathlib import Path
from importlib import import_module

import parsimonious

# define the grammar
grammar = """
DragonCode  = Header _ Species _ Attribute* Garbage
Attribute   = (ActivityIndex / Age / Appendages / BreathWeapon / Colouration / Diet / DragonFriend / Fruitiness / Gender
            / HoardSize / Huggability / HumourIndex / Irritability / Length / MagicAbility / MatingStatus
            / MonetaryPhilosophy / NativeLand / Offspring / PsyPower / RealityIndex / SkinType / SocialLife / Technology
            / Ubiquity / Weight / Width) _
Header      = "DC2."
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
