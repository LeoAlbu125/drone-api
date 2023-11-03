import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
try:
    from src.database.models import db_drop_and_create_all, setup_db, Drone, Photo
    from src.auth.auth import AuthError, requires_auth
except:
    from database.models import db_drop_and_create_all, setup_db, Drone, Photo
    from auth.auth import AuthError, requires_auth


def create_app(test_config=None):

    app = Flask(__name__)
    app.app_context().push()
    setup_db(app)
    CORS(app)


    db_drop_and_create_all()

    # ROUTES

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                                'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                                'GET,PUT,POST,DELETE,OPTIONS')
        return response


    @app.route('/')
    def index():
        return jsonify({
            "success":True
        })




    @app.route('/drones',methods=['GET'])
    def drone_list():
        drones = Drone.query.all()
        if len(drones) == 0:
            abort(404)
        
        return jsonify({
            "success":True,
            "drones": [drone.short() for drone in drones]
        }), 200




    @app.route('/<drone_id>/photos',methods=['GET'])
    @requires_auth('get:photos')
    def drone_photos(payload,drone_id):
        photos_by_drone = Photo.query.filter_by(drone_id=drone_id).all()
        if len(photos_by_drone) == 0:
            abort(404)
        
        return jsonify({
            "success":True,
            "photos": [photos.short() for photos in photos_by_drone]
        }), 200



    @app.route('/photos',methods=['POST'])
    @requires_auth('post:photos')
    def photo_post(payload):
        try:
            form = request.get_json()
            photo = Photo(tag=form['tag'],content=form['content'],drone_id=form['drone_id'])
            photo.insert()
            
            
        except Exception as e:
            print(e)
            abort(422)
            
        return jsonify({
            "success":True,
            "photo":photo.short()
        }), 201
        


    @app.route("/drones/<id>",methods=['PATCH'])
    @requires_auth('patch:drones')
    def drone_patch(payload,id):

        try:
            drone = Drone.query.filter_by(id=id).one_or_none()
            
            if drone:
                form = request.get_json()
                drone_name = form['drone_name']
                drone_model = form['drone_model']
                
                if len(drone_name) != 0:
                    drone.drone_name = drone_name    
                if len(drone_model) != 0:
                    drone.drone_model = drone_model
                    
                drone.update()
                
            else:
                abort(404)
            
        except Exception as error:
            print(error)
            abort(422)
            
        return jsonify({
            "success":True,
            "drone":[drone.short()]
        }), 200



    @app.route("/photos/<id>",methods=['DELETE'])
    @requires_auth('delete:photos')
    def photos_delete(payload,id):

        try:
            photo = Photo.query.filter_by(id=id).one_or_none()
            
            if photo:
                photo.delete()
                
            else:
                abort(404)
            
        except Exception as error:
            print(error)
            abort(422)
            
        return jsonify({
            "success":True,
            "delete":id
        }), 200



    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422




    @app.errorhandler(404)
    def res_not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404


    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500


    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response


    return app

app = create_app()


if __name__== '__main__':
    app.run()