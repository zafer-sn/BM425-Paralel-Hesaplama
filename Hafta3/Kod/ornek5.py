def us_al(taban, us):
    if us == 0:
        return 1
    elif us < 0:
        return 1 / us_al(taban, -us)
    else:
        return taban * us_al(taban, us-1)
    
print(us_al(2, -2))