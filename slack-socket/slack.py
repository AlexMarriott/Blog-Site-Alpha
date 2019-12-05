from flask import Flask
from slackeventsapi import SlackEventAdapter
SLACK_SIGNING_SECRET = '3446455ce24f79eb119cf2f03aa8da83'

# This `app` represents your existing Flask app
app = Flask(__name__)


# An example of one of your Flask app's routes
@app.route("/")
def hello():
  return "Hello there!"


# Bind the Events API route to your existing Flask app by passing the server
# instance as the last param, or with `server=app`.
slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, "/slack/events", app)


# Create an event listener for "reaction_added" events and print the emoji name
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
  emoji = event_data["event"]["reaction"]
  print(emoji)


# Start the server on port 3000
if __name__ == "__main__":
  app.run(port=3000)