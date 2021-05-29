"""
Psy-Power (Q*)
  You may not know it, but there are those who can read your mind like a magazine, or move objects just by thinking. You can indicate your strength in Psionics using this tag.
    Q+++!      There's almost nothing I can't do if I put my mind to it.
    Q+++       I can move mountains, and not bit by bit!
    Q++        I know what you're thinking... did I use six psychic blasts or only five!!!
    Q+         I can talk to the odd spirit, or move very small rocks (churches, lead, ducks, etc.).
    Q          I'm like a book, but haven't learned to read myself yet!
    Q-         Psychics have trouble communicating when I'm around.
    Q--        Only my very outer thoughts are exposed.
    Q---       Psionics just don't seem to have any affect.
    Q---!      Not only am I immune to any Psionic effect, but I prevent them happening around me as well.
  Modifiers:
    [ability]  If you really feel it is necessary, you can specify your general ability within square brackets (try to abbreviate if possible). For example V++[tk] indicates 'I am fairly good at telekinesis.'
  As for Magical-Ability, this tag looks like it represents two seperate abilities. However one will only use the minuses if one has no psionic ability (but still resists psionics), and the plusses if one has psionic ability (it is assumed you resist with your own psionics).
"""

grammar = """
PsyPower = 'Q'
"""
