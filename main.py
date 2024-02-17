# This is a sample Python script.

import io
import joblib
from pydantic import BaseModel
from fastapi import FastAPI
import pandas as pd


class Model(BaseModel):
    X: list[str]


app = FastAPI()

loaded_model = joblib.load("model_lgbm.pkl")


#   datetime Accelerometer1RMS Accelerometer2RMS Current Pressure Temperature Thermocouple Voltage Volume Flow RateRMS
#     '2020-03-09 12:01:24',0.027309,0.039927,0.550615,0.054711,70.5721,25.1955,210.323,32.0
@app.post("/predict")
def predict_model(model: Model):
    string_data = """datetime;Accelerometer1RMS;Accelerometer2RMS;Current;Pressure;Temperature;Thermocouple;Voltage;Volume Flow RateRMS\r\n""" + '\r\n'.join(model.X)
    df = pd.read_csv(io.StringIO(string_data), sep=';', index_col='datetime')
    result = loaded_model.predict(df)
    return {"result": ','.join(map(str, result))}


def main():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
