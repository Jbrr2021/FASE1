import matplotlib.pyplot as plt
import pandas as pd

# Constantes
H = 2845.23  # Altura inicial em metros
m = 60.17  # Massa em kg
k = 14.23  # Coeficiente de arrasto em kg/s
g = 9.8  # Aceleração devido à gravidade em m/s²
delta_t = 0.1  # Passo de tempo em segundos

# Condições iniciais
X = H  # Posição inicial é a altura H
X_prime = 0  # Inicializando a velocidade inicial como zero

# Listas para armazenar os valores de posição e tempo
posicoes = [X]  # Inicialmente, a posição é a altura inicial H
tempos = [0]  # Tempo inicial é 0

# Loop para simular o movimento até atingir o solo (X = 0)
while X > 0:
    X_prime = X_prime - (delta_t / m) * k * X_prime - g * delta_t
    X = X + delta_t * X_prime
    posicoes.append(X)
    tempos.append(tempos[-1] + delta_t)

    # Exibir o tempo e a altura a cada período de tempo
    print(f"Tempo: {tempos[-1]:.2f} s - Altura: {X:.2f} m")

    #Criar um DataFrame com os valores de tempo e altura
    data = {'Tempo (s)': tempos, 'Altura (m)': posicoes}
    df = pd.DataFrame(data)
    # Exibir a tabela com os valores de tempo e altura
    print(df)

# Gerar o gráfico
plt.figure(figsize=(8, 6))
plt.plot(tempos, posicoes)
plt.title('Posição do Objeto ao Longo do Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.grid(True)
plt.show()




