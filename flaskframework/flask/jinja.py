from flask import Flask, render_template,request


app = Flask(__name__)



@app.route('/submit',methods=['GET','POST'])
def submitform():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    else:
        return render_template('form.html')

# Variable rule
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score>50:
        res = "Pass"
    else:
        res = "Fail"
    return render_template('result.html',results=res)

@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score>50:
        res = "Pass"
    else:
        res = "Fail"
    exp={"res":res,"score":score}
    return render_template('resultres.html',results=exp)


@app.route('/successif/<int:score>')
def successif(score):
     return render_template('result.html',results=score)




@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)


@app.route('/getresults')
def getresults():
    return render_template('getresults.html')

def run():
    app.run(debug=True)


if __name__ == '__main__':
    run()
