import requests

def detect_technology(target):

    tech = {}

    try:

        r = requests.get(target, timeout=5)

        headers = r.headers

        if "Server" in headers:
            tech["Server"] = headers["Server"]

        if "X-Powered-By" in headers:
            tech["Language"] = headers["X-Powered-By"]

    except:
        tech["Server"] = "Unknown"

    return tech
