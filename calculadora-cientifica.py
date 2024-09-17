from tkinter import *
import math
import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a expressão
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, END)
        entrada.insert(END, str(resultado))
    except Exception as e:
        entrada.delete(0, END)
        entrada.insert(END, "Erro")

# Função para inserir valores na entrada
def inserir_valor(valor):
    entrada.insert(END, valor)

# Função para limpar a entrada
def limpar():
    entrada.delete(0, END)

# Função para plotar gráficos
def plotar_grafico():
    try:
        x = np.linspace(-10, 10, 400)
        y = eval(entrada.get())
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gráfico')
        plt.grid(True)
        plt.show()
    except Exception as e:
        entrada.delete(0, END)
        entrada.insert(END, "Erro")

# Configuração da janela principal
janela = Tk()
janela.title("Calculadora Científica")

# Configuração da entrada
entrada = Entry(janela, width=30, font=("Arial", 14))
entrada.grid(row=0, column=0, columnspan=5)

# Botões numéricos e de operações
botoes = [
    '7', '8', '9', '/', 'sqrt',
    '4', '5', '6', '*', 'log',
    '1', '2', '3', '-', 'sin',
    '0', '.', '=', '+', 'cos',
    '(', ')', 'tan', 'pi', 'exp'
]

linha = 1
coluna = 0

for botao in botoes:
    if botao == '=':
        Button(janela, text=botao, width=5, height=2, command=calcular).grid(row=linha, column=coluna)
    elif botao == 'sqrt':
        Button(janela, text=botao, width=5, height=2, command=lambda: inserir_valor('math.sqrt(')).grid(row=linha, column=coluna)
    elif botao == 'log':
        Button(janela, text=botao, width=5, height=2, command=lambda: inserir_valor('math.log(')).grid(row=linha, column=coluna)
    elif botao == 'sin':
        Button(janela, text=botao, width=5, height=2, command=lambda: inserir_valor('math.sin(')).grid(row=linha, column=coluna)
    elif botao == 'cos':
        Button(janela, text=botao, width=5, height=2, command=lambda: inserir_valor('math.cos(')).grid(row=linha, column=coluna)
    elif botao == 'tan':
        Button(janela, text=botao, width=5, height=2, command=lambda: inserir_valor('math.tan(')).grid(row=linha, column=coluna)
    elif botao == 'pi':
        Button(janela, text=botao, width=5, height=2, command=lambda: inserir_valor('math.pi')).grid(row=linha, column=coluna)
    elif botao == 'exp':
        Button(janela, text=botao, width=5, height=2, command=lambda: inserir_valor('math.exp(')).grid(row=linha, column=coluna)
    else:
        Button(janela, text=botao, width=5, height=2, command=lambda b=botao: inserir_valor(b)).grid(row=linha, column=coluna)
    
    coluna += 1
    if coluna > 4:
        coluna = 0
        linha += 1

# Botão de limpar
Button(janela, text='C', width=5, height=2, command=limpar).grid(row=linha, column=coluna)

# Botão de plotar gráfico
Button(janela, text='Plotar', width=5, height=2, command=plotar_grafico).grid(row=linha, column=coluna+1)

janela.mainloop()
