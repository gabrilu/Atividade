import numpy as np

s1 = np.array([168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,242, 331, 251, 323, 106, 1055, 170])
s2 = np.array([168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,242, 331, 251, 180, 106, 1055, 200])
print(s1, s2)

# DISTANCIA EUCLIDEANA
# MÉTODO 1
sub = s1 - s2
potencia = sub * sub
soma = np.sum(potencia)
dist1 = np.sqrt(soma)
# MÉTODO 2
dist2 = np.linalg.norm(s1 - s2)
print('Distância euclideana entre as séries:', dist1)

# VALORES MÉDIOS
serie = (s1+s2)/2
medio_s1 = np.average(s1)
medio_s2 = np.average(s2)

print('Série temporal com os valores médios:', serie, '; Média s1: ', medio_s1, '; Média s2: ', medio_s2, '; Média total: ', (medio_s1+medio_s2)/2)

# VALORES MÁXIMOS E MÍNIMOS
print('Série temporal com valores máximos: ', np.maximum(s1, s2))
print('Série temporal com valores mínimos: ', np.minimum(s1, s2))
