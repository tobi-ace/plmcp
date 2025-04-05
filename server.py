import os
import requests
from datetime import datetime
from dotenv import load_dotenv

from fastmcp import FastMCP

load_dotenv()

mcp = FastMCP("Premier League Updates", dependencies=["requests", "python-dotenv"])

BASE_URL = "https://api.football-data.org/v4"
HEADERS = {
    'X-Auth-Token': os.getenv('FOOTBALL_API_KEY')
}



@mcp.tool()
def get_premier_league_table():
    """
    Get the current Premier League standings
    :return: JSON response with the current Premier League standings
    """
    url = f"{BASE_URL}/competitions/PL/standings"
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    
    # Extract and clean up the standings data
    cleaned_standings = []
    
    if 'standings' in data and len(data['standings']) > 0:
        table = data['standings'][0]['table']
        for team in table:
            cleaned_standings.append({
                'position': team['position'],
                'team': team['team']['name'],
                'points': team['points'],
                'wins': team['won'],
                'draws': team['draw'],
                'losses': team['lost']
            })
    
    return {'standings': cleaned_standings}

@mcp.tool()
def get_team_results(team_id: str) -> dict:
    """
    Get the recent matches for a specific team
    :param team_id: The ID of the team
    :return: JSON response with the team's last 5 matches
    """
    url = f"{BASE_URL}/teams/{team_id}/matches"
    params = {
        'status': 'FINISHED',
        'limit': 5
    }
    response = requests.get(url, headers=HEADERS, params=params)
    data = response.json()
    
    cleaned_results = []
    if 'matches' in data:
        for match in data['matches']:
            result = {
                'date': match['utcDate'].split('T')[0],
                'competition': match['competition']['name'],
                'home_team': match['homeTeam']['name'],
                'away_team': match['awayTeam']['name'],
                'score': f"{match['score']['fullTime']['home']} - {match['score']['fullTime']['away']}",
                'winner': match['score']['winner'].replace('_TEAM', '') if match['score']['winner'] else 'DRAW'
            }
            cleaned_results.append(result)
    
    return {'results': cleaned_results}

@mcp.tool()
def get_team_fixtures(team_id: str) -> dict:
    """
    Get the upcoming fixtures for a specific team
    :param team_id: The ID of the team
    :return: JSON response with the team's next 5 fixtures
    """
    url = f"{BASE_URL}/teams/{team_id}/matches"
    params = {
        'status': 'SCHEDULED',
        'limit': 5
    }
    response = requests.get(url, headers=HEADERS, params=params)
    data = response.json()
    
    cleaned_fixtures = []
    if 'matches' in data:
        for match in data['matches']:
            fixture = {
                'date': match['utcDate'].split('T')[0],
                'competition': match['competition']['name'],
                'home_team': match['homeTeam']['name'],
                'away_team': match['awayTeam']['name'],
                'kickoff': match['utcDate'].split('T')[1].split('Z')[0]
            }
            cleaned_fixtures.append(fixture)
    
    return {'fixtures': cleaned_fixtures}

@mcp.tool()
def get_latest_league_results() -> dict:
    """
    Get the latest Premier League match results
    :return: JSON response with the most recent Premier League matches
    """
    url = f"{BASE_URL}/competitions/PL/matches"
    params = {
        'status': 'FINISHED',
        'limit': 10,  
        'competitions': 'PL'
    }
    response = requests.get(url, headers=HEADERS, params=params)
    data = response.json()
    
    cleaned_results = []
    if 'matches' in data:
        for match in data['matches']:
            result = {
                'date': match['utcDate'].split('T')[0],
                'home_team': match['homeTeam']['name'],
                'away_team': match['awayTeam']['name'],
                'score': f"{match['score']['fullTime']['home']} - {match['score']['fullTime']['away']}",
                'winner': match['score']['winner'].replace('_TEAM', '') if match['score']['winner'] else 'DRAW'
            }
            cleaned_results.append(result)
    
    return {'latest_results': cleaned_results}

@mcp.tool()
def get_team_ids():
    """
    Return a dictionary of team names and their corresponding IDs
    """
    return {
            'arsenal': 57,
            'aston villa': 58,
            'bournemouth': 1044,
            'brentford': 402,
            'brighton': 397,
            'chelsea': 61,
            'crystal palace': 354,
            'everton': 62,
            'fulham': 63,
            'liverpool': 64,
            'manchester city': 65,
            'manchester united': 66,
            'newcastle': 67,
            'nottingham forest': 351,
            'tottenham': 73,
            'west ham': 563,
            'wolves': 76,
            'southampton': 340,
            'ipswich town': 349,
            'leicester city': 338
        }
