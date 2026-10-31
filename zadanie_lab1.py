#1
#a)
one=1+2
print(type(one))
#wyjaśnienie: dodawanie

two=1+4.5
print(type(two))
#wyjaśnienie: dodawanie

three=3/2
print(type(three))
#wyjaśnienie: dzielenie zmiennoprzecinkowe

four=4/2
print(type(four))
#wyjaśnienie: dzielenie zmiennoprzecinkowe

five=3//2
print(type(five))
#wyjaśnienie: dzielenie całkowite

six=-3//2
print(type(six))
#wyjaśnienie: dzielenie całkowite

seven=11%2
print(type(seven))
#wyjaśnienie: dzielenie modulo (reszta z dzielenia)

eight=2**10
print(type(eight))
#wyjaśnienie: potęgowanie

nine=8**(1/3)
print(type(nine))
#wyjaśnienie: potęgowanie

#b)
print(int(3.0))
#wyjaśnienie: zamienia liczbę zmiennoprzecinkową na całkowitą

print(float(3))
#wyjaśnienie: zamienia liczbę całkowitą na zmiennoprzecinkową

print(float("3"))
#wyjaśnienie: zamienia tekst zawierający cyfrę na liczbę zmiennoprzecinkową

print(str(12.4))
#wyjaśnienie: zamienia wartość liczbową na łańcuchy znaków, napisy

print(bool(0))
#wyjaśnienie: umożliwia ocenę dowolnego wyrażenia (prawda lub fałsz); liczba 0 daje fałsz

#2
uczelnia='Studiuje na WSIiZ'
print(uczelnia)

#3
imię='Jan'
wiek=20
wzrost=178
print('Nazywam się' ,imię, 'i mam' ,wiek, 'lat.')
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
