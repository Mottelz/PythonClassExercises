games = ["Gloomhaven", "Radlands", "Res Archana", "Shobu", "That Time You Killed Me"]
print(games)
print(games[1])
print(games[1:])
print(games[:2])
print(games[3:7])
print(games[0:3:2])
print(games[3:0:-2])
print(games[::-1])

best = "Res Archana"
print(best[::-1])

games[1] = "Spirit Island"
print(games)
# This will cause an error, because we can't change strings this way
# best[2] = 'x'
# print(best)
