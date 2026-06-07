from flask import Flask, render_template,request,redirect, url_for
app=Flask(__name__)
players=[] 
bowler= {'name': '', 'balls': 0}
#fn only one list will see 
def take_player(name):
    for p in players:
        if p['name']== name:
            return p
    return None



# todo add some more feature btw left line so i cld remember




@app.route('/')
def home():
    total=0 
    for p in players:
        total+= p['runs']
    return render_template('index.html', players=players,total=total, bowler=bowler)
@app.route('/join_player',methods=['POST'])
def join_player():
    name =request.form['name'].strip()
    if name and not take_player(name):
        players.append({'name':name,'runs':0, 'balls':0})
    

    return redirect(url_for('home'))
@app.route('/score_run', methods=['POST']) 
def score_run():
    name=request.form['name']
    runs=request.form['runs']
    try:
        runs=int(runs)
    except:runs=0

    p= take_player(name)
    if p and runs > 0:
        p['runs'] += runs
        p['balls']+= 1
        bowler['balls']+= 1
    
    return redirect(url_for('home'))


@app.route('/factoryreset', methods=['POST'])
def factoryreset():
    global players
    players=[]
    return redirect(url_for('home'))




@app.route('/out', methods=['POST'])
def out():
    global players
    name=request.form['name']
    #kick the boy out
    players=  [p for p in players if p['name']!= name]
    return redirect(url_for('home'))

@app.route('/set_bowler',methods=['POST'])

def set_bowler():
    global bowler
    name=  request.form['name'].strip()
    if name:
        bowler['name']= name
        bowler['balls'] = 0
    return redirect(url_for('home'))



if __name__ =='__main__':
    app.run(debug=True)


