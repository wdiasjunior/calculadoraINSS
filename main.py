import tkinter as tk
from calculo import *

def main():
    root = tk.Tk() # inicializa a GUI
    root.title("Cálculo INSS")

    def calculaINSS():
        salarioInput = e1.get()
        calculoObj = calculo(float(salarioInput))
        descontoINSS = calculoObj.calculaInss()
        result = "Desconto INSS: R$ " + str(format(descontoINSS, ".2f"))
        frame2.pack(padx=10, pady=10)
        labelResult.config(text=result) # atualiza o valor da label com o resultado

    frame1 = tk.LabelFrame(root, text="Cálculo de Desconto de INSS", padx=5, pady=10)
    frame1.pack(padx=10, pady=10)

    label = tk.Label(frame1, text="Salário Bruto")
    label.pack()

    e1 = tk.Entry(frame1, width=10) # input do salario
    e1.pack()
    e1.insert(0, 0)

    b1 = tk.Button(frame1, text="CALCULAR", command=calculaINSS)
    b1.pack(pady=10)

    frame2 = tk.LabelFrame(root, text="RESULTADO", padx=5, pady=5)

    global labelResult
    labelResult = tk.Label(frame2, text="")
    labelResult.pack(padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()
