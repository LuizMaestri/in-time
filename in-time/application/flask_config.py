from flask_api import FlaskAPI
import os

app = FlaskAPI(__name__)
config_file = os.path.join(app.instance_path, 'config.cfg')
app.config.from_pyfile(config_file, silent=True)
