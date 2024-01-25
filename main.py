from marshmallow import Schema, fields
from datetime import datetime
from pprint import pprint
import json

from torch import T

class AdresSchema(Schema):
    ulica = fields.Str(required=True)
    miasto = fields.Str(required=True)
    numer_domu = fields.Str(required=True)
    kod_pocztowy = fields.Str(required=True)


class UczenSchema(Schema):
    imie = fields.Str(required=True)
    nazwisko = fields.Str(required=True)
    adres = fields.Nested(AdresSchema(), required=True)
    oceny = fields.List(fields.Float, required=True)

imie = input('imie')
nazwisko = input('nazwisko')
ulica = input('ulica')
miasto = input('miasto')
numer_domu = input('numer domu')
kod_pocztowy = input('kod pocztowy')
oceny = input("oceny odzielone spacja").split()

dane_ucznia = {
    'imie' : imie,
    'nazwisko' : nazwisko,
    'adres' : {
        'ulica' : ulica,
        'miasto' : miasto,
        'numer_domu' : numer_domu,
        'kod_pocztowy' : kod_pocztowy,
    },
    'oceny' : [float(ocena) for ocena in oceny]
}


uczen_schema = UczenSchema(exclude=("id", "mail"))
uczen_json = uczen_schema.dump(dane_ucznia)

# nazwa_pliku = f"{imie}_{nazwisko}.json"
# with open(nazwa_pliku, 'w') as file:
#     file.write(uczen_json)

