alunos = {}

def print_melhores_alunos(melhores_alunos):
    if len(melhores_alunos[0]) == 1:
        print("O melhor aluno eh:")
    
    else:
        print("Os melhores alunos sao:")
    

    for aluno in range(len(melhores_alunos[1])):
        print(f"{melhores_alunos[0][aluno]} com nota {melhores_alunos[1][aluno]}")


def melhores_alunos(alunos):
    nome_melhores_alunos_atual = []
    nota_melhores_alunos_atual = []

    for aluno in alunos:
        if len(nome_melhores_alunos_atual) == 0 and len(nota_melhores_alunos_atual) == 0:
            nome_melhores_alunos_atual.append(list(alunos.keys())[0])
            nota_melhores_alunos_atual.append(list(alunos.values())[0])


        if alunos[aluno] > nota_melhores_alunos_atual[0]:
            nome_melhores_alunos_atual.clear()
            nota_melhores_alunos_atual.clear()

            nome_melhores_alunos_atual.append(aluno)
            nota_melhores_alunos_atual.append(alunos[aluno])

        elif alunos[aluno] == nota_melhores_alunos_atual[0] and nome_melhores_alunos_atual[0] != aluno:
            nome_melhores_alunos_atual.append(aluno)
            nota_melhores_alunos_atual.append(alunos[aluno])
    

    return (nome_melhores_alunos_atual, nota_melhores_alunos_atual)
              

def adicionar_aluno():
    nome_atual = str(input("Digite o nome do aluno:\t"))
    nota_atual = str(input(f"Digite a nota do aluno {nome_atual}: "))

    alunos[nome_atual] = float(nota_atual)


for aluno in range(5):
    adicionar_aluno()
    print("*----*")

melhores_alunos = melhores_alunos(alunos)
print_melhores_alunos(melhores_alunos)