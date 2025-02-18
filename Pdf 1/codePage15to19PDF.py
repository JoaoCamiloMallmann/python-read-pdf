import pdfplumber
import csv
import re

# Caminho do arquivo PDF
pdf_path = "GaxetaseRaspadores.pdf"
output_csv = "dados_extraidos.csv"

# Abrir o PDF e extrair o texto
with pdfplumber.open(pdf_path) as pdf:
    data = []
    
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            lines = text.split('\n')
            for line in lines:
                # Remover "PC", "9.75" e "5.20"
                line = re.sub(r"\b(PC|9\.75|5\.20)\b", "", line).strip()
                
                # Adicionar ";" depois da numeração (código)
                line = re.sub(r"^(\S+)", r"\1;", line)  

                # Substituir múltiplos espaços por ";"
                line = re.sub(r"\s{2,}", ";", line)

                print(line)  # Para depuração
                data.append(line.split(";"))  # Dividir corretamente os campos

# Salvar os dados extraídos em um CSV sem aspas extras e com escape correto
with open(output_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";", quotechar=None, quoting=csv.QUOTE_NONE, escapechar="\\")
    writer.writerow(["Código", "Descrição", "Preço"])  # Cabeçalhos

    for row in data:
        if len(row) >= 3:  # Garantir que há pelo menos 3 colunas
            writer.writerow(row[:3])  # Apenas as 3 primeiras colunas relevantes

print(f"Dados extraídos e salvos em {output_csv}")
