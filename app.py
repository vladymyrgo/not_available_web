from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    aws_link = "https://vgcvweb.s3.eu-west-2.amazonaws.com/templates/"
    return render_template('index.html', aws_link=aws_link)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=8000)
