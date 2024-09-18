from game_finder import find_qualified_games

def test_case_4():
    game_data = [
        {'gameID': 9, 'playerID': 24, 'gameDate': '01/02/2023', 'fieldGoal2Attempted': 14, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 2, 'freeThrowAttempted': 4, 'freeThrowMade': 3},
        {'gameID': 9, 'playerID': 35, 'gameDate': '01/02/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 2, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 1, 'freeThrowAttempted': 4, 'freeThrowMade': 2},
        {'gameID': 9, 'playerID': 34, 'gameDate': '01/02/2023', 'fieldGoal2Attempted': 8, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 0, 'freeThrowAttempted': 3, 'freeThrowMade': 1},
        {'gameID': 9, 'playerID': 42, 'gameDate': '01/02/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 2, 'freeThrowAttempted': 4, 'freeThrowMade': 0},
        {'gameID': 10, 'playerID': 24, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 8, 'fieldGoal2Made': 7, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 0, 'freeThrowAttempted': 8, 'freeThrowMade': 1},
        {'gameID': 10, 'playerID': 42, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 8, 'fieldGoal2Made': 7, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 1, 'freeThrowAttempted': 2, 'freeThrowMade': 1},
        {'gameID': 10, 'playerID': 25, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 2, 'freeThrowAttempted': 4, 'freeThrowMade': 3},
        {'gameID': 10, 'playerID': 33, 'gameDate': '01/09/2023', 'fieldGoal2Attempted': 6, 'fieldGoal2Made': 2, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 0, 'freeThrowAttempted': 2, 'freeThrowMade': 1},
        {'gameID': 6, 'playerID': 34, 'gameDate': '02/11/2023', 'fieldGoal2Attempted': 12, 'fieldGoal2Made': 6, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 1, 'freeThrowAttempted': 6, 'freeThrowMade': 6},
        {'gameID': 6, 'playerID': 25, 'gameDate': '02/11/2023', 'fieldGoal2Attempted': 9, 'fieldGoal2Made': 2, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 2, 'freeThrowAttempted': 2, 'freeThrowMade': 0},
        {'gameID': 5, 'playerID': 42, 'gameDate': '01/06/2023', 'fieldGoal2Attempted': 4, 'fieldGoal2Made': 3, 'fieldGoal3Attempted': 6, 'fieldGoal3Made': 2, 'freeThrowAttempted': 3, 'freeThrowMade': 3},
        {'gameID': 4, 'playerID': 34, 'gameDate': '01/22/2023', 'fieldGoal2Attempted': 18, 'fieldGoal2Made': 5, 'fieldGoal3Attempted': 5, 'fieldGoal3Made': 3, 'freeThrowAttempted': 2, 'freeThrowMade': 1},
    ]
    qualified_games = find_qualified_games(game_data, 52, 1)
    assert qualified_games == [6, 10, 5]