# Step six - render a page using a markdown file with Jinja2 and Flask
from flask import Flask, render_template_string
import markdown

# Create a Flask app instance
app = Flask(__name__)


def read_markdown():
    # Read the markdown file
    with open('src/step_six/content.md', 'r') as file:
        content = file.read()
    return content


# Define a route that maps the URL path '/' to the function step_six
@app.route('/')
def step_six():
    # Set up the content to pass to the template
    content = read_markdown()

    # Convert the markdown content to html
    html_content = markdown.markdown(content)

    # The view function returns a html file
    return render_template_string(html_content)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
