from mitarbeiter import Mitarbeiter

class Berechtigter(Mitarbeiter):
    def __init__(self, benutzername, passwort):
        super().__init__()
        self.benutzername = benutzername
        self.passwort = passwort

    def login(self):
        """Methode für den Login eines berechtigten Benutzers."""
        benutzername = input("Benutzername eingeben: ")
        passwort = input("Passwort eingeben: ")

        if benutzername == self.benutzername und passwort == self.passwort:
            print("Erfolgreich eingeloggt als berechtigter Benutzer.")
            self.berechtigter_menue()
        else:
            print("Falscher Benutzername oder Passwort. Zugriff verweigert.")

    def berechtigter_menue(self):
        """Menü für berechtigte Benutzer."""
        while True:
            print("\nBerechtigter Menü:")
            print("1. Urlaubsanspruch berechnen")
            print("2. Mitarbeiter abrufen")
            print("3. Krankmeldung")
            print("4. Krankheitsstatus beenden")
            print("5. Prüfen ob Mitarbeiter krank ist")
            print("6. Krankheitstage abrufen")
            print("7. Urlaubmeldung")
            print("8. Mitarbeiter hinzufügen")
            print("9. Beenden")

            wahl = input("Wählen Sie eine Option (1-9): ")

            if wahl == '1':
                self.urlaubsanspruch_berechnen()
            elif wahl == '2':
                self.mitarbeiter_abrufen()
            elif wahl == '3':
                self.krank_melden()
            elif wahl == '4':
                self.krankheit_beenden()
            elif wahl == '5':
                self.ist_momentan_krank()
            elif wahl == '6':
                self.krankheitstage_abrufen()
            elif wahl == '7':
                self.urlaub_melden()
            elif wahl == '8':
                self.mitarbeiter_hinzufügen()
            elif wahl == '9':
                print("Berechtigter-Modus beendet.")
                break
            else:
                print("Ungültige Auswahl. Bitte wählen Sie eine Option von 1 bis 9.")

    def mitarbeiter_hinzufügen(self):
        """Fügt einen neuen Mitarbeiter hinzu und erstellt Zugangsdaten."""
        mitarbeiter = Mitarbeiter()
        mitarbeiter.hinzufügen()
        mitarbeiter.benutzername = input("Benutzername für den Mitarbeiter eingeben: ")
        mitarbeiter.passwort = input("Passwort für den Mitarbeiter eingeben: ")
        mitarbeiter.hinzufügen()  # Speichert die Zugangsdaten in der Datei
        print(f"Mitarbeiter {mitarbeiter.vorname} {mitarbeiter.name} erfolgreich hinzugefügt.")


class Admin(Berechtigter):
    def __init__(self):
        super().__init__("admin", "pass123")
        self.berechtigte_benutzer = {}

    def login(self):
        """Methode für den Login eines Admins."""
        benutzername = input("Benutzername eingeben: ")
        passwort = input("Passwort eingeben: ")

        if benutzername == self.benutzername und passwort == self.passwort:
            print("Erfolgreich eingeloggt als Admin.")
            self.admin_menue()
        else:
            print("Falscher Benutzername oder Passwort. Zugriff verweigert.")

    def admin_menue(self):
        """Menü für Admin-Benutzer."""
        while True:
            print("\nAdmin Menü:")
            print("1. Mitarbeiter hinzufügen")
            print("2. Mitarbeiter löschen")
            print("3. Berechtigten Benutzer hinzufügen")
            print("4. Beenden")

            wahl = input("Wählen Sie eine Option (1-4): ")

            if wahl == '1':
                self.mitarbeiter_hinzufügen()
            elif wahl == '2':
                self.mitarbeiter_löschen()
            elif wahl == '3':
                self.berechtigter_hinzufügen()
            elif wahl == '4':
                print("Admin-Modus beendet.")
                break
            else:
                print("Ungültige Auswahl. Bitte wählen Sie eine Option von 1 bis 4.")

    def mitarbeiter_hinzufügen(self):
        """Fügt einen neuen Mitarbeiter hinzu und erstellt Zugangsdaten."""
        mitarbeiter = Mitarbeiter()
        mitarbeiter.hinzufügen()
        mitarbeiter.benutzername = input("Benutzername für den Mitarbeiter eingeben: ")
        mitarbeiter.passwort = input("Passwort für den Mitarbeiter eingeben: ")
        mitarbeiter.hinzufügen()  # Speichert die Zugangsdaten in der Datei
        print(f"Mitarbeiter {mitarbeiter.vorname} {mitarbeiter.name} erfolgreich hinzugefügt.")
        self.admin_menue()

    def berechtigter_hinzufügen(self):
        """Fügt einen neuen berechtigten Benutzer hinzu."""
        benutzername = input("Benutzername für den berechtigten Benutzer eingeben: ")
        passwort = input("Passwort für den berechtigten Benutzer eingeben: ")
        self.berechtigte_benutzer[benutzername] = passwort
        print("Berechtigter Benutzer hinzugefügt.")


if __name__ == "__main__":
    print("Willkommen! Sind Sie ein Admin oder ein berechtigter Benutzer?")
    rolle = input("Admin/Benutzer: ").lower()

    if rolle == 'admin':
        admin = Admin()
        admin.login()
    elif rolle == 'benutzer':
        benutzername = input("Benutzername eingeben: ")
        passwort = input("Passwort eingeben: ")
        berechtigter = Admin()
        if berechtigter.berechtigte_benutzer.get(benutzername) == passwort:
            print("Erfolgreich eingeloggt.")
            berechtigter.berechtigter_menue()
        else:
            print("Falscher Benutzername oder Passwort. Zugriff verweigert.")
    else:
        print("Ungültige Eingabe. Bitte wählen Sie zwischen 'Admin' und 'Benutzer'.")
