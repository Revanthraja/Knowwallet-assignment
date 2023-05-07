import os
import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)

# ChatGPT API endpoint
API_ENDPOINT = "https://api.openai.com/v1/engines/davinci-codex/completions"


def generate_prompt(user_message):
    prompt = f"Code a Python Flask web application that does the following:\n\n{user_message}\n\nCode:"
    return prompt


def generate_completions(prompt):
    # API request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"
    }

    # API request data
    data = {
        "prompt": prompt,
        "max_tokens": 1024,
        "temperature": 0.7
    }

    # Send request to API
    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    # Handle API response
    if response.status_code == 200:
        response_data = json.loads(response.text)
        completions = response_data["choices"][0]["text"]
        return completions
    else:
        return "Error: API request failed."


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_message = request.form["message"]
        prompt = generate_prompt(user_message)
        completions = generate_completions(prompt)
        return render_template("results.html", user_message=user_message, completions=completions)
    else:
        return render_template("home.html")
@app.route('/results', methods=['POST'])
def results():
    # Handle form data and call ChatGPT API
    return render_template('results.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
