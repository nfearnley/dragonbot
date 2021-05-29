"""
Skin-Type (Sk*)
  What one feels like to the touch is something which can often be nice to know. You can let others know what they're in for by using this tag. If your skin type is what would be considered usual for your species you don't have to use this tag, but what is usual for dragons?
    Skb        Bark.
    Skc        Cellulose.
    Ske        Exoskeleton (shells, Calcium Carbonate).
    Skf        Feathers.
    Skh        Hide.
    Skk        Skin.
    Skl        Leather.
    Skm        Metal.
    Skr        Rock (Stone).
    Sks        Scales.
    Sku        Fur.
    Skx        Crystals.
    Sk         None (just bones).
  Body parts:
    ,a<type>   Arms. Sks,ak is 'My body is scaly, but I have skin on my arms.'
    ,b<type>   Belly. Sks,bm is 'My body is scaly, but I have a metal underside.'
    ,h<type>   Head. Sku,hf is 'My body is furry, and I have a head of feathers.'
    ,l<type>   Legs. Skr,lh is 'My body is rocky, and I have legs of hide.'
    ,n<type>   Neck. Skb,nc is 'My body (trunk) has bark, but my neck (flower stem) is cellulose.'
    ,t<type>   Tail. Sks,th is 'My body is scaly, but my tail has hide.'
    ,w<type>   Wings. Sks,wl is 'My body is scaly, and I have leathery wings.'
  For plants, treat the body as the trunk or stem, legs as roots, arms as branches, wings as leaves, neck as flower stem, and head as the flower.
"""

grammar = """
SkinType = 'Sk'
"""
