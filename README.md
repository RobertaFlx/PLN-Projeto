# Projeto Processamento de Linguagem Natural

## Bibliotecas Necessárias
1. OpenAI, usada para integração com o mecanismo de geração de texto.
    ```bash
   pip install openai
2. Pdfplumber, usada pra extrair texto de arquivos ".pdf"
    ```bash
   pip install pdfplumber
3. Docx, usada pra extrair texto de arquivos ".docx"
    ```bash
   pip install python-docx
4. Pytesseract, usada pra extrair texto de imagens
    ```bash
   pip install pytesseract
5. Cv2, usada para processamento de imagens
    ```bash
   pip install opencv-python
6. Flask, usada para criar um servidor web
    ```bash
   pip install opencv-python

## Configuração do Pytesseract no Windows
1. Baixe o instalador através do seguinte link
    ```bash
   https://github.com/UB-Mannheim/tesseract/wiki
2. Após instalar, atribua o caminho que está o "tesseract.exe" à seguinte variável no main.py
    ```bash
   pytesseract.pytesseract.tesseract_cmd = "caminho/tesseract.exe"
3. Baixe o arquivo de tradução para pt-br através do seguinte link
    ```bash
   https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata
4. Adicione o arquivo "por.traineddata" no seguinte caminho
    ```bash
   caminho/tessdata/
