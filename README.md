# 🍔 Food Delivery Customer Churn Prediction Dashboard

A **Machine Learning + Business Intelligence project** that predicts whether a food delivery customer is **likely to stay or churn** based on service satisfaction, delivery experience, hygiene, and discount-related survey feedback.

This project combines:

* 🌳 **Random Forest Classification**
* 📊 **EDA + Business Insights**
* ⚡ **FastAPI Backend**
* 📘 **Swagger UI API Testing**
* 🎯 **BI Dashboard-ready architecture**

---

# 🚀 Project Preview

## 📘 Swagger UI Screenshot

> Add your screenshot in `screenshots/swagger-ui.png`

![Swagger UI](./screenshots/swagger-ui.png)

## 📊 EDA / Feature Importance Screenshot

> Add your EDA chart screenshot in `screenshots/eda-feature-importance.png`

![EDA Insights](./screenshots/eda-feature-importance.png)

---

# 🎯 Problem Statement

Food delivery platforms face significant **customer churn**, where dissatisfied users stop ordering from the platform.

This project helps businesses **predict churn risk early** using customer survey responses related to:

* Late delivery
* Poor hygiene
* Bad past experiences
* Delivery convenience
* Food quality
* Offers and discounts

This allows businesses to improve:

* retention strategies
* delivery SLAs
* restaurant hygiene monitoring
* targeted discount campaigns

---

# 📊 Dataset

**Kaggle Online Food Dataset**
Dataset link: [https://www.kaggle.com/datasets/sudarshan24byte/online-food-dataset](https://www.kaggle.com/datasets/sudarshan24byte/online-food-dataset)

The dataset contains:

* demographic information
* family size
* ordering behavior
* feedback signals
* churn/stay output labels

### 🎯 Target Column

* `Output`

### ✅ Selected Features

* `Age`
* `Family_size`
* `Late_Delivery`
* `Poor_Hygiene`
* `Bad_past_experience`
* `Long_delivery_time`
* `More_Offers_and_Discount`
* `Good_Food_quality`
* `Ease_and_convenient`

---

# 🧠 Machine Learning Pipeline

```text
Dataset CSV
   ↓
EDA + Data Cleaning
   ↓
Likert Ordinal Mapping
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
🌳 Random Forest Classifier
   ↓
Model Serialization (.pkl)
   ↓
FastAPI Backend
   ↓
Swagger UI
```

---

# 📈 Exploratory Data Analysis (EDA)

The project includes:

* missing value handling
* duplicate removal
* churn class distribution
* feature relation with churn
* ordinal Likert mapping
* numerical feature exploration
* Random Forest feature importance

### 📌 Key Business Insight

High churn probability is strongly associated with:

* repeated late delivery
* poor hygiene complaints
* bad previous experiences
* poor food quality
* low convenience scores

---

# ⚙️ Tech Stack

## 🤖 Machine Learning

* Python
* Pandas
* Scikit-learn
* Joblib

## 🌐 Backend

* FastAPI
* Uvicorn
* Pydantic
* Swagger UI

## 📊 BI / Dashboard

* React (planned)
* KPI cards
* churn analytics charts
* retention recommendation engine

---

# 📂 Project Structure

```text
food-delivery-churn-dashboard/
│
├── backend/
│   ├── data/
│   │   └── onlinedeliverydata.csv
│   │
│   ├── models/
│   │   ├── random_forest.pkl
│   │   └── feature_columns.pkl
│   │
│   ├── api.py
│   ├── main.py
│   ├── churn.py
│   ├── schemas.py
│   └── requirements.txt
│
├── screenshots/
│   ├── swagger-ui.png
│   └── eda-feature-importance.png
│
└── README.md
```

---

# ▶️ Installation & Setup

## 1) Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/food-delivery-customer-churn-dashboard.git
cd food-delivery-customer-churn-dashboard/backend
```

## 2) Install Requirements

```bash
pip install -r requirements.txt
```

## 3) Train Model

```bash
python main.py
```

## 4) Run FastAPI Server

```bash
uvicorn api:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# 🧪 Sample API Test Input

```json
{
  "Age": 28,
  "Family_size": 3,
  "Late_Delivery": "Disagree",
  "Poor_Hygiene": "Disagree",
  "Bad_past_experience": "Disagree",
  "Long_delivery_time": "Disagree",
  "More_Offers_and_Discount": "Agree",
  "Good_Food_quality": "Strongly agree",
  "Ease_and_convenient": "Strongly agree"
}
```

### ✅ Expected Output

```json
{
  "prediction": "Likely to Stay"
}
```

---

# 💼 Business Value

This project enables food delivery platforms to:

* proactively identify churn-risk customers
* personalize retention discounts
* improve restaurant hygiene checks
* optimize delivery operations
* reduce customer acquisition cost

---

# 🚀 Future Scope

## 🎨 Frontend BI Dashboard

Upcoming modules:

* React dashboard
* churn KPI cards
* feature impact charts
* customer segmentation
* retention recommendations
* full-stack deployment

---

# 👩‍💻 Author

**Shreya Malwade**
Final Year IT / AI-ML Project
Food Delivery Customer Churn Prediction + BI Dashboard
