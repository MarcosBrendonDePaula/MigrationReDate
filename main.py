MIGRATIONS_FOLDER = "migrations"
INPUT_FOLDER  = f"{MIGRATIONS_FOLDER}/input"
OUTPUT_FOLDER = f"{MIGRATIONS_FOLDER}/output"
import os
import re
import shutil
from datetime import datetime

MIGRATIONS_FOLDER = "migrations"
INPUT_FOLDER = f"{MIGRATIONS_FOLDER}/input"
OUTPUT_FOLDER = f"{MIGRATIONS_FOLDER}/output"

MIGRATIONS_FORMAT = ".php"

# Verifica se as pastas de entrada e saída existem, se não, cria-as
for folder in [MIGRATIONS_FOLDER, INPUT_FOLDER, OUTPUT_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Lista os arquivos na pasta de entrada
input_files = os.listdir(INPUT_FOLDER)

# Filtra apenas os arquivos com extensão MIGRATIONS_FORMAT na pasta de entrada
input_files = [file for file in input_files if file.endswith(MIGRATIONS_FORMAT)]

# Expressão regular para extrair a data do nome do arquivo
date_pattern = re.compile(r'(\d{4}_\d{2}_\d{2})_(\d{6})_.*')

# Função para extrair a data do nome do arquivo
def extract_date(file_name):
    match = date_pattern.match(file_name)
    if match:
        return match.group(1)
    else:
        return None

# Ordena os arquivos com base na data e no identificador único
input_files.sort(key=lambda x: (extract_date(x), x))

# Atualiza as datas dos arquivos na pasta de saída mantendo o mesmo nome da migration
for idx, file_name in enumerate(input_files):
    current_date = datetime.now().strftime("%Y_%m_%d")
    last_number = str(idx + 1).zfill(6)  # Mantém exatamente 6 dígitos, preenchendo com zeros à esquerda
    migration_name = re.sub(r'\d{4}_\d{2}_\d{2}_\d{6}_', '', file_name)
    new_file_name = f"{current_date}_{last_number}_{migration_name}"
    input_path = os.path.join(INPUT_FOLDER, file_name)
    output_path = os.path.join(OUTPUT_FOLDER, new_file_name)
    shutil.copy(input_path, output_path)

print("Atualização concluída.")