HG = float(input("Note Histo-Geo/40:"))
FR = float(input("Note Français/40:"))
TICE = float(input("Note TICE/40:"))
CDP = float(input("note CDP/40:"))
LABO = float(input("note LABO/40:"))
PC = float(input("note PC/40:"))
MATH = float(input("note MATH/40:"))
EAC = float(input("note EAC/40:"))
SES = float(input("Note SES/40:"))
SVT = float(input("Note SVT/40:"))
MLG = float(input("Note MLG/40:"))
ANG = float(input("note ANGLAIS/40:"))
EPS = float(input("note EPS/40:"))
CDT = float(input("Estimation Conduite/20:"))

total = (HG+MLG+MATH+TICE+SVT+CDP+EAC+SES+PC+LABO+FR+ANG+EPS+CDT)

print('Votre totam est de:',total)
total2 = (total/27)

print('Votre Moyenne est de:',total2)