ano_nascimento = int(input("Digite o ano em que nasceu: "))
ano_atual = 2025  
idade = ano_atual - ano_nascimento

if idade == 18:
    print("Você completa 18 anos este ano!")
elif idade > 18:
    print("Você já tem 18 anos ou mais.")
else:
    print("Você ainda não tem 18 anos.")