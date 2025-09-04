# Flask Practice Projects

This repository contains several small Flask projects (`pro1` to `pro7`) for learning and practicing Flask web development. Each project demonstrates different features and concepts of Flask.

---

## Project List

### pro1: Hello World
- **File:** [`pro1/app.py`](pro1/app.py)
- **Description:** Basic Flask app that returns a "Hello, world!" message at the root route.

### pro2: Static Routes
- **File:** [`pro2/app.py`](pro2/app.py)
- **Description:** Simple Flask app with three static routes: home, about, and contact. Each route returns a plain text message.

### pro3: Dynamic Routes
- **File:** [`pro3/app.py`](pro3/app.py)
- **Description:** Demonstrates dynamic routes with URL parameters. Includes routes for greeting a user and calculating the square of a number.

### pro4: Template Rendering
- **File:** [`pro4/app.py`](pro4/app.py)
- **Templates:** [`pro4/templates/home.html`](pro4/templates/home.html), [`pro4/templates/about.html`](pro4/templates/about.html), [`pro4/templates/contact.html`](pro4/templates/contact.html)
- **Description:** Uses Jinja2 templates to render HTML pages for home, about, and contact routes. Passes variables to templates.

### pro5: Simple Calculator
- **File:** [`pro5/app.py`](pro5/app.py)
- **Templates:** [`pro5/templates/home.html`](pro5/templates/home.html), [`pro5/templates/result.html`](pro5/templates/result.html)
- **Description:** Implements a simple calculator web app. Users can add, subtract, multiply, or divide two numbers using a form.

### pro6: Template Inheritance
- **File:** [`pro6/app.py`](pro6/app.py)
- **Templates:** [`pro6/templates/layout.html`](pro6/templates/layout.html), [`pro6/templates/home.html`](pro6/templates/home.html), [`pro6/templates/about.html`](pro6/templates/about.html), [`pro6/templates/contact.html`](pro6/templates/contact.html)
- **Description:** Demonstrates template inheritance in Flask. All pages extend a common layout template.

### pro7: CRUD App with Database
- **File:** [`pro7/app.py`](pro7/app.py)
- **Templates:** [`pro7/templates/base.html`](pro7/templates/base.html), [`pro7/templates/index.html`](pro7/templates/index.html), [`pro7/templates/add.html`](pro7/templates/add.html), [`pro7/templates/update.html`](pro7/templates/update.html)
- **Database:** [`pro7/instance/books.db`](pro7/instance/books.db)
- **Description:** A CRUD (Create, Read, Update, Delete) app for managing books using Flask and SQLAlchemy. Users can add, update, and delete books.

---

## How to Run

1. **Install dependencies:**
   ```sh
   pip install flask flask_sqlalchemy