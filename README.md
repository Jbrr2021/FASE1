# FASE1
### CURSO: ENGENHARIA DA COMPUTAÇÃO 
### PROJETO: PROJETO PARA DINÂMICA DE FLUIDOS
### NOME: JOÃO BATISTA RODRIGUES RIBEIRO
### MATRÍCULA:23308335

# ENTREGA DA FASE 1.



#### *INTRODUÇÃO*

O presente projeto busca explorar e simular numericamente a dinâmica de um corpo em queda livre considerando a resistência do ar. Através da resolução de uma equação diferencial que descreve o movimento do objeto, utilizando o método de Euler para integração numérica, este estudo visa compreender como variáveis fundamentais, como altura inicial (H), massa (m) e coeficiente de arrasto (k), influenciam o comportamento do corpo em queda.
O código desenvolvido em Python utiliza conceitos da física clássica para modelar o movimento do objeto e, posteriormente, analisar sua posição ao longo do tempo. A abordagem empregada permite a geração de diferentes cenários de queda, já que os valores de H, m e k são aleatórios a cada execução, contribuindo para uma compreensão mais abrangente dos efeitos desses parâmetros no processo de queda livre.
Neste contexto, a fase inicial deste projeto concentra-se na obtenção de valores aleatórios para H, m e k, na simulação do movimento do corpo e na apresentação dos resultados por meio de gráficos e dados tabulares. A análise destes resultados visa fornecer insights sobre a influência dos parâmetros estudados no comportamento do objeto em queda.

#### *OBJETIVO DA FASE*

Esta fase tem como propósito principal a implementação de um modelo computacional que simula a queda de um objeto considerando a resistência do ar. Os objetivos específicos são:

1.	Geração de Valores Aleatórios: Utilizar a função apropriada para gerar valores aleatórios de altura inicial (H), massa (m) e coeficiente de arrasto (k) a cada execução do código, permitindo a análise de diferentes cenários de queda.
2.	Simulação do Movimento: Implementar um algoritmo baseado no método de Euler para a resolução numérica de uma equação diferencial que descreve o movimento do objeto em queda livre, levando em conta a influência do arrasto do ar.
3.	Análise e Apresentação dos Resultados: Gerar gráficos que representem a posição do objeto em função do tempo, fornecendo uma visualização clara do comportamento do corpo durante a queda. Além disso, apresentar os dados obtidos em formato tabular para uma análise mais detalhada.
4.	Inferência sobre os Parâmetros: Analisar como as variações nos valores de H, m e k impactam o comportamento do objeto em queda livre, identificando possíveis relações entre esses parâmetros e o tempo necessário para o objeto atingir o solo.

#### *DESENVOLVIMENTO DA FASE*

O código fornecido simula a queda de um objeto com resistência do ar usando o método de Euler para integração numérica. Vou explicar o desenvolvimento do código passo a passo:

1.	Definição das Constantes:
•	São definidas as constantes como a altura inicial (H), a massa do objeto (m), o coeficiente de arrasto (k), a aceleração devido à gravidade (g) e o intervalo de tempo (delta_t) para a simulação.
2.	Condições Iniciais:
•	São inicializadas as variáveis X (posição inicial) e X_prime (velocidade inicial) de acordo com a altura inicial (H) e a velocidade inicial como zero.
3.	Simulação do Movimento:
•	Utiliza-se um loop while para simular o movimento do objeto até que ele atinja o solo (X = 0).
•	Dentro do loop, são calculadas a nova velocidade (X_prime) e a nova posição (X) do objeto em cada intervalo de tempo, utilizando a equação diferencial para a queda com resistência do ar.
•	Os valores de posição e tempo são armazenados em listas (posicoes e tempos, respectivamente) para posterior análise.
4.	Visualização dos Resultados:
•	Durante a simulação, são exibidos os valores de tempo e altura a cada período.
•	Também é criado um DataFrame (df) para armazenar os valores de tempo e altura.
•	Ao final da simulação, é gerado um gráfico mostrando a posição do objeto ao longo do tempo.
5.	Fator Aleatório:
•	Para atender aos requisitos do projeto, é necessário modificar a geração de valores de H, m e k usando a função random.uniform() para obter valores aleatórios a cada execução do código. Essa modificação garante que cada simulação utilize parâmetros distintos.


![Gráfico_1](https://github.com/Jbrr2021/FASE1/assets/87319898/b11fe34b-b4c9-4864-b365-9bc9e5b0c48d)
