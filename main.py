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

# Exibir o tempo total para atingir o solo
tempo_total = tempos[-1]
tempo_total_minutos = tempo_total / 60  # Converter para minutos
print(f"Tempo total para atingir o solo: {tempo_total:.2f} segundos ({tempo_total_minutos:.2f} minutos)")

# Criar um DataFrame com os valores de tempo e altura
data = {'Tempo (s)': tempos, 'Altura (m)': posicoes}
df = pd.DataFrame(data)

# Gerar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(tempos, posicoes, label='Posição vs. Tempo')
plt.title('Posição do Objeto ao Longo do Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.grid(True)

# Adicionar anotação para mostrar o tempo total em minutos no gráfico
plt.annotate(f'Tempo total: {tempo_total_minutos:.2f} minutos',
             xy=(tempos[-1], posicoes[-1]), xytext=(tempos[-1] / 2, H / 2),
             arrowprops=dict(arrowstyle='->', color='red'),
             fontsize=12, color='red')

# Mostrar o gráfico
plt.legend()
plt.show()






