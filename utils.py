import validators

def validate_url(url):
    return validators.url(url)

def clean_url(url):

    if not url.startswith("http"):
        url = "http://" + url

    return url
