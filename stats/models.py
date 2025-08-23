from django.db import models

# Defines the League model.
class League(models.Model):
    # Name of the league (e.g., "Premier League").
    name = models.CharField(max_length=100)
    # Country where the league is located (optional).
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

# Defines the Team model.
class Team(models.Model):
    # Name of the team (e.g., "Manchester United").
    name = models.CharField(max_length=100)
    # Foreign key to the League model, indicating which league the team belongs to.
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Defines the Player model.
class Player(models.Model):
    # Name of the player.
    name = models.CharField(max_length=100)
    # Foreign key to the Team model, indicating which team the player belongs to.
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # Player's position (e.g., "Forward", "Midfielder").
    position = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        # Ensures that a player's name is unique within a team.
        unique_together = ("name", "team")

    def __str__(self):
        return self.name

# Defines the PlayerSeasonStats model.
class PlayerSeasonStats(models.Model):
    # Foreign key to the Player model.
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    # The season for which the stats are recorded (e.g., "2023-2024").
    season = models.CharField(max_length=20)
    # Number of goals scored by the player in the season.
    goals = models.IntegerField(default=0)
    # Number of matches played by the player in the season.
    matches = models.IntegerField(default=0)

    class Meta:
        # Ensures that a player's stats are unique for a given season.
        unique_together = ("player", "season")

    def __str__(self):
        return f"{self.player.name} - {self.season}"

# Defines the HatTrick model.
class HatTrick(models.Model):
    # Foreign key to the Player model who scored the hat-trick.
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    # Foreign key to the Team for which the hat-trick was scored.
    for_team = models.ForeignKey(Team, related_name="hat_tricks_for", on_delete=models.CASCADE)
    # Foreign key to the Team against which the hat-trick was scored.
    against = models.ForeignKey(Team, related_name="hat_tricks_against", on_delete=models.CASCADE)
    # Result of the match (Win, Loss, or Draw).
    result = models.CharField(max_length=20, choices=[("Win", "Win"), ("Loss", "Loss"), ("Draw", "Draw")])
    # Date when the hat-trick was scored.
    date = models.DateField()

    class Meta:
        # Ensures uniqueness for a hat-trick record.
        unique_together = ("player", "for_team", "against", "date")
        # Plural name for the admin interface.
        verbose_name_plural = "hat-tricks"

    def __str__(self):
        return f"{self.player.name} - {self.for_team.name} vs {self.against.name} on {self.date}"

# Defines the CleanSheet model.
class CleanSheet(models.Model):
    # Foreign key to the Player model who achieved the clean sheet.
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    # The season for which the clean sheet is recorded.
    season = models.CharField(max_length=20)
    # Number of clean sheets achieved by the player in the season.
    clean_sheets = models.IntegerField(default=0)

    class Meta:
        # Ensures uniqueness for a clean sheet record for a player in a given season.
        unique_together = ("player", "season")
        # Plural name for the admin interface.
        verbose_name_plural = "clean sheets"

    def __str__(self):
        return f"{self.player.name} - {self.season} - {self.clean_sheets} clean sheets"
