import csv
import os
import sys
from decimal import Decimal

from config import CSV_DATEINAME
from modelle import Tarif


def _zu_decimal(wert: str) -> Decimal:
    return Decimal(wert.strip())


def finde_csv_pfad() -> str:
    if getattr(sys, "frozen", False):
        anwendungsverzeichnis = os.path.dirname(os.path.abspath(sys.executable))
    else:
        anwendungsverzeichnis = os.path.dirname(os.path.abspath(__file__))

    pfad = os.path.join(anwendungsverzeichnis, CSV_DATEINAME)
    if not os.path.isfile(pfad):
        print(f"Fehler: Tarifdatei '{CSV_DATEINAME}' wurde nicht gefunden.")
        print(f"Erwarteter Pfad: {pfad}")
        input("Enter zum Beenden druecken...")
        sys.exit(1)
    return pfad


def lade_tarife(pfad: str) -> dict[str, Tarif]:
    tarife: dict[str, Tarif] = {}
    with open(pfad, encoding="utf-8-sig", newline="") as datei:
        reader = csv.DictReader(datei, delimiter=";")
        for zeile in reader:
            tarif = Tarif(
                tarif_id=zeile["tarif_id"],
                netzbetreiber=zeile["netzbetreiber"],
                tarifname=zeile["tarifname"],
                energie_q1_rp_kwh=_zu_decimal(zeile["energie_q1_rp_kwh"]),
                energie_q2_rp_kwh=_zu_decimal(zeile["energie_q2_rp_kwh"]),
                energie_q3_rp_kwh=_zu_decimal(zeile["energie_q3_rp_kwh"]),
                energie_q4_rp_kwh=_zu_decimal(zeile["energie_q4_rp_kwh"]),
                netznutzung_rp_kwh=_zu_decimal(zeile["netznutzung_rp_kwh"]),
                weitere_abgaben_rp_kwh=_zu_decimal(zeile["weitere_abgaben_rp_kwh"]),
                grundtarif_chf_monat=_zu_decimal(zeile["grundtarif_chf_monat"]),
                messtarif_chf_monat=_zu_decimal(zeile["messtarif_chf_monat"]),
                mwst_prozent=_zu_decimal(zeile["mwst_prozent"]),
            )
            tarife[tarif.netzbetreiber] = tarif
    return tarife
