from flask import Flask, render_template, request
from analizador_lexico import prueba as analizar_lexico
from Sintactico import prueba_sintactica
from analizador_lexico import analizar_lexico

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    lexico_result = ""
    sintactico_result = ""
    counts = {}
    tokens_info = []

    if request.method == 'POST':
        codigo_fuente = request.form['ingreso']
        
        if 'lexico_button' in request.form:

            tokens_info, counts = analizar_lexico(codigo_fuente)
            lexico_result = "\n".join([f"Token: {t['token']} - Tipo: {t['tipo']}" for t in tokens_info])
            #resultado_lexico = analizar_lexico(codigo_fuente)
            #lexico_result = '\n'.join(resultado_lexico)

        elif 'sintactico_button' in request.form:
                resultado_sintactico = prueba_sintactica(codigo_fuente)
                sintactico_result = '\n'.join(resultado_sintactico)

        elif 'clear_counters' in request.form:
            
            counts = {
                'RESERVADO': 0,
                'IDENTIFICADOR': 0,
                'DELIMITADOR': 0,
                'OPERADOR': 0,
                'NUMERO': 0,
                'SIMBOLO': 0
            }
        

    return render_template('index.html', lexico_result=lexico_result, sintactico_result=sintactico_result, counts=counts)

if __name__ == '__main__':
    app.run(debug=True)
