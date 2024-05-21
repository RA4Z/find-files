import google.generativeai as genai

genai.configure(api_key="AIzaSyBUQf8VqIlaSaOxRphJQYTWK8UprC2LboY")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
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

chat_session = model.start_chat(history=[])

arquivos = open('database/all.txt', 'r', encoding="utf-8").read()
descricao = 'Lista de materiais pendentes da EM'

message = f"""{arquivos}
\n\nLista de pastas principais do PCP: 
Q:\GROUPS\BR_SC_JGS_WM_LOGISTICA\PCP\Central
Q:\GROUPS\BR_SC_JGS_WM_LOGISTICA\PCP\Processos com Automatização
Q:\GROUPS\BR_SC_JGS_WM_LOGISTICA\PCP\Indicadores Automatizados
Q:\GROUPS\BR_SC_JGS_WM_LOGISTICA\PCP\MacrosMadrugada
Q:\GROUPS\BR_SC_JGS_WM_LOGISTICA\PCP\Robert

Ordene os tópicos de acordo com o número de seu Score, de maior para menor;
Faça essa análise se baseando na descrição a seguir: {descricao};
Analisando todos os arquivos acima quero que crie um ranking dos 10 arquivos que mais tem relação com a descrição desejada;

Faça essa análise se baseando nos critérios de avaliação abaixo:
- O nome das pastas que os arquivos se encontram tem relação com a descrição passada como parâmetro? (score: 47/100);
- A última data de atualização é recente? (score: 27/100);
- Os nomes dos arquivos tem relação com a descrição passada como parâmetro? (score: 23/100);
- A pasta do arquivo está entre as principais do PCP? (score: 5/100);

Crie um tópico para cada arquivo, mostrando o caminho EXATO do arquivo, dentro desse tópico crie alguns subtópicos: 
-Explique o motivo pelo posicionamento;
-Nome do arquivo;
-Última data de atualização;
-Score que o arquivo atingiu;
"""

print('\nComando enviado, aguarde alguns instantes...\n')
response = chat_session.send_message(message)
print(response.text)
print('FIM')