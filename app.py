from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

@app.route('/')
def index():
    """
    Display the home page.
    :return: Rendered template of the index page.
    """
    return render_template('index.html')

@app.route('/balance', methods=('GET', 'POST'))
def balance():
    """

    :return: Rendered template of the delete app page.
    """
    return render_template('balance.html')

@app.route('/create', methods=('GET', 'POST'))
def create_app():
    """

    :return: Rendered template of the create app page.
    """
    return render_template('create_app.html')

@app.route('/delete', methods=('GET', 'POST'))
def delete_app():
    """

    :return: Rendered template of the delete app page.
    """
    return render_template('delete_app.html')

@app.route('/delete', methods=('GET', 'POST'))
def update_app():
    """

    :return: Rendered template of the update app page.
    """
    return render_template('update_app.html')

@app.route('/delete', methods=('GET', 'POST'))
def send_sms():
    """

    :return: Rendered template of the send SMS page.
    """
    return render_template('send_sms.html')

if __name__ == '__main__':
    app.run()