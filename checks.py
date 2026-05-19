import requests

sensitive_files = [
    "/robots.txt",
    "/.env",
    "/config.php",
    "/backup.zip"
]

admin_panels = [
    "/admin",
    "/admin/login",
    "/administrator",
    "/admin.php"
]


def check_sensitive_files(target):

    found = []

    for path in sensitive_files:

        try:
            r = requests.get(target + path, timeout=4)

            if r.status_code == 200:
                found.append(path)

        except:
            pass

    return found


def check_admin_panels(target):

    found = []

    for path in admin_panels:

        try:
            r = requests.get(target + path, timeout=4)

            if r.status_code == 200:
                found.append(path)

        except:
            pass

    return found


def check_security_headers(target):

    missing = []

    headers_needed = [
        "X-Frame-Options",
        "X-XSS-Protection",
        "Content-Security-Policy"
    ]

    try:

        r = requests.get(target, timeout=4)

        for h in headers_needed:
            if h not in r.headers:
                missing.append(h)

    except:
        pass

    return missing
