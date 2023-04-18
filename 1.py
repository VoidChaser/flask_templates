from flask import Flask, render_template, redirect, url_for
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['Заготовка'] = 'Домашняя страница'
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

@app.route('/training/<proph>')
def proph(proph):
    param = {}
    param['proph_name_form'] = proph
    prophecy_name = proph.lower()
    if (prophecy_name in prophs.keys() and prophs[prophecy_name] == 'inj') or ('строитель' in prophecy_name or 'инженер' in prophecy_name):
        param['Заготовка'] = 'Маршрут для инженеров'
        param['font_color'] = 'green'
        param['dep_name'] = 'инженерные тренажеры'
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



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
