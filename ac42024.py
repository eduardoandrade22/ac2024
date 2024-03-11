def ler_nome():
    """Retorna o nome do aluno."""
    return input("Informe o seu nome: ")

def ler_notas():
    """Lê as quatro notas das avaliações e retorna os valores."""
    ap1 = float(input("Informe a nota da AP1: "))
    ap2 = float(input("Informe a nota da AP2: "))
    asub = float(input("Informe a nota da AS: "))
    ac = float(input("Informe a nota da AC: "))
    return ap1, ap2, asub, ac

def notas_sao_validas(ap1, ap2, asub, ac):
    """
    Retorna True se as quatro notas estão entre 0 e 10, inclusive.
    Retorna False caso contrário.
    """
    return 0 <= ap1 <= 10 and 0 <= ap2 <= 10 and 0 <= asub <= 10 and 0 <= ac <= 10

def duas_maiores_notas(ap1, ap2, asub):
    """
    Retorna as duas maiores notas dentre as avaliações apresentadas.
    Substitui a AP1 pela AS caso AS > AP1.
    Substitui a AP2 pela AS caso AS > AP2.
    A AS só substitui uma das duas provas (a menor delas).
    Caso a AS seja menor que a AP1 e a AP2, retorna AP1 e AP2.
    """
    if asub > ap1:
        return asub, ap2
    elif asub > ap2:
        return ap1, asub
    else:
        return ap1, ap2

def calcular_media(prova1, prova2, ac):
    """
    Retorna a média das avaliações, arredondando para duas casas decimais.
    M = (NOTA1 + NOTA2) * 0.4 + AC * 0.2
    """
    return round((prova1 + prova2) * 0.4 + ac * 0.2, 2)

def aluno_foi_aprovado(media):
    """
    Retorna True se o aluno tiver média superior ou igual à nota mínima de
    aprovação, e False caso contrário.
    """
    return media >= 7

def informa_resultado(media):
    """Exibe na tela se o aluno foi aprovado ou não."""
    if aluno_foi_aprovado(media):
        print("Aluno foi aprovado!")
    else:
        print("Aluno foi reprovado!")

def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            prova1, prova2 = duas_maiores_notas(ap1, ap2, asub)
            media = calcular_media(prova1, prova2, ac)
            informa_resultado(media)

main()
