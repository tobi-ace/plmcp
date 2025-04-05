# PLMCP

This repository contains the source code for the tutorial "Build an MCP Server in Python" published on Medium. The project demonstrates how to build an MCP server using Python to provide live Premier League football data.

## 📖 Tutorial

For a detailed explanation of how this project works, check out the full tutorial on Medium: [Build an MCP Server in Python](https://medium.com/@jimohtobi/build-an-mcp-server-in-5-minutes-686b632303ed)

## 📋 Prerequisites

- An API key from [football-data.org](https://www.football-data.org/)
- UV library 
- FastMCP library

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/plmcp.git
cd plmcp
```

2. Install the required packages:
```bash
uv pip install fastmcp requests python-dotenv
```

3. Set up your environment variables:
```bash
# Create a .env file and add your API key
FOOTBALL_API_KEY=your_api_key_here
```

## 🚦 Usage

 Start the MCP server:
```bash
fastmcp install server.py
```

The server provides the following tools:
- `get_team_ids()`: Get a mapping of team names to their IDs
- `get_premier_league_table()`: Get current Premier League standings
- `get_team_results(team_id)`: Get recent results for a specific team
- `get_team_fixtures(team_id)`: Get upcoming fixtures for a specific team
- `get_latest_league_results()`: Get the most recent Premier League match results

Each tool returns clean, formatted JSON responses that are easy for an LLM to work with.


