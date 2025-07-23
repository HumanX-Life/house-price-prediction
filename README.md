# 🏠 House Price Prediction

A machine learning application that predicts house prices in Washington state using property features like square footage, bedrooms, bathrooms, location, and more. The project features an XGBoost model optimized with Optuna hyperparameter tuning, served through a FastAPI backend with an interactive Streamlit frontend.

---

## 📦 Project Structure

- `api/` — FastAPI backend with prediction endpoints
- `data/` — Raw and cleaned housing datasets
- `notebooks/` — Jupyter notebooks for EDA, feature engineering, model training, and hyperparameter tuning
- `api/models/` — Saved trained model files (XGBoost with Optuna optimization)
- `streamlit_app/` — Interactive Streamlit frontend application
- `images/` — Data visualization outputs from exploratory data analysis
- `requirements.txt` — Python dependencies

---

## 🚀 Features

- **Machine Learning Model**: XGBoost regressor fine-tuned with Optuna for optimal hyperparameters
- **RESTful API**: FastAPI backend with prediction endpoints and automatic API documentation
- **Interactive Frontend**: User-friendly Streamlit web application for house price predictions
- **Comprehensive EDA**: Detailed exploratory data analysis with visualizations
- **Feature Engineering**: Advanced feature creation including basement percentage, house age, and renovation metrics
- **Data Validation**: Input validation and error handling for robust predictions
- **Clean Architecture**: Modular project structure with separation of concerns

---

## 🛠️ How to Run

```bash
# Step 1: Clone the repo
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction

# Step 2: Install requirements
pip install -r requirements.txt

# Step 3: Run the FastAPI app
cd api
uvicorn main:app --reload --port 8000

# Step 4: Run the Streamlit app (in a new terminal)
cd streamlit_app
streamlit run app.py
```

Once both applications are running:
- FastAPI API will be available at: `http://localhost:8000`
- Interactive docs at: `http://localhost:8000/docs`
- Streamlit app at: `http://localhost:8501`

---

## 📊 Model Performance

The model was trained on Washington state housing data and optimized using Optuna hyperparameter tuning to achieve the best possible predictions for house prices based on property characteristics.