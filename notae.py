import matplotlib.pyplot as plt
import pandas as pd
import funções as cd
#tabela_df = pd.read_excel('media.xlsx')

try:
    df_medias = pd.read_excel('médias_salas.xlsx')

except:
    df_medias = cd.criar_tab_media

#Looping principal:
while True:
    sala = input("\nQual o nome da sala? (ou digite 'sair' para sair) ")

    if sala == 'sair':
      break

    #Tenta abrir o dataframea (que está como arquivo Excel). Se não conseguir, o cria
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

        #Remover
        elif resp == 3:
          tabela_df = cd.rem_aluno(tabela_df)

          resp2 = int(input("Deseja fazer algo mais? sim = 1, não = 2: "))
          if resp2 == 2:
            print("\nOk, até mais!")
            break

        #Ver tabela das médias
        elif resp == 4:
           print(df_medias)
          
           resp2 = int(input("Deseja fazer algo mais? sim = 1, não = 2: "))
           if resp2 == 2:
            print("\nOk, até mais!")
            break
        
        #Sair
        elif resp == 5:
          print("Ok")
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

    resp3 = int(input("Deseja ver o gráfico de comparação? "))
    if resp == 1:
      # Cria um gráfico de barras comparando as médias das salas
      cd.criar_gráfico(df_medias)
