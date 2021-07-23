import random
from time import sleep

def play_size():
	nimsize = None
	while not nimsize:
		nimsize = input("Choose number of rows (4-8): ")
		try:
			nimsize = int(nimsize)
			if nimsize < 4 or nimsize > 8:
				raise ValueError
		except ValueError:
			print("Please choose a number between 4 and 8 inclusive...")
			nimsize = None
	return nimsize

def initialise(nimsize):
	nim = []
	for i in range(0, nimsize):
		nim.append(i+1)
	return(nim)

def print_board(nim):
	print('\n' + '    ' + '='*len(nim))
	for i in range(len(nim)):
		print('[' + chr(ord('A')+i) + '] ' + '|'*nim[i] + ' '*(len(nim)-nim[i] + 2) + '(' + str(nim[i]) + ')')
	print('    ' + '='*len(nim))
	sleep(0.2)
 

def player_turn(nim):
	global player
	player = 1
	print("\n>>>Your turn<<<")
	
	row_chr = None
	while not row_chr:
		row_chr = input("\nChoose a row letter to take from: ")
		try:
			row_num = ord(row_chr.upper())-ord('A')
			if row_num < 0 or row_num > len(nim):
				raise TypeError
			if nim[row_num] == 0:
				print("Selected row has nothing left to take.")
				row_chr = None
		except TypeError:
			print("Please choose a valid row letter.")
			row_chr = None
	
	take_num = None
	while not take_num:
		take_num = input("Choose a number to take: ")
		try:
			take_num = int(take_num)
		except ValueError:
			print("Please choose a whole number.")
			take_num = None
		if take_num > nim[row_num] or take_num < 1:
			print("Please choose a valid number.")
			take_num = None
	
	nim[row_num] = nim[row_num] - take_num
	
	print_board(nim)

def cpu_turn(nim):
	global player
	player = 0
	print("\n<<<CPU's turn>>>")
	sleep(2)
	
	gimlets = [list(range(len(nim)))[i] for i in range(len(nim)) if [nimlet > 1 for nimlet in nim][i]]
	if len(gimlets) == 0:
		gimlets = [list(range(len(nim)))[i] for i in range(len(nim)) if [nimlet > 0 for nimlet in nim][i]]
	cpu_dumb_row = random.choice(gimlets)
	
	imlets = [list(range(len(nim)))[i] for i in range(len(nim)) if [nimlet == 1 for nimlet in nim][i]]
	if len(imlets) % 2 ==  1:
		cpu_dumb_take = nim[cpu_dumb_row]
		
	cpu_dumb_take = random.randint(1, nim[cpu_dumb_row])
	
	nim[cpu_dumb_row] = nim[cpu_dumb_row] - cpu_dumb_take

	print("\nCPU takes " + str(cpu_dumb_take) + " from row " + chr(cpu_dumb_row + ord('A')) + ".")
	print_board(nim)
	
class WinCondition(Exception):
	"""Win condition met"""
	pass
	
def win_condition(nim, player):
	if all(nimlet == 0 for nimlet in nim):
		if player == 1:
			print("\nSorry! You lose!\n")
		if player == 0 :
			print("\nCongratulations! You win!\n")
		input("Press enter to play again.")
		raise WinCondition
	

def play():
	while True:
		nimsize = play_size()
		nim = initialise(nimsize)
		print_board(nim)
		while True:
			try:
				player_turn(nim)
				win_condition(nim, player)
				cpu_turn(nim)
				win_condition(nim, player)
			except WinCondition:
				break

play()
