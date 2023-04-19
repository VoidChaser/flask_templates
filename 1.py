from flask import Flask, render_template, url_for, request
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    param = {'Заготовка': 'Домашняя страница'}
    return render_template('base.html', **param)


prophs = {
    'инженер-исследователь': 'inj',
    'пилот': 'sci',
    'строитель': 'inj',
    'экзобиолог': 'sci',
    'врач': 'sci',
    'инженер по терраформированию': 'sci',
    'астрогеолог': 'sci',
    'гляциолог': 'sci',
    'инженер жизнеобеспеченея': 'inj',
    'метеоролог': 'sci',
    'оператор марсохода': 'inj',
    'киберинженер': 'sci',
    'штурман': 'sci',
    'пилот дронов': 'sci',
}


@app.route('/training/<prophec>')
def proph(prophec):
    param = {'proph_name_form': prophec}
    prophecy_name = prophec.lower()
    if (prophecy_name in prophs.keys() and prophs[prophecy_name] == 'inj')\
            or ('строитель' in prophecy_name or 'инженер' in prophecy_name):
        param['Заготовка'] = 'Маршрут для инженеров'
        param['font_color'] = 'green'
        param['dep_name'] = 'Инженерные тренажеры'
        param['font_size_int'] = 12
        param['image_path'] = url_for('static', filename='img/inj_t.png')
    elif prophecy_name not in prophs.keys() or prophs[prophecy_name] == 'sci':
        param['Заготовка'] = 'Маршрут для учёных'
        param['font_color'] = 'red'
        param['dep_name'] = 'Научные симуляторы'
        param['font_size_int'] = 10
        param['image_path'] = url_for('static', filename='img/science_s.png')

    return render_template('prophecy_inj.html', **param)


@app.route('/list_prof/<list_mark>')
def list_p(list_mark):
    return render_template('list_prof.html', mark=list_mark, proph_list=list(prophs.keys()))


@app.route('/answer', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('form_sample.html')

    elif request.method == 'POST':
        parameters = {'Фамилия': request.form['surname'], 'Имя': request.form['name'],
                      'Образование': request.form['class']}

        prophecys = []
        prophecys.append('Инженер-исследователь') if request.form.get('accept1') else ''
        prophecys.append('Инженер-строитель') if request.form.get('accept2') else ''
        prophecys.append('Пилот') if request.form.get('accept3') else ''
        prophecys.append('Метеоролог') if request.form.get('accept4') else ''
        prophecys.append('Инженер по жизнеобеспечению') if request.form.get('accept5') else ''
        prophecys.append('Инженер по радиационной защите') if request.form.get('accept6') else ''
        prophecys.append('Врач') if request.form.get('accept7') else ''
        prophecys.append('Экзобиолог') if request.form.get('accept8') else ''

        parameters['Профессия'] = \
            f"{', '.join(list(filter(lambda x: x != '', prophecys))) if prophecys else 'не указано'}"
        parameters['Пол'] = request.form.get("sex")
        parameters['О себе'] = request.form.get("about")
        parameters['Готов остаться'] = 'Готов' if request.form.get("acceptRules") else 'Не готов'
        print(parameters)
        return render_template('auto_answer.html', parameters=parameters)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
