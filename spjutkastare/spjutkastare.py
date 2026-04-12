#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


class Spjutkastare:
    """
    Klassen för spjutkastare.

    Objektsattribut: namn, m (medelvärde), s (standardavvikelse)
    """
    def __init__(self, namn, m, s):
        """
        Init används för att sätta objektsvariabler.
        :param namn: string
        :param m: float -- medelvärdet för kastaren
        :param s: float -- standardavvikelsen för kastaren
        """
        self.namn = namn
        self.m = float(m)
        self.s = float(s)

    def kast(self):
        """
        Kasta en gång.
        :return: float -- normalfördelat kastresultat.
        """
        return random.normalvariate(self.m, self.s)

    def __str__(self):
        """
        Strängrepresentation: namnet på kastaren
        :return: string -- namnet på kastaren.
        """
        return self.namn

    def __lt__(self, other):
        """
        Jämförelse (less than) av self.namn.  Behövs för att sortera resultat.
        :param other: objekt att jämföra med
        :return: bool -- self<other
        """
        return self.namn < other.namn


def läs_in_från_sekvens(sekvens):
    """
    Läs in data från en sekvens, tolka ut innehållet och skapa Spjutkastare.
    :param sekvens: sekvens-objekt (iterable med strängar räcker, alltså både fil och lista med strängar)
    :return: lista av spjutkastare
    """
    ret = []  # listan som skall returneras
    for rad in sekvens:
        fields = rad.split(";")  # lista med strängarna mellan ;
        # skapar objekt och lägger till i lista (strip tar bort extra blanksteg)
        ret.append(Spjutkastare(fields[0].strip(), float(fields[1]), float(fields[2])))
    return ret


def kör_tävling(kastare):
    """
    Simulera en tävling med 6 kast per kastare. Returnera det bästa resultatet med motsvarande kastare.
    :param kastare: list[Spjutkastare] -- deltagarna i tävlingen.
    :return: (Spjutkastare, float) -- vinnaren och vinnande resultat.
    """
    ANTAL_KAST_I_TÄVLING = 6
    bästa = {}  # tom dictionary
    for k in kastare:  # lägger in alla kastare (som key) och deras hittils bästa resultat, dvs 0 (som value)
        bästa[k] = 0

    for i in range(ANTAL_KAST_I_TÄVLING):
        for k in bästa:
            bästa[k] = max(bästa[k], k.kast())

    vinnarlängd = -1
    for k in bästa:
        if bästa[k] > vinnarlängd:
            vinnarlängd = bästa[k]
            vinnare = k

    return (vinnare, vinnarlängd)


def skriv_ut_statistik(statistik):
    """
    Skriver ut resultatet av en sekvens av tävlingar.
    :param statistik: dictionary {Spjutkastare : antal vinster}
    """
    return_string = ""
    slist = []
    for s in statistik:
        slist.append((statistik[s], s))  # lägger in tuple (antal_vinster, kastare) i lista
    slist = sorted(slist, reverse=True)  # sorterar omvänt (största först)

    i = 0
    for item in slist:
        i += 1
        return_string += "{0}: {1} med {2} vinster\n".format(i, item[1], item[0])
    print(return_string)
    return return_string


def kör_flera_tävlingar(antal, spjutkastare):
    resultatsträng_för_tävlingar = ""
    statistik = {}  # skapa dictionary med alla kastare som key och 0 som value (antal vinster)
    for k in spjutkastare:
        statistik[k] = 0
    for i in range(antal):
        (vinnare, vinnarlängd) = kör_tävling(spjutkastare)
        resultatsträng_för_tävlingar += str(vinnare) + " vann med " + str(vinnarlängd) + "\n"
        statistik[vinnare] += 1
    print(resultatsträng_för_tävlingar)
    return (resultatsträng_för_tävlingar, statistik)


def main():
    """
    Själva spelets huvudfunktion.
    """
    print("Hej och välkommen till spjutkastar-simulatorn.\n\n")
    filnamn = input("Var finns spjutkastarna? ")
    fobj = open(filnamn, "r")
    spjutkastare = läs_in_från_sekvens(fobj)
    antal = int(input("Hur många tävlingar? "))
    print("\n\nDags för tävlingarna!!\n\n")
    (resultatsträng_för_tävlingar, statistik) = kör_flera_tävlingar(antal, spjutkastare)
    print("\n\nResultat\n\n")
    skriv_ut_statistik(statistik)


if __name__ == '__main__':
    main()
