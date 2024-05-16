# Step four - render a page with a jinja2 template using Flask
from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)


# Define a route that maps the URL path '/' to the function step_four
@app.route('/')
def step_four():
    # Set up the data to pass to the template
    data = {
        'page_title': 'Flask in Steps: Step Four',
        'step': 'Step Four',
        'template': 'Jinja2',
    }

    # The view function returns a html file
    return render_template('index.html', **data)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
