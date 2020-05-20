import matplotlib.pyplot as plt
import numpy as np
idade = ('0 a 4', '5 a 9', '10 a 14', '15 a 19',
         '20 a 24', '25 a 29', '30 a 34', '35 a 39',
         '40 a 44', '45 a 49', '50 a 54', '55 a 59',
         '60 a 64', '65 a 69', '70 a 74', '75 a 79',
         '80 a 84', '85 a 89', '90 a 94', '95 a 99',
         '100 +')

x = np.arange(len(idade))

masc = np.array([7016987, 7624144, 8725413, 8558868, 8630229,
                 8460995, 7717658, 6766664, 6320568, 5692014,
                 4834995, 3902344, 3041035, 2224065, 1667372,
                 1090517, 668623, 310759, 114964, 31529, 7247])

fem = np.array([6779171, 7345231, 8441348, 8432004, 8614963,
                8643419, 8026854, 7121915, 6688796, 6141338,
                5305407, 4373877, 3468085, 2616745, 2074264,
                1472930, 998349, 508724, 211594, 66806, 16989])


fig, ax = plt.subplots(figsize=(16,8))

ax.bar(idade, fem, align='center', color = 'pink')
ax.set_xticks(x)
ax.set_xticklabels(idade, fontsize=8)
ax.set_xlabel('Faixa etaria (em anos)')
ax.set_ylabel('Populacao (em valores absolutos)')
ax.set_title('Populacao feminina por grupo de idade em 2010 (IBGE)')

plt.show()