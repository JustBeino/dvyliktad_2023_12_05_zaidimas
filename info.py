"""
Užduotis: kryžiukų nuliukų žaidimas (Tic Tac Toe),

Sukurti kryžiukų/nuliukų žaidimą, kuris:
Leistų žaisti dviems žaidėjams (X ir O)
Teisingai fiksuotų vieno iš žaidėjų laimėjimą arba lygiasias ir stabdytų žaidimą
Žaidimas vyktų konsolėje, grafinio interfeiso nereikia (bet galima daryti, tada konsolės nebereikia)
Sukurtą žaidimą paskelbti github repozitorijoje,
nuorodą paskelbti teamsuose, tam skirtoje užduotyje (Assignments)

PAPILDOMAI (nebūtina):
Kad baigus žaidimą, programa neišsijungtų, o leistų pakartoti žaidimą.
Taip pat būtų galimybė išjungti programą.
Kad žaidimas skaičiuotų abiejų žaidėjų sesijos laimėjimus.
Leistų žaisti prieš kompiuterį (sukurti logiką, kaip jis elgsis)
Padaryti GUI (su tkinter, pygame, dar kažkuo)
"""
"""     main faile programa, kitur juodrasciai taisymui/pakeitimams
8 sumos laimejimui skaiciuoti
padarytas ivedimas su klaidu tikrinimu
ivedimas - keicia masyva
jei klaida, nepermeta ejimo kitam zaidejui
ejimai atskirti bruksneliais
arlaimejo - skaiciuoja sumas po ejimo
lygiosios po 'x' ejimo, nes jis turi 1 ir 9 paskutini ejima
galima butu ir po 'o' skaiciuoti lygiasias jei zaistu teisingai, ty po 8 ejimu butu
lygiosios returnai buvo su logika kad gal be ifo bus naudojama while cikle
bet kai veikia taip tai ir nekeiciau
programa baigiasi po +, laimejo,  lygiosios
is papildomu tik isjungimas padarytas
"""