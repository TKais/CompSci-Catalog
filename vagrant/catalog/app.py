#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/topics')
def show_topics():
  return render_template('index.html')

@app.route('/topics/<topic_name>/')
def show_topic(topic_name):
  print('A particular topic page')


@app.route('/topics/<topic_name>/categories/')
def show_categories(topic_name):
  print('A set of categories within a particular topic')


@app.route('/topics/<topic_name>/categories/new/')
def create_category(topic_name):
  print('new category')


@app.route('/topics/<topic_name>/categories/<category_name>/')
def show_category(topic_name, category_name):
  print('A particular category page')


@app.route('/topics/<topic_name>/categories/<category_name>/new/', methods=['GET', 'POST'])
def create_article(topic_name, category_name):
  print('new article')


@app.route('/topics/<topic_name>/categories/<category_name>/<article_id>/')
def show_article(topic_name, category_name, article_id):
  print('A particular article')


@app.route('/topics/<topic_name>/categories/<category_name>/<article_id>/edit')
def edit_article(topic_name, category_name, article_id):
  print('Edit an article')


@app.route('/topics/<topic_name>/categories/<category_name>/<article_id>/delete')
def delete_article(topic_name, category_name, article_id):
  print('Delete an article')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

# [X] GET /
# [X] GET /topics
# [X] GET /topics/AI/
# [X] GET /topics/AI/categories/new
# [X] GET /topics/AI/categories/Python/
# [X] GET /topics/AI/categories/Python/new
# [X] GET /topics/AI/categories/Python/4
# [X] GET /topics/AI/categories/Python/4/edit
# [X] GET /topics/AI/categories/Python/4/delete


# topics
    # AI
        # article
        # article
    # Software Engineering


  
