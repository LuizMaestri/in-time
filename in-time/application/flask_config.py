from flask_api import FlaskAPI
import os

app = FlaskAPI('in-time')
config_file = os.path.join(app.root_path, 'config.cfg')
app.config.from_pyfile(config_file, silent=True)
