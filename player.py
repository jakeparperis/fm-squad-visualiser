import math


class Player:
    def __init__(self, id, name, position, age, nationality, personality, squad_num, club, division,
                 transfer_val, wage, injury, height, weight, left_foot, right_foot, pref_foot, all_apps, all_goals,
                 int_caps, int_goals, szn_apps, avg_rating, szn_xg, szn_goals, szn_assists, acceleration, aerial_reach,
                 aggression, agility, anticipation, balance, bravery, command_of_area, communication, composure,
                 concentration, corners, crossing, decisions, determination, dribbling, eccentricity, finishing,
                 first_touch, flair, free_kicks, handling, heading, jumping_reach, kicking, leadership, long_shots,
                 long_throws, marking, natural_fitness, off_the_ball, one_on_ones, pace, passing, penalties,
                 positioning, punching, reflexes, rushing_out, stamina, strength, tackling, teamwork, technique,
                 throwing, vision, work_rate):

        self.id = id
        self.name = name
        self.position = position
        self.age = int(age)
        self.nationality = nationality
        self.personality = personality
        self.squad_num = squad_num
        self.club = club
        self.division = division
        self.transfer_val = transfer_val
        self.wage = wage
        self.injury = injury
        self.height = height
        self.weight = weight
        self.left_foot = left_foot
        self.right_foot = right_foot
        self.pref_foot = pref_foot
        self.all_apps = all_apps
        self.all_goals = all_goals
        self.int_caps = int_caps
        self.int_goals = int_goals
        self.szn_apps = szn_apps
        self.avg_rating = avg_rating
        self.szn_xg = szn_xg
        self.szn_goals = szn_goals
        self.szn_assists = szn_assists
        self.acceleration = int(acceleration)
        self.aerial_reach = int(aerial_reach)
        self.aggression = int(aggression)
        self.agility = int(agility)
        self.anticipation = int(anticipation)
        self.balance = int(balance)
        self.bravery = int(bravery)
        self.command_of_area = int(command_of_area)
        self.communication = int(communication)
        self.composure = int(composure)
        self.concentration = int(concentration)
        self.corners = int(corners)
        self.crossing = int(crossing)
        self.decisions = int(decisions)
        self.determination = int(determination)
        self.dribbling = int(dribbling)
        self.eccentricity = int(eccentricity)
        self.finishing = int(finishing)
        self.first_touch = int(first_touch)
        self.flair = int(flair)
        self.free_kicks = int(free_kicks)
        self.handling = int(handling)
        self.heading = int(heading)
        self.jumping_reach = int(jumping_reach)
        self.kicking = int(kicking)
        self.leadership = int(leadership)
        self.long_shots = int(long_shots)
        self.long_throws = int(long_throws)
        self.marking = int(marking)
        self.natural_fitness = int(natural_fitness)
        self.off_the_ball = int(off_the_ball)
        self.one_on_ones = int(one_on_ones)
        self.pace = int(pace)
        self.passing = int(passing)
        self.penalties = int(penalties)
        self.positioning = int(positioning)
        self.punching = int(punching)
        self.reflexes = int(reflexes)
        self.rushing_out = int(rushing_out)
        self.stamina = int(stamina)
        self.strength = int(strength)
        self.tackling = int(tackling)
        self.teamwork = int(teamwork)
        self.technique = int(technique)
        self.throwing = int(throwing)
        self.vision = int(vision)
        self.work_rate = int(work_rate)

    # Getters

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def get_age(self):
        return self.age

    def get_nationality(self):
        return self.nationality

    def get_personality(self):
        return self.personality

    def get_squad_num(self):
        return self.squad_num

    def get_club(self):
        return self.club

    def get_division(self):
        return self.division

    def get_transfer_val(self):
        return self.transfer_val

    def get_wage(self):
        return self.wage

    def get_injury(self):
        return self.injury

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_left_foot(self):
        return self.left_foot

    def get_right_foot(self):
        return self.right_foot

    def get_pref_foot(self):
        return self.pref_foot

    def get_all_apps(self):
        return self.all_apps

    def get_all_goals(self):
        return self.all_goals

    def get_int_caps(self):
        return self.int_caps

    def get_int_goals(self):
        return self.int_goals

    def get_szn_apps(self):
        return self.szn_apps

    def get_avg_rating(self):
        return self.avg_rating

    def get_szn_xg(self):
        return self.szn_xg

    def get_szn_goals(self):
        return self.szn_goals

    def get_szn_assists(self):
        return self.szn_assists

    def set_name(self, new_name):
        self.name = new_name

    # Conversion calculation

    def calculate_pace(self):
        fm_pace = (self.pace * 0.35 + self.acceleration * 0.65)
        pace = math.ceil(fm_pace * 5.5)
        pace = min(pace, 99)
        return pace

    def calculate_shooting(self):
        fm_shooting = (self.finishing * 0.85 + self.free_kicks * 0.02 + self.long_shots * 0.02 + self.penalties * 0.02 +
                       self.technique * 0.045 + self.composure * 0.045)
        shooting = math.ceil(fm_shooting * 5.5)
        shooting = min(shooting, 99)
        return shooting

    def calculate_passing(self):
        fm_passing = (self.crossing * 0.08 + self.passing * 0.68 + self.technique * 0.08 + self.decisions * 0.08 +
                      self.vision * 0.08)
        passing = math.ceil(fm_passing * 5.5)
        passing = min(passing, 99)
        return passing

    def calculate_dribbling(self):
        fm_dribbling = (self.dribbling * 0.70 + self.first_touch * 0.05 + self.technique * 0.05 +
                        self.composure * 0.05 + self.flair * 0.05 + self.agility * 0.05 + self.balance * 0.05)
        dribbling = math.ceil(fm_dribbling * 5.5)
        dribbling = min(dribbling, 99)
        return dribbling

    def calculate_defending(self):
        fm_defending = (self.marking * 0.3 + self.tackling * 0.3 + self.aggression * 0.017 + self.anticipation * 0.017 +
                        self.bravery * 0.017 + self.composure * 0.017 + self.concentration * 0.017 +
                        self.decisions * 0.017 + self.positioning * 0.3)
        defending = math.ceil(fm_defending * 5.75)
        defending = min(defending, 99)
        return defending

    def calculate_physical(self):
        fm_physical = (self.jumping_reach * 0.20 + self.natural_fitness * 0.05 + self.stamina * 0.30 +
                       self.strength * 0.45)
        physical = math.ceil(fm_physical * 5.5)
        physical = min(physical, 99)
        return physical

    def calculate_overall(self):
        # Positions by index:
        # FB = 0
        # WB = 1
        # CB = 2
        # DM = 3
        # CM = 4
        # AM = 5
        # WM = 6
        # W = 7
        # ST = 8

        ovr = []

        if self.position == "GK":
            gk_ovr = (self.aerial_reach * 0.1825 + self.command_of_area * 0.03 + self.communication * 0.03 +
                      self.handling * 0.1825 + self.kicking * 0.03 + self.reflexes * 0.1825 +
                      self.concentration * 0.03 + self.positioning * 0.03 + self.agility * 0.1825 +
                      self.one_on_ones * 0.03 + self.throwing * 0.03 + self.anticipation * 0.03 + self.decisions * 0.03)

            sk_ovr = (self.command_of_area * 0.03 + self.kicking * 0.03 + self.one_on_ones * 0.03 +
                      self.reflexes * 0.1375 + self.rushing_out * 0.03 + self.anticipation * 0.03 +
                      self.composure * 0.03 + self.concentration * 0.03 + self.positioning * 0.03 +
                      self.agility * 0.1375 + self.aerial_reach * 0.1375 + self.communication * 0.03 +
                      self.first_touch * 0.03 + self.handling * 0.1375 + self.passing * 0.03 + self.throwing * 0.03 +
                      self.decisions * 0.03 + self.vision * 0.03 + self.acceleration * 0.03)

            gk_ovr = math.ceil(gk_ovr * 5.11875)
            gk_ovr = min(gk_ovr, 99)
            sk_ovr = math.ceil(sk_ovr * 5.60625)
            sk_ovr = min(sk_ovr, 99)

            if gk_ovr > sk_ovr:
                ovr.append(gk_ovr)
            else:
                ovr.append(sk_ovr)

        else:
            # All outfield weightings are 0.75/nPrimary and 0.25/nSecondary
            # For example, FB-s weightings are 0.75/8 (0.09375) and 0.25/7 (0.0357142857142857)

            ovr.append(0)
            # Full Back - 1 - FB-s with 8 primary and 7 secondary attributes
            fullback = (self.marking * 0.09375 + self.tackling * 0.09375 + self.anticipation * 0.09375 +
                        self.concentration * 0.09375 + self.positioning * 0.09375 + self.teamwork * 0.09375 +
                        self.acceleration * 0.09375 + self.pace * 0.09375 + self.crossing * 0.0357142857142857 +
                        self.dribbling * 0.0357142857142857 + self.passing * 0.0357142857142857 +
                        self.technique * 0.0357142857142857 + self.work_rate * 0.0357142857142857 +
                        self.decisions * 0.0357142857142857 + self.stamina * 0.0357142857142857)
            fullback = math.ceil(fullback * 4.14375)
            fullback = min(fullback, 99)
            ovr.append(fullback)

            # Wing Back - 2 - WB-a with 10 primary and 10 secondary attributes
            wingback = (self.crossing * 0.075 + self.dribbling * 0.075 + self.tackling * 0.075 +
                        self.technique * 0.075 + self.off_the_ball * 0.075 + self.teamwork * 0.075 +
                        self.work_rate * 0.075 + self.acceleration * 0.075 + self.pace * 0.075 + self.stamina * 0.075 +
                        self.first_touch * 0.025 + self.marking * 0.025 + self.passing * 0.025 +
                        self.anticipation * 0.025 + self.concentration * 0.025 + self.decisions * 0.025 +
                        self.flair * 0.025 + self.positioning * 0.025 + self.agility * 0.025 + self.balance * 0.025)
            wingback = math.ceil(wingback * 5.60625)
            wingback = min(wingback, 99)
            ovr.append(wingback)

            # Centre Back - 3 - CD-d with 8 primary and 6 secondary attributes
            centreback = (self.heading * 0.09375 + self.marking * 0.09375 + self.tackling * 0.09375 +
                          self.positioning * 0.09375 + self.jumping_reach * 0.09375 + self.strength * 0.09375 +
                          self.acceleration * 0.09375 + self.pace * 0.09375 + self.aggression * 0.0416666666666667 +
                          self.anticipation * 0.0416666666666667 + self.bravery * 0.0416666666666667 +
                          self.composure * 0.0416666666666667 + self.concentration * 0.0416666666666667 +
                          self.decisions * 0.0416666666666667)
            centreback = math.ceil(centreback * 5.3625)
            centreback = min(centreback, 99)
            ovr.append(centreback)

            # Defensive Midfielder - 4
            dmid = (self.tackling * 0.15 + self.anticipation * 0.15 + self.concentration * 0.15 +
                    self.positioning * 0.15 + self.teamwork * 0.15 + self.first_touch * 0.03 + self.marking * 0.03 +
                    self.passing * 0.03 + self.aggression * 0.03 + self.composure * 0.03 + self.decisions * 0.03 +
                    self.work_rate * 0.03 + self.stamina * 0.03 + self.strength)
            dmid = math.ceil(dmid * 2.68125)
            dmid = min(dmid, 99)
            ovr.append(dmid)

            # Central Midfielder - 5
            cmid = (self.first_touch * 0.15 + self.passing * 0.15 + self.tackling * 0.15 + self.decisions * 0.15 +
                    self.teamwork * 0.15 + self.technique * 0.025 + self.anticipation * 0.025 +
                    self.composure * 0.025 + self.concentration * 0.025 + self.off_the_ball * 0.025 +
                    self.vision * 0.025 + self.work_rate * 0.025 + self.stamina * 0.025 + self.pace * 0.025 +
                    self.acceleration * 0.025)
            cmid = math.ceil(cmid * 5.484375)
            cmid = min(cmid, 99)
            ovr.append(cmid)

            # Attacking Midfielder - 6
            amid = (self.first_touch * 0.09375 + self.long_shots * 0.09375 + self.passing * 0.09375 +
                    self.technique * 0.09375 + self.anticipation * 0.09375 + self.decisions * 0.09375 +
                    self.flair * 0.09375 + self.off_the_ball * 0.09375 + self.dribbling * 0.0416666666666667
                    + self.composure * 0.0416666666666667 + self.vision * 0.0416666666666667 +
                    self.agility * 0.0416666666666667 + self.pace * 0.0416666666666667 +
                    self.acceleration * 0.0416666666666667)
            amid = math.ceil(amid * 5.60625)
            amid = min(amid, 99)
            ovr.append(amid)

            # Winger - 7
            winger = (self.crossing * 0.15 + self.dribbling * 0.15 + self.technique * 0.15 + self.acceleration * 0.15 +
                      self.agility * 0.15 + self.first_touch * 0.0357142857142857 + self.passing * 0.0357142857142857 +
                      self.off_the_ball * 0.0357142857142857 + self.work_rate * 0.0357142857142857 +
                      self.balance * 0.0357142857142857 + self.pace * 0.0357142857142857
                      + self.stamina * 0.0357142857142857)
            winger = math.ceil(winger * 5.3625)
            winger = min(winger, 99)
            ovr.append(winger)

            # Inside Forward - 8
            fwd = (self.dribbling * 0.09375 + self.finishing * 0.09375 + self.first_touch * 0.09375 +
                   self.technique * 0.09375 + self.anticipation * 0.09375 + self.off_the_ball * 0.09375 +
                   self.acceleration * 0.09375 + self.agility * 0.09375 + self.long_shots * 0.03125 +
                   self.passing * 0.03125 + self.composure * 0.03125 + self.flair * 0.03125 +
                   self.work_rate * 0.03125 + self.balance * 0.03125 + self.pace * 0.03125 +
                   self.stamina * 0.03125)
            fwd = math.ceil(fwd * 5.3625)
            fwd = min(fwd, 99)
            ovr.append(fwd)

            # Striker - 9
            striker = (self.dribbling * 0.07 + self.finishing * 0.07 + self.first_touch * 0.07 +
                       self.heading * 0.07 + self.technique * 0.07 + self.anticipation * 0.07 +
                       self.composure * 0.07 + self.off_the_ball * 0.07 + self.acceleration * 0.07 +
                       self.agility * 0.07 + self.strength * 0.07)
            striker = math.ceil(striker * 7.190625)
            striker = min(striker, 99)
            ovr.append(striker)

        return ovr

    def calc_sm_wf(self):
        weak_foot = ""
        skill_moves = 0

        if 18 <= self.flair <= 20:
            skill_moves = 5
        elif 15 <= self.flair <= 17:
            skill_moves = 4
        elif 12 <= self.flair <= 14:
            skill_moves = 3
        elif 9 <= self.flair <= 11:
            skill_moves = 2
        else:
            skill_moves = 1

        if self.pref_foot == "Right":
            if self.left_foot == "Very Strong" or self.left_foot == "Strong":
                weak_foot = 5
            elif self.left_foot == "Fairly Strong":
                weak_foot = 4
            elif self.left_foot == "Reasonable":
                weak_foot = 3
            elif self.left_foot == "Weak":
                weak_foot = 2
            else:
                weak_foot = 1
        else:
            if self.right_foot == "Very Strong" or self.right_foot == "Strong":
                weak_foot = 5
            elif self.right_foot == "Fairly Strong":
                weak_foot = 4
            elif self.right_foot == "Reasonable":
                weak_foot = 3
            elif self.right_foot == "Weak":
                weak_foot = 2
            else:
                weak_foot = 1

        return skill_moves, weak_foot

    def calc_transfer_val(self):
        transfer_value_range = self.transfer_val
        base = ""
        max_value = ""

        if "M" in transfer_value_range:
            base = "m"
        elif "K" in transfer_value_range:
            base = "k"
        currency = transfer_value_range[0]

        chars = []
        startpoint = 0

        for i in range(len(transfer_value_range)):
            current_char = transfer_value_range[i]
            chars.append(current_char)
            if current_char == "-":
                startpoint = i
        for j in range(startpoint, len(chars)):
            current_char = chars[j]
            if current_char.isdigit() or current_char == ".":
                max_value += current_char

        transfer_value = currency + max_value + base

        return transfer_value
