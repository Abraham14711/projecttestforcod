from flask import Flask,render_template,request,flash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'

@app.route('/',methods=['POST','GET'])
def main_page():
    if request.method=='POST':
        import re
        import urllib.parse
        import urllib.request
        import bs4
        def getReport(myurl):
            try:
                reponse = urllib.request.Request(myurl)
                html = urllib.request.urlopen(reponse).read().decode("utf-8")
                soup = bs4.BeautifulSoup(html, 'html.parser')
                pattern = r'http://v.virscan.org/\w+'
                vLinks = soup.find_all('a', href=re.compile(pattern))
                if len(vLinks) == 0:
                    return 'safe'
                else:
                    for vlink in vLinks:
                        url3 = urllib.parse.quote(vlink['href'])
                        url3 = url3.replace('http%3A', 'http:')
                        if vlink.has_attr('alt'):
                            return 'Unsafe'
                        else:
                            return 'safe'
            except:
                return 'Unsafe'

        if getReport(request.form.get('url')) == 'safe':
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')
    else:
        return render_template('mainpage.html')

@app.route('/vulnerabilities')
def contacts():
    return render_template('vulnerabilities.html')

@app.route('/antiviruses')
def new_things():
    return render_template('antiviruses.html')

if __name__ == '__main__':
    app.run()
