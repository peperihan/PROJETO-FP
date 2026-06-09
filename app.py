from flask import Flask, jsonify, send_from_directory
import os
os.system('cls' if os.name == 'nt' else 'clear')

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')
@app.route('/api/planos', methods=['GET'])
def obter_planos():
    planos = {}
    nome_arquivo = "dados_fitplanner.txt"
    if not os.path.exists(nome_arquivo):
        return jsonify({
            "Treino Hipertrofia A": "Cativado pelo Back-end",
            "Cardio Intenso B": "Sincronizado via API"
        })
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if linha.startswith("PLANO|"):
                    nome_plano = linha.strip().split("|")[1]
                    planos[nome_plano] = "Ativo"
        return jsonify(planos)
    except Exception as e:
        return jsonify({"Erro": str(e)}), 500
    
if __name__ == '__main__':
    print("\n🚀 SERVIDOR FITPLANNER LIGADO!")
    print("👉 Acesse no navegador: http://127.0.0.1:5000\n")
    app.run(debug=True, port=5000)