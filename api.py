from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
from agente import GROQ_API_KEY, GROQ_MODEL

app = Flask(__name__)
CORS(app)

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        dados = request.json
        print(f"Dados recebidos: {dados}")  #  mostra no terminal
        
        client = Groq(api_key=GROQ_API_KEY)
        
        prompt = f"""Você é o FitBot, assistente de fitness do Fit Planner.
O usuário quer perder {dados['calorias']} kcal fazendo {dados['exercicio']},
{dados['minutos']} minutos por sessão, {dados['sessoes']}x por semana.
Isso equivale a {dados['kcalSemana']} kcal/semana e levará {dados['semanas']} semanas.
Dê uma análise motivacional curta e personalizada em português."""

        completion = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_completion_tokens=512
        )
        
        resposta = completion.choices[0].message.content
        print(f"Resposta gerada: {resposta[:50]}...")  #  mostra no terminal
        return jsonify({"resposta": resposta})
    
    except Exception as e:
        print(f"ERRO: {e}")  #  mostra o erro no terminal
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)