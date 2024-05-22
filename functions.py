import os
import json
from tqdm import tqdm
import datetime

def percorrer_pastas(pasta:str, file_type:str, all=False):
  arquivos = {}
  for raiz, _, arquivos_na_pasta in tqdm(os.walk(pasta), desc=f"{file_type} - Percorrendo pastas"):
    arquivos[raiz] = []
    for arquivo in arquivos_na_pasta:
      try:
        caminho_completo = os.path.join(raiz, arquivo)
        if conditionals(arquivo, file_type, all, raiz):
          data_modificacao = datetime.datetime.fromtimestamp(os.path.getmtime(caminho_completo))
          if not all: arquivos[raiz].append(f'{arquivo}; {data_modificacao}')
          
          if all and data_modificacao > datetime.datetime.now() - datetime.timedelta(days=365*2):
            arquivos[raiz].append(f'{arquivo}; {data_modificacao}')

      except:
         pass
      
  return arquivos

def conditionals(arquivo:str, file_type:str, all:bool, folder:str):
  if 'backup' in folder.lower() or 'old' in folder.lower() or 'historico' in folder.lower() or 'histórico' in folder.lower() or 'Q:\GROUPS\BR_SC_JGS_WM_LOGISTICA\PCP\Robert\Indicadores' in folder:
    return False 

  if all and 'Exception' not in arquivo and 'Quick Kaizen' not in arquivo:
    possible_types = ['xlsm','pbix', 'txt', 'pdf', 'docx', 'xlsb']
    for file_type in possible_types:
      if arquivo.lower().endswith(f".{file_type}"):
        if not arquivo.replace(f'.{file_type}','').replace('-','').replace('.','').replace('_','').isdigit():
          return True
    return False
  
  if arquivo.lower().endswith(f'.{file_type}') and 'Exception' not in arquivo and 'Quick Kaizen' not in arquivo:
     if not arquivo.replace(f'.{file_type}','').replace('-','').replace('.','').replace('_','').isdigit():
      return True
  else:
     return False
   

def salvar_dados(desired_files:list, file_type:str, all=False):
    # Cria o caminho completo para o arquivo de texto
    if not all:
      arquivo_txt = os.path.join("database", f"{file_type}.txt")
    else:
      arquivo_txt = os.path.join("database", f"all.txt")

    # Abre o arquivo para escrita, sobrescrevendo se já existir
    with open(arquivo_txt, "w", encoding="utf-8") as arquivo:
        for file in desired_files:
            if len(desired_files[file]) > 0:
              arquivo.write(f"\n{file}:\n")
              for data in desired_files[file]:
                arquivo.write(f"{data}\n")


def add_item(question:str, answer:str):
  inteligence = json.load(open('inteligence.json', 'r', encoding='utf-8'))
  inteligence.append({"Question": question, "Answer": answer})
  json.dump(inteligence,open('inteligence.json', 'w', encoding='utf-8'))
