import csv
import os
from datetime import datetime

def main():
    print("Welkom bij het urenregistratiesysteem.")
    print("Vul onderstaande gegevens in:")

    naam = input("Naam: ")
    project = input("Projectnaam: ")
    datum = input("Datum (dd-mm-jjjj): ")
    uren = input("Gewerkte uren: ")

    # Controleer of het CSV-bestand al bestaat, zo niet, maak er een aan en schrijf de koppen
    if not os.path.exists("urenregistratie.csv"):
        with open("urenregistratie.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Naam", "Project", "Datum", "Uren"])

    # Schrijf de ingevoerde gegevens naar het CSV-bestand
    with open("urenregistratie.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([naam, project, datum, uren])

    print("Gegevens zijn succesvol opgeslagen in urenregistratie.csv")

if __name__ == "__main__":
    main()
