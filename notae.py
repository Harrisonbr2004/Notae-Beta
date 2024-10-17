import matplotlib.pyplot as plt
import os as os
import pandas as pd
import funções as cd
#tabela_df = pd.read_excel('media.xlsx')


#A 'médias_salas' é a planilha onde fica as médias das salas. Aqui, verifica se ela existe, se não, a cria
try:
    df_medias = pd.read_excel('médias_salas.xlsx')

except:
    df_medias = cd.criar_tab_media()

#Primeiro Looping, o principal
while True:
    print("\n***BEM-VINDO***")
    print("\nO que deseja fazer?\n")

    print("Buscar sala (1)")
    print("Modificar salas (adicionar salas, adicionar alunos a salas existentes, remover alunos, etc) (2)")
    print("Remover sala (3)")
    print("Ver média das salas (4)")
    print("Ver gráfico de comparação (5)")

    print("\nDigite 'sair' para sair")

    resposta = input(" :")
    print("\n")

    #Para sair do código
    if resposta == 'sair':
        break

    #Para buscar uma sala
    if resposta == '1':
        sala = input("Qual sala será buscada? ")
        try:
            tabela_df = pd.read_excel(f'{sala}.xlsx')

        except:
            print("ERRO! A sala não está cadastrada!")

        print(tabela_df)

    #Para adicionar e modificar salas
    if resposta == '2':
        #Looping para as modificações
        while True:
            sala = input("\nQual o nome da sala? (ou digite 'sair' para sair) ")

            if sala == 'sair':
                break

            #Tenta abrir o dataframe (que está como arquivo Excel). Se não conseguir, o cria
            try:
                tabela_df = pd.read_excel(f'{sala}.xlsx')

            except:
                tabela_df = cd.criar_df()

            #Segundo looping
            while True:
                #print(tabela_df)
                print(f"\nSala {sala}")
                resp = int(input("1 = Mostrar tabela; 2 = Adicionar um aluno a tabela; 3 = Remover um aluno da tabela; 4 = ... "))

                #Mostrar Tabela
                if resp == 1:
                    print(tabela_df)
                    resp2 = int(input("Deseja fazer algo mais? sim = 1, não = 2: "))
                    if resp2 == 2:
                        print("\nOk, até mais!")
                        break

                #Adicionar Aluno
                elif resp == 2:
                    n = int(input("Quantos alunos você quer adicionar? "))

                #Looping que adiciona alunos
                for j in range (n):
                    n_alunos = cd.add_aluno(sala)
                    tabela_df =  pd.concat([tabela_df, n_alunos], ignore_index=True)

                resp2 = int(input("\nDeseja fazer algo mais? sim = 1, não = 2: "))
                if resp2 == 2:
                    print("\nOk, até mais!")
                    break

                #Remover aluno
                elif resp == 3:
                    tabela_df = cd.rem_aluno(tabela_df)

                    resp2 = int(input("Deseja fazer algo mais? sim = 1, não = 2: "))
                    if resp2 == 2:
                        print("\nOk, até mais!")
                        break

        #Calcula média no final do códigos
        tabela_df['Média'] = round((tabela_df['MAT'] + tabela_df["PORT"] + tabela_df["HIST"])/3, 1)

        # Calcula a média da sala
        nova_média = round(tabela_df['Média'].mean(), 2)
        
        # Atualiza ou adiciona a média da sala no dicionário e o salva
        df_medias = cd.atualizar_tab_media(sala, df_medias, nova_média)
        df_medias.to_excel('médias_salas.xlsx', index=False)

        #Salva a tabela em um arquivo .xlsx(Excel)
        with pd.ExcelWriter(f'{sala}.xlsx') as writer:
            tabela_df.to_excel(writer, sheet_name='Sheet1', index=False)

    if resposta == '3':
        sala = input("Qual o nome da sala que será excluida? ")
        sala1 = f'{sala}.xlsx'
        os.remove(sala1)

    if resposta == '4':
        print(df_medias)
        print("\nMédia das salas gerada com sucesso!")


    if resposta == '5':
        cd.criar_gráfico(df_medias)
