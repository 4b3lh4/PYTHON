import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

formacao_total = pd.DataFrame({
    "uf_regiao": ["Brasil"],
    "total": [25854291],
    "total_homens": [10478534],
    "total_mulheres": [15375757],
})

formacao_stem = pd.DataFrame({
    "uf_regiao": ["Brasil"],
    "total": [4149041],
    "homens": [2750422],
    "mulheres": [1398619],
})

formacao_saude = pd.DataFrame({
    "uf_regiao": ["Brasil"],
    "total": [8079707],
    "homens": [1677985],
    "mulheres": [6401723],
})

brasil = pd.DataFrame(
    {
        "area": ["Graduação (total)", "STEM", "Saúde / educação"],
        "homens": [
            formacao_total.loc[formacao_total["uf_regiao"] == "Brasil", "total_homens"].item(),
            formacao_stem.loc[formacao_stem["uf_regiao"] == "Brasil", "homens"].item(),
            formacao_saude.loc[formacao_saude["uf_regiao"] == "Brasil", "homens"].item(),
        ],
        "mulheres": [
            formacao_total.loc[formacao_total["uf_regiao"] == "Brasil", "total_mulheres"].item(),
            formacao_stem.loc[formacao_stem["uf_regiao"] == "Brasil", "mulheres"].item(),
            formacao_saude.loc[formacao_saude["uf_regiao"] == "Brasil", "mulheres"].item(),
        ],
    }
)
brasil_long = brasil.melt(id_vars="area", var_name="sexo", value_name="pessoas")
print(brasil_long)

fig, ax = plt.subplots(figsize=(9, 5))
sns.barplot(data=brasil_long, x="area", y="pessoas", hue="sexo", ax=ax)
ax.set_title("Brasil: pessoas com graduação, por área e sexo")
ax.set_xlabel("Área")
ax.set_ylabel("Pessoas")
plt.tight_layout()
plt.savefig("grafico_atividade3.png", dpi=150)
plt.show()
