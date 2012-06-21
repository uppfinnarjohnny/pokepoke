import heroku
import requests
import os

cloud = heroku.from_key(os.environ['HEROKU_API_KEY'])

for app in cloud.apps:
    try:
        domain = 'http://' + app.domains[0].domain
    except IndexError:  # if there are no custom domains
        domain = 'http://{app}.herokuapp.com'.format(app=app.name)

    print 'Poking {domain}'.format(domain=domain)
    requests.get(domain)
