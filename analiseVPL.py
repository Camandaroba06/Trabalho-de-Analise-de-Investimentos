import matplotlib.pyplot as plt
import pandas as pd

# Criando o DataFrame com os dados fornecidos
dados = {
    "Taxa": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 64.62, 65, 66, 68, 70, 72, 74],
    "VPL LED": [-2839304.63, -1556092.49, -1077788.61, -838287.17, -696048.14, -602333.86, -536176.87, -487105.53, -449320.31, -419358.02, -395028.67, -374883.23, -357926.99, -343455.76, -330957.82, -320052.78, -310452.18, -301933.43, -294322.07, -287479.39, -281293.75, -275674.27, -270546.16, -265847.36, -261525.87, -257537.83, -253845.93, -250418.28, -247227.41, -244249.55, -241464.03, -238852.76, -238074.75, -237607.42, -236399.86, -234091.33, -231914.79, -229859.21, -227914.78],
    "VPL HPS": [-6820201.86, -3635318.93, -2436862.29, -1830724.79, -1466699.57, -1224036.76, -1050742.12, -920802.59, -819765.38, -738958.75, -672864.32, -617803.22, -571228.52, -531321.04, -496746.70, -466504.99, -439830.83, -416129.15, -394930.20, -375858.19, -358608.93, -342933.53, -328626.43, -315516.33, -303459.34, -292333.73, -282035.81, -272476.72, -263579.86, -255278.84, -247515.87, -240240.37, -238073.07, -236771.32, -233407.91, -226979.28, -220919.77, -215198.54, -209788.05],
    "VPL LED-HPS": [4240930.71, 2188280.31, 1415957.08, 1025373.24, 790822.69, 634485.27, 522852.21, 439158.91, 374091.00, 322059.81, 279508.92, 244067.43, 214093.95, 188416.08, 166174.07, 146723.16, 129570.27, 114331.96, 100705.49, 88448.72, 77365.62, 67295.83, 58106.90, 49688.44, 41947.76, 34806.45, 28197.69, 22064.24, 16356.77, 11032.53, 6054.27, 1389.45, 0, -834.51, -2990.56, -7111.00, -10994.21, -14660.06, -18126.25]
}

df = pd.DataFrame(dados)

# Criando o gráfico com matplotlib
plt.figure(figsize=(10, 6))  # Define o tamanho da figura

# Plotando as linhas com marcadores
plt.plot(df["Taxa"], df["VPL LED"], linestyle='-', label="VPL LED", lw=3, )
plt.plot(df["Taxa"], df["VPL HPS"], linestyle='-', label="VPL HPS", lw=3)
plt.plot(df["Taxa"], df["VPL LED-HPS"], linestyle='-', label="Diferença LED - HPS", lw=3)

plt.scatter(64.621,0, color='red', s=50, label='TIR', zorder = 2)

plt.text(64.621, 0+1, '(64.621%, 0)   ', fontsize=12, color='red', ha='right')

# Personalizando o layout
plt.title("Evolução do VPL com a Taxa de Desconto", fontsize=16)
plt.xlabel("Taxa de Desconto (%)", fontsize=14)
plt.ylabel("Valor Presente Líquido (R$)", fontsize=14)

# Adicionando grade
plt.grid(True, linestyle='--', alpha=0.6)

# Adicionando legenda
plt.legend(fontsize=12)

# Ajustando o layout para evitar cortes
plt.tight_layout()

# Exibindo o gráfico
plt.show()