from flask import Flask, render_template, jsonify, request, redirect, url_for
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import Config

load_dotenv('./.flaskenv')

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import Barang

    @app.route('/')
    def home():
        daftarBarang = Barang.query.all()
        if request.headers.get('X-Requested-Width') =='XMLHttpRequest':
            return jsonify(daftarBarang), 200
        return render_template('latihan.html')
    
    return app