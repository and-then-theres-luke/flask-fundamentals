from flask import Flask, request, render_template, redirect, session
import random
app = Flask(__name__)
app.secret_key = "I will never reveal the Wu Tang secret."



@app.route('/')
def great_number_game():
    if 'secret_number' in session:
        pass
    else:
        session['is_correct'] = False
        session['secret_number'] = random.randint(1,100)
        session['num_of_guesses'] = 0
        print("the secret number " + str(session['secret_number']))
    return render_template('index.html')

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    session['guess'] = int(request.form['guess'])
    session['num_of_guesses'] = session['num_of_guesses'] + 1
    if session['num_of_guesses'] >= 5:
        session['high_or_low'] = "You Lose! Want to try again?"
    elif session['secret_number'] > session['guess']:
        session['high_or_low'] = "Too Low!"
    elif session['secret_number'] < session['guess']:
        session['high_or_low'] = "Too High!"
    else:
        session['high_or_low'] = str(session['secret_number']) + " was the number! It took you " + str(session['num_of_guesses']) + " guesses."
        session['is_correct'] = True
    return redirect('/')

@app.route("/destroy_session", methods=['POST'])
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
