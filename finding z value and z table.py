# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:43:51 2019

@author: mohammed tanveer
"""

from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import scipy.stats as stats
import pandas as pd


# This is needed for z table formatting
pd.options.display.float_format = '{:<.4f}'.format

%matplotlib inline
#for SAT score

mu, sigma = 1000, 150 # mean and standard deviation
s = np.random.normal(mu, sigma, 100000)

h = sorted(s)

fit = stats.norm.pdf(h, np.mean(h), np.std(h))

fig, ax = plt.subplots(figsize=(10, 5), frameon=False);
ax.plot(h, fit, 'k', linewidth=1.2);
ax.set_ylim(bottom=0);
ax.set_xlim(400, 1600);

df = pd.DataFrame(list(zip(h, fit)), columns = ['score', 'integral'])
df[(df['score'] >= 1119.90) & (df['score'] <= 1120.10) ].values.tolist()

# Make the shaded region
verts = [(1119.90, 0)] + df[(df['score'] >= 1119.90) & (df['score'] <= 1120.10) ].values.tolist() + [(1120.1, 0)]
poly = Polygon(verts, facecolor='green', edgecolor='r', alpha = 1, linewidth = 1.2, linestyle = '-')
ax.add_patch(poly);
plt.xticks(fontsize = 22)
ax.set_xlabel('SAT Score (JAVEED)', fontsize = 28)

ax.set_frame_on(False)
ax.axhline(0, c = 'k', linewidth = 3)
ax.get_yaxis().set_visible(False)
ax.text(1120,.0005, '1120', horizontalalignment='center', fontsize=22,
            bbox={'facecolor':'white', 'edgecolor':'black', 'pad':5});
plt.tight_layout()
fig.savefig('SAT_JAVEED.png', dpi = 900)


#for ACT cacualation

mu, sigma = 20, 4 # mean and standard deviation
s = np.random.normal(mu, sigma, 100000)
h = sorted(s)
fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed

fig, ax = plt.subplots(figsize=(10, 5), frameon=False);
ax.plot(h, fit, 'k', linewidth=1.2);
ax.set_ylim(bottom=0);
ax.set_xlim(4, 36);

df = pd.DataFrame(list(zip(h, fit)), columns = ['score', 'integral'])
df[(df['score'] >= 20.99733333333333) & (df['score'] <= 21.002666666666666) ].values.tolist()

# Make the shaded region
ix = np.linspace(21, 21, num = 1)
verts = [(20.99733333333333, 0)] + df[(df['score'] >= 20.99733333333333) & (df['score'] <= 21.002666666666666) ].values.tolist() + [(21.002666666666666, 0)]
poly = Polygon(verts, facecolor='green', edgecolor='b', alpha = 1, linewidth = 1.2, linestyle = '-')
ax.add_patch(poly);
ax.set_xticks(list(range(4, 40, 4)))
plt.xticks(fontsize = 22)
ax.set_xlabel('ACT Score (Adarsh)', fontsize = 27)

ax.set_frame_on(False)
ax.axhline(0, c = 'k', linewidth = 3)
ax.get_yaxis().set_visible(False)

ax.text(21,.015, '21', horizontalalignment='center', fontsize=22,
            bbox={'facecolor':'white', 'edgecolor':'black', 'pad':5});
plt.tight_layout()
fig.savefig('ACT_Adarsh.png', dpi = 900)






