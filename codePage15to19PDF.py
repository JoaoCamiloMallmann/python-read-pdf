import tabula
import pandas as pd

# Lista para armazenar todas as tabelas
todas_tabelas = []

# Itera sobre todas as páginas do PDF
for pagina in range(15, 66):
    # Lê todas as tabelas da página atual do arquivo PDF
    lista_tabelas = tabula.read_pdf("catalogo.pdf", pages=pagina, multiple_tables=True)
    
    # Itera sobre cada tabela extraída da página atual
    for tabela in lista_tabelas:
        todas_tabelas.append(tabela)

# Concatena todas as tabelas em uma única tabela final
tabela_final = pd.concat(todas_tabelas, ignore_index=True)

# Exporta a tabela final como um arquivo CSV
tabela_final.to_csv("todas_tabelas_do_pdf.csv", index=False)

# Exibe a tabela final (oional)
print(tabela_final)


import tabula
import pandas as pd

# Substitua 'caminho_para_seu_arquivo.pdf' pelo caminho real do seu arquivo PDF
pdf_path = 'a.pdf'

# Tentando extrair todas as tabelas do PDF usando o modo lattice
tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True, lattice=False, stream=True)

# Verificando quantas tabelas foram extraídas
print(f"Total de tabelas extraídas: {len(tables)}")

# Concatenando todas as tabelas em um único DataFrame
if tables:
    combined_df = pd.concat(tables, ignore_index=True)
    # Salvando o DataFrame combinado como CSV
    combined_df.to_csv('precos_combinados.csv', index=False)
    print("Tabelas combinadas salvas em 'precos_combinados.csv'")
else:
    print("Nenhuma tabela encontrada no PDF")
