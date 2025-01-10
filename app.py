import os
import openai
from flask import Flask, request, render_template

app = Flask(__name__)

# Definindo a chave da API como variável de ambiente
os.environ['OPENAI_API_KEY'] = 'substituir pela sua chave de API'
openai.api_key = os.environ['OPENAI_API_KEY']

def obter_resposta(pergunta):
    response = openai.ChatCompletion.create(
        model="modelo de lingiagem",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": pergunta}
        ]
    )
    return response.choices[0].message["content"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    pergunta = request.form['pergunta']
    resposta = obter_resposta(pergunta)
    return resposta

if __name__ == '__main__':
    app.run(debug=True)
