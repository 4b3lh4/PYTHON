import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pop = pd.read_excel("CD2022_Populacao_2010_Compatibilizada_20231222.xlsx", header=None, skiprows=3, usecols=[1, 2, 3, 4, 5, 6, 7])
pop.columns = ["UF", "cod_uf", "cod_munic", "municipio", "pop_2010_sinopse", "pop_2010", "2022"]

pop = pop[pop["cod_munic"].notna() & pop["2022"].notna()]
pop["2022"] = pop["2022"].astype(int)
print(pop.shape)

pop_estado = pop.groupby("UF", as_index=False)["2022"].sum()
print(pop_estado.shape)
print(pop_estado["2022"].sum())

fig, ax = plt.subplots(figsize=(9, 8))
ordem = pop_estado.sort_values("2022", ascending=False)
sns.barplot(data=ordem, y="UF", x="2022", ax=ax, color="steelblue")
ax.set_title("População 2022 por UF")
ax.set_xlabel("Habitantes")
ax.set_ylabel("UF")
plt.tight_layout()
plt.savefig("grafico_atividade4.png", dpi=150)
plt.show()
