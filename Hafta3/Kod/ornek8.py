def topla(*args):
    """toplam = 0
    for i in args:
        toplam += i
    return toplam"""
    return sum(args)

print(topla(3, 5))