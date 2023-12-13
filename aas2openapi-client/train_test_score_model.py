import joblib
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR

# Daten in dataframe laden
# Daten in X und y unterteilen

# Daten in test und train splitten
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# MLP model
def train_mlp_model(X_train, X_test, y_train, y_test):
    # MLP model erstellen, trainieren & speichern
    model_mlp = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)
    model_mlp.fit(X_train, y_train)
    joblib.dump(model_mlp, "aas2openapi-client/trained_models/model_mlp.pkl")


def test_evaluate_mlp_model(model_mlp, X_test, y_test):
    # MLP model testen
    y_pred_model_mlp = model_mlp.predict(X_test)

    # MLP model evaluieren
    mean_squared_error(y_test, y_pred_model_mlp)


# SVR model
# SVR model erstellen, trainieren & speichern
model_svm_regressor = SVR(kernel="linear", C=1.0)
model_svm_regressor.fit(X_train, y_train)
joblib.dump(model_svm_regressor, "aas2openapi-client/trained_models/model_svm_regressor.pkl")

# SVR model testen
y_pred_model_svm_regressor = model_svm_regressor.predict(X_test)

# SVR model evaluieren
mse_model_svm_regressor = mean_squared_error(y_test, y_pred_model_svm_regressor)
