from checks import (
    check_sensitive_files,
    check_admin_panels,
    check_security_headers
)

from port_scan import scan_ports
import urllib.parse


def run_scan(target):

    results = {}

    results["Sensitive Files"] = check_sensitive_files(target)

    results["Admin Panels"] = check_admin_panels(target)

    results["Missing Security Headers"] = check_security_headers(target)

    host = urllib.parse.urlparse(target).hostname

    results["Open Ports"] = scan_ports(host)

    return results
