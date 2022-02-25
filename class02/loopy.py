x = 0
while x < 5:
	print('hello')
	x += 1

while True:
	option = input("do you want to quit? ")
	if 'y' in option.lower():
		exit()


for x in range(5):
	print(x)

games = ["Gloomhaven", "Radlands", "Res Archana", "Shobu", "That Time You Killed Me"]
for game in games:
	game += " sucks!"
	print(game)
print(games)
