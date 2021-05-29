"""
Appendages (P*)
  This tag describes the numbers of limbs and other appendages on your body. If you have the 'obvious' numbers of limbs for a creature of your species you can skip this tag... but then what's normal?!?!
    Pa         A pair of arms
    Pf         A pair of fore-limbs (e.g. limbs that can be used as both arms and legs).
    Ph         A head. Yes! There are creatures with more than one!
    Pk         A crest. Normally on ones head, but you never know!
    Pl         A pair of legs.
    Pp         A pair of paddles, flukes, or fins.
    Pt         A tail. Again, some creatures do have more than one!
    Pv         A pair of horns or spines on the head.
    Pw         A pair of wings.
    Pw'        A pair of wings that also act as arms, legs, or fore-limbs.
  Modifiers:
    ^          Appendage ends in a webbed hand or foot. For example Pl^ indicates 'Don't call me a frog!'
    +          One more than normal. For example Ph+ indicates 'I got ahead in advertising!'
    -          One less than normal. For example Pw- indicates 'I have only one wing!'
    !          I have many of these. For example Pl! indicates 'I am a millipede!'
    <number>   I have this many of these. For example Pl3l- indicates 'I am an octopus with a missing leg!'
    ~          Variable. For example Pl~ indicates 'I grow legs when I feel the need for them!'
  You can combine the above options together in any you want. For example Phwlwllt indicates that you have a head, a pair of wings, a pair of legs, a pair of wings, then two pairs of legs, and a tail.
  You can also miss out any options that are obvious for your species - most sensible creatures have only one head and a tail!
"""

grammar = """
Appendages = 'P' Appendages_part*
Appendages_part       = Appendages_arms / Appendages_forelimbs / Appendages_head / Appendages_crest / Appendages_legs
                      / Appendages_paddles / Appendages_tail / Appendages_horns / Appendages_wingarms / Appendages_wings
Appendages_arms       = 'a'
Appendages_forelimbs  = 'f'
Appendages_head       = 'h'
Appendages_crest      = 'k'
Appendages_legs       = 'l'
Appendages_paddles    = 'p'
Appendages_tail       = 't'
Appendages_horns      = 'v'
Appendages_wings      = 'w'
Appendages_wingarms   = "w'"
"""
