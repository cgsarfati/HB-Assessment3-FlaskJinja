from flask import Flask, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


##################### GLOBAL VARIABLES #####################

# Getting our list of MOST LOVED MELONS
MOST_LOVED_MELONS = {
    'cren': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg',
        'name': 'Crenshaw',
        'num_loves': 584,
    },
    'jubi': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg',
        'name': 'Jubilee Watermelon',
        'num_loves': 601,
    },
    'sugb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg',
        'name': 'Sugar Baby Watermelon',
        'num_loves': 587,
    },
    'texb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg',
        'name': 'Texas Golden Watermelon',
        'num_loves': 598,
    },
}


 ##################### HOMEPAGE #####################

# homepage url
@app.route("/")
def display_homepage():
    """Displays homepage with username form."""

    # check if there is a username session already
    # if not, display homepage. if so, redirect to top-melons
    if 'username' in session:
        return redirect('/top-melons')
    else:
        return render_template('homepage.html')


# from homepage, stores session info
@app.route("/get-name")
def store_username_session():

    # add username to session session from homepage form
    session['username'] = request.args.get("username")

    # go back to top melons page
    return redirect('/top-melons')


##################### TOP MELONS PAGE ######################

# from homepage, goes here
@app.route("/top-melons")
def display_top_melons():
    """Displays top 4 melons from UberMelon."""

    # assign dict to var
    fav_melons = MOST_LOVED_MELONS

    # redirect back to homepage if no username session stored
    # if username session exists, continue to top-melons
    if 'username' in session:
        return render_template('/top-melons.html', fav_melons=fav_melons)
    else:
        return redirect('/')


##################### THANK YOU PAGE ######################

# from top melon, goes here
@app.route("/love-melon", methods=["POST"])
def increase_melon_love():
    """Increases a melon's love count from choice in top-melon page."""

    # get melon id (outermost key in global dict) as string, assign to var
    melon_loved = request.form.get("melon-love")

    #increment current num loves to 1
    MOST_LOVED_MELONS[melon_loved]['num_loves'] += 1

    return render_template('thank-you.html')


###########################################################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
