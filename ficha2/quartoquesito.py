idade = int(input("Digite sua idade: "))
if 0 <= idade <= 11:
    print("Criança")
elif 12 <= idade <= 18:
    print("Adolescente")
elif 19 <= idade <= 24:
    print("Jovem")
elif 25 <= idade <= 40:
    print("Adulto")
elif 41 <= idade <= 60:
    print("Meia Idade")
elif idade > 60:
    print("Idoso")
else:
    print("Idade inválida")