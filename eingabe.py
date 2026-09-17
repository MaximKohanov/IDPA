from decimal import Decimal, InvalidOperation

from config import VORGABEWERT_KWH, MIN_VERBRAUCH_KWH, MAX_VERBRAUCH_KWH
from modelle import Tarif


def frage_jahresverbrauch() -> Decimal:
    while True:
        eingabe = input(
            f"Jahresverbrauch 2026 in kWh (0 - 12'999, Enter fuer Vorgabewert "
            f"{VORGABEWERT_KWH} kWh): "
        ).strip()

        if eingabe == "":
            return VORGABEWERT_KWH

        eingabe = eingabe.replace("'", "")
        try:
            verbrauch = Decimal(eingabe)
        except InvalidOperation:
            print("  Ungueltige Eingabe: Bitte eine Zahl eingeben.\n")
            continue

        if verbrauch < MIN_VERBRAUCH_KWH or verbrauch > MAX_VERBRAUCH_KWH:
            print(
                f"  Ungueltige Eingabe: Der Wert muss zwischen "
                f"{MIN_VERBRAUCH_KWH} und {MAX_VERBRAUCH_KWH} kWh liegen.\n"
            )
            continue

        return verbrauch


def frage_auswahl(tarife: dict[str, Tarif]) -> str:
    netzbetreiber = list(tarife.keys())
    print("\nNetzbetreiber / Tarif waehlen:")
    for i, nb in enumerate(netzbetreiber, start=1):
        print(f"  {i}) {nb} ({tarife[nb].tarifname})")
    print(f"  {len(netzbetreiber) + 1}) Beide vergleichen")

    while True:
        eingabe = input("Auswahl: ").strip()
        if eingabe == str(len(netzbetreiber) + 1):
            return "VERGLEICH"
        if eingabe.isdigit() and 1 <= int(eingabe) <= len(netzbetreiber):
            return netzbetreiber[int(eingabe) - 1]
        print("  Ungueltige Auswahl: Bitte eine der angezeigten Nummern eingeben.\n")
