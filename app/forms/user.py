from wtforms import Form, PasswordField, SubmitField, validators, StringField
from wtforms.validators import DataRequired

class RegisterationForm(Form):
    nickname = StringField('이름', [validators.Length(min=2, message="2글자 이상")])
    username = StringField('아이디', [validators.Length(min=4, message="4글자 이상")])
    password = PasswordField('확인', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='비밀번호가 일치하지 않습니다.')
    ])
    confirm = PasswordField('비밀번호')


class LoginForm(Form):
    username = StringField('아이디')
    password = PasswordField('비밀번호')
