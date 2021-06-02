from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, URL, Optional


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL')


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class UserUpdateForm(FlaskForm):
    """ Form for updating users. """
    username = StringField(
        'Username',
        validators=[DataRequired(),
                    Length(max=30)])
    email = StringField(
        'E-mail',
        validators=[DataRequired(),
                    Email()])
    image_url = StringField(
        'Image',
        validators=[DataRequired()])
    header_image_url = StringField(
        'Header Image',
        validators=[DataRequired()])
    bio = StringField(
        'Bio',
        validators=[Optional(),
                    Length(max=300)])
    password = PasswordField(
        'Enter your password',
        validators=[DataRequired(),
                    Length(min=6)]
    )


class UserLogoutForm(FlaskForm):
    """ Form for user logout """


class LikeAddForm(FlaskForm):
    """ Form for adding a like """