'''
Topic: 2D lists and in-place mutation -- ranking, grouping, and
modifying lists/sublists directly (a small player/team management system)
'''

##############################################
def rank_players(players_skills, skills_rank):
##############################################
    result = []

    for i in range(len(players_skills)):
        player = players_skills[i]
        name = player[0]
        total = 0

        # Sum ranking values for each skill the player has (skills can repeat)
        for j in range(1, len(player)):
            skill = player[j]
            found_rank = 0

            # Look up skill in skills_rank; if not found, rank stays 0
            for k in range(len(skills_rank)):
                if skills_rank[k][0] == skill:
                    found_rank = skills_rank[k][1]
                    break

            total = total + found_rank

        result.append([name, total])

    return result


##############################################
def group_ranking(players_rankings):
##############################################
    groups = []

    for i in range(len(players_rankings)):
        name = players_rankings[i][0]
        rank = players_rankings[i][1]

        group_index = -1
        for g in range(len(groups)):
            if groups[g][0] == rank:
                group_index = g
                break

        if group_index == -1:
            groups.append([rank, name])
        else:
            groups[group_index].append(name)

    return groups


##############################################
def build_team(players, team):
##############################################
    teams = []
    current = []

    for i in range(len(players)):
        current.append(players[i])

        if len(current) == team:
            teams.append(current)
            current = []

    if len(current) != 0:
        teams.append(current)

    players.clear()
    for i in range(len(teams)):
        players.append(teams[i])


##############################################
def evaluate_players(players_names, players_scores, threshold):
##############################################
    # iterate backwards so deletions don't skip elements
    for i in range(len(players_names) - 1, -1, -1):
        name = players_names[i]
        total = 0

        # find this player's scores row and sum it
        for r in range(len(players_scores)):
            if players_scores[r][0] == name:
                for s in range(1, len(players_scores[r])):
                    total = total + players_scores[r][s]
                break

        if total < threshold:
            del players_names[i]


##############################################
def find_duplicate(skills):
##############################################
    for i in range(len(skills)):
        name = skills[i][0]
        skill_list = skills[i][1]

        unique = [name]

        for j in range(len(skill_list)):
            sk = skill_list[j]
            already = False

            # check if sk is already in unique (starting from index 1)
            for u in range(1, len(unique)):
                if unique[u] == sk:
                    already = True
                    break

            if not already:
                unique.append(sk)

        skills[i].clear()
        for t in range(len(unique)):
            skills[i].append(unique[t])
