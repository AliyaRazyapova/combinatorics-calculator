import datetime
from flask import Flask, make_response, session, request, render_template, redirect, url_for


app = Flask(__name__)
app.secret_key = "111"

app.permanent_session_lifetime = datetime.timedelta(days=365)


@app.route("/")
def main_page():
    return render_template('main.html.')


if __name__ == '__main__':
    app.run(port=8000, debug=True)