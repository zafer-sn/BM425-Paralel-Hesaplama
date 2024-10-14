def us_al(taban, us):
    if us == 0:
        return 1
    return taban * us_al(taban, us-1)

print(us_al(2, 16))