# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach

# POSTS = [("This is the first post.", datetime.datetime.now())] # provided Starter-Code

DATABASENAME = "forum"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  # return reversed(POSTS)      # provided Starter-Code

  # Connect ro an existing database
  conn = psycopg2.connect(database=DATABASENAME)

  # Open a cursor to perform database operations
  cur = conn.cursor()

  # Query the database and obtain data as Python objects
  query = "select content, time from posts order by time desc;"
  cur.execute(query)
  results = cur.fetchall()

  # Close Communication with the database
  cur.close()
  conn.close()

  return results


def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  # POSTS.append((content, datetime.datetime.now()))  # provided Starter-Code


  # Connect ro an existing database
  conn = psycopg2.connect(database=DATABASENAME)

  # Open a cursor to perform database operations
  cur = conn.cursor()

  # Query the database and obtain data as Python objects
  cleaned_content = bleach.clean(content) # necessary in order to stop the spam
  query = "insert into posts (content, time) values (%s, %s)"
  results = cur.execute(query, (cleaned_content,datetime.datetime.now()) )

  # Make the changes to the database persistent
  conn.commit()

  # Close Communication with the database
  cur.close()
  conn.close()
