from flask_sqlalchemy import SQLAlchemy
# model
from flask import Flask, render_template, request
import pandas as pd
from pandas.io import sql
import tempfile
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///MedCabinet.db"
    DB.init_app(app)

    @app.route('/', methods=['GET', 'POST'])
    def root():
        return render_template('base.html', title='Contents')

    @app.route('/reset')
    def reset():
        DB.drop_all()
        engine = DB.get_engine()
        sql.execute('DROP TABLE IF EXISTS effects;', engine)
        sql.execute('DROP TABLE IF EXISTS flavor;', engine)
        return render_template('reset.html', title='Reset')

    @app.route('/populate', methods=['GET', 'POST'])
    def populate():
        DB.create_all()
        list_of_effects = ['Giggly', 'Aroused', 'Energetic', 'Sleepy', 'Euphoric', 'Uplifted', 'None', 'Focused', 'Creative', 'Talkative', 
        'Mouth', 'Dry', 'Tingly', 'Relaxed', 'Hungry', 'Happy']
        for x in range(len(list_of_effects)):
            DB.session.add(Effects_list(id=x,effect_terms=list_of_effects[x]))
            DB.session.commit()

        list_of_flavors = ['Sweet', 'Tropical', 'Peach', 'Minty', 'Fruit', 'Coffee', 'Chemical', 'Blueberry', 'Pear', 'Apple', 'Woody', 
        'Cheese', 'Pungent', 'Flowery', 'Pepper', 'Sage', 'Chestnut', 'Strawberry', 'Honey', 'Mint', 'Orange', 'Tobacco', 'Tea', 'Lime', 
        'Grapefruit', 'Lavender', 'Tar', 'Skunk', 'Pine', 'Mango', 'Tree', 'Apricot', 'Vanilla', 'Berry', 'Menthol', 'Violet', 'Blue', 
        'Nutty', 'Grape', 'Pineapple', 'Diesel', 'Ammonia', 'Plum', 'Lemon', 'Butter', 'Citrus', 'Rose', 'Earthy', 'Spicy/Herbal', 'None']
        for x in range(len(list_of_flavors)):
                DB.session.add(Flavors_list(id=x,flavor_terms=list_of_flavors[x]))
                DB.session.commit()

        #Read from file
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        engine = DB.get_engine()

        my_file = os.path.join(THIS_FOLDER, 'effects.csv')
        if my_file:
            df = pd.read_csv(my_file)
            df.to_sql('effects', con=engine)
            DB.session.commit()

        my_file = os.path.join(THIS_FOLDER, 'flavor.csv')
        if my_file:
            df = pd.read_csv(my_file)
            df.to_sql('flavor', con=engine)
            DB.session.commit()

        return render_template('populate.html', title='Populate')
    return app