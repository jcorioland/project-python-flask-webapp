"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import python_webapp_flask.views

from applicationinsights.flask.ext import AppInsights
app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = '<YOUR INSTRUMENTATION KEY GOES HERE>'
appinsights = AppInsights(app)