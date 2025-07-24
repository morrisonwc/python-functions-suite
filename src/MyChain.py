# MyChain.py
# Acts as the itertools.chain. 

def mychain(*args):
    for data in args:
        for item in data:
            yield item

