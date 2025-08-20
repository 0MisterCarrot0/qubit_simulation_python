# qubit.py
import numpy as np

class Qubit :
    def __init__(self, alpha, beta):
        '''
        alpha = proba de |0>
        beta = proba de |1>
        '''
        norm = np.sqrt(abs(alpha)**2 + abs(beta)**2)
        if norm > 1:
            alpha /= norm
            beta /= norm
        self.alpha = alpha
        self.beta = beta
    
    def state(self):
        return np.array([[self.alpha], [self.beta]])

    def __repr__(self, round_values=False):
        if round_values:
            a = round(self.alpha.real, 2) + round(self.alpha.imag, 2)*1j
            b = round(self.beta.real, 2) + round(self.beta.imag, 2)*1j
        else:
            a = self.alpha
            b = self.beta
        return f"|ψ> = {a}|0> + {b}|1>"

    def proba(self, round_values=False):
        if round_values:
            return {
                "0" : round(abs(self.alpha), 2),
                "1" : round(abs(self.beta), 2)
            }
        return {
            "0" : abs(self.alpha),
            "1" : abs(self.beta)
        }

    def measure(self, round_values=False):
        import random
        p0, _ = self.proba(round_values).values()
        return 0 if random.random() <= p0 else 1