import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Os dados utilizados referem-se à granulometria (tamanho de partícula) de um testemunho marinho;
# Valores negativos em y indicam a profundidade da coluna estratigráfica em metros, sendo y = 0 o topo do testemunho (início do assoalho oceânico);
# Valores em x indicam o tamanho de partícula na escala phi, na qual maiores valores de phi evidenciam partículas menores;
# Valores em z indicam a porcentagem (ou volume) de determinada fração (y) em função da profundidade (x).
# Valor em branco no plot refere-se a uma amostra de porcentagem muito acima de 14.5% (outlier)

x = pd.read_csv("C:\\Users\\xavie\\Desktop\\fracao.csv", header = 0) # Carregando csv contendo os valores das frações granulométricas (phi)
y = pd.read_csv("C:\\Users\\xavie\\Desktop\\prof.csv", header = 0) # Carregando csv contendo os valores de profundidade do testemunho (m)
z = pd.read_csv("C:\\Users\\xavie\\Desktop\\granulometria.csv", header = 0) # Carregando os valores de porcentagem por peso de peneiramento (Wt. %)
# Obs: Modificar o diretório dos arquivos

X, Y = np.meshgrid(x, y*(-1)) # Agrupando x,y e multiplicando y por (-1) para orientar a coluna estratigráfica do topo para a base
plt.contourf(X, Y, z, np.arange(0, 14.5, 1), cmap='viridis') # Determinando um range entre 0 - 14.5%
plt.title('Particle Size Contour Plot')
plt.xlabel('phi')
plt.ylabel('Depth (m)')
clb = plt.colorbar()
clb.ax.set_title('Wt. (%)')
plt.show()
