from decimal import Decimal

from config import RAPPEN_PRO_FRANKEN, MONATE_PRO_JAHR
from modelle import Tarif, Kostenaufstellung


def berechne_kosten(tarif: Tarif, jahresverbrauch_kwh: Decimal) -> Kostenaufstellung:
    quartalsverbrauch = jahresverbrauch_kwh / Decimal("4")
    quartalspreise = (
        tarif.energie_q1_rp_kwh,
        tarif.energie_q2_rp_kwh,
        tarif.energie_q3_rp_kwh,
        tarif.energie_q4_rp_kwh,
    )
    energiekosten_chf = sum(
        (quartalsverbrauch * preis for preis in quartalspreise), Decimal("0")
    ) / RAPPEN_PRO_FRANKEN

    netznutzung_chf = (jahresverbrauch_kwh * tarif.netznutzung_rp_kwh) / RAPPEN_PRO_FRANKEN
    weitere_abgaben_chf = (jahresverbrauch_kwh * tarif.weitere_abgaben_rp_kwh) / RAPPEN_PRO_FRANKEN
    grundtarif_chf = tarif.grundtarif_chf_monat * MONATE_PRO_JAHR
    messtarif_chf = tarif.messtarif_chf_monat * MONATE_PRO_JAHR

    total_chf = (
        energiekosten_chf
        + netznutzung_chf
        + weitere_abgaben_chf
        + grundtarif_chf
        + messtarif_chf
    )

    mwst_anteil_chf = total_chf * tarif.mwst_prozent / (Decimal("100") + tarif.mwst_prozent)

    return Kostenaufstellung(
        netzbetreiber=tarif.netzbetreiber,
        tarifname=tarif.tarifname,
        jahresverbrauch_kwh=jahresverbrauch_kwh,
        energiekosten_chf=energiekosten_chf,
        netznutzung_chf=netznutzung_chf,
        weitere_abgaben_chf=weitere_abgaben_chf,
        grundtarif_chf=grundtarif_chf,
        messtarif_chf=messtarif_chf,
        mwst_anteil_chf=mwst_anteil_chf,
        total_chf=total_chf,
    )


def vergleiche(a: Kostenaufstellung, b: Kostenaufstellung) -> tuple[Decimal, str]:
    differenz = abs(a.total_chf - b.total_chf)
    guenstiger = a.netzbetreiber if a.total_chf < b.total_chf else b.netzbetreiber
    return differenz, guenstiger
