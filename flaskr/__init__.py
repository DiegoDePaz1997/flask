import os
from flask import Flask
'''
para inicializar la app desde la terminal
flask --app flaskr --debug run --host=0.0.0.0
'''
def create_app(test_config=None):
    #crea y configura la app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev', #para firmar cookies de secion
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try: os.makedirs(app.instance_path)
    except OSError: pass



    @app.route('/hello/')
    def hello():
        return 'hola mundo'
    
    #segunda parte
    from . import db
    db.init_app(app)

    #tercera parte
    from . import auth
    app.register_blueprint(auth.bp)

    #cuarta parte
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')


    return app


