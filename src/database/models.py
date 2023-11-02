import os
from sqlalchemy import Column, String, Integer, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import json
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

#database_filename = "database.db"
#project_dir = os.path.dirname(os.path.abspath(__file__))
#database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

database_path= "postgresql://{}".format(os.getenv("DB_NAME"))


db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    # add one demo row which is helping in POSTMAN test
    
    drink.insert()
    drone = Drone(
        drone_name="Falcon_blue",
        drone_model="T001"
    )

    photo = Photo(
            tag='test',
            content='asdad123asd23423asd1231asdasdadsa',
            drone_id=1
        )

    drink.insert()



class Drone(db.Model):

    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)

    drone_name = Column(String(180), unique=True)

    drone_model = Column(String(180), nullable=False)
    
    photos = db.relationship('Photo', backref="Drone", lazy=True)

    def short(self):
        
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps({
            "id":self.id,
            "drone_name":self.drone_name,
            "drone_model":self.drone_model,
        })


class Photo(db.Model):

    id = Column(Integer(), primary_key=True)

    tag = Column(String(80))
  
    content = Column(String(10000), nullable=False)

    drone_id = Column(Integer(),ForeignKey('Drone.id'),nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps({
            "id":self.id,
            "tag":self.tag,
            "content":self.content,
            "drone_id":self.drone_id
        })