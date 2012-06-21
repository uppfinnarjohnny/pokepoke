import heroku
import requests
import os

cloud = heroku.from_key(os.environ['HEROKU_API_KEY'])

for app in cloud.apps:
    domain = 'http://{app}.herokuapp.com'.format(app=app.name)
    print 'Poking {domain}'.format(domain=domain)
    requests.get(domain)
