"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]

TEMPLATES = ["madlib.html", "madlib_2.html", "madlib_3.html"]


@app.route("/")
def start_here():
    """Display homepage."""

    return render_template("index.html")


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def show_madlib_form():

    """ Shows the user's responce to the question  """

    play_choice = request.args.get("play_choice")

    if play_choice == "yes":
        return render_template("game.html")    
    else:
        return render_template("goodbye.html", play_choice=play_choice)


@app.route("/madlib")
def show_madlib():
    alias = request.args.get("alias")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    flowers = request.args.getlist("flowers")  

    template = choice(TEMPLATES)  

    return render_template(template, alias=alias, color=color, noun=noun, adjective=adjective, flowers=flowers)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
