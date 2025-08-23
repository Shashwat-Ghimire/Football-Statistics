# Import the base class for creating Django management commands
from django.core.management.base import BaseCommand
# Import scraping functions to fetch football statistics
from stats.scraper import scrape_top_scorers, scrape_hat_tricks, scrape_clean_sheets
# Import Django models to interact with the database
from stats.models import League, Team, Player, PlayerSeasonStats, HatTrick, CleanSheet

# Define a custom Django management command for scraping and loading football stats
class Command(BaseCommand):
    # Description of the command, displayed when running `python manage.py help load_football_stats`
    help = "Scrape football stats and load into DB"

    # Define command-line arguments for the script
    def add_arguments(self, parser):
        # Add a required `--url` argument to specify the data source URL
        parser.add_argument("--url", type=str, required=True)
        # Add a required `--league` argument to specify the league name (e.g., Premier League)
        parser.add_argument("--league", type=str, required=True)
        # Add a required `--season` argument to specify the season (e.g., 2023-24)
        parser.add_argument("--season", type=str, required=True)

    # Main logic of the command, executed when the command is run
    def handle(self, *args, **options):
        # Extract the URL, league name, and season from command-line arguments
        url = options["url"]
        league_name = options["league"]
        season = options["season"]

        # Get or create a League object in the database to avoid duplicates
        league, _ = League.objects.get_or_create(name=league_name)

        # Scrape top scorers data from the provided URL
        scorers = scrape_top_scorers(url)
        # Scrape hat-tricks data from the provided URL
        hat_tricks = scrape_hat_tricks(url)

        # Process top scorers data
        for item in scorers:
            # Get or create a Team object for the player's team, associated with the league
            team, _ = Team.objects.get_or_create(name=item["team"], league=league)
            # Get or create a Player object for the player, associated with the team
            player, _ = Player.objects.get_or_create(name=item["name"], team=team)
            # Update or create PlayerSeasonStats to store goals and matches for the season
            PlayerSeasonStats.objects.update_or_create(
                player=player,
                season=season,
                # Set goals from scraped data, default matches to 0 (as not provided in data)
                defaults={"goals": item["goals"], "matches": 0}
            )

        # Process hat-tricks data
        for item in hat_tricks:
            # Get or create a Team object for the team the player scored for
            for_team, _ = Team.objects.get_or_create(name=item["for_team"], league=league)
            # Get or create a Team object for the opposing team
            against, _ = Team.objects.get_or_create(name=item["against"], league=league)
            # Get or create a Player object for the player who scored the hat-trick
            player, _ = Player.objects.get_or_create(name=item["player"], team=for_team)
            # Update or create HatTrick record with match details
            HatTrick.objects.update_or_create(
                player=player,
                for_team=for_team,
                against=against,
                # Store result and date of the hat-trick
                defaults={"result": item["result"], "date": item["date"]}
            )

        # Output a success message to the console after processing scorers and hat-tricks
        self.stdout.write(self.style.SUCCESS(f"Scraping complete ✅ for {season}"))

        # Scrape clean sheets data from the provided URL
        clean_sheets_data = scrape_clean_sheets(url)

        # Process clean sheets data
        for item in clean_sheets_data:
            # Get or create a Team object for the goalkeeper's club
            team, _ = Team.objects.get_or_create(name=item["club"], league=league)
            # Get or create a Player object for the goalkeeper
            player, _ = Player.objects.get_or_create(name=item["player"], team=team)
            # Update or create CleanSheet record for the season
            CleanSheet.objects.update_or_create(
                player=player,
                season=season,
                # Store the number of clean sheets
                defaults={"clean_sheets": item["clean_sheets"]}
            )