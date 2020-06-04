import constants
import copy
import random

if __name__ == '__main__':

    # Learned this nice little trick from from https://teamtreehouse.com/library/overwriting-data-in-python
    teams = copy.deepcopy(constants.TEAMS)
    players = copy.deepcopy(constants.PLAYERS)

    # Setting up blank lists to build and sort teams
    exp = []
    inexp = []

    panthers = []
    bandits = []
    warriors = []


    def sort():
        for player in players:
            player['guardians'] = player['guardians'].split(" and ")
            player['height'] = int(player['height'][:2])  # Takes the first few digits from height to make integer
            if player['experience'] == "YES":
                player['experience'] = True
                exp.append(player)
            else:
                player['experience'] = False
                inexp.append(player)


    sort()

    # Length of teams, players, inexperienced, experienced
    team_len = len(teams)
    player_len = len(players)
    players_per_team = int(player_len / team_len)
    exp_len = len(exp)
    inexp_len = len(inexp)
    exp_per_team = int(exp_len / team_len)
    inexp_per_team = int(inexp_len / team_len)

    # Balance the teams
    def balance_teams(team):
        exp_counter = 0
        while exp_counter < exp_per_team:
            team.append(exp.pop(random.randrange(len(exp))))
            exp_counter += 1
        inexp_counter = 0
        while inexp_counter < inexp_per_team:
            team.append(inexp.pop(random.randrange(len(inexp))))
            inexp_counter += 1


    balance_teams(panthers)
    balance_teams(bandits)
    balance_teams(warriors)

    # Make the teams
    def make_teams(team):

        # Players
        player_names = []
        for player in team:
            player_names.append(player['name'])
        print("Player Names: ", ", ".join(player_names))

        # Player count
        player_count = 0
        for _ in team:  # the underscore is used for an unused variable, which I originally had as 'player' before
            player_count += 1
        print("Number of Players: ", player_count)

        # Experienced count
        exp_count = 0
        for player in team:
            if player['experience']:
                exp_count += 1
        print("Number of Experienced Players: ", exp_count)

        # Inexperienced count
        inexp_count = 0
        for player in team:
            if player['experience']:
                inexp_count += 1
        print("Number of Inexperienced Players: ", inexp_count)

        # Height
        total_height = 0
        for player in team:
            total_height += player['height']
        average_height = float(total_height / player_count)
        print("Average Height of Players: {0:.2f}".format(average_height))

        # Guardians
        guardians = []
        for player in team:
            guardians.extend(player['guardians'])
        print("Guardians: ", ", ".join(guardians))

    def main():
        while True:
            try:
                print("MENU\n\n")
                print("What would you like to do?: \n 1) Display Team Stats \n 2) Quit \n")
                starting_input = int(input())

                if starting_input == 2:
                    print("Thank you! Goodbye.")
                    break
                elif starting_input > 2:
                    print("Pick a valid number please.\n")
                elif starting_input < 1:
                    print("Pick a valid number please.\n")

                elif starting_input == 1:
                    start_game = True
                    while start_game:
                        print("\n Which team would you like to see?: \n 1) Panthers \n 2) Bandits \n 3) Warriors "
                              "\n 4) Return to Main Menu")
                        try:
                            pick_team = int(input())
                            if pick_team > 4:
                                print("Pick a valid number please.\n")
                            if pick_team == 1:
                                print("\nPanthers:")
                                make_teams(panthers)
                            elif pick_team == 2:
                                print("\nBandits:")
                                make_teams(bandits)
                            elif pick_team == 3:
                                print("\nWarriors:")
                                make_teams(warriors)
                            elif pick_team <= 0:
                                print("Pick a valid number please.\n")
                            elif pick_team == 4:
                                break
                        except ValueError:
                            print("Pick a valid number please.\n")
            except ValueError:
                print("Pick a valid number please.\n")


    main()
