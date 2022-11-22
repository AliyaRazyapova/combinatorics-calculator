from flask import Flask, make_response, session, request, render_template, redirect, url_for


app = Flask(__name__)
app.secret_key = "111"


if __name__ == '__main__':
    app.run(port=8000, debug=True)