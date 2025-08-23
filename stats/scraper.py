import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
from datetime import datetime
import re

"""
This module provides web scraping functionalities to extract football statistics
from Wikipedia pages. It includes functions to scrape top scorers, hat-tricks,
and clean sheets data.
"""

def scrape_top_scorers(url):
    """
    Scrapes top scorers data from a given Wikipedia URL.

    Args:
        url (str): The URL of the Wikipedia page containing top scorers data.

    Returns:
        list: A list of dictionaries, each containing player name, team, and goals.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        tables = soup.find_all("table", {"class": "wikitable"})
        if not tables:
            print("No wikitable found on the page.")
            return []

        print(f"Found {len(tables)} wikitable(s) on the page.")

        top_scorers_table = None
        for i, table in enumerate(tables):
            headers = [th.get_text(strip=True).lower().split("[")[0].strip() for th in table.find_all("th")]
            print(f"Table {i} headers: {headers}")
            if "player" in headers and "goals" in headers:
                top_scorers_table = table
                print(f"Top scorers table found at index {i}.")
                break

        if not top_scorers_table:
            print("Top scorers table not found by header check. Trying fallback index.")
            try:
                top_scorers_table = tables[5]
                print("Using table at index 5 as fallback.")
            except IndexError:
                print("Fallback table index out of range.")
                return []

        df = pd.read_html(StringIO(str(top_scorers_table)))[0]
        print(f"DataFrame columns: {list(df.columns)}")

        df.columns = [col.strip().replace("\xa0", " ").lower().split("[")[0].strip() for col in df.columns]

        players = []
        seen = set()  # To track unique player-team combinations
        for _, row in df.iterrows():
            player_name = row.get("player") or row.get("name") or row.get("scorer")
            team = row.get("team") or row.get("club")
            goals = row.get("goals", 0)

            if pd.isna(player_name) or player_name is None:
                continue

            player_name = re.sub(r"\d+$", "", str(player_name)).strip().lower().capitalize()
            team = str(team).strip().lower().capitalize()

            key = (player_name, team)  # Unique key to avoid duplicates
            if key in seen:
                continue
            seen.add(key)

            try:
                goals = int(goals) if pd.notna(goals) else 0
            except (ValueError, TypeError):
                goals = 0

            players.append({
                "name": player_name,
                "team": team,
                "goals": goals
            })

        print(f"Extracted {len(players)} unique players: {players}")
        return players

    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []
    except ValueError as e:
        print(f"Error parsing table: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def scrape_hat_tricks(url):
    """
    Scrapes hat-tricks data from a given Wikipedia URL.

    Args:
        url (str): The URL of the Wikipedia page containing hat-tricks data.

    Returns:
        list: A list of dictionaries, each containing hat-trick details.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        tables = soup.find_all("table", {"class": "wikitable"})
        if not tables:
            print("No wikitable found on the page.")
            return []

        print(f"Found {len(tables)} wikitable(s) on the page.")

        hat_tricks_table = None
        for i, table in enumerate(tables):
            headers = [th.get_text(strip=True).lower().split("[")[0].strip() for th in table.find_all("th")]
            print(f"Table {i} headers: {headers}")
            if "player" in headers and "date" in headers and "result" in headers:
                hat_tricks_table = table
                print(f"Hat-tricks table found at index {i}.")
                break

        if not hat_tricks_table:
            print("Hat-tricks table not found by header check. Trying fallback index.")
            try:
                hat_tricks_table = tables[6]
                print("Using table at index 6 as fallback.")
            except IndexError:
                print("Fallback table index out of range.")
                return []

        df = pd.read_html(StringIO(str(hat_tricks_table)))[0]
        print(f"DataFrame columns: {list(df.columns)}")

        df.columns = [col.strip().replace("\xa0", " ").lower().split("[")[0].strip() for col in df.columns]

        hat_tricks = []
        seen = set()  # To track unique player-team-against-date combinations
        for _, row in df.iterrows():
            player_name = row.get("player") or row.get("name") or row.get("scorer")
            for_team = row.get("for") or row.get("for team")
            against = row.get("against")
            result = row.get("result")
            date_str = row.get("date")

            if pd.isna(player_name) or player_name is None:
                continue

            player_name = re.sub(r"\d+$", "", str(player_name)).strip().lower().capitalize()
            for_team = re.sub(r"\[\d+\]", "", str(for_team)).strip().lower().capitalize()
            against = re.sub(r"\[\d+\]", "", str(against)).strip().lower().capitalize()
            result = re.sub(r"\[\d+\]", "", str(result)).strip().lower().capitalize()

            date = None
            try:
                date = datetime.strptime(date_str, "%d %B %Y").date() if pd.notna(date_str) else None
            except (ValueError, TypeError):
                date = datetime.now().date()  #Fallback to current date

            key = (player_name, for_team, against, date)  #Unique key to avoid duplicates
            if key in seen:
                continue
            seen.add(key)

            hat_tricks.append({
                "player": player_name,
                "for_team": for_team,
                "against": against,
                "result": result,
                "date": date
            })

        print(f"Extracted {len(hat_tricks)} unique hat-tricks: {hat_tricks}")
        return hat_tricks

    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []
    except ValueError as e:
        print(f"Error parsing table: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def scrape_clean_sheets(url):
    """
    Scrapes clean sheets data from a given Wikipedia URL.

    Args:
        url (str): The URL of the Wikipedia page containing clean sheets data.

    Returns:
        list: A list of dictionaries, each containing clean sheet details.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        tables = soup.find_all("table", {"class": "wikitable"})
        if not tables:
            print("No wikitable found on the page.")
            return []

        print(f"Found {len(tables)} wikitable(s) on the page.")

        clean_sheets_table = None
        for i, table in enumerate(tables):
            headers = [th.get_text(strip=True).lower().split("[")[0].strip() for th in table.find_all("th")]
            print(f"Table {i} headers: {headers}")
            if "rank" in headers and "player" in headers and "clean sheets" in headers:
                clean_sheets_table = table
                print(f"Clean sheets table found at index {i}.")
                break

        if not clean_sheets_table:
            print("Clean sheets table not found by header check. Trying fallback index.")
            try:
                clean_sheets_table = tables[7] # Based on previous observation, this is likely the correct index
                print("Using table at index 7 as fallback.")
            except IndexError:
                print("Fallback table index out of range.")
                return []

        df = pd.read_html(StringIO(str(clean_sheets_table)))[0]
        print(f"DataFrame columns: {list(df.columns)}")

        df.columns = [col.strip().replace("\xa0", " ").lower().split("[")[0].strip() for col in df.columns]

        clean_sheets = []
        seen = set() # To track unique player-club combinations
        for _, row in df.iterrows():
            player_name = row.get("player")
            club = row.get("club")
            clean_sheets_count = row.get("clean sheets")

            if pd.isna(player_name) or player_name is None:
                continue

            player_name = re.sub(r"\d+$", "", str(player_name)).strip().lower().capitalize()
            club = str(club).strip().lower().capitalize()

            key = (player_name, club)
            if key in seen:
                continue
            seen.add(key)

            try:
                clean_sheets_count = int(clean_sheets_count) if pd.notna(clean_sheets_count) else 0
            except (ValueError, TypeError):
                clean_sheets_count = 0

            clean_sheets.append({
                "player": player_name,
                "club": club,
                "clean_sheets": clean_sheets_count
            })

        print(f"Extracted {len(clean_sheets)} unique clean sheets: {clean_sheets}")
        return clean_sheets

    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []
    except ValueError as e:
        print(f"Error parsing table: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []