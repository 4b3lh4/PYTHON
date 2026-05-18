from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def painel():
    dados_linhas = {
        "82": {"nome": "BRT Move - Estação São Gabriel / Centro", "tempo": "5 min", "paradas": ["Estação São Gabriel", "Av. Cristiano Machado", "Estação Central"]},
        "5106": {"nome": "Bandeirantes / BH Shopping", "tempo": "12 min", "paradas": ["Igreja da Pampulha", "Av. Antônio Carlos", "Praça da Savassi", "BH Shopping"]},
        "SC01": {"nome": "Circular Contorno", "tempo": "8 min", "paradas": ["Praça da Estação", "Av. do Contorno", "Hospital Felício Rocho"]}
    }
    
    linha_selecionada = None
    erro = None

    if request.method == 'POST':
        numero_linha = request.form.get('num_linha')
        
        if numero_linha in dados_linhas:
            linha_selecionada = dados_linhas[numero_linha]
        else:
            erro = f"A linha '{numero_linha}' não foi localizada no sistema."

    return render_template('painel.html', linha=linha_selecionada, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)