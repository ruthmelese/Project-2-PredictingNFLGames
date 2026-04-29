# DS 4320 Project 2: Predicting NFL Game Outcomes

## Executive Summary

This project builds a document-based dataset (D1) to support predicting NFL game outcomes. Using historical game data, each game is represented as a structured document that captures key features such as team performance, rest days, and betting spread. A simple logistic regression model is then used to predict whether the home team wins. The goal is to show how organizing data in the document model can make it easier to support analysis and prediction tasks.

**Name**: Ruth Melese  
**NetID**: cup6cd
- **DOI:** [Zenodo](https://doi.org/10.5281/zenodo.19887697)
- **Press Release:** [Predicting NFL Game Outcomes Using Structured Game Data](press_release.md)
- **Data:** [OneDrive Folder Link](https://myuva-my.sharepoint.com/:f:/g/personal/cup6cd_virginia_edu/IgBt2TBIcuczT5f5OeIR7gbXAc0K37oitoZwMZ0K5nHATXc?e=NwxeIr)
- **Pipeline:** [notebooks/pipeline.ipynb](notebooks/pipeline.ipynb)
- **License:**  [MIT](https://github.com/ruthmelese/Project-2-PredictingNFLGames/blob/main/LICENSE)


## Problem Definition

### Item 1 – Initial General Problem and Refined Specific Problem Statement

People are often interested in predicting the outcome of sports games, but it’s not as simple as comparing two teams’ records. Game results are influenced by a mix of factors like scoring ability, team conditions, and recent performance, which makes outcomes difficult to predict using a single statistic.

This project focuses specifically on predicting NFL game outcomes by building a secondary dataset (D1) using the document model. Each document represents a single game and includes relevant context for both teams, such as rest days, scoring outcomes, and betting spread. This structure supports predicting whether the home team is more likely to win.

### Item 2 – Rationale for the Refinement

Focusing on individual NFL games makes the problem easier to define and evaluate, since each game has a clear outcome. Instead of pulling information from multiple sources every time, the dataset is structured so that each document already contains the key features needed for analysis. This makes the data easier to work with and better suited for modeling.

### Item 3 – Motivation for the Project

I’ve always been interested in how game outcomes aren’t just random, but influenced by patterns in performance and context. This project gave me a way to explore that idea by actually building something that uses real game data to make predictions. It also helped me understand how structuring data properly can make analysis much more straightforward.

## Domain Exposition

## Item 1 – Terminology

| Term | Definition |
|------|-----------|
| Game Outcome | The result of a game, typically whether the home or away team wins |
| Points Per Game (PPG) | Average number of points a team scores per game |
| Points Allowed | Average number of points a team gives up per game |
| Win Percentage | The proportion of games a team has won over a season |
| Recent Form | A team’s performance over its most recent games (e.g., last 3–5 games) |
| Home Field Advantage | The tendency for the home team to perform better due to location and crowd factors |
| Matchup | The pairing of two teams in a game and how their strengths compare |
| Offensive Strength | A measure of how effectively a team scores points |
| Defensive Strength | A measure of how well a team prevents opponents from scoring |
| Point Differential | The difference between points scored and points allowed, often used as an overall strength indicator |
| Target Variable | The outcome being predicted, such as whether the home team wins |
| Feature | A measurable input used for prediction, such as PPG or win percentage |
| Document Model | A structure where all game-related data is stored together in a single document |
| Secondary Dataset (D1) | A reorganized dataset where each game contains all relevant team and matchup information |

### Item 2 – Domain Description

This project exists in the domain of sports analytics, specifically NFL game prediction. Sports analytics focuses on using historical and contextual data to better understand performance and outcomes. In football, game results are influenced by a combination of team strength, recent performance, and external factors like rest and environment. By organizing this information into structured documents, it becomes easier to analyze patterns and build models that can support predictions.

### Background Readings
NFL Reading Folder: https://myuva-my.sharepoint.com/:f:/g/personal/cup6cd_virginia_edu/IgDJcGEF5KssQIsJzM9HUacUASgXbEgit6540l9TCH-deaQ?e=EU28vp

### Reading Summary Table

| Title | Description | Link to file in folder |
|---|---|---|
| 5 Key Metrics to Consider When Making NFL Predictions | This article explains the core factors that influence NFL game outcomes, including offense and defense rankings, quarterback performance, turnover differential, strength of schedule, and weather conditions. It emphasizes that relying on a single stat is not enough and that multiple factors must be considered together. | [5keymetrics.pdf](https://myuva-my.sharepoint.com/:b:/g/personal/cup6cd_virginia_edu/IQBqMqDy-JysS7f6egCcsf_kAajltheSo6b0nExIHjZU4hk?e=mGEfAv) |
| Advanced Model Creation with NFL Data | This reading introduces how statistical models, especially regression, are used to understand relationships between football statistics like yards and points. It explains how multiple variables can be combined to improve predictions and highlights the importance of interpreting model results correctly. | [AdvancedModelCreation.pdf](https://myuva-my.sharepoint.com/:b:/g/personal/cup6cd_virginia_edu/IQACmX155kjXS7ogKcNW7tfLARBoLagOoRF65rqYywTve40?e=5V9S5H) |
| How I Built a Competitive NFL Prediction Model with Only Five Statistics | This article shows how a simple predictive model can be built using a small number of key statistics, such as passing yards, rushing yards, and turnovers. It also introduces the idea of simulating games many times to estimate likely outcomes. | [NFLPredictiveModel.pdf](https://myuva-my.sharepoint.com/:b:/g/personal/cup6cd_virginia_edu/IQBHC8agdgCbR7MaQT-RX2YqAec7xdja-uNDFhebyEtK-Ew?e=z8bKGp) |
| Analyzing the Predictive Power of NFL Statistics | This paper explores how different statistics contribute to predicting game outcomes, showing that individual stats are weak predictors on their own but become more useful when combined in a model. It uses logistic regression to model win/loss outcomes. | [PredictivePowersofStats.pdf](https://myuva-my.sharepoint.com/:b:/g/personal/cup6cd_virginia_edu/IQCWQiJa6bS6S4k-KcF8aD5PASmIIYhBGEsrRvohkw0_N6Y?e=j9K13S) |
| Predicting Sport Event Outcomes Using Deep Learning | This paper discusses how modern machine learning methods, including deep learning, can improve prediction accuracy by capturing complex relationships between variables. It highlights how many different factors, such as player condition and environment, influence outcomes. | [SportsandDeepLearning.pdf](https://myuva-my.sharepoint.com/:b:/g/personal/cup6cd_virginia_edu/IQA4JucsRODDSIh2SAfZ3hnPAdXUfzVVqV4HKJJxOa43Nh4?e=NhxzR7) |

## Data Creation

### Item 1 – Data Acquisition

The raw data used in this project comes from a publicly available NFL games dataset that includes historical game-level information such as teams, scores, game conditions, and basic contextual variables. Each row represents a single NFL game, which makes it a strong starting point for building a prediction dataset. The dataset was downloaded as a CSV file and loaded into the analysis environment using Python.

After loading the data, I selected relevant columns and created additional features to better support prediction. For example, I derived a binary outcome variable indicating whether the home team won, and I used existing fields like rest days and game conditions as inputs. The data was then reorganized into a secondary dataset (D1) where each document represents a single game with both teams’ context included. This restructuring step is important because it aligns the data with the prediction task and allows for more direct querying and analysis.

### Item 2 – Code Table

| File Name | Description | Link |
|-----------|------------|------|
| games.py | Loads and explores the core NFL games dataset, including team performance, scoring, and contextual features like rest, weather, and home-field advantage. Also computes metrics such as home win rate and scoring trends. | [games.py](https://github.com/ruthmelese/Project-2-PredictingNFLGames/blob/main/pipeline/games.py) |
| rosters.py | Analyzes roster-level data, including player positions, approximate value (AV), and team composition across seasons to provide context on team strength. | [rosters.py](https://github.com/ruthmelese/Project-2-PredictingNFLGames/blob/main/pipeline/rosters.py) |
| initial_lines.py | Processes opening betting lines from sportsbooks and analyzes trends such as average spreads and differences between opening and closing lines. | [initial_lines.py](https://github.com/ruthmelese/Project-2-PredictingNFLGames/blob/main/pipeline/initial_lines.py) |
| closing_lines.py | Analyzes final betting lines and outcomes, including cover rates, implied probabilities, and how betting markets relate to actual game results. | [closing_lines.py](https://github.com/ruthmelese/Project-2-PredictingNFLGames/blob/main/pipeline/closing_lines.py) |

### Item 3 – Bias Identification

This dataset introduces bias in a few specific ways. First, there is temporal bias, since older seasons are more likely to have missing or less complete data (especially betting lines). This creates uneven coverage across time. For example, if early seasons have around 15–20% missing values in key variables, the analysis will lean more heavily on recent seasons.

There is also feature omission bias. The dataset only includes recorded, structured variables like scores, betting lines, and rosters. It does not capture factors like injuries, player fatigue, or coaching decisions, which are known to influence game outcomes. This means any model built on this data is limited to observable variables and may systematically miss important drivers.

Finally, there is selection bias in how games are represented. While all games are included, differences across contexts (such as early vs late season or different team conditions) are not explicitly accounted for. If model performance varies across these subsets, it indicates the presence of bias.

### Item 4 – Bias Mitigation

To address these biases, several steps can be taken. First, missing data should be explicitly measured and reported. For each variable, the missing rate can be calculated as the proportion of missing values. Features with more than about 10% missingness should either be excluded or handled carefully with imputation.

Second, results should be checked across time. Splitting the data by season (for example, training on earlier seasons and testing on later ones) helps identify whether performance is consistent. If accuracy or other metrics change by more than about 5–10% across time periods, this suggests temporal bias.

Third, robustness checks should be used. Running the same analysis on different subsets (such as early vs late season weeks) helps quantify how stable the results are. Variation in results across subsets provides a rough uncertainty range, typically on the order of ±1–5%.

Finally, conclusions should clearly state that results are limited to the variables included in the dataset and do not account for unobserved factors like injuries or in-game decisions.

### Item 5 – Rationale for Decisions

Several design decisions were made when preparing the dataset. First, the data was structured so that each document represents a single game, with related information grouped into categories such as teams, environment, and results. This improves readability and aligns with how the data will be analyzed. Additionally, missing values were explicitly handled rather than removed to preserve as much data as possible. Some derived features, such as point differential and total points, were created to simplify analysis, which introduces minor uncertainty but improves interpretability. These decisions balance data completeness, usability, and clarity while acknowledging that some simplifications may affect precision.

## Metadata

## Implicit Schema

The dataset follows a relational structure where `game_id` is the main linking key across game-level tables. The `games.csv` file acts as the central table because each row represents one NFL game. The `initial_lines.csv` and `closing_lines.csv` tables connect to `games.csv` through `game_id`, allowing each game to be matched with both opening and final betting market information.

The `rosters.csv` table is connected at the team level using the `team` field, which matches the `home_team` and `away_team` fields in `games.csv`. Unlike the betting line tables, rosters are not directly linked by `game_id`; instead, they provide player-level information for each team.

Overall, the schema is structured around games, betting lines, and team rosters. This allows the project to combine game outcomes, market expectations, and team/player information into a secondary dataset for analysis.

| Table | Key Field | Connects To | Relationship |
|------|-----------|-------------|--------------|
| games.csv | game_id | initial_lines.csv, closing_lines.csv | One game to one set of initial and closing lines |
| initial_lines.csv | game_id | games.csv | One initial betting line record per game |
| closing_lines.csv | game_id | games.csv | One closing betting line record per game |
| rosters.csv | team | games.csv home_team / away_team | One team to many players |

## Data Summary

This dataset contains information about NFL games, betting lines, and team rosters. The main unit of analysis is a single NFL game, identified by `game_id`. The `games.csv` file includes basic game information such as season, week, teams, stadium, and final scores. The betting line files provide initial and closing market expectations, including spread lines, total lines, and moneyline odds. The roster file contains player-level information such as team, name, position, jersey number, height, and weight.

The combined dataset can be used to study how well betting market expectations align with actual game outcomes. For example, the spread line can be compared to the final point differential, and moneyline odds can be converted into implied probabilities to compare expected win chances with actual wins.

Key variables include `home_score`, `away_score`, `spread_line`, `total_line`, `home_moneyline`, and `away_moneyline`. The main outcome variable is game result, such as whether the home team won. Important derived variables may include point differential, total points scored, implied probability, and prediction error.

Potential limitations include missing values in betting lines or roster fields, differences in data completeness across seasons, and the absence of important unobserved factors such as injuries, weather, coaching decisions, or player availability.

## Data Table

games.csv
| Name        | Data Type | Description                                   | Example              | Uncertainty |
|------------|----------|-----------------------------------------------|----------------------|------------|
| game_id    | string   | Unique identifier for each NFL game           | 2021_01_DAL_TB       | N/A |
| season     | integer  | NFL season year                              | 2021                 | ±0 |
| week       | integer  | Week number in the season                    | 1                    | ±0 |
| home_team  | string   | Home team abbreviation                       | TB                   | N/A |
| away_team  | string   | Away team abbreviation                       | DAL                  | N/A |
| home_score | integer  | Points scored by home team                   | 31                   | ±0 |
| away_score | integer  | Points scored by away team                   | 29                   | ±0 |
| stadium    | string   | Name of the stadium                          | Raymond James Stadium| negligible |

closing_lines.csv
| Name            | Data Type | Description                                   | Example              | Uncertainty |
|-----------------|----------|-----------------------------------------------|----------------------|------------|
| game_id         | string   | Identifier linking to games.csv               | 2021_01_DAL_TB       | N/A |
| spread_line     | float    | Final predicted point difference              | -8.0                 | ±1–2 points |
| total_line      | float    | Predicted total points (over/under)           | 51.5                 | ±2–3 points |
| home_moneyline  | integer  | Odds for home team to win                     | -350                 | ±5–10% implied probability |
| away_moneyline  | integer  | Odds for away team to win                     | 275                  | ±5–10% implied probability |

initial_lines.csv
| Name            | Data Type | Description                                   | Example              | Uncertainty |
|-----------------|----------|-----------------------------------------------|----------------------|------------|
| game_id         | string   | Identifier linking to games.csv               | 2021_01_DAL_TB       | N/A |
| spread_line     | float    | Initial predicted point difference            | -6.5                 | ±1–3 points |
| total_line      | float    | Initial predicted total points                | 52.0                 | ±2–4 points |
| home_moneyline  | integer  | Initial home team odds                        | -300                 | ±5–10% implied probability |
| away_moneyline  | integer  | Initial away team odds                        | 250                  | ±5–10% implied probability |

rosters.csv
| Name           | Data Type | Description                                   | Example       | Uncertainty |
|----------------|----------|-----------------------------------------------|---------------|------------|
| team           | string   | Team abbreviation                            | TB            | N/A |
| player_name    | string   | Name of player                               | Tom Brady     | N/A |
| position       | string   | Player position                              | QB            | N/A |
| jersey_number  | integer  | Player jersey number                         | 12            | ±0 |
| height         | string   | Player height                                | 6-4           | ±1 inch |
| weight         | integer  | Player weight (lbs)                          | 225           | ±2–5 lbs |

## Pipeline

The full pipeline can be found here:

[Pipeline Notebook](notebooks/pipeline.ipynb)

This includes:
- Data loading from MongoDB  
- Feature selection  
- Model training (logistic regression)  
- Visualization  

---

## Press Release

[Predicting NFL Game Outcomes Using Structured Game Data](press_release.md)

---

## License

MIT License