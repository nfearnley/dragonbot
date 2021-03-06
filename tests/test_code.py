from typing import List

import pytest

from parsimonious import ParseError

from dragonbot.lib.dragon import DragonCode


def parse_lines(lines: str) -> List[str]:
    raw_lines = lines.splitlines()
    stripped_lines = (line.strip() for line in raw_lines)
    filtered_lines = (line for line in stripped_lines if line)
    return list(filtered_lines)


codes = parse_lines(R"""
DC2.Dd Gf L--- W- T-- Pfhltw Skk Cbz%,e~(gr/bl=hpy,ye=alrm, re=angry) Bfl A---! Fr-- Nr M--- O H---! $-- Fc/m R+ J+++! U! I---! V++['port] Q++[tp] Tc+ E++
DC2.H Gm L- W- T- Cfs++,ebl\gy,f"blond"++ A- N"suburb" M-- O H+ $ Fj-- Ac+++ J+++ S-- U--- I-- V Q-- Tc++ E
DC2. Dw Gm L W T Phvfwlt Sks Cbk\bl-,bgy,vwh Bfl A- M- H++ $ Fc J I--# V+++ Tc+++! E-
DC2.D~ Gm L120f60t180w W T Phwalt Sks Cbk,ere' Bfl A+++! Fr+++ Nm M+ O H+ $ Fc~ R+++! Ac+++ J+ S++ U! I# V+++! Q Tc++ E++
DC2.DfGfMOA$--FjR+++S+PhfwltSksFr++"cacao"L25c45tW-TV++Cbl+,baq,evi,sag^-,w_\rbB"music"
DC2.D Gm L W- T- Phwalt Skh Cta\~+,bta+ Bfl/ic A Fr- Nn M O H--- $~ Fo R+ Ac+ J+ S? I---# V Q? Tc++[technition] E+
DC2.Dw Gm L100f Cau- A Fr++ M--xy H++ $ R+++ S-- I---##
DC2.R Gm L25f W-- T Phwat Sks Cja@ta B"Venom" A- Fr? N? M? O H $? F+++c R-- Ac+ J+ S? U* I# V+++![Necromancy] Q+++! Tc-- E---!# Df
DC2.D Gf L+ W T Phawlt Sks,hl,wl Ceb,ere Tc++(satcom) ° Omnia mutantur B"napalm"/"guacamole" A+++ Fr++ N"alpine meadows" ° Nihil interit Mr++v/ H++ $+ Fo++ R+++ Ac+ J+++! S+ I++# V+++ U*
DC2.~Dw/H Gf L49f W- Sks,wl Cgr-_,biv,ere',ceb-,veb- Bfl A--(56) Nn M- 0 H++ $ Fc R+++! Ac+ J+ S-- U! I V~ Q~ Tc+ E+
DC2.DwGmL72fW--TSklC"tiger-like"BflA(rv+)Fr++M--H+$FoR++Ac++JSI--VQ---Tc++E
DC2.D Gf A+++ L20f Fm R+++! J++ S+++ Fr+++ M+++!xx Q+++!
DC2.H^Mcf Gm L6f W T Sku Cbk,bag,ebl,cag A- Fr++"mango" Nu M(r+v+++1|2*) Ov+3 F+o R+ Ac+++ J+ S- U--- I V Q Tc++[anything but programming] E
DC2.Dw~ Gm L40f75w W- T- Sks,wl Cre-,eau Bfl A- Fr+ Nm R+ Ac++ J+ Tc++
DC2.D Gf L310f130t650w W- T4600t Phfwlt Skf Cag/bk,wbk B"anti-matter" A- Fr Ns M(v+r/) O H+ $ Fp R+++! Ac++ J- S++ U I--- V Q++ Tc+++ E+
DC2.Mfd~ Gm L~ W T Afhlt~ Sku~ Cwh\rb~ B- A Fr++^ N! M- O H++ $ F+/Fo R- Ac J+ S- U? I- V++ Q- Tc+ E+ Df+
DC2.D~ Gm L120f60t180w W T Pawl Sks Cbk,ere' Bfl A+++! Fr++ Nm M O H+ $ Fo R+++! Ac+ J-- S++ U! I# V+++! Q Tc++
DC2.H^Dw^As~ Gf L14f4w W+ T++ PhPwPaPtPl S"salamander type skin" Cbl+,wbl+_ Bfl#/"slime"/Bfl| A- Fr+ Nf Mr/Mv O+ H+++! $+ F++/Fj/Fo R+++! Ac+++ J+++! S+++! U I---!# V++ Q Tc+++![biological] E+++
DC2.~Mm{L- Sku Crb'>rb'}/Df^Et{L-- Sks Crb'.rb',wrb'_>wrb'_} Gm T+ Ben A Fr N! M- H+ $- Foj+ Ac+ U* V+++![chaos] Q++[prec] Tc++[sw] Df+++
DC2.Dw~GmLWTSksCwh|bl,ebl,wblB~A-FrM-H+++!$+F~R+++Ac++J+++!S++U!I--#V+++![???]Q+++!Tc+++!
""")

bad_codes = parse_lines(R"""
DC.DDC?(D)f+s-h++++CjSa-$+m ++d+wl+f*Fr-LEFWe++++g-U++
""")


@pytest.mark.parametrize("code", codes)
def test_codes(code):
    dc = DragonCode.parse(code)
    assert dc is not None


@pytest.mark.parametrize("code", bad_codes)
def test_bad_codes(code):
    with pytest.raises(ParseError):
        DragonCode.parse(code)
