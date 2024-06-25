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
                            row[61], row[62], row[63], row[64], row[65], row[66], row[67], row[68], row[69]))
    return squad


# Call above functions to reduce clutter in the app.py file
def initialise_squad(file):
    players = parse_html(file)
    squad = create_player_objects(players)
    return squad


# Returns a list of each player's position (Goalkeeper, Defender, Midfielder, Attacker)
def store_positions(squad):
    positions = []
    for player in squad:
        positions.append({'Position': player.find_position()})
    return positions


def calculate_player_info(squad):
    player_info = []
    for player in squad:
        player_id = player.get_id()
        nation = player.get_nationality()
        name = player.get_name()
        age = player.get_age()
        club = player.get_club()
        division = player.get_division()
        squad_number = player.get_squad_num()
        personality = player.get_personality()
        int_caps = player.get_int_caps()
        int_goals = player.get_int_goals()
        szn_apps = player.get_szn_apps()
        avg_rating = player.get_avg_rating()
        szn_goals = player.get_szn_goals()
        szn_assists = player.get_szn_assists()
        pac = player.calculate_pace()
        sho = player.calculate_shooting()
        pas = player.calculate_passing()
        dri = player.calculate_dribbling()
        d3f = player.calculate_defending()
        phy = player.calculate_physical()
        skill_moves, weak_foot = player.calc_sm_wf()
        pref_foot = player.get_pref_foot()
        height = player.get_height()
        weight = player.get_weight()
        transfer_value = player.calc_transfer_val()
        wage = player.get_wage()
        injury = player.get_injury()

        position_overalls = player.calculate_overall()

        best_overall = 0
        for ovr in position_overalls:
            if ovr > best_overall:
                best_overall = ovr

        positions = ["FB", "WB", "CB", "DM", "CM", "AM", "W", "IF", "ST"]

        if len(position_overalls) > 1:
            print(name, "best overall:", best_overall)
            for i in range(len(position_overalls)):
                if position_overalls[i] > 0:
                    print(name, "-", positions[i], ":", position_overalls[i])

        player_info.append({'Player ID': player_id,
                            'Nation': nation,
                            'Name': name,
                            'Age': age,
                            'Club': club,
                            'Division': division,
                            'Squad Number': squad_number,
                            'Personality': personality,
                            'International Appearances': int_caps,
                            'International Goals': int_goals,
                            'Season Appearances': szn_apps,
                            'Average Rating': avg_rating,
                            'Season Goals': szn_goals,
                            'Season Assists': szn_assists,
                            'Best Overall': best_overall,
                            'Position Overalls': position_overalls,
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
        print(player_info)
    return player_info
