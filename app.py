from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cgu')
def cgu():
    return render_template('cgu.html')

@app.route('/mentions-legales')
def mentions_legales():
    return render_template('mentions-legales.html')

@app.route('/parametres-cookies')
def parametres_cookies():
    return render_template('parametres-cookies.html')

@app.route('/politique-confidentialite')
def politique_confidentialite():
    return render_template('politique-confidentialite.html')

# Ex. formulaire de réservation
@app.route('/reserver', methods=['POST'])
def reserver():
    nom = request.form.get('nom')
    email = request.form.get('email')
    message = request.form.get('message')
    print(f"Réservation reçue : {nom} / {email} / {message}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
