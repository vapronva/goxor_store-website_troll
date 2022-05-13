from flask import Flask

app = Flask("web-goxorstore", template_folder="gxrstr/templates")

from gxrstr import views # skipcq: PY-W2000
