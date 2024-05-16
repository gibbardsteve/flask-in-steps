# Step three - render a page using ONS design system Flask
from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)


# Define a route that maps the URL path '/' to the function step_three
@app.route('/')
def step_three():
    # The view function returns a html file
    return render_template('index.html')


@app.route('/three_a')
def step_three_a():
    # The view function returns a html file
    return render_template('three_a.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
