# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:50:41 2019

@author: mohammed tanveer
"""

# Import all libraries for this portion of the blog post
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline
x = np.linspace(-4, 4, num = 100)
constant = 1.0 / np.sqrt(2*np.pi)
pdf_normal_distribution = constant * np.exp((-x**2) / 2.0)
fig, ax = plt.subplots(figsize=(10, 5));
ax.plot(x, pdf_normal_distribution);
ax.set_ylim(0);
ax.set_title('Normal Distribution', size = 20);
ax.set_ylabel('Probability Density', size = 20);



def normalProbabilityDensity(x):
    constant = 1.0 / np.sqrt(2*np.pi)
    return(constant * np.exp((-x**2) / 2.0) )
adarsh_percentile, _ = quad(normalProbabilityDensity, np.NINF, 1.75)
javeed_percentile, _ = quad(normalProbabilityDensity, np.NINF, 0.8)
print('adarsh: ', adarsh_percentile)
print('javeed: ', javeed_percentile)


standard_normal_table = pd.DataFrame(data = [],
                                     index = np.round(np.arange(0, 3.5, .1),2),
                                     columns = np.round(np.arange(0.00, .1, .01), 2))


for index in standard_normal_table.index:
    for column in standard_normal_table.columns:
        z = np.round(index + column, 2)
        value, _ = quad(normalProbabilityDensity, np.NINF, z)
        standard_normal_table.loc[index, column] = value
        
        
standard_normal_table.index = standard_normal_table.index.astype(str)
standard_normal_table.columns = [str(column).ljust(4,'0') for column in standard_normal_table.columns]
