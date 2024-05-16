# Step two - render a page using HTML and CSS using Flask
from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)


# Define a route that maps the URL path '/' to the function step_two
@app.route('/')
def step_two():
    # The view function returns a html file
    return render_template('index.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
