"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""

def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:
    results = [] # To store the final list of qualified game IDs
    unique_game_ids = [] # To keep track of game IDs that meet the true shooting cutoff
    
    # Sort the game data by gameDate in descending order (most recent first)
    game_data.sort(key=lambda x: x['gameDate'], reverse=True)
    for game in game_data:
        
        # Calculate the player's True Shooting percentage using the formula
        player_true_shooting = (game['fieldGoal2Made'] * 2 + game['fieldGoal3Made'] * 3 + game['freeThrowMade']) / (2 * (game['fieldGoal2Attempted'] + game['fieldGoal3Attempted'] + (0.44 * game['freeThrowAttempted'])))
        
        # Check if the player's True Shooting percentage meets or exceeds the cutoff
        if player_true_shooting * 100 >= true_shooting_cutoff:
            unique_game_ids.append(game['gameID'])
    
    # Now, check for game IDs that have enough qualifying players
    for id in unique_game_ids:
        if unique_game_ids.count(id) >= player_count and id not in results:
            results.append(id) # Add the game ID to the final results list
    return results # Return the list of qualified game IDs
 