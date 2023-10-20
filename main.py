from flask import Flask, request, jsonify, render_template
import openai
import pdfplumber
import pytesseract
import docx
import cv2

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

openai.api_key = "KEY_OPEN_AI" #Precisa alterar 

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

def extract_text_from_txt(file_name):
    text = ""
    with open(f"files/{file_name}", "r", encoding="utf-8") as file:
        text = file.read()
    return text

def extract_text_from_pdf(file_name):
    text = ""
    with pdfplumber.open(file_name) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text 

def extract_text_from_image(file_name):
    text = ""
    image = cv2.imread(file_name)

    pytesseract.pytesseract.tesseract_cmd = r"caminho\tesseract.exe" #Precisa alterar 
    text = pytesseract.image_to_string(image, lang="por") 
    return text 

def extract_text_from_docx(file_name):
    doc = docx.Document(file_name)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

@app.route('/resumir', methods=['POST'])
def resumir():
    base_name = request.form.get('fileName')
    file_extension = request.form.get('fileExtension')

    if not base_name:
        return jsonify({"summary": "O nome do arquivo não foi fornecido."})

    try:
        if file_extension == "txt":
            extracted_text = extract_text_from_txt(f"{base_name}.{file_extension}")

        elif file_extension == "pdf":
            extracted_text = extract_text_from_pdf(f"{base_name}.{file_extension}")

        elif file_extension == "png" or file_extension == "jpg":
            extracted_text = extract_text_from_image(f"{base_name}.{file_extension}")

        elif file_extension == "docx":
            extracted_text = extract_text_from_docx(f"{base_name}.{file_extension}")

        prompt = f"""Summarize the text delimited by triple backticks into a single sentence in portuguese.
        ```{extracted_text}```"""

        response = get_completion(prompt)
        return jsonify({"summary": response})

    except FileNotFoundError:
        return jsonify({"summary": f"O arquivo '{base_name}.{file_extension}' não foi encontrado."})
    except Exception as e:
        return jsonify({"summary": f"Ocorreu um erro ao abrir o arquivo: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
