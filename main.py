import datetime, math
from flask import Flask, request, render_template


app = Flask(__name__)
app.secret_key = "111"

app.permanent_session_lifetime = datetime.timedelta(days=365)


@app.route("/")
def main_page():
    return render_template('main.html.')


@app.route("/perestanovki/")
def perestanovki_list():
    title = 'Перестановки'
    title_1 = 'perestanovki'
    return render_template('base.html', title=title, title_1=title_1)
#с повторениями и без повторений


@app.route("/perestanovki/repeat/", methods=['GET', 'POST'])
def perestanovki_repeat_list():
    k = request.form.get('k')
    if k:
        k = int(k)
        return render_template('perestanovki_repeat.html', k=k)
    else:
        repeat_list = request.form.getlist('num')
        print(repeat_list)
        sm = 0
        prz = 1
        for i in range(len(repeat_list)):
            a = int(repeat_list[i])
            sm += a
            prz *= math.factorial(a)
        response = str(int(math.factorial(sm)/prz))
        response = 'Число перестановок с повторений из ' + str(len(repeat_list)) + ' элементов: ' + response
        error = 'Введите данные'
    return render_template('perestanovki_repeat.html', error=error, response=response)


@app.route("/perestanovki/not_repeat/", methods=['GET', 'POST'])
def perestanovki_not_repeat_list():
    num = request.form.get('num')
    if num:
        response = str(math.factorial(int(num)))
        response = 'Число перестановок без повторений из ' + num + ' элементов: ' + response
        return render_template('perestanovki_not_repeat.html', num=num, response=response)
    else:
        error = 'Введите данные'
        return render_template('perestanovki_not_repeat.html', error=error)
#max: num=1558


@app.route("/sochetaniay/")
def sochetaniay_list():
    title = 'Сочетания'
    title_1 = 'sochetaniay'
    return render_template('base.html', title=title, title_1=title_1)


@app.route("/sochetaniay/repeat/", methods=['GET', 'POST'])
def sochetaniay_repeat_list():
    num = request.form.get('num')
    num_1 = request.form.get('num_1')
    if num and num_1:
        response = str(int((math.factorial(int(num)+int(num_1)-1))/(math.factorial(int(num_1))*math.factorial(int(num)- 1))))
        response = 'Число сочетаний с повторениями из ' + num + ' по ' + num_1 + ': ' + response
        return render_template('sochetaniay_repeat.html', num=num, num_1=num_1, response=response)
    else:
        error = 'Введите данные'
        return render_template('sochetaniay_repeat.html', error=error)


@app.route("/sochetaniay/not_repeat/", methods=['GET', 'POST'])
def sochetaniay_not_repeat_list():
    num = request.form.get('num')
    num_1 = request.form.get('num_1')
    if num and num_1:
        response = str(int(math.factorial(int(num))/(math.factorial(int(num_1))*math.factorial(int(num)-int(num_1)))))
        response = 'Число сочетаний без повторений из ' + num + ' по ' + num_1 + ': ' + response
        return render_template('sochetaniay_not_repeat.html', num=num, num_1=num_1, response=response)
    else:
        error = 'Введите данные'
        return render_template('sochetaniay_not_repeat.html', error=error)


@app.route("/razmeheniya/")
def razmeheniya_list():
    title = 'Размещения'
    title_1 = 'razmeheniya'
    return render_template('base.html', title=title, title_1=title_1)


@app.route("/razmeheniya/repeat/", methods=['GET', 'POST'])
def razmeheniya_repeat_list():
    num = request.form.get('num')
    num_1 = request.form.get('num_1')
    if num and num_1:
        response = str(int((int(num))**(int(num_1))))
        response = 'Число размещений c повторениями из ' + num + ' по ' + num_1 + ': ' + response
        return render_template('razmeheniya_repeat.html', num=num, num_1=num_1, response=response)
    else:
        error = 'Введите данные'
        return render_template('razmeheniya_repeat.html', error=error)


@app.route("/razmeheniya/not_repeat/", methods=['GET', 'POST'])
def razmeheniya_not_repeat_list():
    num = request.form.get('num')
    num_1 = request.form.get('num_1')
    if num and num_1:
        response = str(int(math.factorial(int(num))/(math.factorial(int(num)-int(num_1)))))
        response = 'Число размещений без повторений из ' + num + ' по ' + num_1 + ': ' + response
        return render_template('razmeheniya_not repeat.html', num=num, num_1=num_1, response=response)
    else:
        error = 'Введите данные'
        return render_template('razmeheniya_not repeat.html', error=error)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
