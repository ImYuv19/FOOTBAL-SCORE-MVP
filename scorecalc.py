# MVP Points Calculator (Multiple Players)

# weightages
WEIGHTS = {
    "passes": 1.5,
    "tackles": 2,
    "dribbles": 1.5,
    "goals": 3,
    "assists": 2,
    "saves": 3
}

def calculate_mvp(player_stats, team_stats):
    score = 0.0
    
    # team-based stats
    for stat in ["passes", "tackles", "dribbles"]:
        team_total = team_stats.get(stat, 0)
        if team_total > 0:
            contribution = player_stats.get(stat, 0) / team_total
            score += contribution * WEIGHTS[stat]
    
    # individual stats
    for stat in ["goals", "assists", "saves"]:
        score += player_stats.get(stat, 0) * WEIGHTS[stat]
    
    return round(score, 2)


# ----------------- INPUT SECTION -----------------
print("Enter TEAM totals first:\n")
team_stats = {
    "passes": int(input("TEAM successful passes: ")),
    "tackles": int(input("TEAM successful tackles: ")),
    "dribbles": int(input("TEAM dribbles: "))
}

print("\n--- MVP Calculator Ready ---\n")

while True:
    name = input("Enter player name: ")
    
    player_stats = {
        "passes": int(input("Player successful passes: ")),
        "tackles": int(input("Player successful tackles: ")),
        "dribbles": int(input("Player dribbles: ")),
        "goals": int(input("Player goals: ")),
        "assists": int(input("Player assists: ")),
        "saves": int(input("Player GK saves: "))
    }
    
    points = calculate_mvp(player_stats, team_stats)
    print(f"\nMVP Points for {name}: {points}\n")
    
    cont = input("Do you want to enter another player? (y/n): ").strip().lower()
    if cont != 'y':
        break
