# NFL Game Outcome Prediction Pipeline

## Data Preparation

In this section, data is loaded from MongoDB and converted into a DataFrame for analysis.


```python
!python3 -m pip install pymongo certifi
```

    Requirement already satisfied: pymongo in /Users/ruthmelese/anaconda3/lib/python3.11/site-packages (4.16.0)
    Requirement already satisfied: certifi in /Users/ruthmelese/anaconda3/lib/python3.11/site-packages (2023.7.22)
    Requirement already satisfied: dnspython<3.0.0,>=2.6.1 in /Users/ruthmelese/anaconda3/lib/python3.11/site-packages (from pymongo) (2.7.0)



```python
import logging
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Pipeline started")
```


```python
import pandas as pd
games = pd.read_csv("../data/games.csv")
logging.info("Data loaded successfully")

games.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>game_id</th>
      <th>season</th>
      <th>game_type</th>
      <th>week</th>
      <th>gameday</th>
      <th>weekday</th>
      <th>gametime</th>
      <th>away_team</th>
      <th>away_score</th>
      <th>home_team</th>
      <th>...</th>
      <th>wind</th>
      <th>away_qb_id</th>
      <th>home_qb_id</th>
      <th>away_qb_name</th>
      <th>home_qb_name</th>
      <th>away_coach</th>
      <th>home_coach</th>
      <th>referee</th>
      <th>stadium_id</th>
      <th>stadium</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1999_01_MIN_ATL</td>
      <td>1999</td>
      <td>REG</td>
      <td>1</td>
      <td>9/12/1999</td>
      <td>Sunday</td>
      <td>NaN</td>
      <td>MIN</td>
      <td>17</td>
      <td>ATL</td>
      <td>...</td>
      <td>NaN</td>
      <td>00-0003761</td>
      <td>00-0002876</td>
      <td>Randall Cunningham</td>
      <td>Chris Chandler</td>
      <td>Dennis Green</td>
      <td>Dan Reeves</td>
      <td>Gerry Austin</td>
      <td>ATL00</td>
      <td>Georgia Dome</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1999_01_KC_CHI</td>
      <td>1999</td>
      <td>REG</td>
      <td>1</td>
      <td>9/12/1999</td>
      <td>Sunday</td>
      <td>NaN</td>
      <td>KC</td>
      <td>17</td>
      <td>CHI</td>
      <td>...</td>
      <td>12.0</td>
      <td>00-0006300</td>
      <td>00-0010560</td>
      <td>Elvis Grbac</td>
      <td>Shane Matthews</td>
      <td>Gunther Cunningham</td>
      <td>Dick Jauron</td>
      <td>Phil Luckett</td>
      <td>CHI98</td>
      <td>Soldier Field</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1999_01_PIT_CLE</td>
      <td>1999</td>
      <td>REG</td>
      <td>1</td>
      <td>9/12/1999</td>
      <td>Sunday</td>
      <td>NaN</td>
      <td>PIT</td>
      <td>43</td>
      <td>CLE</td>
      <td>...</td>
      <td>12.0</td>
      <td>00-0015700</td>
      <td>00-0004230</td>
      <td>Kordell Stewart</td>
      <td>Ty Detmer</td>
      <td>Bill Cowher</td>
      <td>Chris Palmer</td>
      <td>Bob McElwee</td>
      <td>CLE00</td>
      <td>Cleveland Browns Stadium</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1999_01_OAK_GB</td>
      <td>1999</td>
      <td>REG</td>
      <td>1</td>
      <td>9/12/1999</td>
      <td>Sunday</td>
      <td>NaN</td>
      <td>OAK</td>
      <td>24</td>
      <td>GB</td>
      <td>...</td>
      <td>10.0</td>
      <td>00-0005741</td>
      <td>00-0005106</td>
      <td>Rich Gannon</td>
      <td>Brett Favre</td>
      <td>Jon Gruden</td>
      <td>Ray Rhodes</td>
      <td>Tony Corrente</td>
      <td>GNB00</td>
      <td>Lambeau Field</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1999_01_BUF_IND</td>
      <td>1999</td>
      <td>REG</td>
      <td>1</td>
      <td>9/12/1999</td>
      <td>Sunday</td>
      <td>NaN</td>
      <td>BUF</td>
      <td>14</td>
      <td>IND</td>
      <td>...</td>
      <td>NaN</td>
      <td>00-0005363</td>
      <td>00-0010346</td>
      <td>Doug Flutie</td>
      <td>Peyton Manning</td>
      <td>Wade Phillips</td>
      <td>Jim Mora</td>
      <td>Ron Blum</td>
      <td>IND99</td>
      <td>RCA Dome</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 46 columns</p>
</div>




```python
from pymongo import MongoClient
import certifi
import pandas as pd

MONGO_URI = "mongodb+srv://rmelese1:Hayfield.123@m0.bjyxxnv.mongodb.net/?retryWrites=true&w=majority&appName=M0"

client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())

db = client["nfl_db"]
collection = db["games_d1"]

print("Connected")
print("Documents:", collection.count_documents({}))
```

    Connected
    Documents: 7276



```python
games = pd.read_csv("../data/games.csv")

# actual outcome
games["point_diff"] = games["home_score"] - games["away_score"]

# prediction error (this is the bias)
games["error"] = games["point_diff"] - games["spread_line"]

d1 = games[
    [
        "game_id",
        "home_team",
        "away_team",
        "home_score",
        "away_score",
        "home_rest",
        "away_rest",
        "spread_line",
        "temp",
        "wind"
    ]
].copy()

d1 = d1.dropna(subset=["home_score", "away_score"])

d1["home_win"] = (d1["home_score"] > d1["away_score"]).astype(int)

logging.info("Features created: home_win, point_diff, error")

d1.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>game_id</th>
      <th>home_team</th>
      <th>away_team</th>
      <th>home_score</th>
      <th>away_score</th>
      <th>home_rest</th>
      <th>away_rest</th>
      <th>spread_line</th>
      <th>temp</th>
      <th>wind</th>
      <th>home_win</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1999_01_MIN_ATL</td>
      <td>ATL</td>
      <td>MIN</td>
      <td>14</td>
      <td>17</td>
      <td>7</td>
      <td>7</td>
      <td>-4.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1999_01_KC_CHI</td>
      <td>CHI</td>
      <td>KC</td>
      <td>20</td>
      <td>17</td>
      <td>7</td>
      <td>7</td>
      <td>-3.0</td>
      <td>80.0</td>
      <td>12.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1999_01_PIT_CLE</td>
      <td>CLE</td>
      <td>PIT</td>
      <td>0</td>
      <td>43</td>
      <td>7</td>
      <td>7</td>
      <td>-6.0</td>
      <td>78.0</td>
      <td>12.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1999_01_OAK_GB</td>
      <td>GB</td>
      <td>OAK</td>
      <td>28</td>
      <td>24</td>
      <td>7</td>
      <td>7</td>
      <td>9.0</td>
      <td>67.0</td>
      <td>10.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1999_01_BUF_IND</td>
      <td>IND</td>
      <td>BUF</td>
      <td>31</td>
      <td>14</td>
      <td>7</td>
      <td>7</td>
      <td>-3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
collection.delete_many({})

records = d1.to_dict("records")
collection.insert_many(records)

print("Inserted documents:", collection.count_documents({}))
```

    Inserted documents: 7276


## Feature Selection

The features selected for prediction include home_rest, away_rest, and spread_line. The rest variables capture differences in recovery time between teams, which may affect performance, while the spread line reflects market expectations about the game outcome. In addition to these inputs, a point differential variable was constructed to measure the actual margin of victory, and an error term was defined as the difference between the observed outcome and the spread. This allows both predictive modeling and evaluation of whether betting markets are systematically biased.


```python
# create target
games["home_win"] = (games["home_score"] > games["away_score"]).astype(int)

# create point differential
games["point_diff"] = games["home_score"] - games["away_score"]

# create error 
games["error"] = games["point_diff"] - games["spread_line"]

# define dataset
d1 = games[
    [
        "home_rest",
        "away_rest",
        "spread_line",
        "point_diff",
        "error",
        "home_win"
    ]
]

df = d1.dropna().copy()

# features + target
features = ["home_rest", "away_rest", "spread_line"]
X = df[features]
y = df["home_win"]
```

## Model Training

Logistic regression was chosen because the outcome variable is binary and the model provides a straightforward way to estimate the relationship between input features and win probability. The inclusion of the spread line reflects aggregated market information and serves as a strong baseline predictor.


```python
try:
    logging.info("Model training started")

    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    print("Accuracy:", accuracy)
    logging.info(f"Model accuracy: {accuracy}")
except Exception as e:
    logging.error(f"Error during model training: {e}")
    print("Error during model training:", e)
```

    Accuracy: 0.6648351648351648



```python
df["error"].mean()
```




    0.09380153930731171



## Visualization

The symmetry of the distribution around zero suggests no strong systematic bias, while the long tails indicate that large prediction errors still occur. This highlights that betting markets are generally well-calibrated but still subject to significant uncertainty at the individual game level.


```python
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.hist(df["error"], bins=30, color="#4C72B0", edgecolor="black", alpha=0.85)

plt.axvline(0, linestyle="--", linewidth=2, color="#DD8452")
plt.title("Prediction Error of Betting Spread", fontsize=14)
plt.xlabel("Actual - Predicted Point Differential", fontsize=12)
plt.ylabel("Frequency", fontsize=12)

for spine in ["top", "right"]:
    plt.gca().spines[spine].set_visible(False)

plt.tight_layout()
plt.show()

mean_error = df["error"].mean()
std_error = df["error"].std()

print("Mean error:", round(mean_error, 2))
print("Std dev:", round(std_error, 2))

logging.info("Bias visualization completed")
```


    
![png](pipeline_files/pipeline_14_0.png)
    


    Mean error: 0.09
    Std dev: 13.2


## Results

The distribution of prediction error is centered close to zero, indicating that betting spreads are approximately unbiased on average. However, the wide spread of values suggests significant variability in individual game outcomes. This indicates that while betting markets are effective at capturing general expectations, they are not precise predictors of exact score differences.

This pipeline integrates data preparation, feature engineering, predictive modeling, and evaluation to analyze NFL game outcomes. By combining betting market data with game-level features, the pipeline not only predicts game results but also evaluates the reliability of betting spreads. 

Overall, betting spreads provide a strong baseline for predicting game outcomes, but their variability highlights the limits of market-based predictions at the individual game level.
