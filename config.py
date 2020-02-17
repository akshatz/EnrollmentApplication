import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET KEY') or "secret_string"

    MONGODB_SETTINGS ={'db':'Enrollment',
        #'host':'mongodb://127.0.0.1:27001/Enrollment'
    }