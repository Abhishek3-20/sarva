"""
from celery import Celery
app = Celery('educademy')
app.config_from_object('educademy.settings', namespace='CELERY')

if __name__ == '__main__':
    app.start(argv=['worker', '-P', 'solo', '--loglevel=info'])
"""
