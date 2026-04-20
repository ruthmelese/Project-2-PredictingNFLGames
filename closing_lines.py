import pandas as pd

# Closing betting lines — one row per game × bet type × side.
# Primary key: (game_id, type, side)
# Columns: game_id, alt_game_id, type, side, line, odds, outcome
#   type    : MONEYLINE | SPREAD | TOTAL
#   outcome : 1 = winning side, 0 = losing side

df = pd.read_csv("closing_lines.csv")

print(df.shape)
print(df.dtypes)
print(df.head())

# Split by bet type
moneylines = df[df["type"] == "MONEYLINE"]
spreads    = df[df["type"] == "SPREAD"]
totals     = df[df["type"] == "TOTAL"]

# Favourite cover rate (spread): favourite = line < 0
fav = spreads[spreads["line"] < 0]
cover_rate = fav["outcome"].mean()
print(f"Favourite cover rate: {cover_rate:.2%}")

# Underdog cover rate
dog = spreads[spreads["line"] > 0]
dog_cover_rate = dog["outcome"].mean()
print(f"Underdog cover rate: {dog_cover_rate:.2%}")

# Cover rate by spread bucket (e.g. <3, 3-7, 7-10, 10+)
spreads = spreads.copy()
spreads["abs_line"] = spreads["line"].abs()
spreads["spread_bucket"] = pd.cut(
    spreads["abs_line"],
    bins=[0, 3, 7, 10, 100],
    labels=["<3", "3-7", "7-10", "10+"]
)
cover_by_bucket = (
    spreads[spreads["line"] < 0]
    .groupby("spread_bucket", observed=True)["outcome"]
    .agg(["mean", "count"])
    .rename(columns={"mean": "cover_rate", "count": "games"})
)
print(cover_by_bucket)

# Average closing moneyline odds for winners vs losers
ml_avg = moneylines.groupby("outcome")["odds"].mean()
print(ml_avg)

# Moneyline implied probability vs actual win rate
moneylines = moneylines.copy()
moneylines["implied_prob"] = moneylines["odds"].apply(
    lambda x: (-x / (-x + 100)) if x < 0 else (100 / (x + 100))
)
ml_accuracy = moneylines.groupby(
    pd.cut(moneylines["implied_prob"], bins=5)
)[["implied_prob", "outcome"]].mean()
print(ml_accuracy)

# Over/under cover rate
overs  = totals[totals["side"] == "OVER"]
unders = totals[totals["side"] == "UNDER"]
print(f"Over cover rate:  {overs['outcome'].mean():.2%}")
print(f"Under cover rate: {unders['outcome'].mean():.2%}")

# Average total line over time — merge with games for season
games = pd.read_csv("games.csv")[["game_id", "season"]]
merged = df.merge(games, on="game_id")

avg_total_line = (
    merged[merged["type"] == "TOTAL"]
    .groupby("season")["line"]
    .mean()
)
print(avg_total_line)

# Favourite cover rate by season
fav_by_season = (
    merged[(merged["type"] == "SPREAD") & (merged["line"] < 0)]
    .groupby("season")["outcome"]
    .mean()
    .rename("fav_cover_rate")
)
print(fav_by_season)
