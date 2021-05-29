"""
Diet (F*)
  Most creatures eat something (or feed on something to be more exact). This simply indicates your favourite food groups and how much you tend to eat.
    F+++!   Insatiable - 'More! More! More!'
    F+++    Voracious - 'At least you don't have to wash up the plates now!'
    F++     Glutton - 'I have three square meals an hour!'
    F+      Overindulgent - 'One more of those won't hurt!'
    F       Normal for your species - 'I have three square meals a day!'
    F-      Dieting - 'Only a soup&ccedil;on of that if you please!'
    F--     Efficient - 'Only soup if you please!'
    F---    Anorexic - 'Eating is something I do every blue moon!'
    F---!   Fasting - 'Duke Humphrey is an ideal dinner guest!'
  Food groups:
    Fc      Carnivourous.
    Ff      Fluids - 'Here fishy fishy fish!'
    Fj      Junk food addict - 'Chocolate for ME!'
    Fm      Mineral-eater - 'I AM the Big Red Rock Eater!'
    Fo      Omnivorous.
    Fp      Photosynthesiser.
    Fv      Vegetarian.
  Modifiers:
    /       If you eat several things, you can seperate their codes with /. For example Fv/f indicates 'I eat and drink normally, but nothing animate!'
    ~       This indicates that you eat anything. If put after a food group it indicates you eat anything of that type. For example Fv~ indicates 'I eat anything vegetable.'
  You can combine the above in any order, for example F---f is the same as Ff--- which indicates 'I live in a desert!'
  The amount you tend to eat should only appear once and is not related to the food groups.
"""

grammar = """
Diet = 'F'
"""
