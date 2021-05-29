"""
Age (A*)
  Your age is something that can be very personal, or something to be very proud of!
    A+++!   Ancient
    A+++    Venerable
    A++     Old enough to know better!
    A+      You've been around.
    A       Mature Adult
    A-      Young Adult
    A--     Still under Mom's (or Dad's) wing.
    A---    Hatchling
    A---!   An egg (nearly hatched)!
    A?      I have no idea how old I am .. I lost count years ago!
  Modifiers:
    r       Put after the A, this indicates that one is specifying one's 'Real Life' age. For example Ar- indicates 'I am a young adult in real life.'
    v       Put after the A, this indicates that one is specifying one's 'Virtual Life' age. For example Av+ indicates 'I've been around on the 'net!'
    ( )     You can use both of the above in seperate tags to specify both ages, but you can also use a short-form method by just putting the r and v parts within parenthesis. For example Ar-Av+ and A(r-v+) both indicate 'I am a young adult in real life, but have been around on the 'net.'
  For reference, Human teenagers would be A-, A would indicate someone in their 20s to mid-30s, and every + would indicate about another 15 years.
"""

grammar = """
Age = 'A'
"""
