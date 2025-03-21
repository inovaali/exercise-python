import math

def autorization():
    print("Qual é a sua idade?")
    age = int(input())
    if age >= 18: 
        return "Autorizado"
    else: 
        return "Não autorizado"
print(autorization())

def areaCalc():
     print("Qual é a area do circulo?")
     raio = float(input())
     PI = 3.14
     totalArea = PI * raio ** 2
     return totalArea
print(areaCalc())

def upperStr():
    print("Digite um texto:")
    text = str(input())
    if text == "iaguinho":
        return "iagao".upper()
    print(text.upper())

print(upperStr())

def replaceStr():
    print("Digite um texto e vamos mudar as letras:")
    text = str(input())
    print("Mudamos a letra a por i e ficou: ", text.replace("a", "i"))
replaceStr()

def countWords(): 
    print("Digite um texto e vamos verificar quantas letras 'e' tem:")
    text = str(input())
    print("Existe " , text.count("e"), " letras e no seu codigo")
countWords()

def coordinates():
    print("Digite a coordenada x:")
    x = int(input())
    print("Digite a coordenada y:")
    y = int(input())
    magnitude = math.sqrt(x ** 2 + y ** 2)
    print("Digite a coordenada x2:")
    x2 = int(input())
    print("Digite a coordenada y2:")
    y2 = int(input())
    distance = math.sqrt((x2 - x)**2 + (y2 - y)**2)
    return "Magnitude e: ", magnitude, " distancia e: ", distance
print(coordinates())