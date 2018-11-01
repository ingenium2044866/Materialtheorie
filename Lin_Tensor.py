import numpy as np


class Tensor:
    """
    Lineare Spannungs- und Verzerrungstensoren.

    Input: Tensorkomponenten (Cuachy-Spannungstensor und Verzerrungstensor). Als Komponeneten:
            T11, T22, T33, T12, T13, T23. Sechs Komponenten, weil die Tensoren ymmetrisch sind.

    Output: Tensoren selbst, Kugeltensor, Deviator, Invarianten, Vergleichsgroessen (von Mises, Tresca)

    """

    def __init__(self, T11: float, T22: float, T33: float, T12: float, T13: float, T23: float, stressValues: bool):

        self.T11 = T11
        self.T22 = T22
        self.T33 = T33
        self.T12 = T12
        self.T13 = T13
        self.T23 = T23
        self.stressVaues = stressValues

    @property
    def tensor(self):
        # Spannugstensor
        return np.array([[self.T11, self.T12, self.T13],
                         [self.T12, self.T22, self.T23],
                         [self.T13, self.T23, self.T33]])

    @property
    def kugeltensor(self):
        # hydrostatischer Tensoranteil = Kugeltensor
        return 1 / 3 * np.tensordot(self.tensor, np.identity(3)) * np.identity(3)

    @property
    def deviator(self):
        # Deviatorischer Tensoranteil
        return np.subtract(self.tensor, self.kugeltensor)

    @property
    def invarianten(self):
        # Invarianten Tupel Dummy
        I = np.zeros(3)
        # Erste Invariante
        I[0] = np.trace(self.tensor)
        # Zweite Invariante
        for j in range(0, len(self.tensor)):
            for i in range(0, len(self.tensor)):
                I[1] = I[1] + 0.5 * (self.tensor[i, i] * self.tensor[j, j] - self.tensor[i, j] * self.tensor[i, j])
        # Dritte Invariante
        I[2] = np.linalg.det(self.tensor)
        return I

    @property
    def haupttensor(self):
        """
        Berechnung der Hauptspannungen aus den Invarianten.
        Alle Hauptspannungen muessen reell sein.
        		Sind zwei Hauptspannungen Null, liegt einfacher oder einachsiger Zug oder Druck vor.
        		Ist nur eine Hauptspannung Null, heisst der Spannungszustand eben oder zweiachsig.
        """
        coeffs = np.append([-1],
                           [np.multiply(self.invarianten, [1, -1, 1])])  # Koeffizienten des char. Polynoms
        # Hauptspannungen im Vekotr. Sortiert von gross nach klein
        principalStress = np.flip(np.sort(np.roots(coeffs)), axis=-1)
        # Ausgabe des Hauptspannungstensors als Dyade
        return np.diag(principalStress)

    @property
    def vonMises(self):
        if self.stressVaues:
            # Von Mises Vergleichsspannung
            return np.sqrt(3 / 2 * np.tensordot(self.deviator, self.deviator))
        else:
            # Von Mises Verzerrung. Noch zu prueffen
            return np.sqrt(2 / 3 * np.tensordot(self.deviator, self.deviator))

    @property
    def tresca(self):
        principalDifferences = [abs(self.haupttensor[0, 0] - self.haupttensor[1, 1]),
                                abs(self.haupttensor[1, 1] - self.haupttensor[2, 2]),
                                abs(self.haupttensor[2, 2] - self.haupttensor[0, 0])]
        if self.stressVaues:
            # Vergleichsspannung nach Tresca
            return max(principalDifferences)


if __name__ == '__main__':
    sxx = -2
    syy = 0
    szz = -2
    sxy = 6
    sxz = -4
    szy = 6

    tensor1 = Tensor(sxx, syy, szz, sxy, sxz, szy, True)
    s_VM = tensor1.vonMises
    tresca = tensor1.tresca

    print("Stress,vMises = %.2f MPa" % s_VM)
    print("Stress,Tresca = %.2f MPa" % tresca)
