"""
Magical-Ability (Voodoo) (V*)
  Magical prowess is often associated with dragons, not least in the ability to shape change or to ride the winds, but in other forms as well. This tag indicates how adept you are in the arcane arts.
    V+++!    I have reached the pinnacle of my profession.
    V+++     I'm reasonably adept in my field.
    V++      I know a number of spells.
    V+       I can perform a few cantrips with candles.
    V        Magic is something I've never really looked into.
    V-       Magicians worry when I'm near.
    V--      Most magic seems to fail when I'm nearby!
    V---     Only a few spells seem to have an effect, but that could just be psychological.
    V---!    Magic? What's that?
  Modifiers:
    [field]  If you really feel it is necessary, you can specify your specialist field within square brackets. For example V++[fire] indicates 'I know a number of spells of fire magic.'
  It may look as though this tag shows two abilities, but this is not so. If one has no magical ability, but prevents magic occurring around one then one uses the minuses. However if one has magical ability then you would tend to use that to prevent magic from occurring, thus you would use the plusses.
"""

grammar = """
MagicAbility = 'V'
"""
