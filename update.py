from functions import *

pasta = 'Q:\GROUPS\BR_SC_JGS_WM_LOGISTICA\PCP'
file_types = ['xlsm','pbix', 'txt', 'pdf', 'docx', 'doc', 'xlsb', 'xls', 'xlsx']

# for file_type in file_types:
#     file_path = os.path.join('database', f'{file_type}.txt')
#     if os.path.exists(file_path):
#         last_modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).date()
#         if last_modified_date < datetime.date.today():
#             desired_files = percorrer_pastas(pasta, file_type)
#             salvar_dados(desired_files, file_type)
#     else:
#         desired_files = percorrer_pastas(pasta, file_type)
#         salvar_dados(desired_files, file_type)

file_type = ''
file_path = os.path.join('database', f'all.txt')
if os.path.exists(file_path):
    last_modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).date()
    if last_modified_date < datetime.date.today():
        desired_files = percorrer_pastas(pasta, file_type, True)
        salvar_dados(desired_files, file_type, True)
else:
    desired_files = percorrer_pastas(pasta, file_type, True)
    salvar_dados(desired_files, file_type, True)

print('Dados atualizados!')