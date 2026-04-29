# DS 4320 Project 2: Predicting NFL Game Outcomes

## Executive Summary

This project builds a document-based dataset (D1) to support predicting NFL game outcomes. Using historical game data, each game is represented as a structured document that captures key features such as team performance, rest days, and betting spread. A simple logistic regression model is then used to predict whether the home team wins. The goal is to show how organizing data in the document model can make it easier to support analysis and prediction tasks.

Name: Ruth Melese  

NetID: cup6cd

DOI: (put your DOI or leave blank if not required)

## Problem Definition

### Item 1 – Initial General Problem and Refined Specific Problem Statement

People are often interested in predicting the outcome of sports games, but it’s not as simple as comparing two teams’ records. Game results are influenced by a mix of factors like scoring ability, team conditions, and recent performance, which makes outcomes difficult to predict using a single statistic.

This project focuses specifically on predicting NFL game outcomes by building a secondary dataset (D1) using the document model. Each document represents a single game and includes relevant context for both teams, such as rest days, scoring outcomes, and betting spread. This structure supports predicting whether the home team is more likely to win.

### Item 2 – Rationale for the Refinement

Focusing on individual NFL games makes the problem easier to define and evaluate, since each game has a clear outcome. Instead of pulling information from multiple sources every time, the dataset is structured so that each document already contains the key features needed for analysis. This makes the data easier to work with and better suited for modeling.

### Item 3 – Motivation for the Project

I’ve always been interested in how game outcomes aren’t just random, but influenced by patterns in performance and context. This project gave me a way to explore that idea by actually building something that uses real game data to make predictions. It also helped me understand how structuring data properly can make analysis much more straightforward.

## Domain Exposition

### Item 1 – Terminology

| Term | Meaning |
|-----|--------|
| Home Team | The team playing at their home stadium |
| Away Team | The visiting team |
| Spread Line | Expected point difference between teams |
| Rest Days | Number of days since a team’s last game |
| Home Win | Binary outcome indicating if home team won |
| Feature | Input variable used in prediction |
| Target Variable | Outcome being predicted |


### Item 2 – Domain Description

This project exists in the domain of sports analytics, specifically NFL game prediction. Sports analytics focuses on using historical and contextual data to better understand performance and outcomes. In football, game results are influenced by a combination of team strength, recent performance, and external factors like rest and environment. By organizing this information into structured documents, it becomes easier to analyze patterns and build models that can support predictions.


## Data Creation

### Item 1 – Data Acquisition

The dataset used in this project comes from historical NFL game records. The raw data includes information about teams, scores, rest days, and betting lines. This data was loaded from CSV format and then transformed into a document-based structure (D1), where each document represents a single game with selected features.

### Item 2 – Code Table

| File | Description |
|------|------------|
| `games.py` | Loads and processes raw game data |
| `closing_lines.py` | Handles betting line data (if used) |
| `initial_lines.py` | Handles early betting predictions (if used) |
| `rosters.py` | Contains roster-related data processing |
| `pipeline.ipynb` | Main pipeline for modeling and visualization |

### Item 3 – Bias Identification

Bias can be introduced through the selection of features and the structure of the dataset. For example, betting spread reflects market expectations, which may already include human assumptions and biases. Additionally, focusing only on certain features may leave out other important factors like injuries or coaching strategies.

### Item 4 – Bias Mitigation

To reduce bias, the model focuses on a small set of interpretable features and avoids overfitting to complex or noisy variables. The dataset is also cleaned to remove incomplete records, which helps ensure more consistent comparisons across games.

### Item 5 – Rationale for Decisions

The decision to use a limited set of features was intentional to keep the model interpretable and aligned with the document-based structure. Features like rest days and betting spread were chosen because they provide meaningful context without overcomplicating the dataset. This also reduces uncertainty by avoiding unnecessary or inconsistent variables.

## Metadata

The D1 dataset is structured as a collection of documents where each document represents a single NFL game.

### Key Fields

- `game_id`: Unique identifier for each game  
- `home_team`: Name of the home team  
- `away_team`: Name of the away team  
- `home_score`: Points scored by home team  
- `away_score`: Points scored by away team  
- `home_rest`: Days of rest for home team  
- `away_rest`: Days of rest for away team  
- `spread_line`: Betting spread  
- `temp`: Game temperature  
- `wind`: Wind conditions  
- `home_win`: Binary outcome (1 = home win, 0 = loss)  

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

[Press Release](press_release.md)

---

## License

MIT License