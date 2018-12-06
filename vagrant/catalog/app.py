#!/usr/bin/python3

from flask import Flask, render_template, jsonify, request, redirect, url_for, flash, make_response
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from db import Base, Topic, Category, Article

app = Flask(__name__)

engine = create_engine('sqlite:///compscicatalog.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def url_maker(url):
  return url.replace(' ', '-').lower()


def check_category_uniqueness(topic_id, name):
  categories = session.query(Category).filter_by(topic_id=topic_id).all()
  edited_name = name.replace(' ', '').lower()
  for category in categories:
    category_name = category.name.replace(' ', '').lower()
    if edited_name == category_name:
      return False
  return True

# JSON APIs

@app.route('/topics/JSON/')
def return_topics_JSON():
  topics = session.query(Topic)
  return jsonify(topics=[topic.serialize for topic in topics])

@app.route('/topics/<topic_url>/JSON/')
def return_topic_JSON(topic_url):
  topic = session.query(Topic).filter_by(url = topic_url).one()
  return jsonify(topic=topic.serialize)

@app.route('/')
@app.route('/topics/')
def show_topics():
  topics = session.query(Topic)
  return render_template('topics.html', topics=topics)


@app.route('/topics/<topic_url>/')
def show_topic(topic_url):
  topic = session.query(Topic).filter_by(url = topic_url).one()
  categories = session.query(Category).filter_by(topic_id = topic.id).all()
  return render_template('topic.html', topic=topic, categories=categories)


@app.route('/topics/<topic_url>/categories/new/', methods=['GET', 'POST'])
def create_category(topic_url):
  topic = session.query(Topic).filter_by(url = topic_url).one()
  if request.method == 'POST':
    isUnique = check_category_uniqueness(topic.id, request.form['cname']);
    if isUnique:
      new_url = url_maker(request.form['cname'])
      new_category = Category(name=request.form['cname'], url=new_url, topic_id=topic.id)
      session.add(new_category)
      session.commit()
      return redirect(url_for('show_topic', topic_url=topic_url))
    else:
      print('PLEASE CHOOSE A NEW CATEGORY')
      return redirect(url_for('show_topic', topic_url=topic_url))
  else:
    return render_template('new_category.html', topic=topic)


@app.route('/topics/<topic_url>/categories/<category_url>/')
def show_category(topic_url, category_url):
  category = session.query(Category).filter_by(url=category_url).one()
  articles = session.query(Article).filter_by(category_id=category.id).all()
  return render_template('category.html', category=category, articles=articles, topic_url=topic_url)


@app.route('/topics/<topic_url>/categories/<category_url>/new/', methods=['GET', 'POST'])
def create_article(topic_url, category_url):
  if request.method == 'POST':
    category = session.query(Category).filter_by(url=category_url).one()
    new_article = Article(name=request.form['aname'], content=request.form['acontent'], category_id=category.id)
    session.add(new_article)
    session.commit()
    return redirect(url_for('show_category', topic_url=topic_url, category_url=category_url))
  else:
    return render_template('new_article.html')


@app.route('/topics/<topic_url>/categories/<category_url>/<article_id>/')
def show_article(topic_url, category_url, article_id):
  category = session.query(Category).filter_by(url=category_url).one()
  article = session.query(Article).filter_by(id=article_id).one()
  return render_template('article.html', article=article)


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


  

