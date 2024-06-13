from wtforms import Form, StringField
from wtforms.validators import DataRequired

class FormBarang(Form):
    namaBarang = StringField('namaBarang', validators=[DataRequired()])
    merk = StringField('merk', validators=[DataRequired()])
    tipe = StringField('tipe', validators=[DataRequired()])
    sn = StringField('sn', validators=[DataRequired()])
    status = StringField('status', validators=[DataRequired()])
