import matplotlib.pyplot as plt
import numpy as np
idade = ('0 a 4 anos', '5 a 9 anos', '10 a 14 anos', '15 a 19 anos',
         '20 a 24 anos', '25 a 29 anos', '30 a 34 anos', '35 a 39 anos',
         '40 a 44 anos', '45 a 49 anos', '50 a 54 anos', '55 a 59 anos',
         '60 a 64 anos', '65 a 69 anos', '70 a 74 anos', '75 a 79 anos',
         '80 a 84 anos', '85 a 89 anos', '90 a 94 anos', '95 a 99 anos',
         '100 anos e mais')

y = np.arange(len(idade))

masc = np.array([7016987, 7624144, 8725413, 8558868, 8630229,
                 8460995, 7717658, 6766664, 6320568, 5692014,
                 4834995, 3902344, 3041035, 2224065, 1667372,
                 1090517, 668623, 310759, 114964, 31529, 7247])

fem = np.array([6779171, 7345231, 8441348, 8432004, 8614.963,
                8643419, 8026854, 7121915, 6688796, 6141338,
                5305407, 4373877, 3468085, 2616745, 2074264,
                1472930, 998349, 508724, 211594, 66806, 16989])


fig, ax = plt.subplots(figsize=(12,6))

ax.barh(idade, masc, align='center')
ax.set_yticks(y)
ax.set_yticklabels(idade)
ax.set_xlabel('Populacao (em valores absolutos)')
ax.set_title('Populacao masculina por grupo de idade em 2010 (IBGE)')

plt.show()