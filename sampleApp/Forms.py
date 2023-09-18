from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, EmailField, SubmitField
from wtforms.validators import Length, DataRequired, Email, Regexp


class AddEmployeeForm(FlaskForm):

    # name field
    # validations : min , max length and regexp to ensure no numbers are entered in name field
    name = StringField(
        "Name : ",
        validators=[
            Length(min=3, max=25),
            DataRequired("Please Enter the name"),
            Regexp(regex="^[a-z A-Z]+$",message="Name should only contain Alphabets (a-z A-Z)"), # regex to check if name contains character other then alphabets
        ],
    )

    # email field
    # validations : default email validations
    email = EmailField(
        "Email : ", validators=[DataRequired("Please Enter the email"), Email()]
    )

    # select field for role
    role = SelectField(
        "Role : ",
        choices=[("", "--select role--"), ("role-1", "Role-1"), ("role-2", "Role-2")],
        validators=[DataRequired("Please select one")],
    )
    # Submit button field
    submit = SubmitField("Save Details")
