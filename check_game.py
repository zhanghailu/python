#!/usr/bin/env python
#-*- conding: utf-8 -*-


import commands
import re


def zonename():
	passwdfile = open('/publish/passwd','r')
	
	for line in passwdfile.readlines():
		rematch = re.match(r'_\w+_s(?=\d+:)',line)
		split = re.split(r':',line)
		if rematch:
			print split[0],split[2]
		else:
			pass
def getconprocs(info):
	conprocs = set()
	for line in info:
		rematch = re.match('\s*\<info',line)
		split = re.split('\W+',line)
		if rematch:
			conprocs.add(split[5])
	print conprocs 
	print len(conprocs)
	return conprocs

def getnowprocs(username):
	procsout = commands.getoutput('ps  -u %s' % username)
	print procsout



def getzoneinfo(zonename,zone_s1):
	confidir = "/publish/%s" %(zonename)
	commfname = confidir + '/ServerConfig.xml'
	s1fname = confidir + '/ServerConfig_kuaqu.xml'
	comfile = open(commfname,'r')
	s1file = open(s1fname,'r')
	


	
	if zone_s1 == 's1':
		readalines = comfile.readlines() + s1file.readlines()
		getconprocs(readalines)	
	else:
		readalines = comfile.readlines()
		getconprocs(readalines)

		




if __name__ == '__main__':

	zonename()
	getzoneinfo('_ihuanju_s1','s2')
	getnowprocs('zhangumilu')