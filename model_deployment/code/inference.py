import joblib
import os
import json
import pandas as pd


def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    return model


def transform_fn(model, request_body, content_type, accept_type):
    if content_type == "application/json" and accept_type == "application/json":
        data = json.loads(request_body)
        df = pd.DataFrame([data])
        price = model.predict(df)[0]
        price = round(price, 3)
        return json.dumps({'prediction': str(price)})
    else:
        raise ValueError(f"{content_type} not supported by script!")

