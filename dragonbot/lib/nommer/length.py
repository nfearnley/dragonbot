"""
Length (L*)
  Given that there is a collosal variation in size between Dragons, Dragon Friends, and other Species, it is important to know just what you're pounce-tackling or snuggle-hugging! You don't want to be accidentally squished after all!
  There are two methods of specifying ones length, an order of magnitude and an exact measure. You are free to choose whichever you feel is best for you.
    L+++!        Celestial - 'I hate it when planets get in my mouth when I yawn!'
    L+++         Mistaken for mountain ranges - 'Sorry Mr Battleship, I didn't see you!'
    L++          Can't see own tail on a foggy day - 'Can you say "jungle gym"?'
    L+           Godzilla-sized - 'They look up to me. Literally.'
    L            Draco-sized - 'About as normal as dragons get.'
    L-           Human-sized - 'Please, don't step on the tail...'
    L--          Dog-sized - 'Please, don't step on me...'
    L---         Pocket Dragon-sized or below - 'Please, don't sneeze...'
    L---!        Microscopic - 'Honey, I shrunk the dragon!'
    L~           Variable - 'I change size on a whim!'
    L^           One-Dragon-Sized - 'I am just long enough to reach the ground!'
  Quantitative method:
    L<number>i   You are about that number of inches long (1 inch = 2.54 centimetres). For example L480f indicates 'I am about 480 inches long.'
    L<number>f   You are about that number of feet long (1 foot = 30.5 centimetres). For example L40f indicates 'I am about 40 feet long.'
    L<number>y   You are about that number of yards long (1 yard = 0.914 metres). For example L13f indicates 'I am about 13 yards long.'
    L<number>c   You are about that number of centimetres long (1 centimetre = 0.393 inches). For example L1220c indicates 'I am about 1220 centimetres long.'
    L<number>m   You are about that number of metres long (1 metre = 3.28 feet). For example L12m indicates 'I am about 12 metres long.'
    L<number>k   You are about that number of kilometres long (1 kilometre = 0.621 miles). For example L0.01k indicates 'I am about a hundredth of a kilometre long.'
  Measurements are nose to tail for quadrupeds, snakes, serpents, etc; and are full standing height for bipeds (and others that stand upright). If you are not sure how to measure yourself, take the length from nose to tail tip.
  If you want to be more specific as to your dimensions, you can specify your tail, neck and head, and legs/arms length using these modifiers (which use the same unit of measure as the main length):
  Modifiers:
    <number>a    Put after the length, this specifies your 'arm' length (primarilly for bipeds). For example L6f2a indicates 'I am 6 foot tall with arms that are 2 feet long each.'
    <number>l    Put after the length, this specified your 'leg' length. For example L30c5l indicates 'I am 30 centimetres long with 5 centimetre long legs.'
    <number>n    Put after the length, this specifies your 'neck and head' length. For example L1k0.2n indicates 'I am a kilometre in length with a neck and head that are 300 metres in length.'
    <number>t    Put after the length, this specifies your 'tail' length. For example L6i2t indicates 'I am 6 inches long with a 2 inch long tail.'
    <number>w    Put after the length, this specifies your 'wingspan' (wing-tip to wing-tip). For example L3i6w indicates 'I am 3 inches tall with a 6 inch wingspan.'
  You can also combine modifiers, for example L10m4t1l indicates 'I am 10 metres long with a 4 metre long tail and 1 metre long legs.'
  For plants, treat the body as the trunk or stem, legs as roots, arms as branches, wings as leaves, and the neck and head as the flower and its stem.
"""

grammar = """
Length = 'L'
"""
