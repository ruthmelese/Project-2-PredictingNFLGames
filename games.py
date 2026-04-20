```python
import pandas as pd

# One row per NFL game (1999–present).
# Primary key: game_id
# Columns: game_id, season, game_type, week, gameday, weekday,
#          gametime, away_team, away_score, home_team, home_score,
#          location, result, total, overtime, spread_line, total_line,
#          away_moneyline, home_moneyline, away_spread_odds,
#          home_spread_odds, under_odds, over_odds, div_game,
#          roof, surface, temp, wind, away_qb_id, home_qb_id,
#          away_qb_name, home_qb_name, away_coach, home_coach,
#          referee, stadium_id, stadium, ... (46 cols total)

df = pd.read_csv("games.csv")

print(df.shape)
print(df.dtypes)
print(df.head())

# Regular-season games only
reg = df[df["game_type"] == "REG"]

# Home-team win rate by season (result > 0 means home team won)
home_win_rate = (
    reg.groupby("season")["result"]
    .apply(lambda s: (s > 0).mean())
    .rename("home_win_rate")
)
print(home_win_rate)

# Home win rate by week — does it shift late in the season?
home_win_by_week = (
    reg.groupby("week")["result"]
    .apply(lambda s: (s > 0).mean())
    .rename("home_win_rate")
)
print(home_win_by_week)

# Average total points per season
df["total_points"] = df["away_score"] + df["home_score"]
avg_total = df.groupby("season")["total_points"].mean()
print(avg_total)

# Average margin of victory (absolute result) by season
reg = reg.copy()
reg["margin"] = reg["result"].abs()
avg_margin = reg.groupby("season")["margin"].mean()
print(avg_margin)

# Overtime rate by season
ot_rate = reg.groupby("season")["overtime"].mean().rename("ot_rate")
print(ot_rate)
print(f"Overall overtime rate: {reg['overtime'].mean():.2%}")

# Divisional games vs non-divisional: are they closer?
reg["is_div"] = reg["div_game"] == 1
div_margin = reg.groupby("is_div")["margin"].mean()
print(div_margin)

# Home-field advantage by roof type (outdoor vs dome vs retractable)
roof_home_wr = (
    reg.groupby("roof")["result"]
    .apply(lambda s: (s > 0).mean())
    .rename("home_win_rate")
    .sort_values(ascending=False)
)
print(roof_home_wr)

# Effect of rest advantage on home win rate
# away_rest and home_rest = days since last game
reg["rest_adv"] = reg["home_rest"] - reg["away_rest"]
reg["rest_bucket"] = pd.cut(
    reg["rest_adv"],
    bins=[-20, -4, 4, 20],
    labels=["away_rested", "even", "home_rested"]
)
rest_win_rate = (
    reg.groupby("rest_bucket", observed=True)["result"]
    .apply(lambda s: (s > 0).mean())
    .rename("home_win_rate")
)
print(rest_win_rate)

# Weather effects: does wind reduce scoring?
outdoor = reg[reg["roof"] == "outdoors"].copy()
outdoor["wind_bucket"] = pd.cut(
    outdoor["wind"],
    bins=[0, 10, 20, 100],
    labels=["calm", "moderate", "high"]
)
scoring_by_wind = outdoor.groupby("wind_bucket", observed=True)["total_points"].mean()
print(scoring_by_wind)

# QB-level home win rate (min 10 home starts)
qb_home = (
    reg.groupby("home_qb_name")["result"]
    .apply(lambda s: (s > 0).mean())
    .rename("home_win_rate")
)
qb_home_games = reg.groupby("home_qb_name")["result"].count().rename("games")
qb_summary = pd.concat([qb_home, qb_home_games], axis=1)
qb_summary = qb_summary[qb_summary["games"] >= 10].sort_values("home_win_rate", ascending=False)
print(qb_summary.head(15))
```

Removed the `---` labels and added home win rate by week, margin of victory, divisional vs non-divisional tightness, roof type effect, rest advantage buckets, wind vs scoring, and QB-level home win rate.