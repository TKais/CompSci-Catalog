#!/usr/bin/python3

from flask import Flask, render_template, jsonify, request, redirect, url_for, flash, make_response
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from db import Base, Topic, Category, Article, User
from flask import session as login_session
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import random
import string
import json
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "CompSci Catalog"

engine = create_engine('sqlite:///compscicatalog.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Helper methods

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


def find_user(email):
  try:
    user = session.query(User).filter_by(email=email).one()
    return user.id
  except:
    return None


def create_user(login_session):
    new_user = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(new_user)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

# LOGIN Endpoints

@app.route('/login/')
def show_login():
  # Create anti-forgery state token
  state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
  login_session['state'] = state
  return render_template('login.html', STATE = state)

@app.route('/connect', methods=['POST'])
def google_connect():
  if request.args.get('state') != login_session['state']:
    response = make_response(json.dumps('Invalid state parameter.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

  code = request.data

  try:
    # Upgrade the authorization code into a credentials object
    oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
    oauth_flow.redirect_uri = 'postmessage'
    credentials = oauth_flow.step2_exchange(code)
  except FlowExchangeError:
    response = make_response(json.dumps('Failed to upgrade the authorization code.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Check that the access token is valid.
  access_token = credentials.access_token
  url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
         % access_token)
  data = requests.get(url).json()

  # If there was an error in the access token info, abort.
  if data.get('error') is not None:
    response = make_response(json.dumps(data.get('error')), 500)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Verify that the access token is used for the intended user.
  google_id = credentials.id_token['sub']
  if data['user_id'] != google_id:
    response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Verify that the access token is valid for this app.
  if data['issued_to'] != CLIENT_ID:
    response = make_response(json.dumps("Token's client ID does not match app's."), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Store the access token in the session for later use.
  login_session['access_token'] = credentials.access_token
  login_session['google_id'] = google_id

  stored_access_token = login_session.get('access_token')
  stored_google_id = login_session.get('google_id')
  # if stored_access_token is not None and google_id == stored_google_id:
  #   response = make_response(json.dumps('Current user is already connected.'), 200)
  #   response.headers['Content-Type'] = 'application/json'
  #   return response

  # Get user info
  userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
  params = {'access_token': credentials.access_token, 'alt': 'json'}
  answer = requests.get(userinfo_url, params=params)

  user_data = answer.json()

  login_session['username'] = user_data['name']
  login_session['picture'] = user_data['picture']
  login_session['email'] = user_data['email']
  login_session['provider'] = 'google'

  # see if user exists, if it doesn't make a new one
  user_id = find_user(user_data['email'])
  if not user_id:
      user_id = create_user(login_session)
  login_session['user_id'] = user_id

  output = ''
  output += '<h1>Welcome, '
  output += login_session['username']
  output += '!</h1>'
  output += '<img src="'
  output += login_session['picture']
  output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

  return output

# JSON APIs

@app.route('/topics/JSON/')
def return_topics_JSON():
  topics = session.query(Topic)
  return jsonify(topics=[topic.serialize for topic in topics])

@app.route('/topics/<topic_url>/JSON/')
def return_topic_JSON(topic_url):
  topic = session.query(Topic).filter_by(url = topic_url).one()
  categories = session.query(Category).filter_by(topic_id = topic.id)
  return jsonify(categories = [category.serialize for category in categories], topic = topic.serialize)

@app.route('/topics/<topic_url>/categories/<category_url>/JSON')
def return_category_JSON(topic_url, category_url):
  category = session.query(Category).filter_by(url = category_url).one()
  articles = session.query(Article).filter_by(category_id = category.id)
  return jsonify(category = category.serialize, articles = [article.serialize for article in articles])

@app.route('/topics/<topic_url>/categories/<category_url>/<article_id>/JSON/')
def return_article_JSON(topic_url, category_url, article_id):
  article = session.query(Article).filter_by(id=article_id).one()
  return jsonify(article=article.serialize)

# HTML Endpoints

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
    is_unique = check_category_uniqueness(topic.id, request.form['cname']);
    if is_unique:
      new_url = url_maker(request.form['cname'])
      new_category = Category(name=request.form['cname'], url=new_url, topic_id=topic.id)
      session.add(new_category)
      session.commit()
      return redirect(url_for('show_topic', topic_url=topic_url))
    else:
      return render_template('new_category.html', topic=topic, error=True)
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
  return render_template('article.html', article=article, topic_url=topic_url, category_url=category_url)


@app.route('/topics/<topic_url>/categories/<category_url>/<article_id>/edit/', methods=['GET', 'POST'])
def edit_article(topic_url, category_url, article_id):
  article = session.query(Article).filter_by(id = article_id).one()
  if request.method == 'POST':
    if request.form['aname']:
      article.name = request.form['aname']
    if request.form['acontent']:
      article.content = request.form['acontent']
    session.add(article)
    session.commit()
    return redirect(url_for('show_article', topic_url=topic_url, category_url=category_url, article_id=article_id))
  else:
    return render_template('edit_article.html', topic_url=topic_url, category_url=category_url, article_id=article_id, article=article)



@app.route('/topics/<topic_url>/categories/<category_url>/<article_id>/delete/', methods=['GET', 'POST'])
def delete_article(topic_url, category_url, article_id):
  article = session.query(Article).filter_by(id = article_id).one()
  if request.method == 'POST':
    session.delete(article)
    session.commit()
    return redirect(url_for('show_category', topic_url=topic_url, category_url=category_url))
  else:
    return render_template('delete_article.html', topic_url=topic_url, category_url=category_url, article_id=article_id, article=article)


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=5000)