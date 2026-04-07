# Calculator 
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
operacao = input("Digite a operação: ")

match operacao:
    case "+":
        res = num1+num2+num3
    case "-": 
        res = num1-num2-num3
    case "*":
        res = num1*num2*num3
    case "/": 
        res = num1/num2/num3
        
print(f"resultado igual a {res} ")