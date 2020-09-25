from random import randint
import os

i = 3
j = 3

mat_to_compare = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
game = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

num_random_moves = 2500
moves = 0
####################################################################
def verify():
	aux = True
	for l in range(len(mat_to_compare)):
		for m in range(len(mat_to_compare[l])):
			if mat_to_compare[l][m] != game[l][m]:
				aux = False
				break
			if aux == False:
				break
	return aux
####################################################################
def print_Matriz():
	for line in game:
	    for num in line:
	        print(f'{num:>3}', end=" ")
	    print()
####################################################################
def random_moves(num):
	aux = 0
	while aux != num :
		a = randint(0,3)
		if a == 0 :
			left_move()
		if a == 1 :
			right_move()
		if a == 2 :
			down_move()
		if a == 3 :
			up_move()
		aux = aux + 1
####################################################################
def left_move():
	global j, game
	if j > 0:
		game[i][j] = game[i][j-1]
		game[i][j-1] = 0
		j = j-1
####################################################################
def right_move():
	global j, game
	if j < 3:
		game[i][j] = game[i][j+1]
		game[i][j+1] = 0
		j = j+1
####################################################################
def down_move():
	global i, game
	if i < 3:
		game[i][j] = game[i+1][j]
		game[i+1][j] = 0
		i = i+1
####################################################################
def up_move():
	global i, game
	if i > 0:
		game[i][j] = game[i-1][j]
		game[i-1][j] = 0
		i = i-1
####################################################################
def option_moves(var):
	if var == "w":
  		up_move()
	elif var == "a":
		left_move()
	elif var == "s":
		down_move()
	elif var == "d":
		right_move()
	else:
	  print("error");
###########				Ranking					####################
def ranking():
	player = input("Qual o seu nome?\n")	
	file = ranking_sort(ranking_read(),player,moves)
	print(ranking_write(file))
####################################################################
def ranking_read():
	file = open("ranking.txt",'r') 
	f = file.read()
	f = f.split("\n")
	aux = []
	for i in f:
		i = i.split(" - ")
		aux = aux + [i[1:]]
	return aux
####################################################################
def ranking_sort(ranking_list, string, moves):
	position = 0
	for i in ranking_list:
		if int(i[1]) > moves:
			break
		position = position + 1
	ranking_list.insert(position, [string, str(moves)])
	return ranking_list[:-1]
####################################################################
def ranking_write(ranking_list):
	aux = ""
	count = 1
	for i in ranking_list:
		aux = aux + " - ".join([str(count)]+i) + "\n"
		count = count + 1
	file = open('ranking.txt','w')
	file.write(str(aux[:-1]))
	file.close()
	return  aux[:-1]
####################################################################
def main():
	global i,j,mat_to_compare,game,moves,num_random_moves
	random_moves(num_random_moves)
	while not(verify()) :
		print_Matriz()
		move = input("\n")
		option_moves(move)
		os.system("cls")
		moves = moves + 1
		print(moves)
####################################################################
main()
ranking()