import google.generativeai as genai
from history import historico
import os
from functions import add_item

genai.configure(api_key=os.environ['GEMINI_API_KEY'])

generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-latest",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

chat_session = model.start_chat(history=historico)

arquivos = open('database/all.txt', 'r', encoding="utf-8").read()

file_amount = int(input('\nInsira a quantidade de arquivos que deseja ter de retorno:\n'))
descricao = input('\nInsira a descrição do arquivo que está procurando:\n')

message = f"""{arquivos}
Ordene os tópicos de acordo com o número de seu Score, de maior para menor;
Faça essa análise se baseando na descrição a seguir: {descricao};
Analisando todos os arquivos acima quero que crie um ranking dos {file_amount} arquivos que mais tem relação com a descrição desejada;

Faça essa análise se baseando nos critérios de avaliação abaixo:
- O nome das pastas que os arquivos se encontram tem relação com a descrição passada como parâmetro? (score máximo: 30/100);
- A pasta do arquivo tem um mapeamento que condiz com a descrição passada como parâmetro? (score máximo: 20/100);
- Os nomes dos arquivos tem relação com a descrição passada como parâmetro? (score máximo: 20/100);
- Baseado no histórico de perguntas, a descrição passada como parâmetro condiz com alguma resposta anterior? (score máximo: 15/100);
- A última data de atualização é recente? (score máximo: 15/100);

Crie um tópico para cada arquivo, mostrando o caminho EXATO do arquivo, dentro desse tópico crie alguns subtópicos: 
-Explique o motivo pelo posicionamento;
-Nome do arquivo;
-Última data de atualização;
-Score que o arquivo atingiu;
"""

print('\nComando enviado, aguarde alguns instantes...\n')
attempts = 3

while attempts > 0:
  try:
    response = chat_session.send_message(message)
    break
  except Exception as err:
    if attempts > 1:
      response = str(err)
      attempts = attempts - 1

print(response.text)

linhas = response.text.splitlines()  # Divide o texto em linhas
folders = []

for linha in linhas:
    if "BR_SC_JGS_WM_LOGISTICA" in linha:
        folders.append(linha.replace('**',''))

alternativa = -1
while alternativa > file_amount or alternativa < 0:
  alternativa = int(input('\nEm qual das alternativas eu acertei? (0 para nenhuma)\n'))

if alternativa > 0 and alternativa <= file_amount:
  add_item(descricao,r'{}'.format(folders[alternativa-1]))
  print('Obrigado pela contribuição!')
else:
  print('Desculpe por não conseguir ajudar!')

