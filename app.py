from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = '09183475091837450918734' 

goal = 200

@app.route('/')
def index():
    if not 'counter' in session:
        session['counter'] = 0
    if not 'gold' in session:
        session['gold'] = 0
    if not 'getgold' in session:
        session['getgold'] = 0
    if not 'history' in session:
        session['history'] = ""
    if not 'wincondition' in session:
        session['wincondition'] = 3
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def gold():
    session['counter'] += 1
    if session['counter'] < 15 and session['gold'] < goal:
        if request.form['getgold'] == 'farm':
            farm = random.randint(10, 20)
            session['gold'] += farm
            session['action'] = f" class=\"green\"> user chose farm and added {farm} gold."
        if request.form['getgold'] == 'cave':
            cave = random.randint(5, 10)
            session['gold'] += cave
            session['action'] = f" class=\"green\"> user chose farm and added {cave} gold."
        if request.form['getgold'] == 'house':
            house = random.randint(2, 5)
            session['gold'] += house
            session['action'] = f" class=\"green\"> user chose farm and added {house} gold."
        if request.form['getgold'] == 'casino':
            casino = random.randint(0, 100) - 50
            session['gold'] += casino
            if casino > 0:
                session['action'] = f" class=\"green\"> user chose farm and added {casino} gold."
            else:
                session['action'] = f" class=\"red\"> user chose farm and lost {-casino} gold."
        session['history'] = "<p" + session['action'] + "</p>" + session['history']
    else:
        session['wincondition'] = 0
    if session['counter'] < 15 and session['gold'] >= goal:
        session['wincondition'] = 1
    if request.form['getgold'] == 'reset':
        del session['history']
        del session['gold']
        del session['getgold']
        del session['counter']
        del session['wincondition']
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)