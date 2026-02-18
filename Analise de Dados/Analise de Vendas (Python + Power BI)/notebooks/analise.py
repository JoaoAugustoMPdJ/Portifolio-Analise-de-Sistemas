import pandas as pd
import matplotlib.pyplot as plt
import os


print("=======================================")
print("PIPELINE PROFISSIONAL - SUPERSTORE")
print("=======================================")


# ===============================
# 0 CRIAR PASTA OUTPUT
# ===============================

if not os.path.exists("../output"):
    os.makedirs("../output")


# ===============================
# 1 EXTRAÇÃO
# ===============================

print("\n[1] EXTRAINDO DADOS")

df = pd.read_csv("dados/superstore.csv", encoding="latin1")

df.columns = (
    df.columns
      .str.strip()
      .str.replace(" ", "_")
      .str.lower()
)

print("Linhas:", df.shape[0])
print("Colunas:", df.shape[1])


# ===============================
# 2 LIMPEZA
# ===============================

print("\n[2] LIMPANDO DADOS")

df.drop_duplicates(inplace=True)

df.dropna(subset=["sales", "profit"], inplace=True)

print("Limpeza concluída")


# ===============================
# 3 KPI
# ===============================

print("\n[3] GERANDO KPI")

vendas_total = df["sales"].sum()
lucro_total = df["profit"].sum()
ticket_medio = df["sales"].mean()
quantidade_total = df["quantity"].sum()
margem_lucro = (lucro_total / vendas_total) * 100

print("KPIs gerados")


# ===============================
# 4 EXPORTAR DADOS LIMPOS
# ===============================

print("\n[4] EXPORTANDO CSV LIMPO")

df.to_csv("output/superstore_limpo.csv", index=False)

print("CSV exportado")


# ===============================
# 5 CRIAR GRÁFICOS
# ===============================

print("\n[5] CRIANDO GRÁFICOS")

# Vendas por Categoria
vendas_categoria = df.groupby("category")["sales"].sum().sort_values(ascending=False)

plt.figure()
vendas_categoria.plot(kind="bar")
plt.title("Vendas por Categoria")
plt.ylabel("Vendas")
plt.tight_layout()
plt.savefig("output/vendas_por_categoria.png")
plt.close()


# Lucro por Região
lucro_regiao = df.groupby("region")["profit"].sum().sort_values(ascending=False)

plt.figure()
lucro_regiao.plot(kind="bar")
plt.title("Lucro por Região")
plt.ylabel("Lucro")
plt.tight_layout()
plt.savefig("output/lucro_por_regiao.png")
plt.close()


print("Gráficos criados")


# ===============================
# 6 GERAR RELATÓRIO
# ===============================

print("\n[6] GERANDO RELATÓRIO")

with open("output/relatorio.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("RELATORIO SUPERSTORE\n\n")
    arquivo.write(f"Vendas Totais: {vendas_total:.2f}\n")
    arquivo.write(f"Lucro Total: {lucro_total:.2f}\n")
    arquivo.write(f"Ticket Medio: {ticket_medio:.2f}\n")
    arquivo.write(f"Quantidade Total Vendida: {quantidade_total}\n")
    arquivo.write(f"Margem de Lucro: {margem_lucro:.2f}%\n")

print("Relatório criado")


print("\nPIPELINE FINALIZADO COM SUCESSO")
