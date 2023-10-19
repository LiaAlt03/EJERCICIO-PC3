def validar_tarjeta(num_tarjeta):
#Se invierte el numero y se extraen los digitos de 2 en 2
    digitos=[int(digito) for digito in num_tarjeta[-2::-2]]
#Se multiplica por 2 a cada numero que se extrajo
    digitos=[2*int(digito) for digito in digitos]
#Se suman los digitos de los numeros multiplicados anteriormente
    digitos+=[int(digito) for digito in num_tarjeta[-1::-2]]
#Se calcula la suma total de todos los digitos
    suma_total=sum([int(digito)//10+int(digito)%10 for digito in digitos])
#La suma total debe ser divisible por 10 para que la tarjeta sea valida
    return suma_total%10==0

def definir_tipo_tarjeta(num_tarjeta):
#Verificamos la longitud del numero ingresado y que coincidan las condiciones de los primeros numeros
    if len(num_tarjeta)==15 and (num_tarjeta[0:2]=="34" or num_tarjeta[0:2]=="37"):
        return "AMEX"
    elif len(num_tarjeta)==16 and (num_tarjeta[0:2] in ("51","52","53","54","55")):
        return "MASTERCARD"
    elif (len(num_tarjeta)==13 or len(num_tarjeta)==16) and num_tarjeta[0]=="4":
        return "VISA"
    else:
        return "INVALID"

def main():
    num_tarjeta=input("Digite el numero de la tarjeta: ")
    if validar_tarjeta(num_tarjeta):
        tipo_tarjeta=definir_tipo_tarjeta(num_tarjeta)
        print(tipo_tarjeta)
    else:
        print("INVALID")

main()