# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 09:21:56 2016

@author: Sergej
"""
print(chr(27) + "[2J\n")
from Data import Spannungen
from Plotts import plotter
if __name__ == '__main__':
    sigma_x = 100
    sigma_y = 500
    sigma_z = 100
    tau_xy = 100
    tau_xz = 300
    tau_yz = 100
    

    
    S = Spannungen (sigma_x,sigma_y,sigma_z,tau_xy,tau_xz,tau_yz)
    
    sigma = S.Hauptspannungen()
    
    S.ausgabe('sigma2d')
    S.ausgabe('sigma3d')
    S.ausgabe('I1')
    S.ausgabe('I2')
    S.ausgabe('I3')
    S.ausgabe('J1')
    S.ausgabe('J2')
    S.ausgabe('J3')
    S.ausgabe('Haupttensor')
    S.ausgabe('hauptspannungen')
    S.ausgabe('mises')
    plotter.sigma2D(sigma[0,0],sigma[1,1])
    