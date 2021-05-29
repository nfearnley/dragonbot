"""
Mating-Status (M*)
  Sure, there are those lucky/unlucky dragons among us who are mated/tied-down in reality, but what about those who have a Special Someone on-line? Or are looking ... desperately?! Or are hiding from the lookers?!
    M+++!     I'm mated in real life to my on-line mate's real life self as well!
    M+++      Am I mated? Ask my hatchlings!
    M++       Ask my significant other!
    M+        Ask my mate-to-be!
    M         Ask me, and I might just say yes!
    M-        Don't ask!
    M--       Ask my (poker/football/bridge/Trivial Pursuit) buddies!
    M---      I'm single and very proud of it!
    M---!     Not only am I single, but I despise the idea of mating.
    M/        Ask me, and I'll ask your snout to meet your kidneys!
  Modifiers:
    <space>   Put before the plusses (doesn't apply to minuses), this indicates that one is distant from one's mate. For example M ++ indicates 'Ask my significant other, who is far from home!'
    <number>  Put after the plusses, this indicates the number of mates one has. For example M++3 indicates 'Ask my three significant others!'
    |         Put after the plusses (doesn't apply to minuses) or the number of mates if specified, this indicates that you are seperated (e.g. divorced). If you have more than one mate, you should put the number of seperated mates after the |, for example M+++2|1 indicates 'Am I mated? Ask my hatchlings of either of my two mates, one of which I am seperated from.'
    *         Identical to | above except that it indicates one was bitter about it!
    _         Identical to | above except that it indicates your mate is dead.
    xx        Put at the end of the tag, this indicates that one is a card-carrying member of the XX Conspiracy!
    xy        Put at the end of the tag, this indicates that one is a card-carrying member of the XY Conspiracy!
    r         Put after the M, this indicates that one is specifying one's 'Real Life' mating status. For example Mr- indicates 'Don't ask me in real life.'
    v         Put after the M, this indicates that one is specifying one's 'Virtual Life' mating status. For example Mv+ indicates 'Ask my mate-to-be on the 'net.'
    ( )       You can use both of the above in seperate tags to specify both mating statuses, but you can also use a short-form method by just putting the r and v parts within parenthesis. For example Mr-Mv+ and M(r-v+) both indicate 'Don't ask me in real life, but ask my mate-to-be on the 'net.'
"""

grammar = """
MatingStatus = 'M'
"""
