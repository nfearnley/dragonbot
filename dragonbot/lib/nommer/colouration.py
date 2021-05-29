R"""
Colouration (C*)
  Ones colour can be very important to some, especially dragons. This tag has been expanded and revolutionised from the original Colour tag such that you can now specify the colour of almost every part of your body!
    Cag         Silver (Argent)
    Cam         Amber
    Caq         Aquamarine
    Cau         Gold (Aurum)
    Cbk         Black
    Cbl         Blue
    Cbr         Brown
    Cbs         Brass
    Cbz         Bronze
    Cch         Chromium
    Ccu         Copper (Cuprum)
    Ccy         Cyan
    Ceb         Ebony
    Cfs         Flesh (Human)
    Cgr         Green
    Cgy         Grey
    Chg         Mercury / Quicksilver (Hydrargyrum)
    Cin         Indigo
    Civ         Ivory
    Cja         Jade
    Cma         Magenta
    Cmv         Mauve
    Cor         Orange
    Cpi         Pink
    Cpu         Purple
    Crb         Rainbow (violet, indigo, blue, green, yellow, orange, red).
    Cre         Red
    Cta         Tan
    Ctu         Turquoise
    Cmb         Umber
    Cvi         Violet
    Cwh         White
    Cye         Yellow
    C~          Chameleonic. 'I can be whatever colour I want to.'
    C?          Unknown. 'Either I don't know what colour I am, or I'm just not saying!.'
    C           Colourless (ice, crystal, or invisible creatures).
  Modifiers:
    +           Put after the colour, this indicates 'light'. The more the plusses, the lighter the colour. For example, Cbl+ is Light Blue.
    -           Put after the colour, this indicates 'dark'. The more the minuses, the lighter the colour.  For example, Cbl- is Dark Blue.
    ^           Put after the colour, this indicates 'metallic'. For example, Cbl^ is Metallic Blue.
    _           Put after the colour, this indicates 'transparent' or 'gemstone'. For example, Cbl_ is Transparent Blue, Blue glass, or Sapphire.
    '           Put after the colour, this indicates 'fiery' or 'luminescent'. For example, Cbl' is Blue flame, or luminous Blue.
    %           Put after the colour, this indicates 'pearlescent' (having the look of mother of pearl). For example, Cbl% is pearlescent Blue.
    !           Put after the colour, this indicates 'glittery' or 'sparkly'. For example, Cbl! is glittery Blue.
  Further Modifiers:
    |<colour>   Put after the colour and any modifiers, this indicates 'stripes'. For example, Cbl+|au is 'light blue with gold stripes.'
    =<colour>   Put after the colour and any modifiers, this indicates 'bands'. For example, Cbl+=au is 'light blue with gold bands.'
    :<colour>   Put after the colour and any modifiers, this indicates 'spots'. For example, Cbl+:au is 'light blue with gold spots.'
    *<colour>   Put after the colour and any modifiers, this indicates 'stars'. For example, Cbl+*au is 'light blue with gold stars.'
    @<colour>   Put after the colour and any modifiers, this indicates 'mottled'. For example, Cbl+@au is 'light blue mottled with gold.'
    \<colour>   Put after the colour and any modifiers, this indicates 'iridescence', i.e. another colour that shows under a different light or viewing angle. For example, Cbl+\au is 'light blue with gold iridescence.'
    /<colour>   Mix. This goes after a colour part to indicate that one is a random mix of several colours. For example Cpu/ye/wh indicates 'I have areas of purple, yellow, and white!'
    #<colour>   Put after the colour, this indicates 'plaid'. The first colour is the main colour of the plaid with the following colours the overlays. For example, Cre#bl#bk is Red Plaid with Blue and Black.
    &<colour>   Put after the colour, this indicates 'patterned'. The first colour is the main colour with the following colours the overlays of the pattern. For example, Cgy&re&in+ is Grey patterned with Red and light Indigo.
    &1<colour>  Put after the colour, this indicates 'marble patterned'. The first colour is the main colour with the following colours the veins of the marble pattern. For example, Cre&1re-&pu is Red marble with Dark Red and Purple veins. Lovely!
    ><colour>   In transition. For those who are changing from one colour to another. For example, Cau>ag is 'gold changing to silver.'
  Body parts:
    ,a<colour>  Arms. Cbl,apu is 'Blue with Purple arms.'
    ,b<colour>  Belly or Underside. Cbl,bpu is 'Blue with a Purple belly.'
    ,c<colour>  Claws/Feet/Hands. Cbl,cpu is 'Blue with Purple claws.'
    ,e<colour>  Eyes. Cbl,epu is 'Blue with Purple eyes.'
    ,f<colour>  Fur/Hair. Cbl,fpu is 'Blue with Purple fur.'
    ,h<colour>  Head. Cbl,hpu is 'Blue with a Purple head.'
    ,k<colour>  Crest. Cbl,kpu is 'Blue with a Purple crest.'
    ,l<colour>  Legs. Cbl,lpu is 'Blue with Purple legs.'
    ,n<colour>  Neck. Cbl,npu is 'Blue with a Purple neck.'
    ,p<colour>  Points. Cbl,ppu is 'Blue with Purple points or highlights.'
    ,s<colour>  Spines. Cbl,spu is 'Blue with Purple spines.'
    ,t<colour>  Tail. Cbl,tpu is 'Blue with a Purple tail.'
    ,u<colour>  Aura. Cbl,upu is 'Blue with a Purple aura.'
    ,v<colour>  Horns/Spines. Cbl,vpu is 'Blue with Purple horns.'
    ,w<colour>  Wings. Cbl,wpu is 'Blue with Purple wings.'
  You can combine the above modifiers and body parts to make a complicated colour tag if required. For example Cre-/br,bbl+,wor_,pye,eau indicates 'I am a mix of dark red and brown with a light blue belly, transparent orange wings, yellow points, and golden eyes.'
  For plants, treat the body as the trunk or stem, legs as roots, arms as branches, wings as leaves, neck as flower stem, and head as the flower.
"""

grammar = """
Colouration = 'C'
"""
