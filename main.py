import sys

from daten import finde_csv_pfad, lade_tarife
from berechnung import berechne_kosten
from eingabe import frage_jahresverbrauch, frage_auswahl
from anzeige import zeige_kostenaufstellung, zeige_vergleich


def main() -> None:
    print("=" * 50)
    print("  Stromkostenrechner 2026")
    print("=" * 50)

    tarife = lade_tarife(finde_csv_pfad())

    weiter = True
    while weiter:
        jahresverbrauch = frage_jahresverbrauch()
        auswahl = frage_auswahl(tarife)

        if auswahl == "VERGLEICH":
            netzbetreiber = list(tarife.keys())
            ergebnis_a = berechne_kosten(tarife[netzbetreiber[0]], jahresverbrauch)
            ergebnis_b = berechne_kosten(tarife[netzbetreiber[1]], jahresverbrauch)
            zeige_vergleich(ergebnis_a, ergebnis_b)
        else:
            ergebnis = berechne_kosten(tarife[auswahl], jahresverbrauch)
            zeige_kostenaufstellung(ergebnis)

        antwort = input("\nWeitere Berechnung durchfuehren? (j/n): ").strip().lower()
        weiter = antwort in ("j", "ja", "y", "yes")

    print("\nProgramm beendet.")

    if getattr(sys, "frozen", False):
        input("Enter druecken zum Schliessen...")


if __name__ == "__main__":
    main()
