from flask import Flask, render_template, request, redirect, url_for
import json
import boto3

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('home_page.html')


@app.route("/form")
def form_page():
    return render_template('form.html')


@app.route("/data")
def statistics_page():
    return render_template('data.html')


def send_request(endpoint_name, payload, runtime):
    response = runtime.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/json', Body=payload)
    prediction = response['Body'].read()
    prediction = json.loads(prediction)
    return prediction["prediction"]


@app.route("/predict", methods=["POST"])
def predict():
    req_data = json.dumps(request.json)
    runtime = boto3.Session().client(service_name='sagemaker-runtime', region_name='us-east-1')
    endpoint_name = "predict-price"
    result = send_request(endpoint_name, req_data, runtime)
    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
