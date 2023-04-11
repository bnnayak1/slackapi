import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

SLACK_BOT_TOKEN="xoxb-"
SLACK_APP_TOKEN="xapp-1-2"
# Install the Slack app and get xoxb- token in advance
app = App(token=SLACK_BOT_TOKEN)

@app.command("/hello-socket-mode")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi, <@{user_id}>!")

@app.event("app_mention")
def event_test(say):
    say("I am good, How are you")

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
