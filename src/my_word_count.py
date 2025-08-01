# mywordcount.py

def mywordcount(filename):
    counts = {"characters": 0, "words": 0, "lines": 0}
    unique_words = set()

    for one_line in open(filename):
        counts["lines"] += 1
        counts["characters"] += len(one_line)
        counts["words"] += len(one_line.split())

        unique_words.update(one_line.split())

    counts["unique words"] = len(unique_words)
    for key, value in counts.items():
        print(f'{key}: {value}')


mywordcount("/home/morrisonw/Desktop/workbench/my-ai/pretraining-text/the-verdict.txt")
