import pdfplumber
import pandas as pd

# Caminho do arquivo PDF
pdf_path = "./GaxetaseRaspadores.pdf"

data = []  # Lista para armazenar os dados extraídos

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_text()
        for line in tables.split("\n"):
            if line:
                data.append(line.split())
        
print(data)

# Criando um DataFrame
colunas = ["Código", "Descrição", "Medidas", "Preço Unitário", "Unidade"]
df = pd.DataFrame(data, columns=colunas)

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Opcional: salvar os dados em CSV
df.to_csv("./gaxetas_e_raspadores.csv", index=False)
