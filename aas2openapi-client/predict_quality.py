import joblib

# lade model
loaded_mlp = joblib.load("aas2openapi-client/trained_models/model_mlp.pkl")

# get new data

# predict on new data
result = loaded_mlp.predict()


# result_check aus anderem Projekt
