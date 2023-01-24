#importierungen
from model import InputForm
from flask import Flask, render_template, request
from compute import plot_formula as compute
import random

# erstellen der request an die server
app = Flask(__name__)

# app routing um server aufrecht zu erhalten, dafür wird die Seite alle paar Minuten angepingt
# lädt die website und synchronisiert sie mit dem programm
@app.route('/', methods=['GET', 'POST'])
def index():
    #anfrage an html5
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        # ausrechnen der eingegebenen Rechnung und plotten des Graphes
        result = compute(form.Formula.data, form.Domain.data)
    else:
        result = None
    #Ausgabe des Ergebnisses
    return render_template('view.html', form=form, result=result)
#startet alles
if __name__ == '__main__':
    app.run(
		host='0.0.0.0',  
		port=random.randint(2000, 9000)
	)
