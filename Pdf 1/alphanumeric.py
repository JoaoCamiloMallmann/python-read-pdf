import pandas as pd

# Carregar o arquivo CSV
arquivo_csv = 'vitor/Itens.csv'
nome_coluna = 'Alfanumérico'

df = pd.read_csv(arquivo_csv)

# Mapeamento para substituição
substituicoes = {
    '0': 'J', '1': 'I', '2': 'H', '3': 'G', '4': 'F',
    '5': 'E', '6': 'D', '7': 'C', '8': 'B', '9': 'A'
}

def substituir_caractere(valor, posicao):
    if len(valor) > posicao and valor[posicao].isalnum():
        caractere = valor[posicao]
        if caractere in substituicoes:
            valor = valor[:posicao] + substituicoes[caractere] + valor[posicao + 1:]
    return valor

if nome_coluna in df.columns:
    for i in range(len(df)):
        valor = df.at[i, nome_coluna]
        if len(valor) > 0:
         
      
            if valor[0].isnumeric():
               valor = substituir_caractere(valor, 0)  
            
            elif valor[0] == 'A' or valor[0] == 'C':
                valor = substituir_caractere(valor, 2) 
                
            elif valor[0] == 'T':
                valor = substituir_caractere(valor, 3)
                
            else:
             print(valor)

    
                
            
            df.at[i, nome_coluna] = (f"GAXETA {valor}")

    # print(df[nome_coluna])

    # Salvar a última coluna modificada em um novo arquivo CSV
    novo_arquivo_csv = 'vitor/Ultima_coluna_modificada.csv'
    df[[nome_coluna]].to_csv(novo_arquivo_csv, index=False)
    print(f"Arquivo CSV com a última coluna modificada salvo com sucesso em '{novo_arquivo_csv}'.")
else:
    print(f"A coluna '{nome_coluna}' não foi encontrada no CSV.")
