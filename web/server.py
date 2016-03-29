# Simple Web Server using Flask
#
# This server is the basis for the platform which users of the
# application select data that was correctly identified and
# save it or send it for further review.
from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def main():
  return "Hello world"

@app.route("/review")
def showReview():
  return render_template("review.html")

@app.route("/data/<path:path>")
def serverData(path):
  return send_from_directory("data", path)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
