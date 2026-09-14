import zipfile
import pandas as pd


df = pd.read_excel("CD2022_Populacao_2010_Compatibilizada_20231222.xlsx", header=2)
df = df[df["UF"].str.len() == 2]

df = df.rename(columns={
    "População 2010 (Alterações de Limites até 2022)1": "POP_2010",
    "População Censo 2022": "POP_2022"
})


df_estados = (
    df.groupby("UF")[["POP_2010", "POP_2022"]]
    .sum()
    .reset_index()
)
df_estados["CRESCIMENTO"] = df_estados["POP_2022"] - df_estados["POP_2010"]
df_estados = df_estados.sort_values(by="CRESCIMENTO", ascending=False)
df_estados.to_csv(r"populacao_estados.csv", sep=";", index=False)


df_municipios = df[["UF", "NOME DO MUNICÍPIO", "POP_2010", "POP_2022"]].copy()
df_municipios["CRESCIMENTO"] = df_municipios["POP_2022"] - df_municipios["POP_2010"]
df_municipios = df_municipios.sort_values(by="CRESCIMENTO", ascending=False)
df_municipios.to_csv(r"populacao_municipios.csv", sep=";", index=False)


arquivos = [
    "CD2022_Populacao_2010_Compatibilizada_20231222.xlsx",
    "populacao_estados.csv",
    "populacao_municipios.csv"
]

with zipfile.ZipFile("projeto.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for arq in arquivos:
        z.write(arq)


