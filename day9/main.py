year = int(input("What year were you born? "))
if year in range(1925,1947):
    print("You are from Traditionalists!")
elif year in range(1947,1965):
    print("You are from Baby Boomers!")
elif year in range(1965,1982):
    print("You are from Generation X!")
elif year in range(1982,1996):
    print("You are from Millenials!")
elif year in range(1996,2016):
    print("You are from Generation Z!")