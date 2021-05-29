"""
Weight (Tonnage) (T*)
  As well as knowing the dimensions of another Dragon, it is also important to know it's weight too. Especially if one intends on having it sit on one's lap!
  There are two methods of specifying ones weight, an order of magnitude and an exact measure. You are free to choose whichever you feel is best for you.
    T+++!        Black-Hole - 'Everything gravitates towards me eventually!'
    T+++         Massive - 'I've been eating rocks again!'
    T++          Obese - 'I'm on a sea-food diet ... I see food and eat it!'
    T+           Over-weight - 'I've been eating too many doughnuts again!'
    T            Normal - 'I'm as normal a weight as one gets.'
    T-           Under-weight - 'I've not had a good meal for ages!'
    T--          Buoyant - 'I've been breathing helium again!'
    T---         Feather-weight - 'I get blown about by the wind.'
    T---!        Weightless - 'I'm made out of gossamer.'
  As with most other tags, ? and ~ are valid modifiers for unknown and variable, respectively.
  Quantitative method:
    T<number>c   You weigh about that number of long hundredweight avoirdupois (1 cwt = 50.8 kilogrammes or 8 stone / 112 pounds). For example T16c indicates 'I am about 16 hundredweight.'
    T<number>g   You weigh about that number of grammes (1 gramme = 0.0353 ounces). For example T800000g indicates 'I am about 800000 grammes.'
    T<number>k   You weigh about that number of kilogrammes (1 kilogramme = 2.205 pounds). For example T800k indicates 'I am about 800 kilogrammes.'
    T<number>l   You weigh about that number of pounds avoirdupois (1 pound = 0.4536 kilogrammes or 16 ounces). For example T1800l indicates 'I am about 1800 pounds.'
    T<number>o   You weigh about that number of ounces avoirdupois (1 ounce = 28.35 grammes). For example T28700o indicates 'I am about 28700 ounces.'
    T<number>s   You weigh about that number of stones avoirdupois (1 stone = 6.35 kilogrammes or 14 pounds). For example T128s indicates 'I am about 128 stones.'
    T<number>t   You weigh about that number of tons avoirdupois or metric tonnes (1 ton = 1016 kilogrammes or 2240 pounds, 1 tonne = 2205 pounds or 1000 kilogrammes). It's up to you which one you mean! For example T0.8t indicates 'I am about 0.8 tons.'
"""

grammar = """
Weight = 'T' (Weight_4 / Weight_3 / Weight_2 / Weight_1 / Weight_n4 / Weight_n3 / Weight_n2 / Weight_n1 / Weight_unknown / Weight_variable / Weight_0)
Weight_4  = '+++!'
Weight_3  = '+++'
Weight_2  = '++'
Weight_1  = '+'
Weight_0  = ''
Weight_n1 = '-'
Weight_n2 = '--'
Weight_n3 = '---'
Weight_n4 = '---!'
Weight_unknown  = '?'
Weight_variable = '~'
"""
