from flask import Flask, render_template, request
import random
import requests
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def hello():
    name = "World!!"
    return f'Hello {name}!'

@app.route('/mulcam')
def mulcam():
    return 'Hello mulcamp'

@app.route('/greeting/<string:name>') #String은 받은 것의 타입! name은 변수명!
def greeting(name):
    return f'{name}님 안녕하세요.'
#실행 방법은 http://127.0.0.1:8000/greeting/이희수

@app.route('/lunch/<int:num>')
def lunch(num):
    menu = ["짜장면" , "짬뽕", "라면" , "스파게티", "삼격살" , "수육"] 
    order = random.sample(menu, num) #menu를 기준으로 num만큼 뽑겠다는 메서드
    return str(order)

@app.route('/lotto')
def lotto():
    total = range(1,47)
    lottonum = random.sample(total, 6)
    return str(lottonum)

@app.route('/html')
def html():
    mutiline = '''
    <h1> This is H1 Tag</h1>
    <p> This is p Tag</p>
    '''
    return mutiline
@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html' , name=name) #앞의 name은 html의 name, 뒤의 name은 주소에 지정한 name

@app.route('/menu/<int:num>')
def menu(num):
    menu = ["짜장면", "짬뽕", "라면"]
    order = random.sample(menu, num)
    #return str(order)
    return render_template('menu.html', menu=order)
    
@app.route('/fake_naver')
def fake_naver():
    return render_template('fake_naver.html')


@app.route('/fake_google')
def fake_google():
    return render_template('fake_google.html')

@app.route('/send')
def send():
    return render_template('send.html')


# @app.route('/receive')
# def receive():
#     name = request.args.get('name')
#     message = request.args.get('message')
#     return render_template('receive.html', name=name, msg=message)

@app.route('/receive')
def receive():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('receive.html', name=name, msg=message)


@app.route('/send2')
def send2():
    return render_template('indian.html')


@app.route('/indian_receive')
def indian():
    year = int(request.args.get('year'))
    month = int(request.args.get('month'))-1
    day = int(request.args.get('day'))-1


    year_name = ["시끄러운, 말많은", "푸른", "어두운 -> 적색", "조용한", "웅크린", "백색", "지혜로운","용감한", "날카로운","욕심 많은"]
    month_name = ["늑대","태양","양","매","황소","불꽃","나무","달빛","말","돼지","하늘","바람"] 
    day_name = ["~와(과) 함께 춤을","~의 기상","~은(는) 그림자 속에","따로 붙는 말이 없음"
,"따로 붙는 말이 없음","따로 붙는 말이 없음","~의 환생","~의 죽음","~아래에서","~을(를) 보라."
,"~이(가) 노래하다.","~의 그늘 → 그림자","~의 일격","~에게 쫒기는 남자","~의 행진"
,"~의 왕","~의 유령","~을 죽인 자.","~은(는) 맨날 잠잔다.","~처럼..","~의 고향","~의 전사"
,"~은(는) 나의 친구","~의 노래","~의 정령","~의 파수꾼","~의 악마","~와(과) 같은 사나이"
,"~의 심판자→을(를) 쓰러뜨린 자","~의 혼","~은(는) 말이 없다."]
    year_name.pop()
    return render_template('receive2.html', year=year_name.pop(year), month=month_name.pop(month), day=day_name.pop(day))

@app.route('/lotto_get')
def lotto_get():
    return render_template('lotto_get.html')



@app.route('/lotto_num')
def lotto_num():
    num = request.args.get("num")
    url = f"https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}"
    res = requests.get(url).json()
    #List comprehension
    #[ 받는변수 for 받는변수 in 범위로된 데이터(ex List)]
    wnum = [ res[f'drwtNo{i}'] for i in range(1,7)]
    lotto = random.sample(range(1,47), 6)
    match = list(set(wnum) & set(lotto))
    count = len(match)
    if count == 6:
        msg = "1등"
    elif count == 5:
        msg = "2등"
    elif count == 4:
        msg = "3등"
    elif count == 3:
        msg = "4등"
    else:
        msg = "다음에"
    return render_template('lotto_result.html', num=num, wnum = wnum, msg = msg)




if __name__ == "__main__":
    app.run(debug=True, port=8000) 