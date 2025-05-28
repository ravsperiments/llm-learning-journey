# 🧭 Spaceship Titanic - Project Plan

## 🎯 Project Objective

Replicate the full end-to-end workflow from the original Titanic Kaggle competition on the Spaceship Titanic dataset — including EDA, feature engineering, preprocessing, modeling, validation, and leaderboard submission.

---

## ✅ Phase 1: Exploratory Data Analysis (EDA)

| Task                                | Output                   | Tools               |
| ----------------------------------- | ------------------------ | ------------------- |
| Load train/test datasets            | `df_train`, `df_test`    | pandas              |
| Null/missing matrix                 | Bar chart or matrix plot | pandas, missingno   |
| Class distribution of `Transported` | Countplot                | seaborn             |
| Plot each feature vs. target        | Histograms, boxplots     | matplotlib, seaborn |
| Understand `Cabin`, `Name`, and IDs | Break into components    | string parsing      |

---

## ✅ Phase 2: Feature Engineering

| Task                                    | Description                                              |
| --------------------------------------- | -------------------------------------------------------- |
| `TotalSpend`                            | Sum of RoomService, FoodCourt, ShoppingMall, Spa, VRDeck |
| `CabinDeck`, `CabinSide`, `CabinNumber` | Extract from `Cabin` string                              |
| Binary columns                          | Clean `CryoSleep`, `VIP` to 0/1 and impute               |
| `Alone` flag                            | Based on family or group info (if inferrable)            |
| Handle missing `Age`                    | Fill with medians or predictive strategy                 |

---

## ✅ Phase 3: Preprocessing Pipeline

| Task                                | Output                                        |
| ----------------------------------- | --------------------------------------------- |
| Encode categoricals                 | One-hot for HomePlanet, Destination, etc.     |
| Normalize numerics                  | StandardScaler or MinMax for Age, Spend, etc. |
| Impute missing values               | Strategy per column                           |
| Create train matrix `X`, target `y` | Final input to models                         |

---

## ✅ Phase 4: Modeling + Validation

| Task                          | Details                                        |
| ----------------------------- | ---------------------------------------------- |
| Baseline: Logistic Regression | Use with/without L2 regularization             |
| Random Forest                 | Tree-based performance and feature importances |
| XGBoost / LightGBM            | Gradient boosting models                       |
| Validation Strategy           | StratifiedKFold (e.g. 5 folds)                 |
| Compare models                | Accuracy, Confusion Matrix, CV scores          |
| Ensemble                      | VotingClassifier or stacking (optional)        |

---

## ✅ Phase 5: Submission + Iteration

| Task                      | Output                              |
| ------------------------- | ----------------------------------- |
| Generate `submission.csv` | `PassengerId`, `Transported`        |
| Submit to Kaggle          | Record leaderboard score            |
| Track CV vs LB score      | Spot overfitting or leakage         |
| Improve based on insights | Iterate on features, tuning, models |

---

## 📁 Notebook Breakdown

| Notebook                       | Purpose                              |
| ------------------------------ | ------------------------------------ |
| `01_eda_baseline.ipynb`        | Load, inspect, visualize, clean data |
| `02_feature_engineering.ipynb` | Parse and construct new features     |
| `03_modeling.ipynb`            | Train, tune, and validate models     |
| `04_submission.ipynb`          | Final prediction and CSV creation    |

---

## 🔁 Optional Enhancements

* Optuna or GridSearchCV for tuning
* Feature importance via SHAP or permutation
* Explainability write-up
* Version tracking for models, CV, LB scores
* Ensembling of diverse classifiers

---

## 🧱 Final Deliverables

* Clean submission with >80% LB accuracy
* Public write-up (optional)
* Git-tracked project with modular notebooks
* Learning log with what worked and what didn’t
