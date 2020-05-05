Python:
  # start.py
  from flask import Flask, render_template
  app = Flask(__name__, template_folder='./build', static_folder = './build/static')
  @app.route('/')
  def index():
      return render_template('index.html')
  app.run()

Requirement:
  wheel
  click
  Flask
  itsdangerous
  Jinja2
  MarkupSafe
  Werkzeug
Commnad:
python3 start.py
