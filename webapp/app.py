from flask import Flask, render_template, request
import json
import boto3
import generate_plots

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('home_page.html')


@app.route("/form")
def form_page():
    return render_template('form.html')


@app.route("/statistics")
def statistics_page():
    price_distribution = generate_plots.get_price_distribution()
    categorical_distribution = generate_plots.get_categorical_distribution()
    numerical_distribution = generate_plots.get_numerical_distribution()

    return render_template('statistics.html', price_distribution=price_distribution, categorical_distribution=categorical_distribution, numerical_distribution=numerical_distribution)


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
    # df = pd.DataFrame(req_data).reindex(columns=col_names)
    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
