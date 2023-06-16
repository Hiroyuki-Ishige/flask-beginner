from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    my_dict = {"insert_something1":"This is insert_something1",
               "insert_something2": "This is insert_something2",
               "test_titles":["title1", "title2", "title3"]
               }

    return render_template("testapp/index.html", my_dict = my_dict)


@app.route("/test")
def other1():
    return "This is test page"





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)