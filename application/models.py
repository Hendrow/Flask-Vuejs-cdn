from dataclasses import dataclass
from datetime import datetime
from application import db


@dataclass
class Barang(db.Model):
    id: int
    namaBarang: str
    merk: str
    tipe: str
    sn: str
    status: str
    modifikasiData: datetime


    id = db.Column(db.Integer(), primary_key=True)
    namaBarang = db.Column(db.String(140))
    merk = db.Column(db.String(140))
    tipe = db.Column(db.String(200))
    sn = db.Column(db.String(50))
    status = db.Column(db.String(15))
    modifikasiData = db.Column(db.DateTime(), default=datetime.now())


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def __repr__(self):
        return f'(ID Barang: {self.id}-{self.namaBarang})'





