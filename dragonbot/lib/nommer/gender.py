"""
Gender (G*)
  One's Gender is something that can influence how others treat you. However there's more to it than just one's physical appearance.
    Gf      Female
    Gh      Hermaphrodite
    Gm      Male
    Gn      Neuter
    Gp      Pseudo-hermaphrodite (One who has some characteristics of both male and female, but is not fully hermaphrodite, e.g. feminising testicular syndrome).
    G~      Variable between two or more. If you want to specify the various genders, include them in parenthesis after the ~, for example G~(fm) indicates 'I vary between female and male.'
    G?      Unknown - 'No dice! Cartoon characters aren't anatomically correct!'
  Modifiers:
    >       In transition between two types. You should indicate what you are changing from and to either side of the >. For example Gm>n indicates 'I am a male who is changing to a neuter.'
    " "     If you have a different gender, you can put it after the G in "double quotes". For example G"sex".
    /       There are those who want to specify a different mental gender to their physical, in this case you use / to seperate the two with the mental gender going second. For example Gm/f indicates 'I am a female stuck in a male body.'
"""

grammar = """
Gender = 'G' (Gender_Female / Gender_Hermaphrodite / Gender_Male / Gender_Neuter / Gender_PseudoHermaphrodite / Gender_Variable / Gender_Unknown)
Gender_Female = 'f'
Gender_Hermaphrodite = 'h'
Gender_Male = 'm'
Gender_Neuter = 'n'
Gender_PseudoHermaphrodite = 'p'
Gender_Variable = '~'
Gender_Unknown = '?'
"""
