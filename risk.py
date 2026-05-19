def calculate_risk(results):

    score = 0

    if results["Sensitive Files"]:
        score += 40

    if results["Admin Panels"]:
        score += 30

    if results["Missing Security Headers"]:
        score += 20

    if results["Open Ports"]:
        score += 10

    if score > 100:
        score = 100

    return score
