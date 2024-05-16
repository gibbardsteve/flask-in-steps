# Step one - render a simple text string using Flask
from flask import Flask

# Create a Flask app instance
app = Flask(__name__)


# Define a route that maps the URL path '/' to the function first_flask
@app.route('/')
def first_flask():
    # The view function returns a string that will be rendered
    # as an HTTP response
    return 'Hello, Flask!'


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
