#Código para realizar análise de sensibilidade do trabalho 1 de analise de investimentos

import matplotlib.pyplot as plt
import numpy as np



def calculaVAUE (dados, taxaJuros, variacao):
    
    taxaJuros = taxaJuros/100
    
    VAUE = []
    
    vplBase = (dados[0]) + (dados[1]*((1+taxaJuros)**dados[3] - 1)/(taxaJuros*(1+taxaJuros)**dados[3])) + (dados[2]/(1+taxaJuros)**dados[3])
    vaueBase = vplBase*(taxaJuros*(1+taxaJuros)**dados[3])/((1+taxaJuros)**dados[3] - 1)

    for k in range(3):
        dadosNovos = dados.copy()
        dadosNovos[k] = (dadosNovos[k]*(variacao/100)) + dadosNovos[k]
        
        vpl = (dadosNovos[0]) + (dadosNovos[1]*((1+taxaJuros)**dadosNovos[3] - 1)/(taxaJuros*(1+taxaJuros)**dadosNovos[3])) + (dadosNovos[2]/(1+taxaJuros)**dadosNovos[3])
        vaue = vpl*(taxaJuros*(1+taxaJuros)**dadosNovos[3])/((1+taxaJuros)**dadosNovos[3] - 1)
        print(vaue)
    
        VAUE.append((1 - (vpl*(taxaJuros*(1+taxaJuros)**dadosNovos[3])/((1+taxaJuros)**dadosNovos[3] - 1))/vaueBase)*100)
    
    return VAUE



#Taxa de juros
i = 10.89

variacoes = np.arange(-20, 21, 1)

dadosLED = [-157920,   -51795.79,  -2528.6, 23]
dadosHPS = [-16072.12, -142884.93, -733.2,  6]

vauesLED = []
vauesHPS = []

for j in range(len(variacoes)):
    vauesLED.append(calculaVAUE(dadosLED, i, variacoes[j]))
    vauesHPS.append(calculaVAUE(dadosHPS, i, variacoes[j]))

valoresInv = []
valoresCustOp = []
valoresCustRes = []

for j in range(len(vauesHPS)):
    valoresInv.append(vauesHPS[j][0])
    valoresCustOp.append(vauesHPS[j][1])
    valoresCustRes.append(vauesHPS[j][2])

# Criando a figura
plt.figure(figsize=(8, 5))

# Plotando os gráficos
plt.plot(variacoes, valoresInv, color='blue', linestyle='-', label='investimento', lw=3)  # Linha tracejada verde
plt.plot(variacoes, valoresCustOp, color='k', linestyle='-', label='custo operacional', lw=3)  # Linha pontilhada azul
plt.plot(variacoes, valoresCustRes, color='orange', linestyle='-', label='custo residual', lw=3)  # Linha com x preto

# plt.plot(i, VAUESHPSREL, color='purple', linestyle='--', label='HPS')  # Linha pontilhada roxa

# Adicionando título, rótulos e legendas
plt.title("Análise de sensibilidade do HPS", fontsize=16) 
plt.xlabel("Taxa de variação (%)", fontsize=16)
plt.ylabel("Diferença relativa VAUEs (%)", fontsize=16)
plt.tick_params(axis='both', labelsize=12)
plt.legend(fontsize=12)

# Adicionando grades
plt.grid(True)

# Definindo limites dos eixos
# plt.xlim(0, 10)
# plt.ylim(-1.5, 1.5)

# Exibindo o gráfico
plt.show()