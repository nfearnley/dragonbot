"""
Technology (Tc*)
  The ability to use technology, or cause it to fail as soon as you touch it, can be quite important to a dragon. You can indicate your abilities using this tag.
    Tc+++!    I write microcode in my spare time!
    Tc+++     I can program computers using assembly language.
    Tc++      I can program computers using high-level languages.
    Tc+       I can program the video.
    Tc        I haven't yet learned how to wire a plug!
    Tc-       If a program has a bug, I'll find it!
    Tc--      Electricity does funny things when I'm at the controls!
    Tc---     Only the most basic mechanisms survive when I get hold of them!
    Tc---!    All items of technology fail when I'm near!
  Modifiers:
    [field]   If you really feel it is necessary, you can specify your specialist field within square brackets (try to abbreviate if possible). For example Tc++[sw] indicates 'I am fairly good at writing software.'
"""

grammar = """
Technology = 'Tc'
"""
