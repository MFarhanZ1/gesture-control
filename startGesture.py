#!/usr/bin/python3
#coding=utf-8

import os
import dinoGame as dg
import flappyBirdGame as fpg
import time
import pyautogui
import sys

def startMenu():

	os.system('cls')

	banner = """



		██╗  ██╗ █████╗ ███╗   ██╗███████╗      █████╗ ██╗
		██║  ██║██╔══██╗████╗  ██║╚══███╔╝     ██╔══██╗██║	v2.89
		███████║███████║██╔██╗ ██║  ███╔╝█████╗███████║██║	Developed by Hanz	
		██╔══██║██╔══██║██║╚██╗██║ ███╔╝ ╚════╝██╔══██║██║	github.com/mfarhanz1
		██║  ██║██║  ██║██║ ╚████║███████╗     ██║  ██║██║
		╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝     ╚═╝  ╚═╝╚═╝		                                                
	"""


	print(banner)

	inputGame = str(input("\t\tMau Maen Game Apa Nih?\n\t\t1. Dino Game\n\t\t2. Flappy Bird\n\t\t3. Exit\n\n\t\tSilekan Pilih Mau Nomor Berapa \n\t\t>>> "))

	if inputGame == "1" or inputGame == "01":
		print(""" 

\t\tSelamat Bermain Dino Game !

\t\tCara Mainnya :
\t\t1. Kan nanti ada garis putih tuh
\t\t2. Nah kalau mau si dinonya tu loncat \n\t\t   letakin aja telunjuk di atas garis putih
\t\t2. Nah kalau mau si dinonya tu nunduk \n\t\t   letakin aja kelingking di atas garis putih
			""")
		loadBar = "\t\tBentar Ye Loading Dulu Nih Game-nya"

		for x in range (0,8):  
			loadBar += "."
			print (loadBar, end="\r")
			time.sleep(1)

		print("")
		os.system("cls")
		pyautogui.hotkey("winleft","m")
		dg.playDinoGame()

	elif inputGame == "2" or inputGame == "02":
		print(""" 

\t\tSelamat Bermain Flappy Bird Game !

\t\tCara Mainnya :
\t\t1. Kan nanti ada garis putih tuh
\t\t2. Nah kalau mau si burungnya tu loncat \n\t\t   letakin aja telunjuk di atas garis putih


			""")
		loadBar = "\t\tBentar Ye Loading Dulu Nih Game-nya"

		for x in range (0,8):  
			loadBar += "."
			print (loadBar, end="\r")
			time.sleep(1)

		print("")
		os.system("cls")
		pyautogui.hotkey("winleft","m")
		fpg.playFlappyBirdGame()

	elif inputGame == "3" or inputGame == "03":
		os.system("exit")

	# startMenu()

startMenu()