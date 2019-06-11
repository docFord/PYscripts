#!/usr/bin/env python

from time import sleep
from sys import exit
import getpass,shutil,os

#Vars
banner = '''

*-------------------------------------------------------------------------------*
|   _             __       _ _ _                                            	| 
|  | | ___   __ _/ _\_ __ | (_) |_                                          	|
|  | |/ _ \ / _` \ \| '_ \| | | __|                                         	|
|  | | (_) | (_| |\ \ |_) | | | |_                                          	|
|  |_|\___/ \__, \__/ .__/|_|_|\__|                                         	|
|           |___/   |_|                                                     	|
|                                                           		    	|
|    Created by: TkdZZ05tVWdOekVnTWpBZ05HVWdOakVnTm1VZ056a2dObU1nTmpZZ05qYz0=   |
|                                                           			|
|                                                           			|
| This script will parse a csv logfile and split the log lines in the file into |
|   unique logs based on sensor name.   					|
|										|
| These files can then be attached to notification emails to the 		|
|    affected partners.                 					|
|                                                           			|
| Example: <sensorName>.csv, <sensorName1>.csv etc., rather than having to 	|
|		split the file manually in Excel.       			|
|                                                           			|
| Version 1.06                                                      		|
| TLP-PURPDRANK                                                     		|
*-------------------------------------------------------------------------------*
'''



csv = ".csv"
sensorfile = "sensor.csv"
b = getpass.getuser()


#Functions
#-----------------+
#####################

def derr():
    inp = raw_input("Enter log file to split: ")
    if csv in inp:
        return inp
    else:
        print("Input file is not a log file!! \n")
        inp = raw_input("Let's try this again.... Enter a log file to split [in csv format] this time...: ")
        if csv not in inp:
            print("Seriously....")
            exit(1)
        else:
            return inp

def logpath():
    dir1 = os.listdir('/home/') ; dir1
    if b not in dir1:
        dir1 = os.listdir('/home2/home/') ; dir1
        if b in dir1:
            path = "/home2/home/"
            return path
        else:
           print("User not found!")
           return None
    else:
        path = "/home/"
        return path

#Write new logs files based on lines in the input file by like sensor names
def sensor2file(sensor, data):
    file = open(path + b + "/logSplit/" + saveFol + "/" + sensor + ".csv", "a")
    file.write(data)
    file.close()

#Check to see if the directory logSplit exists in the user's directory, 
def mklogsplit():
    c = os.listdir(path + b + '/') ; c
    d = [element.lower() for element in c] ; c
    
    if "logsplit" not in d:
        print("logSplit directory not found in user's home directory. Creating the directory to save all sorted logs into.")
        os.mkdir(path + b + '/logSplit')
    
    else:
        return

#Make the output directory for log files to be saved into, using the name of the input file 
def mkoutputdir():
    os.mkdir(path + b + '/logSplit/' + saveFol)
    print("Created directory: ~/logSplit/" + saveFol + " this is where you will retrieve your logs.")

#Move files for sensor exemptions
def exemptSensors():
    tparty = raw_input("Is this query for a third party entity that the customer does not want to share data with? If so, press y: ")
    tparty.strip('\n')
    #print(tparty[0])

    if tparty[0].lower() == 'y':
        print("Creating the folder sensorExceptions in " + saveFol + " where the logs will be placed for sensors that do not want their data shared.")
        exemptFolder = path + b + '/logSplit/' + saveFol + '/sensorExceptions'
        origFolder = path + b + '/logSplit/' + saveFol
        os.mkdir(exemptFolder)
        sleep(1)
        exemptionList = open(path + b + "/exemptionList.txt", "r")

        for exemptSensor in exemptionList:
            exemptSensor = exemptSensor.strip('\n')
            exemptSensor = origFolder + "/" + exemptSensor + csv
            #print(exemptSensor)

            try:
                shutil.move(exemptSensor, exemptFolder)
            except IOError:
                #print(file + " already exists in " + b + "/completed/")
                pass
        
    else:
        print("Error with input.")
        return

#####################


#Start Runtime
print banner
sleep(1)
inp = derr()

#Input vars
data = open(inp, "r")
rem = inp.split('.csv')
saveFol = str(rem[0])

#Continue runtime
path = logpath()
#print(path) #This is a debug line
sleep(1)
mklogsplit()
sleep(1)
mkoutputdir()
sleep(1)

#Parse the logs by sensor name and append them to the files
for line in data:
    sensor = line.split(",")[11]
    sensor = sensor.strip("\n")
    sensor2file(sensor,line)
sleep(1)
exemptSensors()
#delete the sensor.csv file, which only cointains the header of the input csv file
os.remove(path + b + '/logSplit/' + saveFol + '/' + sensorfile)
