from decimal import Decimal, ROUND_HALF_UP

from modelle import Kostenaufstellung
from berechnung import vergleiche


def runde(betrag: Decimal) -> Decimal:
    return betrag.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def formatiere_chf(betrag: Decimal) -> str:
    return f"CHF {runde(betrag):,.2f}".replace(",", "'")


def zeige_kostenaufstellung(k: Kostenaufstellung) -> None:
    print(f"\n{'-' * 50}")
    print(f"Netzbetreiber:        {k.netzbetreiber}")
    print(f"Tarif:                {k.tarifname}")
    print(f"Jahresverbrauch:      {k.jahresverbrauch_kwh} kWh")
    print(f"{'-' * 50}")
    print(f"Energiekosten:        {formatiere_chf(k.energiekosten_chf):>15}")
    print(f"Netznutzung:          {formatiere_chf(k.netznutzung_chf):>15}")
    print(f"Weitere Abgaben:      {formatiere_chf(k.weitere_abgaben_chf):>15}")
    print(f"Grundtarif:           {formatiere_chf(k.grundtarif_chf):>15}")
    print(f"Messtarif:            {formatiere_chf(k.messtarif_chf):>15}")
    print(f"davon MWST-Anteil:    {formatiere_chf(k.mwst_anteil_chf):>15}")
    print(f"{'-' * 50}")
    print(f"Totalbetrag:          {formatiere_chf(k.total_chf):>15}")
    print(f"{'-' * 50}")


def zeige_vergleich(a: Kostenaufstellung, b: Kostenaufstellung) -> None:
    zeige_kostenaufstellung(a)
    zeige_kostenaufstellung(b)
    differenz, guenstiger = vergleiche(a, b)
    print(f"\nKostendifferenz:      {formatiere_chf(differenz)}")
    print(f"Guenstigerer Tarif:   {guenstiger}")
    
