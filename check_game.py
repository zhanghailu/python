#!/usr/bin/env python
#-*- conding: utf-8 -*-


import commands
import os
import re
import sys


def zonenamelist():
	passwdfile = open('/etc/passwd','r')
	zonelist = {}
	for line in passwdfile.readlines():
		rematch = re.match(r'_\w+_s(?=\d+:)',line)
		split = re.split(r':',line)
		if rematch:
			zonelist[split[0]] = split[2]
		else:
			pass
	return zonelist
def getconprocs(info):
	conprocs = set()
	for line in info:
		rematch = re.match('\s*\<info',line)
		split = re.split('\W+',line)
		if rematch:
			conprocs.add(split[5])
	return conprocs

def getnowprocs(username,userid,procs):
#	procsout = commands.getoutput('ps e -u %s ' % username)
	nowprocs = set() 
	for line in procs:
		rematchname = re.match(username,line)
		rematchid = re.match(userid,line)
		split = re.split('\s+',line)
		if rematchname or rematchid:
			nowprocs.add(split[1])
	return nowprocs


def getzoneinfo(zonename):
	confidir = "/home/%s" %(zonename)
	commfname = confidir + '/SanServer/ServerConfig.xml'
	s1fname = confidir + '/SanServer/ServerConfig_kuaqu.xml'
	comfile = open(commfname,'r')
	s1file = open(s1fname,'r')
	zone_s1 = zonename.split('_')[2]
	if zone_s1 == 's1':
		readalines = comfile.readlines() + s1file.readlines()
		nowprocs = getconprocs(readalines)	
	else:
		readalines = comfile.readlines()
		nowprocs = getconprocs(readalines)
	return nowprocs
		
def judgeinfo(conprocs,nowprocs,zonename):
	judge = len(conprocs) - len(nowprocs)
	if judge != 0:
		lostlist = conprocs - nowprocs
		lostdic[zonename] = lostlist
#		print "%s lost" %(zonename )
	else:
#		print "%s is OK" %(zonename) 
		pass
	

if __name__ == '__main__':
	lists = zonenamelist()
	procs = os.popen('ps aux | awk -F \'-n| +\' \'{print $1\" \"$NF}\'')
	procswap = procs.readlines()
	for Key in lists:
		zonename = Key
		zoneid = lists[Key]
		conprocs = getzoneinfo(zonename)
		nowprocs = getnowprocs(zonename,zoneid,procswap)
		judgeinfo(conprocs,nowprocs,zonename)
	lostdic = {}
	Error = len(lostdic)
	All = len(lists)
	Correct = All - Error
	if len(lostdic) == 0:
		print 'GameProcs OK - CorrectNum/AllNum: %s/%s|CorrectNum=%s;AllNum=%s' %(Correct,All,Correct,All)
		sys.exit(0)
	else:
		print 'GameProcs CRITCAL - ErrorNum/AllNum: %s/%s|CorrectNum=%s;AllNum=%s' %(Error,All,Correct,All)
		sys.exit(2)
