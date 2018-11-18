#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/topics')
def show_topics():
  return render_template('index.html')


@app.route('/topics/category/<category_name>/new', methods=['GET', 'POST'])
def create_article(category_name):
  print("new article")


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

# GET /
# GET /topics
# GET /topics/category/AI
# GET /topics/category/AI/4

# topics
  # AI
    # article
    # article
  # Software Engineering


  

