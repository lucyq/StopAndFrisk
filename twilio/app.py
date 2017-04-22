from flask import Flask, render_template
import twilio.twiml


app = Flask(__name__)

@app.route("/")
def displayIndex():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()



