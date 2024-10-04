import pandas as pd
import matplotlib.pyplot as plt

def criar_df():
  tabela = {
            'SALA':[],
            'ALUNO':[],
            'PORT':[],
            'MAT':[],
            'HIST':[]
              }

  return pd.DataFrame(tabela)

def add_aluno(sala):
  novos_alunos = pd.DataFrame({'SALA': [f"sala {sala}"], 'ALUNO': [str(input(f"\nNome do aluno: "))], 'MAT': [float(input("Nota em matemática: "))], 'PORT': [float(input("Nota em Português: "))], 'HIST': [float(input("Nota em História: "))]})

  return novos_alunos

def rem_aluno(tabela_df):
  print("\n*******!!!ATENÇÃO!!!*******")
  print("\nA exclusão é feita a partir do índice do produto.")
  print("O índice é a posição do produto indicado ao seu lado esquerdo.")

  print("\n")
  print(tabela_df)
  print("\n")

  remover = int(input("Qual aluno irá ser removido? "))
  tabela_df = tabela_df.drop(remover, axis=0)
  return tabela_df


def criar_tab_media():
  tabela_m = {
            'SALA':[],
            'MÉDIA':[]
              }


def atualizar_tab_media(sala, df_medias, nova_média):
    if sala in df_medias['Sala'].values:
      # Atualiza a média da sala existente
      df_medias.loc[df_medias['Sala'] == sala, 'Média'] = nova_média
    else:
      # Adiciona uma nova sala
      novo_registro = pd.DataFrame({'Sala': [sala], 'Média': [nova_média]})
      df_medias = pd.concat([df_medias, novo_registro], ignore_index=True)

    return df_medias


def criar_gráfico(df_medias):
  plt.bar(df_medias.index, df_medias['Média'])
  plt.xlabel('Sala')
  plt.ylabel('Média')
  plt.title('Comparação das Médias por Sala')
  plt.show()