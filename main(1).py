while True:
    num1= int(input("Introduce un número:"))
    num2 = int(input("Introduce otro número:"))
    operación= input("Introduce operación +, -, * o /: ")
    
    if operación == "/":
        resultado = num1 / num2
        print ("El resultado de la operación: %d / %d = %f" % (num1, num2, resultado))

    if operación == "+":
        resultado= num1+num2
        print("El resultado de la operación: %d + %d = %f"% (num1, num2, resultado))

    if operación == "-":
        resultado= num1-num2
        print("El resultado de la operación: %d - %d = %f"% (num1, num2, resultado))

    if operación == "*":
        resultado= num1*num2
        print("El resultado de la operación es: %d * %d = %f"% (num1, num2, resultado))
    continuar=input("¿Desea realizar otra operación? ")
    if continuar== "no":
        break


