# getfinalline.py

def getfinalline(filename):
    final_line = ""
    for current_line in open(filename):
        final_line = current_line
    return final_line

print(getfinalline("/home/morrisonw/Desktop/workbench/my-ai/pretraining-text/the-verdict.txt"))
