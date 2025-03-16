import datetime
import os


class Mitarbeiter:
    def __init__(self):
        self.krank = "Nein"
        self.in_Urlaub = "Nein"
        self.Kranktagekonto = 0
        self.genommener_urlaub = 0
        self.benutzername = None
        self.passwort = None

    def hinzufügen(self):
        """Fügt einen neuen Mitarbeiter hinzu und speichert die Daten in einer Textdatei."""
        self.Personalnummer = input("Geben Sie Ihrem neuen Mitarbeiter eine Personalnummer: ")
        self.vorname = input("Bitte geben Sie den Vornamen des Mitarbeiters ein: ")
        self.name = input("Bitte geben Sie den Namen des Mitarbeiters ein: ")
        self.geburtsdatum = input("Bitte geben Sie das Geburtsdatum des Mitarbeiters ein (YYYY-MM-DD): ")
        self.eintrittsdatum = input("Bitte geben Sie das Eintrittsdatum des Mitarbeiters ein (YYYY-MM-DD): ")
        self.benutzername = input("Benutzername für den Mitarbeiter eingeben: ")
        self.passwort = input("Passwort für den Mitarbeiter eingeben: ")
        dateiname = f"{self.Personalnummer}.txt"

        mitarbeiter_daten = {
            'Personalnummer': self.Personalnummer, 'Vorname': self.vorname, 'Name': self.name,
            'Geburtsdatum': self.geburtsdatum, 'Eintrittsdatum': self.eintrittsdatum,
            'Kranktagekonto': self.Kranktagekonto, 'Krank': self.krank,
            'genommener_urlaub': self.genommener_urlaub, 'in_Urlaub': self.in_Urlaub,
            'Benutzername': self.benutzername, 'Passwort': self.passwort
        }

        with open(dateiname, 'w+') as mitarbeiter_datei:
            aktuelles_datum = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            mitarbeiter_datei.write(f"Der Mitarbeiter wurde am {aktuelles_datum} hinzugefügt \n")
            for attribut, wert in mitarbeiter_daten.items():
                mitarbeiter_datei.write(f"{attribut}: {wert}\n")

    def urlaubsanspruch_berechnen(self):
        """Berechnet den Urlaubsanspruch eines Mitarbeiters."""
        dateiname = f"{input('Geben Sie die Personalnummer ein: ')}.txt"
        if not os.path.exists(dateiname):
            print("Mitarbeiterdatei nicht gefunden.")
            return

        schlüsselwort = "Eintrittsdatum:"
        vorname1 = "Vorname:"
        name1 = "Name:"
        geburtsdatum1 = "Geburtsdatum:"

        with open(dateiname, 'r') as data:
            for zeile in data:
                if vorname1 in zeile:
                    vorname = zeile.split(vorname1)[1].strip()
                if name1 in zeile:
                    nachname = zeile.split(name1)[1].strip()
                if geburtsdatum1 in zeile:
                    geburtsdatum = zeile.split(geburtsdatum1)[1].strip()
                if schlüsselwort in zeile:
                    eintrittsdatum = zeile.split(schlüsselwort)[1].strip()
                    startdatum_obj = datetime.datetime.strptime(eintrittsdatum, "%Y-%m-%d")
                    heutigesdatum = datetime.datetime.now()
                    tage = (heutigesdatum - startdatum_obj).days
                    urlaub_pro_tag = 2.5 / 30
                    urlaubsanspruch = int(urlaub_pro_tag * tage)
                    with open(dateiname, 'r') as file:
                        for line in file:
                            if "genommener_urlaub:" in line:
                                genommener_urlaub = int(line.split(":")[1].strip())
                                urlaubsanspruch -= genommener_urlaub
                    print(f"Der Mitarbeiter {vorname} {nachname} mit dem Geburtsdatum: {geburtsdatum}")
                    print(f"hat {urlaubsanspruch} Tage Urlaubsanspruch")

    def mitarbeiter_abrufen(self):
        """Ruft die Daten eines Mitarbeiters ab und zeigt sie an."""
        dateiname = f"{input('Geben Sie die Personalnummer des Mitarbeiters ein: ')}.txt"
        if not os.path.exists(dateiname):
            print("Mitarbeiterdatei nicht gefunden.")
            return

        with open(dateiname, 'r') as datei:
            for daten in datei:
                print(daten)

    def mitarbeiter_löschen(self):
        """Löscht die Datei eines Mitarbeiters nach Bestätigung."""
        dateiname = f"{input('Geben Sie die Personalnummer des zu löschenden Mitarbeiters ein: ')}.txt"
        if os.path.exists(dateiname):
            if input(f"Sind Sie sicher, dass Sie den Mitarbeiter mit der Personalnummer {dateiname[:-4]} löschen möchten? (ja/nein): ").lower() == 'ja':
                os.remove(dateiname)
                print(f"Der Mitarbeiter mit der Personalnummer {dateiname[:-4]} wurde gelöscht")
            else:
                print("Löschvorgang abgebrochen.")
        else:
            print(f"Der Mitarbeiter mit der Personalnummer {dateiname[:-4]} wurde nicht gefunden.")

    def krank_melden(self):
        """Meldet einen Mitarbeiter als krank und aktualisiert die Kranktage."""
        dateiname = f"{input('Geben Sie die Personalnummer des erkrankten Mitarbeiters ein: ')}.txt"
        if not os.path.exists(dateiname):
            print("Mitarbeiterdatei nicht gefunden.")
            return

        beginn_datum = input("Geben Sie das Beginn Datum in folgendem Format (YYYY-MM-DD) ein: ")
        ende_datum = input("Geben Sie das Ende Datum in folgendem Format (YYYY-MM-DD) ein: ")

        try:
            kranktage_beginn = datetime.datetime.strptime(beginn_datum, "%Y-%m-%d")
            kranktage_ende = datetime.datetime.strptime(ende_datum, "%Y-%m-%d")
        except ValueError:
            print("Falsches Datumsformat!")
            return

        krankentage = 0
        with open(dateiname, 'r') as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                if "Kranktagekonto:" in line:
                    krankentage = int(line.split(":")[1].strip())
                    lines[index] = f"Kranktagekonto: {krankentage + (kranktage_ende - kranktage_beginn).days}\n"

        with open(dateiname, 'w') as file:
            file.writelines(lines)

    def krankheit_beenden(self):
        """Beendet den Krankheitsstatus eines Mitarbeiters."""
        dateiname = f"{input('Geben Sie die Personalnummer des Mitarbeiters ein: ')}.txt"
        if not os.path.exists(dateiname):
            print("Mitarbeiterdatei nicht gefunden.")
            return

        with open(dateiname, 'r') as file:
            lines = file.readlines()

        with open(dateiname, 'w') as file:
            for line in lines:
                if "Krank: Ja" in line:
                    line = line.replace("Krank: Ja", "Krank: Nein")
                file.write(line)

        print(f"Der Krankheitsstatus des Mitarbeiters mit der Personalnummer {dateiname[:-4]} wurde auf 'Krank: Nein' geändert.")

    def ist_momentan_krank(self):
        """Überprüft, ob ein Mitarbeiter momentan krank ist."""
        dateiname = f"{input('Geben Sie die Personalnummer des Mitarbeiters ein: ')}.txt"
        if not os.path.exists(dateiname):
            print("Mitarbeiterdatei nicht gefunden.")
            return

        with open(dateiname, 'r') as file:
            for line in file:
                if "Krank: Ja" in line:
                    print(f"Der Mitarbeiter mit der Personalnummer {dateiname[:-4]} ist momentan krank.")
                    return

        print(f"Der Mitarbeiter mit der Personalnummer {dateiname[:-4]} ist momentan nicht krank.")

    def krankheitstage_abrufen(self):
        """Ruft die Anzahl der Kranktage eines Mitarbeiters ab."""
        dateiname = f"{input('Geben Sie die Personalnummer des Mitarbeiters ein: ')}.txt"
        if not os.path.exists(dateiname):
            print("Mitarbeiterdatei nicht gefunden.")
            return

        krankentage = 0
        with open(dateiname, 'r') as file:
            for line in file:
                if "Kranktagekonto:" in line:
                    krankentage = int(line.split(":")[1].strip())
                    break

        print(f"Der Mitarbeiter mit der Personalnummer {dateiname[:-4]} war insgesamt {krankentage} Tage krank.")
        return krankentage

    def urlaub_melden(self):
        """Meldet einen Mitarbeiter als im Urlaub und aktualisiert die Urlaubstage."""
        dateiname = f"{input('Geben Sie die Personalnummer des Mitarbeiters ein: ')}.txt"
        if not os.path.exists(dateiname):
            print("Mitarbeiterdatei nicht gefunden.")
            return

        beginn_datum = input("Geben Sie das Beginn Datum in folgendem Format (YYYY-MM-DD) ein: ")
        ende_datum = input("Geben Sie das Ende Datum in folgendem Format (YYYY-MM-DD) ein: ")

        try:
            urlaub_beginn = datetime.datetime.strptime(beginn_datum, "%Y-%m-%d")
            urlaub_ende = datetime.datetime.strptime(ende_datum, "%Y-%m-%d")
        except ValueError:
            print("Falsches Datumsformat!")
            return

        urlaubstage = 0
        with open(dateiname, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if "genommener_urlaub:" in line:
                    urlaubstage = int(line.split(":")[1].strip())
                    urlaubstage_berechnung = (urlaub_ende - urlaub_beginn).days
                    genommener_urlaub = urlaubstage + urlaubstage_berechnung
                    line = f"genommener_urlaub: {genommener_urlaub}\n"

        with open(dateiname, 'w') as file:
            file.writelines(lines)

    def login(self):
        """Ermöglicht einem Mitarbeiter, sich einzuloggen."""
        benutzername = input("Benutzername eingeben: ")
        passwort = input("Passwort eingeben: ")

        if self.benutzername == benutzername und self.passwort == passwort:
            print("Erfolgreich eingeloggt.")
            # Hier können wir später die Funktionen hinzufügen, die diese Mitarbeiter ausführen können.
        else:
            print("Falscher Benutzername oder Passwort. Zugriff verweigert.")
