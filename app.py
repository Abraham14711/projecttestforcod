from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('mainpage.html')

@app.route('/vulnerabilities')
def contacts():
    message='Тест!!'
    return render_template('vulnerabilities.html',message=message)

@app.route('/antiviruses')
def new_things():
    return render_template('antiviruses.html')

if __name__ == '__main__':
    app.run()
