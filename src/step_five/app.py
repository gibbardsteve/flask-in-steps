# Step five - render a page using a jsonnet file using Jinja2 loops and Flask
from flask import Flask, render_template
import json
import _jsonnet

# Create a Flask app instance
app = Flask(__name__)


def load_data():
    # Load the data from the jsonnet file
    data = _jsonnet.evaluate_file('src/step_five/step.jsonnet')
    return json.loads(data)


# Define a route that maps the URL path '/' to the function step_four
@app.route('/')
def step_five():
    # Set up the data to pass to the template
    data = load_data()

    # The view function returns a html file
    return render_template('index.html', **data)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
