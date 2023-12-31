from flask import Flask,render_template,jsonify
api = Flask(__name__)

def dados_capacete(arquivo):
    with open(f'{arquivo}','r') as metadados:
        return metadados.read()

def dados_traje(arquivo):
    with open(f'{arquivo}','r') as metadados:
        return metadados.read()

@api.route('/')
def home():
    return render_template('index.html')


@api.route('/confidencial')
def response_estaplanetar():
    dr_man_capacete = dados_capacete('astronautas/capacete/dr_man.txt')
    dr_man_traje = dados_traje('astronautas/roupa/dr_man.txt')
    dra_brand_capacete = dados_capacete('astronautas/capacete/dra_brand.txt')
    dra_brand_traje = dados_traje('astronautas/roupa/dra_brand.txt')

    dados = {'dr.man_capacete':dr_man_capacete,'dra.brand_capacete':dra_brand_capacete,'dr.man_traje':dr_man_traje,'dra.man_traje':dra_brand_traje}
    return jsonify(dados)
api.run(port=5000,host='localhost',debug=True)