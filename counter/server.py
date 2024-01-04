from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = "I will never reveal the Wu Tang secret."


@app.route('/')
def index_accessed():
    if 'clicks' in session:
        pass
    else:
        session['clicks'] = 0
    if 'times_visited' in session:
        session['times_visited'] += 1
    else:
        session['times_visited'] = 1
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.pop('times_visited')
    session['clicks'] +=1
    return redirect('/')

@app.route('/increase_by_two')
def increase_by_two():
    session['times_visited'] +=1
    session['clicks'] +=1
    return redirect('/')

@app.route('/increase_by_what', methods=["Get", "post"])
def increase_by_what():
    print(request.form)
    session['times_visited'] += (int(request.form['amount']) - 1)
    session['clicks'] +=1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)