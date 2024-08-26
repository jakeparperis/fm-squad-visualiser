from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_session import Session
import os
from process_squad import initialise_squad, store_positions, calculate_player_info

app = Flask(__name__, static_url_path='/static')
secret_key = os.urandom(32)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = secret_key
Session(app)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file.filename.endswith('.html'):
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
                    'All Time Appearances': info['All Time Appearances'],
                    'All Time Goals': info['All Time Goals'],
                    'International Appearances': info['International Appearances'],
                    'International Goals': info['International Goals'],
                    'Season Appearances': info['Season Appearances'],
                    'Average Rating': info['Average Rating'],
                    'Season xG': info['Season xG'],
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

            return redirect(url_for('squad_overview'))
        else:
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
        if pos == "GK":
            goalkeepers.append(player_data)
        elif pos == "DEF":
            defenders.append(player_data)
        elif pos == "MID":
            midfielders.append(player_data)
        elif pos == "ATT":
            attackers.append(player_data)

    sort_by = request.args.get('sort_by', 'Best Overall')
    reverse = request.args.get('reverse', 'false').lower() == 'true'
    goalkeepers.sort(key=lambda x: x[sort_by], reverse=True)
    defenders.sort(key=lambda x: x[sort_by], reverse=True)
    midfielders.sort(key=lambda x: x[sort_by], reverse=True)
    attackers.sort(key=lambda x: x[sort_by], reverse=True)

    return render_template('squad_overview.html', goalkeepers=goalkeepers, defenders=defenders,
                           midfielders=midfielders, attackers=attackers)

@app.route('/squad_builder', methods=['GET'])
def squad_builder():
    goalkeepers = []
    defenders = []
    midfielders = []
    attackers = []
    squad_data = session.get('squad_data', [])

    for player_data in squad_data:
        pos = player_data['Position']
        if pos == "GK":
            goalkeepers.append(player_data)
        elif pos == "DEF":
            defenders.append(player_data)
        elif pos == "MID":
            midfielders.append(player_data)
        elif pos == "ATT":
            attackers.append(player_data)

    sort_by = request.args.get('sort_by', 'Best Overall')
    reverse = request.args.get('reverse', 'false').lower() == 'true'
    goalkeepers.sort(key=lambda x: x[sort_by], reverse=True)
    defenders.sort(key=lambda x: x[sort_by], reverse=True)
    midfielders.sort(key=lambda x: x[sort_by], reverse=True)
    attackers.sort(key=lambda x: x[sort_by], reverse=True)

    default_player_id = squad_data[0]['Player ID'] if squad_data else None
    default_player = squad_data[0] if squad_data else None

    return render_template('squad_builder.html', goalkeepers=goalkeepers, defenders=defenders,
                           midfielders=midfielders, attackers=attackers, default_player_id=default_player_id,
                           default_player=default_player)

@app.route('/show_card', methods=['GET'])
def show_card():
    player_id = request.args.get('player_id')
    squad_data = session.get('squad_data', [])

    for player_data in squad_data:
        if player_data['Player ID'] == player_id:
            player = player_data
            return render_template('player_card_template.html', player=player)

    return '', 404


@app.route('/player_info_page', methods=['GET'])
def player_info_page():
    player_id = request.args.get('player_id')
    squad_data = session.get('squad_data', [])

    for player_data in squad_data:
        if player_data['Player ID'] == player_id:
            player = player_data
            break

    return render_template('player_info.html', player=player)


if __name__ == '__main__':
    app.run()
