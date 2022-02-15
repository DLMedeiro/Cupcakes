from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,FloatField
from wtforms.validators import InputRequired, URL, NumberRange


class AddCupcakeForm(FlaskForm):
    """Form for adding a cupcake"""

    flavor = StringField("Cupcake Flavor", validators = [InputRequired(message = "Flavor can't be blank")])

    size = SelectField("Cupcake Size", 
        choices = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])
    
    rating = FloatField("Cupcake Rating", validators = [NumberRange(min=1, max=10, message="Rating must be between 1 and 10")])

    image = StringField("Cupcake Photo", validators = [URL()], default = "https://tinyurl.com/demo-cupcake")
