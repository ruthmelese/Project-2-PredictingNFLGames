import pandas as pd

# Season-level roster entries — one row per player per season per team.
# Columns: season, team, playerid, full_name, name, side, category,
#          position, games, starts, years, av
#   side: Offense | Defense | Special Teams
#   category: e.g. Quarterback, Linebacker, Wide Receiver, etc
#   av: Pro Football Reference Approximate Value

df = pd.read_csv("rosters.csv")

print(df.shape)
print(df.dtypes)
print(df.head())

# Position distribution
print(df["position"].value_counts().head(20))

# Average AV by position
avg_av = df.groupby("position")["av"].mean().sort_values(ascending=False)
print(avg_av.head(10))

# Average AV by side (Offense / Defense / Special Teams)
avg_av_side = df.groupby("side")["av"].mean().sort_values(ascending=False)
print(avg_av_side)

# Starters per team per season
starters = df[df["starts"] > 0]
starters_per_team = (
    starters.groupby(["season", "team"])["playerid"]
    .count()
    .reset_index()
    .rename(columns={"playerid": "starters"})
)
print(starters_per_team.head())

# Roster turnover: average years of experience per team per season
avg_exp = (
    df.groupby(["season", "team"])["years"]
    .mean()
    .reset_index()
    .rename(columns={"years": "avg_experience"})
)
print(avg_exp.head())

# Top players by career AV
career_av = (
    df.groupby(["playerid", "full_name"])["av"]
    .sum()
    .sort_values(ascending=False)
    .head(15)
)
print(career_av)

# Career longevity: seasons played per player
seasons_played = (
    df.groupby(["playerid", "full_name"])["season"]
    .nunique()
    .sort_values(ascending=False)
    .rename("seasons")
    .head(15)
)
print(seasons_played)

# AV efficiency: AV per game played (min 16 games in a season)
df_active = df[df["games"] >= 16].copy()
df_active["av_per_game"] = df_active["av"] / df_active["games"]
av_per_game = (
    df_active.groupby("position")["av_per_game"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
print(av_per_game)

# Team roster AV by season — proxy for overall team talent
team_av = (
    df.groupby(["season", "team"])["av"]
    .sum()
    .reset_index()
    .rename(columns={"av": "total_av"})
    .sort_values(["season", "total_av"], ascending=[True, False])
)
print(team_av.head(20))

# Best single-season AV performances by player
best_seasons = (
    df[["full_name", "team", "season", "position", "av"]]
    .sort_values("av", ascending=False)
    .head(20)
)
print(best_seasons)
