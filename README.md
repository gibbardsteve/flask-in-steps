# Flask - Step by Step

## Description

A step by step approach to understanding Python Flask, useful for quickly building web applications

## Pre-requisites

The code is written in Python utilising the Flask framework and is packaged using Poetry. It is assumed Poetry is installed on your local system.

The **pyproject.toml** file can be viewed to determine the dependencies in use by this code, these will automatically be installed when the installation steps are followed.

## Installation

Clone the repository and install dependencies:

```bash
git clone <this-repository>
cd <this-repository>
poetry install
```

## Steps

Flask concepts are taught in a step by step approach.  Each step introduces a simple concept and builds upon the previous step to quickly build understanding.

[Step One](src/step_one) builds the most basic Flask application, returning a simple text string when the user navigates to "/"

[Step Two](src/step_two) renders a page using HTML and CSS when the user navigates to "/"

[Step Three](src/step_three) renders a page using the ONS Design System HTML source when the user navigates to "/". This step also shows how multiple routes can be used and linked. three_a shows how Nunjucks components are used to render a page in Flask using the ONS Design System.

[Step Four](src/step_four) renders a page using a hardcoded data structure and Jinja2 template when the user navigates to "/"

[Step Five](src/step_five) renders a page using data from a jsonnet file and introduces loops in Jinja2 templates to dynamically add content when the user navigates to "/"

[Step Six](src/step_six) renders a page using markdown and Jinja2 templates to dynamically add content when the user navigates to "/"

## Usage

Each step is a separate Flask application, each step can be executed by running the following in a terminal window from the project root:

```bash
poetry run python src/step_<number>/app.py
```

This will launch the web page in the browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)
