from flask import Flask
import logging

app = Flask("web-goxorstore", template_folder="gxrstr/templates")

from gxrstr import views
