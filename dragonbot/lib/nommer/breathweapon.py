"""
Breath-Weapon (B*)
  Quite a few Dragons have been famed for their ability to exhale a stream of fire at their enemies. However there are many other types of Breath-Weapon in use.
  The following options are by no means a definitive list and are being added to constantly. However, if you don't see your particular type of breath-weapon listed, you can write it out in "double quotes". For example B"skittles" indicates that you breath skittles - presumably not the ten-pin kind!
    Bac     Acid.
    Bco     Cold or frost.
    Ben     Enchantment.
    Beg     Energy.
    Bfl     Flame or fire.
    Bhe     Heat.
    Bic     Ice.
    Bla     Lava or magma.
    Bph     Photons or Light.
    Bpl     Plasma.
    Bro     Rot.
    Bsm     Smoke.
    Bst     Steam.
    Bsu     Sulphur.
    Bvg     Volcanic gasses (e.g. pyroclastics).
    Bwa     Water.
    Bwi     Wind.
    Bzz     Electricity or lightning.
    B-      No Breath-Weapon. You could also use B"none".
  Modifiers:
    |       Beam - For example Beg| indicates 'I am a Dalek! Exterminate! Exterminate!'
    #       Cloud - For example Bsm# indicates 'When I breathe, ships need to use their fog-horns!'
    /       If you have several breath-weapons, you can specify them all using / to seperate each one. For example Bfl/ac/"chocolate" indicates 'I breathe fire, acid, and chocolate ... anyone for melted acid drops?'
  You can also put the specific type of weapon after the option in "double quotes". For example Bac"sulphuric" indicates that you breathe sulphuric acid.
"""

grammar = """
BreathWeapon = 'B'
"""
