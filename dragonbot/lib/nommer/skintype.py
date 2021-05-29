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
SkinType    = 'Sk' SkinType_Type SkinType_BodyPartSkinType*
SkinType_Type = SkinType_Bark / SkinType_Cellulose / SkinType_Exoskeleton / SkinType_Feathers / SkinType_Hide
              / SkinType_Skin / SkinType_Leather / SkinType_Metal / SkinType_Rock / SkinType_Scales / SkinType_Fur
              / SkinType_Crystals / SkinType_None
SkinType_Bark           = 'b'
SkinType_Cellulose      = 'c'
SkinType_Exoskeleton    = 'e'
SkinType_Feathers       = 'f'
SkinType_Hide           = 'h'
SkinType_Skin           = 'k'
SkinType_Leather        = 'l'
SkinType_Metal          = 'm'
SkinType_Rock           = 'r'
SkinType_Scales         = 's'
SkinType_Fur            = 'u'
SkinType_Crystals       = 'x'
SkinType_None           = ''
SkinType_BodyPartSkinType = SkinType_BodyPart SkinType_Type
SkinType_BodyPart   = SkinType_BodyPart_Arms / SkinType_BodyPart_Belly / SkinType_BodyPart_Head / SkinType_BodyPart_Legs
                    / SkinType_BodyPart_Neck / SkinType_BodyPart_Tail / SkinType_BodyPart_Wings
SkinType_BodyPart_Arms  = ',a'
SkinType_BodyPart_Belly = ',b'
SkinType_BodyPart_Head  = ',h'
SkinType_BodyPart_Legs  = ',l'
SkinType_BodyPart_Neck  = ',n'
SkinType_BodyPart_Tail  = ',t'
SkinType_BodyPart_Wings = ',w'
"""
