[README.md](https://github.com/user-attachments/files/35469596/README.md)
Loan Approval Prediction System

A web-based loan approval prediction project built with **Python, Flask, Pandas, NumPy, and Scikit-learn**. The application accepts an applicant's financial details, sends the values to a trained Decision Tree classification model, and displays a predicted loan status: **Approved** or **Rejected**.

> Project purpose: This is an academic machine-learning project demonstrating data preprocessing, model training, prediction, and integration of a machine-learning model into a Flask web application. Its predictions are not financial advice and must not be used as the sole basis for real lending decisions.

Features

- Loan status prediction:** Predicts an applicant's loan status using nine applicant and financial attributes.
- Machine-learning model:** Uses a Decision Tree Classifier with entropy as the splitting criterion and a maximum depth of 5.
- Web interface:** Uses Flask routes to handle login, registration, applicant input, and prediction-result pages.
- Prediction logging:** Appends submitted applicant details and the predicted status to `user_data.csv`.
- Model persistence:** Saves the trained model as `model.pkl` using Python's `pickle` module so the Flask application can load it.

Technology Stack

| Component | Technology |
| Programming language | Python |
| Web framework | Flask |
| Data processing | Pandas, NumPy |
| Machine learning | Scikit-learn |
| Model | Decision Tree Classifier |
| Model serialization | Pickle |
| Data storage | CSV files |

Dataset and Model Inputs

The training dataset is `data.csv`. It contains **4,269 records** and the following columns:

| Input feature | Description |
| `no_of_dependents` | Number of dependents |
| `income_annum` | Applicant's annual income |
| `loan_amount` | Requested loan amount |
| `loan_term` | Loan term |
| `cibil_score` | Applicant's CIBIL score |
| `residential_assets_value` | Value of residential assets |
| `commercial_assets_value` | Value of commercial assets |
| `luxury_assets_value` | Value of luxury assets |
| `bank_asset_value` | Value of bank assets |

The target column is `loan_status`, mapped to numeric labels during training:

- `Approved` → `1`
- `Rejected` → `0`

The `loan_id` column is present in the dataset but is not used as a model input.

## Model Training

The training script (`model(1).py`) performs the following steps:

1. Loads `data.csv` with Pandas.
2. Converts the text labels in `loan_status` into numeric target values.
3. Selects the nine applicant and financial attributes as model features.
4. Creates a `DecisionTreeClassifier` with `criterion='entropy'`, `max_depth=5`, and `random_state=42`.
5. Fits the classifier and saves the trained model to `model.pkl`.
6. Prints the model's accuracy on the same data used for training.

To retrain the model, run:

```bash
python "model(1).py"
```

The command recreates `model.pkl` in the project directory.

## Project Structure

```text
Loan-Approval-Prediction/
│
├── app.py                 # Flask application and prediction routes
├── login.py               # Login validation function
├── model(1).py            # Model training script
├── model.pkl              # Serialized trained Decision Tree model
├── data.csv               # Training dataset
├── login.csv              # Local login and registration data
├── user_data.csv          # Created/appended by the app to log predictions
├── templates/             # HTML pages rendered by Flask (required)
│   ├── login.html
│   ├── register.html
│   ├── home.html
│   ├── predictor.html
│   ├── result.html
│   └── about.html
└── README.md
```

The HTML templates are referenced by `app.py` and must be present in a `templates/` directory. They were not included among the project files supplied for this README.

## Installation and Setup

### 1. Clone or download the project

```bash
git clone <your-repository-url>
cd Loan-Approval-Prediction
```

If you are not using Git, extract the project files into one folder and open that folder in your terminal.

### 2. Create and activate a virtual environment (recommended)

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install Flask numpy pandas scikit-learn
```

### 4. Check the project files

Make sure `app.py`, `login.py`, `model.pkl`, `login.csv`, and the `templates/` directory are in the project folder. Keep `data.csv` and `model(1).py` in the folder if you intend to retrain the model.

### 5. Run the application

```bash
python app.py
```

Open the local address printed by Flask in your browser. By default, Flask runs on port `5000`.

Application Workflow

1. The user opens the login page.
2. The application validates the submitted credentials against `login.csv`.
3. After login, the user navigates to the loan prediction form.
4. The form submits the nine model input values to the Flask prediction route.
5. The application loads the trained model and predicts the loan status.
6. The result page displays **Approved** or **Rejected**, and the submitted values and prediction are appended to `user_data.csv`.

Notes and Limitations

- The accuracy printed by the training script is calculated on the same dataset used to train the model. It is **training accuracy**, not an independent test result. A separate train/test split or cross-validation should be used to estimate how well the model generalizes to new applicants.
- The current login implementation stores passwords as plain text in `login.csv`. This is suitable only for a basic classroom demonstration; a real application should use secure password hashing and a proper database.
- The Flask application currently runs with `debug=True`. Debug mode should be disabled before any deployment, and the development server should not be exposed publicly.
- Input validation, error handling, authorization, and data privacy protections should be strengthened before using the application beyond a local academic demonstration.
- Only use trusted model files. Loading a pickle file from an untrusted source can execute malicious code.

Possible Improvements

- Add a train/test split and report precision, recall, F1-score, and a confusion matrix.
- Replace CSV-based login storage with a database and hashed passwords.
- Add server-side validation for all prediction inputs.
- Improve the interface with clearer form guidance and prediction explanations.
- Add model versioning and an evaluation report.

Author

Madhanakrishnan M  
M.Sc. Computer Science | DGDVC 
mail:madhanakrishnan5310@gmail.com | LinkedIn:/in/madhanakrishnan-m-408391235?


*Developed as an academic machine-learning and web application project.*
