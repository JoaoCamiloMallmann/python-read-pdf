
---

# Projeto: Extração de Dados de PDF para CSV

## Descrição

Este projeto utiliza a biblioteca `pdfplumber` para extrair dados de um arquivo PDF contendo tabelas e informações. O código lê as páginas do PDF, extrai o texto de cada uma delas e organiza as informações em um formato estruturado utilizando `pandas`. Ao final, os dados são armazenados em um arquivo CSV.

## Funcionalidade

1. **Leitura do PDF**: O código abre o PDF especificado no caminho `pdf_path` e percorre suas páginas.
2. **Extração de Dados**: O texto de cada página é extraído utilizando o método `extract_text()`. O texto extraído é processado linha por linha e dividido em colunas baseadas nos espaços.
3. **Estruturação dos Dados**: As informações extraídas são organizadas em um DataFrame do `pandas` com as colunas: "Código", "Descrição", "Medidas", "Preço Unitário", e "Unidade".
4. **Exportação para CSV**: Após a organização dos dados, o código pode salvar o DataFrame em um arquivo CSV para fácil manipulação e análise posterior.


## Dependências

- `pdfplumber`: Para extrair texto de arquivos PDF.
- `pandas`: Para manipulação e estruturação dos dados extraídos.

---
