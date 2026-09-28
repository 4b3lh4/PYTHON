import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

indicador_1 = pd.read_excel("Tabela_1_1_1.xlsx", sheet_name="2022", header=None, skiprows=8, nrows=33)
indicador_1.columns = ["uf_regiao", "total", "total_branca", "total_preta_parda",
                       "homem_branca", "homem_preta_parda",
                       "mulher_branca", "mulher_preta_parda"]

regioes = ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"]

reg = indicador_1[indicador_1["uf_regiao"].isin(regioes)].copy()
reg["homens"] = (reg["homem_branca"] + reg["homem_preta_parda"]) / 2
reg["mulheres"] = (reg["mulher_branca"] + reg["mulher_preta_parda"]) / 2

reg_long = reg.melt(
    id_vars="uf_regiao",
    value_vars=["homens", "mulheres"],
    var_name="sexo",
    value_name="horas",
)
print(reg_long)

fig, ax = plt.subplots(figsize=(9, 5))
sns.barplot(data=reg_long, x="uf_regiao", y="horas", hue="sexo", ax=ax)
ax.set_title("Afazeres domésticos por região e sexo")
ax.set_xlabel("Região")
ax.set_ylabel("Horas / semana")
plt.tight_layout()
plt.savefig("grafico_atividade2.png", dpi=150)
plt.show()
