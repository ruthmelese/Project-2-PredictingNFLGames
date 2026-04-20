import pandas as pd

# Opening/initial betting lines by sportsbook.
# One row per sportsbook × bet type × side.
# Columns: season, sportsbook, type, about, side, line
#   type  : SPREAD | MONEYLINE | TOTAL

df = pd.read_csv("initial_lines.csv")

print(df.shape)
print(df.dtypes)
print(df.head())

print(df["sportsbook"].unique())

# Bet type distribution
print(df["type"].value_counts())

# Average opening spread by season (favourite side only)
spreads = df[df["type"] == "SPREAD"]
fav_spreads = spreads[spreads["line"] < 0]
avg_open_spread = fav_spreads.groupby("season")["line"].mean()
print(avg_open_spread)


# Compare opening vs closing spread
closing = pd.read_csv("closing_lines.csv")

# Extract season from alt_game_id (example: "2021_01_DAL_TB" → 2021)
closing["season"] = closing["alt_game_id"].str[:4].astype(int)

# Keep only spread lines, favourite side (negative line)
closing_spreads = closing[(closing["type"] == "SPREAD") & (closing["line"] < 0)]

# Average opening spread across sportsbooks to avoid duplicate rows per game
opening_spreads = (
    df[(df["type"] == "SPREAD") & (df["line"] < 0)]
    .groupby("about", as_index=False)["line"]
    .mean()
)

# Sanity check before merging
print(f"Opening spreads: {len(opening_spreads)} games")
print(f"Closing spreads: {len(closing_spreads)} games")

# Merge on shared game identifier (about = alt_game_id)
merged = opening_spreads.merge(
    closing_spreads[["alt_game_id", "line", "outcome"]],
    left_on="about",
    right_on="alt_game_id",
    suffixes=("_open", "_close")
)

print(f"Merged rows: {len(merged)} (should match opening spreads if all games found)")

# Line movement: negative = favourite got bigger, positive = favourite got smaller
# example: -6.5 → -3.5 : line_move = +3.0 (moved toward underdog)
# example: -3.5 → -6.5 : line_move = -3.0 (moved toward favourite)
merged["line_move"] = merged["line_close"] - merged["line_open"]

print(merged[["about", "line_open", "line_close", "line_move", "outcome"]].head())
print(f"\nAverage line movement: {merged['line_move'].mean():.3f}")

# Cover rate by direction of line movement
moved_toward_fav = merged[merged["line_move"] < 0]["outcome"].mean()  # spread grew
moved_toward_dog = merged[merged["line_move"] > 0]["outcome"].mean()  # spread shrunk
print(f"Cover rate when line moved toward favourite : {moved_toward_fav:.2%}")
print(f"Cover rate when line moved toward underdog  : {moved_toward_dog:.2%}")