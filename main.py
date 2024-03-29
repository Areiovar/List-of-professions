from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index/<title>')
def index(title='Заголовок страницы'):
    return render_template('base.html', title=title)

@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    if list_type == 'ol':
        professions = ['Инженер', 'Биолог', 'Астронавт', 'Геолог', 'Пилот']
        return render_template('list_prof.html', list_type=list_type, professions=professions)
    elif list_type == 'ul':
        professions = ['Инженер', 'Биолог', 'Астронавт', 'Геолог', 'Пилот']
        return render_template('list_prof.html', list_type=list_type, professions=professions)

if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
