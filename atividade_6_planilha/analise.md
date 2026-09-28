# Análise – Desocupação por sexo (2012 x 2026) e horas de cuidados (2022)

## 1. Junção das Tabelas 5
`t2012.merge(t2026, on=["Sigla", "Código", "Estado"], how="inner")` → 27 UFs nas duas tabelas, nenhuma perdida.

## 2. Comparação ano a ano
- A participação média das mulheres entre os desocupados caiu de **54,6% (2012)** para **53,0% (2026)**; a dos homens subiu de 45,4% para 47,0%.
- Mulheres eram maioria em **23 UFs** em 2012 e em **22 UFs** em 2026.
- Mudaram de maioria: **AC, AL e AP** (mulheres → homens) e **RN e TO** (homens → mulheres).
- Maiores altas na parcela feminina: **RO (+10,4 p.p.)**, **TO (+9,1)** e **SE (+6,2)**.
- Maiores quedas: **AC (−7,9 p.p.)**, **DF (−6,9)** e **GO (−6,5)**.
- Atenção: RO 2026 (67% mulheres) é um valor extremo e pode refletir amostra pequena.

## 3. Cruzamento com a Tabela 1.1.1 (2022)
Como a Tabela 1.1.1 não tem Sigla/Código, o merge foi feito pelo nome do **Estado**, depois de remover as linhas "Brasil" e das Grandes Regiões (seguindo o tratamento da Aula 2: pular o cabeçalho, renomear colunas e manter só as 27 UFs).
Horas por sexo = média simples entre "Branca" e "Preta ou parda" (a tabela não traz o total por sexo).
- Em todas as UFs as mulheres dedicam mais horas que os homens; a diferença vai de ~5,4 h (AP) a ~12,9 h (RN) por semana.
- Correlação entre horas das mulheres e % de mulheres entre os desocupados: **−0,24 (2012)** e **−0,09 (2026)** → relação fraca, sem evidência de associação clara.
- Ressalva: os anos são diferentes (2012, 2022, 2026) e correlação não implica causalidade.
