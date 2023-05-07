# Knowwallet-assignment
a. Purpose and Functionality:
The purpose of this web application is to generate text using the OpenAI GPT-3.5 model. The application takes user input as a prompt and generates text based on that input using the API integration with the OpenAI GPT-3.5 model. The generated text is displayed on the results page.

b. Setup, Installation, and Running the Application:
To set up and run the application, follow these steps:

# Clone the repository from GitHub using the following command:

git clone https://github.com/Revanthraja/Knowwallet-assignment.git
# Navigate to the project directory:

cd Knowwallet-assignment
# Run the Flask app:
python app.py

The app will now be running on http://127.0.0.1:5000/.

c. Examples of API Calls and Responses:

API endpoint: /api/generate_text
Request method: POST
Request body: JSON object with a prompt key and a string value representing the prompt text.
Response body: JSON object with a generated_text key and a string value representing the generated text.
