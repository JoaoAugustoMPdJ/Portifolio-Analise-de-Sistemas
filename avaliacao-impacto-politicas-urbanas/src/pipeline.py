import pandas as pd

from src.core.impact import evaluate_impact
from src.domains.seguranca import process_seguranca
from src.domains.mobilidade import process_mobilidade
from src.domains.clima import process_clima


class Pipeline:
    def __init__(self):
        pass

    def detect_domain(self, df: pd.DataFrame):
        cols = set(df.columns.str.lower())

        if {"tipo_crime", "bairro", "quantidade"} <= cols:
            return "Segurança"

        if {"fluxo_veiculos"} <= cols:
            return "Mobilidade"

        if {"temperatura", "chuva_mm"} <= cols:
            return "Clima"

        return None

    def run(
        self,
        df: pd.DataFrame,
        domain: str,
        analysis: str,
        crime_tipo: str = None,
        bairro: str = None,
    ):
        detected = self.detect_domain(df)

        if detected is None:
            return {"error": "❌ Não foi possível identificar o domínio do CSV."}

        if detected != domain:
            return {
                "error": f"⚠️ CSV identificado como '{detected}', mas o domínio selecionado foi '{domain}'."
            }

        # ==========================
        # PROCESSAMENTO POR DOMÍNIO
        # ==========================
        if domain == "Segurança":
            data = process_seguranca(df, crime_tipo, bairro)

        elif domain == "Mobilidade":
            data = process_mobilidade(df)

        elif domain == "Clima":
            data = process_clima(df)

        else:
            return None

        if data is None or len(data) < 5:
            return None

        # ==========================
        # ANÁLISE
        # ==========================
        if analysis == "Exploração":
            return data

        if analysis == "Impacto":
            return evaluate_impact(data)

        return None
