# Project-2-PredictingNFLGames

**Ruth Melese (cup6cd)**

---

## Initial General Problem and Refined Specific Problem Statement

People are often interested in predicting the outcome of sports games, but it's not as simple as comparing two teams' records. Game results are influenced by a mix of factors like scoring ability, defensive performance, and recent momentum, which makes outcomes difficult to predict using a single statistic.

This project narrows that problem down to building a secondary dataset using the document model. The dataset will organize historical NFL game data into structured documents where each game includes relevant context for both teams, such as average points scored, win percentage, and recent performance. This D1 dataset will then support predicting whether the home or away team is more likely to win a given matchup.

## Rationale for the Refinement

Focusing on predicting individual NFL game outcomes makes the problem more clear and easier to evaluate, since each game has a definite result. A single game already brings together multiple pieces of information, like both teams and how they’ve been performing leading up to that matchup. Instead of pulling that information from different places each time, the dataset is organized so that each game already includes the key details needed for analysis. That makes the data easier to work with and more useful for making predictions.

## Motivation for the Project

This project is interesting to me because predicting sports outcomes is something I already do informally when watching games. It’s easy to look at two teams and make a quick judgment, but those guesses are usually based on a few obvious stats or recent results. I wanted to see what happens when you actually organize more of that information and look at it in a more structured way. It’s also a good opportunity to understand how data organization affects analysis. By building a document-based dataset, each game becomes one complete unit with all the relevant context in one place. That makes it easier to think about the matchup as a whole and use the data in a more meaningful way for prediction.
