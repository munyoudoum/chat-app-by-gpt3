import openai
import os
from flask import Flask, render_template, request

# Set up the OpenAI API client
openai.api_key = os.environ["OPENAI_API_KEY"]

# Create a Flask app
app = Flask(__name__)

# Set up the root route
@app.route("/")
def index():
    return render_template("index.html")

# Set up a route to handle the form submission
@app.route("/send_message", methods=["POST"])
def send_message():
    # Get the message from the form submission
    message = request.form["message"]

    # Use the OpenAI API to retrieve a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the response from the API response
    response_text = response["choices"][0]["text"]

    # Render the response in the template
    return render_template("index.html", response=response_text)

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
