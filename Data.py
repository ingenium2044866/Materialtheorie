# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 22:08:19 2016

@author: 2044866
"""
import numpy as np
from Solver import solver

class Spannungen:
      def __init__(self, sigma_x = 0, sigma_y = 0, sigma_z = 0,
                   tau_xy = 0, tau_xz = 0, tau_yz = 0):
            self.sigma_x = sigma_x
            self.sigma_y = sigma_y
            self.sigma_z = sigma_z
            self.tau_xy = tau_xy
            self.tau_xz = tau_xz
            self.tau_yz = tau_yz

      def Tensor2D(self):
            sigma = np.array([[self.sigma_x,self.tau_xy],
                              [self.tau_xy,self.sigma_y]])
            return sigma
      def Tensor3D(self):
            sigma = np.array([[self.sigma_x,self.tau_xy,self.tau_xz],
                              [self.tau_xy,self.sigma_y,self.tau_yz],
                              [self.tau_xz,self.tau_yz,self.sigma_z]])
            return sigma
      def I1(self):
            return np.trace(Spannungen.Tensor3D(self))
      def I2(self):
            return      self.sigma_x*self.sigma_y + \
                        self.sigma_x*self.sigma_z + \
                        self.sigma_y*self.sigma_z - \
                        self.tau_xy**2 - self.tau_yz**2 - self.tau_xz**2
      def I3(self):
            return np.linalg.det(Spannungen.Tensor3D(self))
      def Deviator(self):
            sigma_m = 1/3*np.trace(Spannungen.Tensor3D(self))
            return Spannungen.Tensor3D(self) - sigma_m*np.eye(3)
      def Hauptspannungen(self):
            I1 = Spannungen.I1(self)
            I2 = Spannungen.I2(self)
            I3 = Spannungen.I3(self)
            return np.diag(solver.newton('cubic',1,-I1,-I2,-I3))
      def HauptDeviator(self):
          sigma_m = 1/3 * np.trace(Spannungen.Hauptspannungen(self))
          return Spannungen.Hauptspannungen(self) - sigma_m * np.eye(3)
#------------------------------------------------------------------------------
      def J1(self):
          return np.trace(Spannungen.HauptDeviator(self))
          
      def J2(self):
          return 0.5*np.trace(np.dot(Spannungen.HauptDeviator(self),\
                                   Spannungen.HauptDeviator(self)))
      def J3(self):
          return np.linalg.det(Spannungen.HauptDeviator(self))
      def vonMises(self):
            sigma = Spannungen.Hauptspannungen(self)
            s1 = sigma[0,0]
            s2 = sigma[1,1]
            s3 = sigma[2,2]
            return (0.5*((s1-s2)**2+(s2-s3)**2+(s3-s1)**2))**0.5
      def ausgabe(self,string):
          if (string == 'Tenso2d' or string == 'Tensor2D' \
              or string == 'sigma2d' or string == 'sigma2D'):
              print('Der Spannungstensor in 2D:')
              print(Spannungen.Tensor2D(self),'MPa\n')
          if (string == 'Tenso3d' or string == 'Tensor3D' \
              or string == 'sigma3d' or string == 'sigma3D'):
              print('Der Spannungstensor in 3D:')
              print(Spannungen.Tensor3D(self),'MPa\n')
          if (string == 'I1' or string == 'Invariante1'):
              print('Invariante 1 = %9.1f MPa\n'%Spannungen.I1(self))
          if (string == 'I2' or string == 'Invariante2'):
              print('Invariante 2 = %9.1f MPa\n'%Spannungen.I2(self))
          if (string == 'I3' or string == 'Invariante3'):
              print('Invariante 3 = %9.1f MPa\n'%Spannungen.I3(self))
          if (string == 'TensorHauptspannungen' or \
              string == 'Hauptspannungstensor' or \
              string == 'Haupttensor'):
              print('Tensor der Hauptspannungen :')
              print(Spannungen.Hauptspannungen(self), 'MPa\n')
          if (string == 'Hauptspannungen' or \
              string == 'hauptspannungen'):
              sigma = Spannungen.Hauptspannungen(self)
              print('sigma I   = %5.1f MPa'%sigma[0,0])
              print('sigma II  = %5.1f MPa'%sigma[1,1])
              print('sigma III = %5.1f MPa\n'%sigma[2,2])
          if (string == 'J1'):
              print('Invariante 1 des Haupttensors = %9.1f MPa\n'\
                    %Spannungen.J1(self))
          if (string == 'J2'):
              print('Invariante 2 des Haupttensors = %9.1f MPa\n'\
                    %Spannungen.J2(self))
          if (string == 'J3'):
              print('Invariante 3 des Haupttensors = %9.1f MPa\n'\
                    %Spannungen.J3(self))
          if (string == 'Mises' or string == 'mises' \
              or string == 'von Mises' or string == 'vonMises'):
                print('Fliessspannung nach von Mises = %6.1f MPa'\
                      %Spannungen.vonMises(self))
              
class Verzerrungen:
      pass



