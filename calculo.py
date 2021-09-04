class calculo:
    def __init__(self, salarioBruto):
        self.salarioBruto = salarioBruto

    def calculaInss(self):
        if self.salarioBruto <= 1100.00:
            return self.salarioBruto * 0.075

        elif self.salarioBruto >= 1100.01 and self.salarioBruto <= 2203.48:
            faixa1 = 1100.00 * 0.075
            faixa2 = (self.salarioBruto - 1100.00) * 0.09
            return faixa1 + faixa2

        elif self.salarioBruto >= 2203.49 and self.salarioBruto <= 3305.22:
            faixa1 = 1100.00 * 0.075
            faixa2 = (2203.48 - 1100.00) * 0.09
            faixa3 = (self.salarioBruto - 2203.48) * 0.12
            return faixa1 + faixa2 + faixa3

        elif self.salarioBruto >= 3305.23 and self.salarioBruto <= 6433.57:
            faixa1 = 1100.00 * 0.075
            faixa2 = (2203.48 - 1100.00) * 0.09
            faixa3 = (3305.23 - 2203.48) * 0.12
            faixa4 = (self.salarioBruto - 3305.23) * 0.14
            return faixa1 + faixa2 + faixa3 + faixa4

        else:
            return 751.99
