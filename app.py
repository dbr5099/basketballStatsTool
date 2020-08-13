import copy
import constants


players_copy = copy.deepcopy(constants.PLAYERS)
teams_copy = copy.deepcopy(constants.TEAMS)
Teams = dict.fromkeys(teams_copy, [])
Panthers = []
Bandits = []
Warriors = []

NUM_PLAYERS_TEAM = len(constants.PLAYERS) / len(constants.TEAMS)


def clean_height():
    for player in players_copy:
        player['height'] = int(player['height'][:2])


def clean_experience():
    for player in players_copy:
        player['experience'] = True if player['experience'].lower() == 'yes' else False


def clean_guardians():
    for player in players_copy:
        player['guardians'] = player['guardians'].split(' and ')


def random_player_balance():
    exp = 0
    for player in players_copy:
        if player['experience'] == bool('TRUE'):
            exp += 1
    num_exp_players_team = exp / len(constants.TEAMS)
    num_non_exp_players_team = NUM_PLAYERS_TEAM - num_exp_players_team

    count = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for player in players_copy:
        if player['experience'] == bool('TRUE') and count < num_exp_players_team:
            Panthers.append(player)
            count += 1
        elif player['experience'] == bool('TRUE') and count2 < num_exp_players_team:
            Bandits.append(player)
            count2 += 1
        elif player['experience'] == bool('') and count3 < num_non_exp_players_team:
            Panthers.append(player)
            count3 += 1
        elif player['experience'] == bool('') and count4 < num_non_exp_players_team:
            Bandits.append(player)
            count4 += 1
        else:
            Warriors.append(player)


def start_menu():
    print("\nBASKETBALL TEAM STATS TOOL")
    print("\n---- MENU----")
    print("\nHere are your choices:")
    print("1) Display Team Stats \n2) Quit")
    choice = input("\nEnter an option > ")
    next = False
    while next is False:
        if choice == "1":
            next = True
            team_menu()
        elif choice == "2":
            next = True
            print("\nGoodbye")
        else:
            print("That was not a valid option.")
            choice = input("\nEnter an option > ")


def team_menu():
        print("\nChoose a team:\n", " 1) Panthers\n", " 2) Bandits\n", " 3) Warriors\n", " 4) Quit\n")
        team = input("\nChoose an option > ")
        next = False
        while next is False:
            if team == '1':
                next = True
                print('\nTeam: Panthers Stats\n')
                print('--------------------')
                stats(Panthers)
            elif team == '2':
                next = True
                print('\nTeam: Bandits Stats\n')
                print('--------------------')
                stats(Bandits)
            elif team == '3':
                next = True
                print('\nTeam: Warriors Stats\n')
                print('--------------------')
                stats(Warriors)
            elif team == '4':
                next = True
                print('\nGoodbye\n')
            else:
                print('The selection was not a valid option')
                team = input("\nChoose an option > ")


def stats(input_team):
    total_height = 0
    exp = 0
    players_list = []
    guardians_list = []
    for player in input_team:
        total_height += player['height']
        players_list.append(player['name'])
        guardians_list.extend(player['guardians'])
        if player['experience'] == bool('TRUE'):
            exp += 1
    average_height = round(total_height / len(input_team), 2)

    print(f'Total players: {len(input_team)}')
    print(f'Total experienced: {exp}')
    print(f'Total inexperienced: {exp}')
    print(f'Average height: {average_height}')
    print('\nPlayers on Team: \n ' + ', '.join(players_list))
    print('\nGuardians: \n ' + ', '.join(guardians_list))
    input('\nPress ENTER to continue... ')
    start_menu()

if __name__ == "__main__":
    clean_height()
    clean_experience()
    clean_guardians()
    random_player_balance()
    start_menu()
