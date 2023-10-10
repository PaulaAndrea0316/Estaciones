def centigrados_a_farenheit (centigrados):
    conversion = ((centigrados * 9)/5) + 32
    return conversion

centigrados = float(input('Ingrese grados centigrados: '))
farenheit = centigrados_a_farenheit(centigrados)
print(f'Grados Farenheit: {farenheit} ')