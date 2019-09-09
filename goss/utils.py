import datetime, time
from dateutil import parser
import os
try: # python2.7
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse


__GOSS_URI__ = os.environ.get("GOSS_URI", "localhost:61613")
__GOSS_USER__ = os.environ.get("GOSS_USER", "system")
__GOSS_PASS__ = os.environ.get("GOSS_PASS", "manager")
__GOSS_URI__
if not __GOSS_URI__.startswith("tcp://"):
    __GOSS_URI__ = "tcp://" + __GOSS_URI__
__GOSS_URI_PARSED__ = urlparse(__GOSS_URI__)


def datetime_to_epoche(dt):
    return time.mktime(dt.timetuple()) * 1000


def datestr_to_epoche(dt_str):
    dt = parser.parse(dt_str)
    return datetime_to_epoche(dt)


def epoche_to_datetime(epoche):
    return datetime.datetime.fromtimestamp(epoche)


def utc_timestamp():
    return datetime_to_epoche(datetime.datetime.utcnow())


def validate_goss_uri():
    problems = []

    goss_uri = __GOSS_URI__
    if not goss_uri.startswith("tcp://"):
        goss_uri = "tcp://" + goss_uri

    goss_parsed_uri = urlparse(goss_uri)

    if not goss_parsed_uri.port:
        problems.append("Invalid port specified in URI modify environment GOSS_URI")

    if not goss_parsed_uri.hostname:
        problems.append("Invalid hostname not specified!")

    return problems


def get_goss_address():
    """
    Returns the address in such a way that the response will be
    able to be passed directly to a socket and/or the stomp libraray.

    :return: tuple(adddress, port)
    """
    return (__GOSS_URI_PARSED__.hostname,
            __GOSS_URI_PARSED__.port)


def get_goss_user():
    return __GOSS_USER__


def get_goss_pass():
    return __GOSS_PASS__


def get_goss_application_id():
    """ Retrieve the application_id from the environment.

    In order to use this function an environmental variable `GOSS_APPLICATION_ID`
    must have been set.  For docker containers this is done in the
    `goss.app_registration` callback when the application is started.  If the
    environmental variable is not set an AttributeError will be raised.
    """
    app_id = os.environ.get("GOSS_APPLICATION_ID")
    if not app_id:
        raise AttributeError("environmental variable for GOSS_APPLICATION_ID is not set")
    return app_id


def get_goss_simulation_id():
    """ Retrieve simulation_id from environment.

    This method will return a `None` if the GOSS_SIMULATION_ID environmental
    variable is not set.
    """
    simulation_id = os.environ.get("GOSS_SIMULATION_ID")
    return simulation_id
