from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_session import Session
import os
from process_squad import initialise_squad, store_positions, calculate_player_info
import player

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(24)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'supersecretkey'
Session(app)


@app.route('/', methods=['GET','POST'])
def index():
    upload_success = True

    if request.method == 'POST':
        if 'file' not in request.files:
            upload_success = False
            flash('No file found')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            upload_success = False
            flash('No file selected')
            return redirect(request.url)

        if upload_success:
            squad = initialise_squad(file)  # List of Player objects
            player_info = calculate_player_info(squad)  # List of dicts
            positions = store_positions(squad)  # List of strings

            squad_data = []
            for info, position in zip(player_info, positions):
                player_data = {
                    'Player ID': info['Player ID'],
                    'Nation': info['Nation'],
                    'Name': info['Name'],
                    'Age': info['Age'],
                    'Best Overall': info['Best Overall'],
                    'Position Overalls': info['Position Overalls'],
                    'Position': position['Position'],
                    'Pace': info['Pace'],
                    'Shooting': info['Shooting'],
                    'Passing': info['Passing'],
                    'Dribbling': info['Dribbling'],
                    'Defending': info['Defending'],
                    'Physical': info['Physical'],
                }
                squad_data.append(player_data)

            session['squad_data'] = squad_data
            sort_by = request.args.get('sort_by', 'Name')
            reverse = request.args.get('reverse', 'false').lower() == 'true'

            squad_data.sort(key=lambda x: x[sort_by], reverse=reverse)

            return redirect(url_for('squad_overview'))

        return redirect(url_for('index'))
    return render_template('index.html', title='Home Page')


@app.route('/squad_overview', methods=['GET'])
def squad_overview():
    goalkeepers = []
    defenders = []
    midfielders = []
    attackers = []
    squad_data = session.get('squad_data', [])

    for player_data in squad_data:
        pos = player_data['Position']
        if pos == "Goalkeeper":
            goalkeepers.append(player_data)
        elif pos == "Defender":
            defenders.append(player_data)
        elif pos == "Midfielder":
            midfielders.append(player_data)
        elif pos == "Attacker":
            attackers.append(player_data)

    sort_by = request.args.get('sort_by', 'Name')
    reverse = request.args.get('reverse', 'false').lower() == 'true'
    goalkeepers.sort(key=lambda x: x[sort_by], reverse=reverse)
    defenders.sort(key=lambda x: x[sort_by], reverse=reverse)
    midfielders.sort(key=lambda x: x[sort_by], reverse=reverse)
    attackers.sort(key=lambda x: x[sort_by], reverse=reverse)

    rectangle = {'id': 'squad_background', 'top': 25, 'left': 37.5}

    return render_template('squad_overview.html', rectangle=rectangle, goalkeepers=goalkeepers,
                           defenders=defenders, midfielders=midfielders, attackers=attackers)


@app.route('/player_info_page', methods=['GET'])
def player_info_page():
    squad_data = session.get('squad_data', [])

    return render_template('player_info_page.html')


if __name__ == '__main__':
    app.run(debug=True)
