# -*- coding: utf-8 -*-
"""
Aula: juntar as Tabelas 5 (desocupação por sexo, 2012 e 2026) e cruzar
com a Tabela 1.1.1 do IBGE (horas semanais de cuidados/afazeres, 2022).
"""
import pandas as pd

# ---------- 1. Abrir as duas Tabelas 5 ----------
t2012 = pd.read_csv("Tabela5-sem_emprego_2012.csv", sep=";", decimal=",", encoding="utf-8-sig")
t2026 = pd.read_csv("Tabela5-sem_emprego_2026.csv", sep=";", decimal=",", encoding="utf-8-sig")

t2012.columns = ["Sigla", "Código", "Estado", "Homens 2012 (%)", "Mulheres 2012 (%)"]
t2026.columns = ["Sigla", "Código", "Estado", "Homens 2026 (%)", "Mulheres 2026 (%)"]

# ---------- 2. Juntar (merge) ----------
comp = t2012.merge(t2026, on=["Sigla", "Código", "Estado"], how="inner")

# ---------- 3. Comparar ano a ano ----------
comp["Var. Homens (p.p.)"] = (comp["Homens 2026 (%)"] - comp["Homens 2012 (%)"]).round(1)
comp["Var. Mulheres (p.p.)"] = (comp["Mulheres 2026 (%)"] - comp["Mulheres 2012 (%)"]).round(1)
comp["Maioria 2012"] = comp.apply(lambda r: "Mulheres" if r["Mulheres 2012 (%)"] > r["Homens 2012 (%)"] else "Homens", axis=1)
comp["Maioria 2026"] = comp.apply(lambda r: "Mulheres" if r["Mulheres 2026 (%)"] > r["Homens 2026 (%)"] else "Homens", axis=1)

# ---------- 4. Tabela 1.1.1 (Aula 2): abas '2022', linhas 9 a 41, sem Brasil/regiões ----------
raw = pd.read_excel("Tabela_1_1_1.xlsx", sheet_name="2022", header=None, skiprows=8, nrows=33)
raw.columns = ["Estado", "Total", "Total - Branca", "Total - Preta ou parda",
               "Homem - Branca", "Homem - Preta ou parda",
               "Mulher - Branca", "Mulher - Preta ou parda"]
regioes = ["Brasil", "Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"]
t111 = raw[~raw["Estado"].isin(regioes)].copy()
t111["Estado"] = t111["Estado"].str.strip()

# Horas médias por sexo (média simples entre branca e preta/parda) e diferença M - H
t111["Horas Homem (média)"] = t111[["Homem - Branca", "Homem - Preta ou parda"]].mean(axis=1)
t111["Horas Mulher (média)"] = t111[["Mulher - Branca", "Mulher - Preta ou parda"]].mean(axis=1)
t111["Diferença horas (M - H)"] = t111["Horas Mulher (média)"] - t111["Horas Homem (média)"]

# ---------- 5. Cruzar tudo pelo nome do Estado ----------
final = comp.merge(
    t111[["Estado", "Total", "Horas Homem (média)", "Horas Mulher (média)", "Diferença horas (M - H)"]]
        .rename(columns={"Total": "Horas total 2022"}),
    on="Estado", how="inner")
final = final.round(2)

# ---------- 6. Correlações ----------
corr = final[["Mulheres 2012 (%)", "Mulheres 2026 (%)", "Var. Mulheres (p.p.)",
              "Horas Mulher (média)", "Diferença horas (M - H)"]].corr().round(3)

if __name__ == "__main__":
    print(comp.shape, t111.shape, final.shape)
    print(final.head())
    print(corr)
    final.to_csv("resultado_final.csv", sep=";", decimal=",", index=False, encoding="utf-8-sig")
