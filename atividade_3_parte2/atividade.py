import pandas as pd

t2012 = pd.read_csv("Tabela5-sem_emprego_2012.csv", sep=";", decimal=",", encoding="utf-8-sig")
t2026 = pd.read_csv("Tabela5-sem_emprego_2026.csv", sep=";", decimal=",", encoding="utf-8-sig")

t2012.columns = ["Sigla", "Código", "Estado", "Homens 2012", "Mulheres 2012"]
t2026.columns = ["Sigla", "Código", "Estado", "Homens 2026", "Mulheres 2026"]

comp = t2012.merge(t2026, on=["Sigla", "Código", "Estado"], how="inner")
print(comp.shape)
print(comp.head())

comp["Dif Homens"] = comp["Homens 2026"] - comp["Homens 2012"]
comp["Dif Mulheres"] = comp["Mulheres 2026"] - comp["Mulheres 2012"]
comp["Maioria 2012"] = comp["Mulheres 2012"].apply(lambda x: "Mulheres" if x > 50 else "Homens")
comp["Maioria 2026"] = comp["Mulheres 2026"].apply(lambda x: "Mulheres" if x > 50 else "Homens")

print(comp[["Homens 2012", "Mulheres 2012", "Homens 2026", "Mulheres 2026"]].mean())
print(comp["Maioria 2012"].value_counts())
print(comp["Maioria 2026"].value_counts())
print(comp.sort_values("Dif Mulheres", ascending=False).head(3)[["Estado", "Dif Mulheres"]])
print(comp.sort_values("Dif Mulheres").head(3)[["Estado", "Dif Mulheres"]])

t111 = pd.read_excel("Tabela_1_1_1.xlsx", sheet_name="2022", header=None, skiprows=8, nrows=33)
t111.columns = ["Estado", "Total", "Total Branca", "Total Preta ou parda",
                "Homem Branca", "Homem Preta ou parda",
                "Mulher Branca", "Mulher Preta ou parda"]

regioes = ["Brasil", "Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"]
t111 = t111[~t111["Estado"].isin(regioes)]

t111["Horas Homem"] = (t111["Homem Branca"] + t111["Homem Preta ou parda"]) / 2
t111["Horas Mulher"] = (t111["Mulher Branca"] + t111["Mulher Preta ou parda"]) / 2
t111["Dif Horas"] = t111["Horas Mulher"] - t111["Horas Homem"]

final = comp.merge(t111[["Estado", "Total", "Horas Homem", "Horas Mulher", "Dif Horas"]], on="Estado", how="inner")
final = final.rename(columns={"Total": "Horas Total 2022"}).round(2)
print(final.shape)

print(final[["Mulheres 2012", "Mulheres 2026", "Dif Mulheres", "Horas Mulher", "Dif Horas"]].corr().round(2))

final.to_csv("resultado_final.csv", sep=";", decimal=",", index=False, encoding="utf-8-sig")
final.to_excel("resultado_final.xlsx", index=False)
