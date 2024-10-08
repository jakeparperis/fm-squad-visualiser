import math

from bs4 import BeautifulSoup
from player import Player


# Return a list players containing data from the table in the specified html file
def parse_html(file):
    content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    table = soup.find('table')

    players = []

    for row in table.find_all('tr')[1:]:
        columns = row.find_all(['td', 'th'])
        players.append([column.get_text(strip=True) for column in columns])

    header_row = table.find('tr')
    headers = [header.get_text(strip=True) for header in header_row.find_all(['th', 'td'])]

    return players


# Create instances of the Player class using the list returned above and return them in the list squad
def create_player_objects(players):
    squad = []

    for row in players:
        squad.append(Player(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                            row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20],
                            row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30],
                            row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39], row[40],
                            row[41], row[42], row[43], row[44], row[45], row[46], row[47], row[48], row[49], row[50],
                            row[51], row[52], row[53], row[54], row[55], row[56], row[57], row[58], row[59], row[60],
                            row[61], row[62], row[63], row[64], row[65], row[66], row[67], row[68], row[69], row[70],
                            row[71], row[72]))
    return squad


# Call above functions to reduce clutter in the app.py file
def initialise_squad(file):
    players = parse_html(file)
    squad = create_player_objects(players)
    return squad


def find_best_position(player):
    if player.get_position() != "GK":

        positions = ["FB", "WB", "CB", "CDM", "CM", "CAM", "WM", "FW", "ST"]
        best_position = ""
        highest = -1
        position_overalls = player.calculate_overall()
        for i in range(9):
            if position_overalls[i+1] > highest:
                highest = position_overalls[i+1]
                best_position = positions[i]
    else:
        best_position = "GK"

    return best_position


# Returns a list of each player's position (Goalkeeper, Defender, Midfielder, Attacker)
def store_positions(squad):
    positions = []
    for player in squad:
        best_position = find_best_position(player)
        positions.append({'Position': best_position})
    return positions


def calculate_player_info(squad):
    player_info = []
    for player in squad:
        best_position = find_best_position(player)

        player_id = player.get_id()
        nation = player.get_nationality()
        name = player.get_name()
        age = player.get_age()
        club = player.get_club()
        division = player.get_division()
        squad_number = player.get_squad_num()
        if squad_number == "-":
            squad_number = "#"
        personality = player.get_personality()
        all_apps = player.get_all_apps()
        if all_apps == "-":
            all_apps = 0
        all_goals = player.get_all_goals()
        if all_goals == "-":
            all_goals = 0
        int_caps = player.get_int_caps()
        if int_caps == "-":
            int_caps = 0
        int_goals = player.get_int_goals()
        if int_goals == "-":
            int_goals = 0
        szn_apps = player.get_szn_apps()
        if szn_apps == "-":
            szn_apps = 0
        avg_rating = player.get_avg_rating()
        if avg_rating == "-":
            avg_rating = 0
        szn_xg = player.get_szn_xg()
        if szn_xg == "-":
            szn_xg = 0
        szn_goals = player.get_szn_goals()
        if szn_goals == "-":
            szn_goals = 0
        szn_assists = player.get_szn_assists()
        if szn_assists == "-":
            szn_assists = 0
        pac = player.calculate_pace()
        sho = player.calculate_shooting()
        pas = player.calculate_passing()
        dri = player.calculate_dribbling()
        d3f = player.calculate_defending()
        phy = player.calculate_physical()
        skill_moves, weak_foot = player.calc_sm_wf()
        pref_foot = player.get_pref_foot()
        if pref_foot == "Right Only":
            pref_foot = "Right"
        elif pref_foot == "Left Only":
            pref_foot = "Left"
        height = player.get_height()
        weight = player.get_weight()
        transfer_value = player.calc_transfer_val()
        wage = player.get_wage()
        injury = player.get_injury()
        if injury == "-":
            injury = "Not injured"

        position_overalls = player.calculate_overall()

        best_overall = 0
        for ovr in position_overalls:
            if ovr > best_overall:
                best_overall = ovr

        final_position_overalls = []
        for ovr in position_overalls:
            if ovr == 0:
                final_position_overalls.append("N/A")
            else:
                final_position_overalls.append(ovr)

        if player.get_position() == "GK":
            for i in range(9):
                final_position_overalls.append("N/A")

        player_info.append({'Player ID': player_id,
                            'Nation': nation,
                            'Name': name,
                            'Age': age,
                            'Club': club,
                            'Division': division,
                            'Squad Number': squad_number,
                            'Personality': personality,
                            'All Time Appearances': all_apps,
                            'All Time Goals': all_goals,
                            'International Appearances': int_caps,
                            'International Goals': int_goals,
                            'Season Appearances': szn_apps,
                            'Average Rating': avg_rating,
                            'Season xG': szn_xg,
                            'Season Goals': szn_goals,
                            'Season Assists': szn_assists,
                            'Best Overall': best_overall,
                            'Position Overalls': final_position_overalls,
                            'Best Position': best_position,
                            'Pace': pac,
                            'Shooting': sho,
                            'Passing': pas,
                            'Dribbling': dri,
                            'Defending': d3f,
                            'Physical': phy,
                            'Skill Moves': skill_moves,
                            'Weak Foot': weak_foot,
                            'Preferred Foot': pref_foot,
                            'Height': height,
                            'Weight': weight,
                            'Transfer Value': transfer_value,
                            'Wage': wage,
                            'Injury': injury})
    return player_info
