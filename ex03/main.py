
def gera_sequencia(n):
    sequencia=[0.1]
    a=1

    for i in range(1, n+1):
        sequencia.append(a*sequencia[-1]*(1-sequencia[-1]))

    return sequencia

def calcula_media(sequencia):
    return (1/len(sequencia)) * sum(sequencia)

def calcula_desvio_padrao(sequencia, media):
    desvios = []
    tamanho = len(sequencia)

    for i in range(tamanho):
        desvios.append((sequencia[i] - media)**2)

    return (1/(tamanho-1)) * sum(desvios)


sequencia = gera_sequencia(5000)
media = calcula_media(sequencia)
desvio_padrao = calcula_desvio_padrao(sequencia, media)

print('Media:', media)
print('Desvio padrão:', desvio_padrao)
