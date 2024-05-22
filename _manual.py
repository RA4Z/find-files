import os
from tqdm import tqdm
import datetime

def percorrer_pastas(pasta:str, file_types:list):
  arquivos = {}
  for raiz, _, arquivos_na_pasta in tqdm(os.walk(pasta), desc=f"Percorrendo pastas"):
    arquivos[raiz] = []
    for arquivo in arquivos_na_pasta:
      try:
        for file_type in file_types:
            if arquivo.lower().endswith(f".{file_type}"):
                caminho_completo = os.path.join(raiz, arquivo)
                data_modificacao = datetime.datetime.fromtimestamp(os.path.getmtime(caminho_completo))
                arquivos[raiz].append(f'{arquivo}; {data_modificacao}')

      except:
         pass
      
  return arquivos

def salvar_dados(desired_files:list):
    arquivo_txt = os.path.join("database", f"manualExec.txt")

    # Abre o arquivo para escrita, sobrescrevendo se já existir
    with open(arquivo_txt, "w", encoding="utf-8") as arquivo:
        for file in desired_files:
            if len(desired_files[file]) > 0:
              arquivo.write(f"\n{file}:\n")
              for data in desired_files[file]:
                arquivo.write(f"{data}\n")


pasta = 'Q:\GROUPS\BR_SC_JGS_WM_LOGISTICA\PCP\Central'
file_types = ['xlsm','pbix', 'pdf', 'docx', 'doc', 'xlsb', 'xls', 'xlsx', 'ico', 'exe', 'py']
desired_files = percorrer_pastas(pasta, file_types)
salvar_dados(desired_files)