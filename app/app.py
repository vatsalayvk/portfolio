from logging import debug
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
# from .forms import ContactForm
# from flask_mail import Mail, Message

app = Flask(__name__)

# configurations
# app.config['SECRET_KEY'] = 'thisismysecret'
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_USERNAME'] = 'vatsalayvk1434@gmail.com'
# app.config['MAIL_PASSWORD'] = 'push mubo ncef grxv'

# mail = Mail(app)

@app.route('/home')
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/work')
def work():
    return render_template('work.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    # form = ContactForm()
    # if request.method == 'GET':
    #     return render_template('contact.html', form=form)
    # elif request.method == 'POST':
    #     if form.validate() == False:
    #         return "All Fields are required !"
    #     else:
    #         msg = Message(form.message.data, sender='[SENDER_MAIL]', recipients=['vatsalayvk1434@gmail.com'])
    #         msg.body = """
    #         from: %s &lt;%s&gt
    #         %s
    #         """% (form.name.data, form.email.data, form.message.data)
    #         mail.send(msg)
    #         flash("Thanks !")
    #         return redirect(url_for('contact'))
    #     return '<h1>Form submitted !</h1>' 
    return render_template('contact.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template("not_found.html"), 404

# sitemap
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == '__main__':
    app.run(debug=True)
