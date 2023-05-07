from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "YOUR_API_KEY"

def generate_response(prompt):
    try:
        response = openai.Completion.create(
          engine="davinci", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5
        )
        message = response.choices[0].text.strip()
        return message
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    message = request.form['message']
    prompt = f"User: {message}\nAI:"
    response = generate_response(prompt)
    return render_template('results.html', message=message, response=response)

if __name__ == '__main__':
    app.run(debug=True)
