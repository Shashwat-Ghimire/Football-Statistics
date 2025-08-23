from django.shortcuts import render
from django.http import JsonResponse
from .models import PlayerSeasonStats, HatTrick, CleanSheet

"""
This module contains the views for the football statistics application.
Views are responsible for processing user requests and returning appropriate responses,
rendering HTML templates, or providing JSON data for API endpoints.
"""

def index(request):
    """
    Renders the main page of the football statistics application.
    This view fetches and displays top 10 scorers, hat-tricks, and clean sheets data.
    """
    # Fetch top 10 players by goals, prefetching related team data for efficiency.
    stats = (
        PlayerSeasonStats.objects
        .select_related("player__team")
        .all()
        .order_by("-goals")[:10]
    )
    # Fetch all hat-tricks, prefetching related player, for_team, and against team data,
    # ordered by date in descending order.
    hat_tricks = HatTrick.objects.select_related("player__team", "for_team", "against").order_by("-date")

    # Fetch all clean sheets, prefetching related player and team data, ordered by clean sheets count.
    clean_sheets = CleanSheet.objects.select_related("player__team").order_by("-clean_sheets")

    # Render the \"stats/index.html\" template with the fetched data.
    return render(request, "stats/index.html", {
        "stats": stats,
        "hat_tricks": hat_tricks,
        "clean_sheets": clean_sheets
    })

def top_players_api(request):
    """
    API endpoint to return top 10 players\" stats, with optional filtering by season.
    This view provides a JSON response suitable for client-side consumption.
    """
    # Get the \"season\" parameter from the request, if provided.
    season = request.GET.get("season")

    # Start with all PlayerSeasonStats, prefetching player and team data.
    qs = PlayerSeasonStats.objects.select_related("player__team")
    # If a season is specified, filter the queryset by that season.
    if season:
        qs = qs.filter(season=season)
    # Order the results by goals in descending order and limit to top 10.
    qs = qs.order_by("-goals")[:10]

    # Format the fetched player statistics into a list of dictionaries.
    data = [{
        "player": s.player.name,
        "team": s.player.team.name if s.player.team else "Unknown",
        "goals": s.goals
    } for s in qs]

    # Fetch all hat-tricks, prefetching related data, ordered by date.
    hat_tricks = HatTrick.objects.select_related("player__team", "for_team", "against").order_by("-date")
    # Append hat-tricks data to the main data list.
    data.append({
        "hat_tricks": [{
            "player": h.player.name,
            "for_team": h.for_team.name,
            "against": h.against.name,
            "result": h.result,
            "date": h.date.strftime("%Y-%m-%d") # Format date as YYYY-MM-DD string.
        } for h in hat_tricks]
    })

    # Return the combined data as a JSON response.
    return JsonResponse(data, safe=False)