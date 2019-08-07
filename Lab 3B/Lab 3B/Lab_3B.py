#Jake Desmarais
#SE 126.02
#Lab 3B

import time
import csv
import os


with open("C:/Users/001369972/Desktop/rooms.csv") as csvfile:
	file = csv.reader(csvfile)
	totalRecords = 0
	overLimit = 0

	for record in file:
		roomName = record[0]
		maxCapacity = float(record[1])
		attendees = float(record[2])
		print("------------------------------------------------------")
		print("\n\n\tROOM NAME: ", roomName)
		print("\n\n\tMAX CAPACITY: ",maxCapacity)
		print("\n\n\tATTENDEES: ", attendees)

		fireCode = maxCapacity - attendees

		if fireCode < 0:
			fireCode = abs(fireCode)
			overLimit += 1
			print("\n\n\tWARNING. ROOM EXCEEDS FIRE CODE. {0:2} ATTENDEES NEED TO BE PUT ON THE WAITING LIST FOR THIS EVENT.\n\n\t".format(fireCode))
		else:
			print("\n\n\tThis room is currently within the legal limit.\n\n")
		print("------------------------------------------------------")
		totalRecords += 1

	print("------------------------------------------------------")
	print("\n\n\tTotal Records Processed: ", totalRecords)
	print("\n\n\tRooms Over-Limit: ", overLimit )

		


		