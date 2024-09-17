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


## Como Calcular

1. Iniciar a Calculadora:
    
- Execute o script Python. A janela da calculadora será exibida.
    
    
2. Inserir Valores e Operações:
    
- Use os botões numéricos e de operações para inserir valores e expressões na entrada.
- Por exemplo, para calcular (5 + 3), clique nos botões 5, +, 3, e depois =.
    
    
3. Funções Matemáticas:

- Para usar funções como raiz quadrada, logaritmo, seno, cosseno, tangente, pi e exponencial, clique nos botões correspondentes.
- Por exemplo, para calcular a raiz quadrada de 16, clique em sqrt, insira 16 e clique em =.

    
4.  Limpar a Entrada:
    
- Para limpar a entrada, clique no botão C.


## Exemplos de Cálculos

1. Operações Básicas:

- Adição: 5 + 3 e clique em =.
- Subtração: 10 - 4 e clique em =.
- Multiplicação: 7 * 8 e clique em =.
- Divisão: 20 / 5 e clique em =.


2. Funções Matemáticas:

- Raiz Quadrada: sqrt(16) e clique em =.
- Logaritmo Natural: log(10) e clique em =.
- Seno: sin(pi/2) e clique em =.
- Cosseno: cos(0) e clique em =.
- Tangente: tan(pi/4) e clique em =.
- Exponencial: exp(1) e clique em =.


## Como Plotar Gráficos

1. Inserir a Função:
    
- Insira a função matemática na entrada. Por exemplo, para plotar (y = x^2), insira x**2.

    
2.Plotar o Gráfico:
    
- Clique no botão Plotar. Um gráfico da função será exibido.


## Exemplos de Uso do NumPy

1.  Soma de Arrays:

- Insira np.array([1, 2, 3]) + np.array([4, 5, 6]) e clique em =.


2. Seno de um Array:

- Insira np.sin(np.array([0, np.pi/2, np.pi])) e clique em =.


3. Produto de Matrizes:
    
- Insira np.dot(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])) e clique em =.

    
4. Array de Números Aleatórios:
    
- Insira np.random.rand(5) e clique em =.
