# Calculadora Científica com Tkinter

Este projeto é uma calculadora científica simples desenvolvida em Python usando a biblioteca Tkinter para a interface gráfica. A calculadora permite realizar operações matemáticas básicas e avançadas, além de plotar gráficos de funções matemáticas.

## Funcionalidades

- **Operações Básicas**: Adição, subtração, multiplicação e divisão.
- **Funções Matemáticas**: `sqrt`, `log`, `sin`, `cos`, `tan`, `pi`, `exp`.
- **Plotagem de Gráficos**: Plotagem de gráficos de funções matemáticas usando Matplotlib.
- **Limpar Entrada**: Botão para limpar a entrada.

## Requisitos

- Python 3.x
- Tkinter (geralmente incluído na instalação padrão do Python)
- NumPy
- Matplotlib

## Instalação

1. Certifique-se de ter o Python 3.x instalado em seu sistema.
2. Instale as bibliotecas necessárias usando pip:
    ```bash
    pip install numpy matplotlib
    ```

## Uso

1. Execute o script Python:
    ```bash
    python calculadora_cientifica.py
    ```
2. A interface da calculadora será exibida. Use os botões para inserir valores e operações.
3. Para plotar um gráfico, insira a função matemática na entrada e clique no botão "Plotar".

## Exemplos de calculos

1. Operações Básicas:
    Adição: 5 + 3
    Subtração: 10 - 4
    Multiplicação: 7 * 8
    Divisão: 20 / 5

2. Funções Matemáticas:
    Raiz Quadrada: math.sqrt(16) (ou simplesmente sqrt(16) se você usar o botão correspondente)
    Logaritmo Natural: math.log(10) (ou log(10))
    Seno: math.sin(math.pi/2) (ou sin(pi/2))
    Cosseno: math.cos(0) (ou cos(0))
    Tangente: math.tan(math.pi/4) (ou tan(pi/4))
    Exponencial: math.exp(1) (ou exp(1))

3. Constantes:
    Pi: math.pi (ou pi)

4. Expressões Complexas:
    Combinação de Operações: (5 + 3) * (10 - 4) / 2
    Funções Aninhadas: math.sqrt(math.sin(math.pi/4)) (ou sqrt(sin(pi/4)))

5. Plotagem de Gráficos:
    Para plotar o gráfico da função y = x**2, você pode inserir x**2 na entrada e clicar no botão “Plotar”.
