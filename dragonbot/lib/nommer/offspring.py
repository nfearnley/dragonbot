"""
Offspring (O*)
  Many dragons who are mated (and also a few who aren't) have either guarded a clutch or two of eggs or protected some hatchlings against predators (yum yum)! This tag allows you to show how many hatchlings you have raised (or are raising).
    O+++!       I have many of them, and none of them look like leaving yet!
    O+++        I have several that haven't fledged yet.
    O++         I have a couple that have not yet left home.
    O+          I've got one still in the nest.
    O           There's just me (and my mate, if applicable).
    O-          I had one, but they've left home.
    O--         I had a couple, but they're living their own lives now.
    O---        I've had several, all successfully fledged.
    O---!       I've had many, but they've all flown away now.
    O+<number>  Indicates exactly how many you have and that they've not left home yet.
    O-<number>  Indicates exactly how many you have had that have flown the coop.
    O?          I lost track long ago. If it meeps, I feed it.
    O~          I have a variable number, depending on who I'm fostering this month!
    O/          If I ever heard one was my fault, I'd faint!
  Modifiers:
    r           Put after the O, this indicates that one is specifying one's 'Real Life' offspring. For example Or- indicates 'I had one in real life, but they left home.'
    v           Put after the O, this indicates that one is specifying one's 'Virtual Life' offspring. For example Ov+ indicates 'I've got one on the 'net, still in the nest.'
    ( )         You can use both of the above in seperate tags to specify both types of offspring, but you can also use a short-form method by just putting the r and v parts within parenthesis. For example Or-Ov+ and O(r-v+) both indicate 'I had one in real life, but they left home; and I've got one on the 'net, still in the nest.'
    a           Put before any plusses or minuses, this indicates that one is specifying adopted offspring. This can be real or virtual. For example Ova+ indicates 'I've got one adopted on the 'net that is still at home.'
"""

grammar = """
Offspring = 'O'
"""
