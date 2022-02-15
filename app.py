from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
from flask_sqlalchemy import SQLAlchemy
from forms import AddCupcakeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "cupcakes"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route("/")
def index():
    form = AddCupcakeForm()
    if form.validate_on_submit():
        flavor = form.flavor.data
        size = form.size.data
        rating = form.rating.data
        image = form.image.data

        cupcake = Cupcake(flavor = flavor, size = size, rating = rating, image = image)
        db.session.add(cupcake)
        db.session.commit()

        return redirect('/')
    else:
        return render_template("index.html", form = form)

@app.route("/api/cupcakes")
def list_cupcakes():
    """Get data about all cupcakes.
       
        Respond with JSON like: {cupcakes: [{id, flavor, size, rating, image}, ...]}.
        
        The values should come from each cupcake instance
    """
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]

    return jsonify(cupcakes = all_cupcakes)

@app.route("/api/cupcakes/<int:id>")
def get_cupcake(id):
    """Get data about a single cupcake.
        
        Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}.
        
        This should raise a 404 if the cupcake cannot be found.
    """

    cupcake = Cupcake.query.get_or_404(id)

    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes", methods = ["POST"])
def create_cupcake():
    """Create a cupcake with flavor, size, rating and image data from the body of the request.
    
        Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}.
    """

    new_cupcake = Cupcake(flavor=request.json["flavor"], size=request.json["size"], rating=request.json["rating"], image=request.json["image"])

    db.session.add(new_cupcake)
    db.session.commit()

    return(jsonify(cupcake = new_cupcake.serialize()), 201)

@app.route("/api/cupcakes/<int:id>", methods = ["DELETE"])
def delete_cupcake(id):
    """This should raise a 404 if the cupcake cannot be found.

        Delete cupcake with the id passed in the URL. Respond with JSON like {message: "Deleted"}.
    """
    cupcake = Cupcake.query.get_or_404(id)
    
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message = 'Deleted')


@app.route("/api/cupcakes/<int:id>", methods = ["PATCH"])
def update_cupcake(id):
    """Update a cupcake with the id passed in the URL and flavor, size, rating and image data from the body of the request. You can always assume that the entire cupcake object will be passed to the backend.

    This should raise a 404 if the cupcake cannot be found.

    Respond with JSON of the newly-updated cupcake, like this: {cupcake: {id, flavor, size, rating, image}}.
    """
    cupcake = Cupcake.query.get_or_404(id)
    
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)
    
    db.session.commit()
    return jsonify(cupcake = cupcake.serialize())
