from os import listdir, path
from time import sleep

api_module = './api'

__all__ = [
    filename.replace('.py', '')
    for filename in listdir(api_module)
    if not path.isdir(
        path.join(api_module, filename)
    ) and filename != '__init__.py'
]
