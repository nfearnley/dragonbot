"""
Width (W*)
  There comes a time in a human's life when they stop growing vertically and start to grow horizontally! Well, so do Dragons! This tag is a measure of your spread, or lack of it.
    W+++!   'I am Athelind! My belly is now several galaxies wide ... while I'm only a few hundred feet long!'
    W+++    'Planets have been known to crack in half with my arrival!'
    W++     'My digestion of food has been known to cause earthquakes.'
    W+      'I move by rolling. Flying has always been an effort for me.'
    W       'What can I say ... I'm normal, except for a few feasts here or there.'
    W-      'I'm slightly on the slim side!'
    W--     'Ever heard of serpentine?'
    W---    'Whoah! Whaddaya mean I look like a long string with wings?'
    W---!   'I'm one-dimensional - all length and no width or depth. Just one long super-string!'
    W~      Variable - 'My girth depends on what I've just eaten!'
"""

grammar = """
Width = 'W' (Width_4 / Width_3 / Width_2 / Width_1 / Width_n4 / Width_n3 / Width_n2 / Width_n1 / Width_0)
Width_4  = '+++!'
Width_3  = '+++'
Width_2  = '++'
Width_1  = '+'
Width_0  = ''
Width_n1 = '-'
Width_n2 = '--'
Width_n3 = '---'
Width_n4 = '---!'
"""
