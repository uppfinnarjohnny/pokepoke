import heroku
import requests
import os
import sched
import time


def poke(domain):
    print 'Poking {domain}'.format(domain=domain)
    requests.get(domain)


def poke_all(apps):
    for app in apps:
        poke('http://{app}.herokuapp.com'.format(app=app.name))


def run(cloud, sch):
    poke_all(cloud.apps)
    sch.enter(3600, 1, run, (cloud, sch))

if __name__ == '__main__':
    cloud = heroku.from_key(os.environ['HEROKU_API_KEY'])
    scheduler = sched.scheduler(time.time, time.sleep)
    run(cloud, scheduler)
    scheduler.run()
