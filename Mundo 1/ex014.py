#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tempC = float(input('Informea  temperatura em Celsius: '))
print(f' {tempC}°C = {(tempC*9)/5+32.:2}°F')