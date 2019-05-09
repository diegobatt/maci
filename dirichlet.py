import matplotlib
import matplotlib.pyplot as plt

import numpy as np
import scipy.stats as stats

plt.style.use('seaborn')
matplotlib.rc('font', size=18)

fig = plt.figure(figsize=(12,5), frameon=False)

ax = fig.add_subplot(1, 1, 1)
ax.axis('off')
ax.set_ylim([0, 10])
ax.set_xlim([0, 10])

vlw = 5
left_bar_c='#656565'
active_bar_c='#0aca24'

""" PLOT"""
alturas = np.linspace(9, 1, 6)#[9,7,5,3,1]
lost_lens = [0.1, 0.3, 0.6, 0.5, 0.3, 0.2]
left_len = 1
for i, (altura, lost_len) in enumerate(zip(alturas, lost_lens)):
    xmin_active = (1 - left_len)
    left_len -= left_len * lost_len
    xmin = (1 - left_len)
    pi = xmin - xmin_active
    x_text_active = 10 * (xmin + xmin_active) / 2
    x_text_left = 10 * (xmin + left_len / 2)
    text_active = rf'$\pi_{i}$'
    text_left = rf'$(1-v_{i})$'
    ax.axhline(
        y=altura, linewidth=vlw, xmin=xmin_active, xmax=xmin, color=active_bar_c)
    ax.axhline(
        y=altura, linewidth=vlw, xmin=xmin, color=left_bar_c)
    if i < len(alturas) - 1:
        ax.axvline(
            x=10 * xmin,
            linewidth=2,
            ymin=alturas[i+1]/10 + 0.05,
            ymax=alturas[i]/10 - 0.05,
            color='#b32727',
            linestyle='--')
    ax.text(y=altura-0.5, x=x_text_active - 0.10, s=text_active, fontsize=10)
    x_pi = 5  + 1.8 * np.random.randn()

# plt.title(r'$\pi_i = v_i \prod_{j=0}^{i-1}(1-v_j)$')
plt.savefig('figures/stick-breaking-process', bbox_inches='tight')
plt.show()
