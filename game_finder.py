"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""
from datetime import datetime


def find_qualified_games(game_data, true_shooting_cutoff: int, player_count: int) -> list[int]:
    qualified_game_ids = {}

    for player_stats in game_data:
        game_id = player_stats['gameID']
        true_shooting_percentage = calculate_true_shooting_percentage(player_stats)

        if true_shooting_percentage >= true_shooting_cutoff:
            if game_id in qualified_game_ids:
                qualified_game_ids[game_id] += 1
            else:
                qualified_game_ids[game_id] = 1

    valid_games = [game_id for game_id, count in qualified_game_ids.items() if count >= player_count]

    valid_games_with_dates = {game['gameID']: game['gameDate'] for game in game_data if game['gameID'] in valid_games}
    
    sorted_games = sorted(valid_games_with_dates.items(), key=lambda x: datetime.strptime(x[1], '%m/%d/%Y'), reverse=True)
    return [game_id for game_id, _ in sorted_games]


def calculate_true_shooting_percentage(player_stats: dict) -> float:

	# get this formula from "https://en.wikipedia.org/wiki/True_shooting_percentage"
	points_scored = (2 * player_stats['fieldGoal2Made']
				    + 3 * player_stats['fieldGoal3Made']
					+ player_stats['freeThrowMade'])
	
	total_attempts = (player_stats['fieldGoal2Attempted'] + 
					player_stats['fieldGoal3Attempted'] +
					0.44 * player_stats['freeThrowAttempted'])
	
	if total_attempts == 0:
		return 0 # corner case
	
	true_shooting_percentage = (points_scored / (2 * total_attempts)) * 100
	return true_shooting_percentage

