from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_session import Session
import os
from process_squad import initialise_squad, store_positions, calculate_player_info
import player

app = Flask(__name__, static_url_path='/static')
secret_key = os.urandom(32)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = secret_key
Session(app)


@app.route('/', methods=['GET','POST'])
def index():
    rectangle = {'id': 'background', 'top': 40, 'left': 120, 'width': 1620, 'height': 760}

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
                    'Club': info['Club'],
                    'Division': info['Division'],
                    'Squad Number': info['Squad Number'],
                    'Personality': info['Personality'],
                    'International Appearances': info['International Appearances'],
                    'International Goals': info['International Goals'],
                    'Season Appearances': info['Season Appearances'],
                    'Average Rating': info['Average Rating'],
                    'Season Goals': info['Season Goals'],
                    'Season Assists': info['Season Assists'],
                    'Best Overall': info['Best Overall'],
                    'Position Overalls': info['Position Overalls'],
                    'Position': position['Position'],
                    'Pace': info['Pace'],
                    'Shooting': info['Shooting'],
                    'Passing': info['Passing'],
                    'Dribbling': info['Dribbling'],
                    'Defending': info['Defending'],
                    'Physical': info['Physical'],
                    'Skill Moves': info['Skill Moves'],
                    'Weak Foot': info['Weak Foot'],
                    'Preferred Foot': info['Preferred Foot'],
                    'Height': info['Height'],
                    'Weight': info['Weight'],
                    'Transfer Value': info['Transfer Value'],
                    'Wage': info['Wage'],
                    'Injury': info['Injury']
                }
                squad_data.append(player_data)

            session['squad_data'] = squad_data
            sort_by = request.args.get('sort_by', 'Name')
            reverse = request.args.get('reverse', 'false').lower() == 'true'

            squad_data.sort(key=lambda x: x[sort_by], reverse=reverse)

            return redirect(url_for('squad_overview'))

        return redirect(url_for('index'))
    return render_template('index.html', rectangle=rectangle, title='Home Page')


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

    rectangle = {'id': 'background', 'top': 40, 'left': 120, 'width': 1620, 'height': 760}

    return render_template('squad_overview.html', rectangle=rectangle, goalkeepers=goalkeepers,
                           defenders=defenders, midfielders=midfielders, attackers=attackers)


@app.route('/player_info_page', methods=['GET'])
def player_info_page():
    player_id = request.args.get('player_id')
    squad_data = session.get('squad_data', [])

    for player_data in squad_data:
        if player_data['Player ID'] == player_id:
            player = player_data
            break

    # Deal with "-" in player attributes
    if player['Injury'] == "-":
        player['Injury'] = "Not Injured"
    if player['International Appearances'] == "-":
        player['International Appearances'] = "0"
    if player['International Goals'] == "-":
        player['International Goals'] = "0"
    if player['Season Appearances'] == "-":
        player['Season Appearances'] = "0"
    if player['Average Rating'] == "-":
        player['Average Rating'] = "0"
    if player['Season Goals'] == "-":
        player['Season Goals'] = "0"
    if player['Season Assists'] == "-":
        player['Season Assists'] = "0"

    if player['Position'] == "Goalkeeper":
        player['Position'] = "GK"
    elif player['Position'] == "Midfielder":
        player['Position'] = "MID"
    elif player['Position'] == "Defender":
        player['Position'] = "DEF"
    elif player['Position'] == "Attacker":
        player['Position'] = "ATT"

    rectangle = {'id': 'background', 'top': 40, 'left': 120, 'width': 1620, 'height': 760}

    return render_template('player_info_page.html', rectangle=rectangle, player=player)


if __name__ == '__main__':
    app.run(debug=True)
