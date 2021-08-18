from flask import Flask
import os
import yaml
# import bcrypt

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        if app.config['ENV'] == 'development':
            config_file = os.path.join(app.instance_path, 'development.yaml')
            app.config.from_file(config_file, load=yaml.safe_load)


    @app.route('/hello')
    def hello():
        return 'hello world'
    
    #register the database
    from . import db_model
    db_model.init_app(app)

    #apply the blueprints to the app
    from . import auth_controller
    app.register_blueprint(auth_controller.bp)

    return app