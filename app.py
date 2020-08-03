from flask import Flask, request, render_template
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "chickenzarecooll21837"

debug = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    html = """
    <html>
        <body>
            <h1>Home Page</h1>
            <p>Welcome to my simple app!</p>
            <a href='/hello'> Go to hello page</a>
        </body>
    </html>
    """
    return html


@app.route("/form")
def show_form():
    return render_template("form.html")


@app.route("/form-2")
def show_form_2():
    return render_template("form_2.html")


COMPLIMENTS = ["cool", "clever", "tenacious", "awesome", "pythonic"]


@app.route("/greeter")
def get_greeting():
    username = request.args["username"]
    compliment = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment=compliment)


@app.route("/greeter-2")
def get_greeting_2():
    username = request.args["username"]
    wants_compliments = request.args.get("wants_compliments")
    compliment = choice(COMPLIMENTS)
    nice_things = sample(COMPLIMENTS, 3)
    return render_template(
        "greet_2.html",
        username=username,
        wants_compliments=wants_compliments,
        compliment=nice_things,
    )


@app.route("/lucky")
def lucky_number():
    num = randint(1, 10)
    return render_template("lucky.html", lucky_num=num, msg="you are so lucky!")


@app.route("/spell/<word>")
def spell_word(word):
    caps_word = word.upper()
    return render_template("spell_word.html", word=caps_word)


@app.route("/hello")
def say_hello():
    """Shows Hello Page"""
    return render_template("hello.html")


@app.route("/goodbye")
def say_bye():
    return "GOOD BYE!!!"


@app.route("/search")
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search Results For: {term}</h1> <p>Sorting by: {sort}</p>"


# @app.route("/post", methods=["POST"])
# def post_demo():
#     return "YOU MADE A POST REQUEST"


@app.route("/add-comment")
def add_comment_form():
    return """
    <h1>Add your Comment!</h1>
    <form method="POST">
        <input type='text' placeholder='comment' name='comment'/>
        <input type='text' placeholder='username' name='username'/>
        <button>Submit</button>
    </form>
    """


@app.route("/add-comment", methods=["POST"])
def save_comment():
    """"""
    comment = request.form["comment"]
    username = request.form["username"]
    return f"""
      <h1>Saved your comment</h1>
      <ul>
        <li>Username: {username}</li>
        <li>Comment: {comment}</li>
      </ul>
    """


@app.route("/r/<subreddit>")
def show_subreddit(subreddit):
    return f"<h1>Browsing The {subreddit} subreddit </h1>"


@app.route("/r/<subreddit>/comments/<int:post_id>")
def show_comments(subreddit, post_id):
    return f"<h1>Viewing comments for post with: {post_id} from the {subreddit} subreddit </h1>"


POSTS = {
    1: "I like chicken tenders",
    2: "I hate mayo!",
    3: "Double rainbow all the way",
    4: "YOLO OMG (Kill me)",
}


@app.route("/posts/<int:id>")
def find_post(id):
    post = POSTS.get(id, "post not found")
    return f"<p>{post}</p>"
