# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:16:00 2016

@author: 2044866 Mini
"""
import matplotlib.pyplot as plt
import numpy as np

class plotter:
    
    @staticmethod
    def sigma2D(sigmaI,sigmaII):
        x = np.linspace(0,sigmaI,100)
        y = np.linspace(0,sigmaII,100)
        plt.plot(x,y)
        plt.plot(sigmaI,sigmaII,marker = 'o', markersize = 10, color = 'r')
        plt.grid(True)
        plt.xlabel('$\sigma_I$ [MPa]',fontsize = 14)
        plt.ylabel('$\sigma_{II}$ [MPa]',fontsize = 14)
        plt.title('Hauptspannungen $\sigma_I, \sigma_{II}$',fontsize = 16)
        plt.savefig('sigma2D.eps')
        plt.savefig('sigma2D.png')
        plt.show()
