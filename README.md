1. Utwórz branch `feature/zadanie`. Na nim zaimplementuj wszystkie poniższe punkty i utwórz PR (pozostawiając nauczycielowi zmergowanie zmian)
2. Skonfiguruj plik .gitignore tak aby katalog VENV został zignorowany przez gita oraz przygotuj plik requirements.txt który będzie zawierał listę użytych bibliotek.
3. Utwórz wirtualne środowisko w którym dołączysz bibliotekę marshmallow służącą do serializacji i deserializacji danych
4. Napisz skrypt w którym zdefiniujesz model ucznia. Model ten powinien zawierać imię, nazwisko, **model zagnieżdżony** z danymi adresowymi oraz listę ocen
5. Skrypt powinien poprosić o powyższe dane, następnie utworzyć plik o nazwie imie_nazwisko.json zawierający uzyskane dane w formacie JSONa