import datetime

def get_high_score():
    with open('high_scores.txt', 'r') as f:
        text = f.read()
        hige_scores = eval(text)
    return hige_scores


def save_high_score(lst):
    with open('high_scores.txt', 'w') as f:
        text = repr(lst).replace("), (", "),\n(")
        f.write(text)