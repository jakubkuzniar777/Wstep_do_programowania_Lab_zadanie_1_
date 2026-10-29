#1
#a)
one=1+2
print(type(one))

two=1+4.5
print(type(two))

three=3/2
print(type(three))

four=4//2
print(type(four))

five=3//2
print(type(five))

six=-3//2
print(type(six))

seven=11%2
print(type(seven))

eight=2**10
print(type(eight))

nine=8**(1/3)
print(type(nine))

#b)
print(int(3.0))
print(float(3))
print(float("3"))
print(str(12.4))
print(bool(0))

#2
uczelnia='Studiuje na WSIiZ'
print(uczelnia)

#3
imię='Jan'
wiek=20
wzrost=178
print('Nazywam się Jan i mam' ,wiek, 'lat.')
print('Mój wzrost to' ,wzrost, 'cm.')

#4
Cena=39.99
Rabat=0.2
cena_po_rabacie=Cena * (1-Rabat)
print(round(cena_po_rabacie,2))

#5
a=float(input('Podaj długość perwszego boku: '))
b=float(input('Podaj długość drugiego boku: '))
pole=a*b
obwód=2*(a+b)
print(f'Pole prostokąta wynosi: {pole}')
print(f'Obwód prostokąta wynosi: {obwód}',)

#6
import random

print("Obliczanie kosztów podróży")
droga = random.randint(50, 500)
print(f"Wylosowana długość trasy: {droga} km")

spalanie = float(input("Podaj średnie spalanie samochodu (l/100 km): "))
cena_paliwa = float(input("Podaj aktualną cenę paliwa (zł/l): "))

zuzycie_paliwa = (droga * spalanie) / 100
koszt_podrozy = zuzycie_paliwa * cena_paliwa

print("Wynik podróży")
print(f"Przejechana droga: {droga} km")
print(f"Średnie spalanie: {spalanie} l/100 km")
print(f"Przewidywane zużycie paliwa: {zuzycie_paliwa:.2f} l")
print(f"Szacowany koszt podróży: {koszt_podrozy:.2f} zł")
