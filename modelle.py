from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Tarif:
    tarif_id: str
    netzbetreiber: str
    tarifname: str
    energie_q1_rp_kwh: Decimal
    energie_q2_rp_kwh: Decimal
    energie_q3_rp_kwh: Decimal
    energie_q4_rp_kwh: Decimal
    netznutzung_rp_kwh: Decimal
    weitere_abgaben_rp_kwh: Decimal
    grundtarif_chf_monat: Decimal
    messtarif_chf_monat: Decimal
    mwst_prozent: Decimal


@dataclass(frozen=True)
class Kostenaufstellung:
    netzbetreiber: str
    tarifname: str
    jahresverbrauch_kwh: Decimal
    energiekosten_chf: Decimal
    netznutzung_chf: Decimal
    weitere_abgaben_chf: Decimal
    grundtarif_chf: Decimal
    messtarif_chf: Decimal
    mwst_anteil_chf: Decimal
    total_chf: Decimal
