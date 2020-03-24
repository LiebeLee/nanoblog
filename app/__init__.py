# app/__ init__.py：Flask应用程序实例#
from flask import Flask
 
app = Flask(__name__)
 
from app import routes