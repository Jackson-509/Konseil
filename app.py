from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'super-secret-key'  # à changer en prod

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nom = request.form.get('lastname')
        prenom = request.form.get('firstname')
        email = request.form.get('email')
        service = request.form.get('service')
        date = request.form.get('date')
        heure = request.form.get('time')

        print(f"[Réservation] {nom} {prenom} - {email} - {service} le {date} à {heure}")
        flash("🎉 Réservation enregistrée avec succès !", "success")
        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/cgu')
def cgu():
    return render_template('cgu.html')

@app.route('/mentions-legales')
def mentions():
    return render_template('mentions-legales.html')

@app.route('/parametres-cookies')
def cookies():
    return render_template('parametres-cookies.html')

@app.route('/politique-confidentialite')
def politique():
    return render_template('politique-confidentialite.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
