#!/usr/bin/env python
#-*- conding: utf-8 -*-
import re
import sys
import os
import paramiko
import profile
import datetime

hostname = sys.argv[1]
ConfFile = open ('/md/publish/serverInfo.cfg','r')
now = datetime.datetime.now()
logtime = now.strftime('%Y-%m-%d %H:%M:%S')
name_lost = {}
usernamelist = []
for line in ConfFile.readlines():
	rexpect=re.match(r"^#",line)
	rematch=re.search(hostname,line)
	split=re.split('\W+',line)
	if rexpect:
		pass
	else:
		if rematch:
			usernamelist.append([split[0],split[2]])	
		else:
			pass
def log_content(write):
	logname = now.strftime('%Y%m%d')
	logfilename = "/var/log/check_game/%s" %(logname)
	writelog = open(logfilename,'a')	
	writelog.writelines(write)
	writelog.close

def print_lost(info):
	for lost in info:
		return lost, 


def judge(info):
	CorrectNum = len(usernamelist) - len(info)
	if len(info) != 0 :
		print "GameProcs CRITICAL - ErrorNum/AllNum: %s/%s|CorrectNum=%s;AllNum=%s" %(len(info),len(usernamelist),len(usernamelist),CorrectNum)
		for Key in info:
			print_lost_list = print_lost(info[Key])
			out = "%s %s proc error,lost proc list is : %s\n" %(logtime,Key,print_lost_list)
			print out
			log_content(out)
		sys.exit(2)
	else:
		print 'GameProcs OK - CorrectNum/AllNum: %s/%s|CorrectNum=%s;AllNum=%s' %(len(usernamelist),len(usernamelist),len(usernamelist),CorrectNum)
		sys.exit(0)

def ssh(username,zone_s1):
	port = 22
	pkey_file='/root/.ssh/id_rsa'

	key = paramiko.RSAKey.from_private_key_file(pkey_file)
	s = paramiko.SSHClient()
	s.load_system_host_keys()
	s.connect(hostname,port,username,pkey=key)
	if zone_s1 == 's1' or zone_s1 == 's0':
		stdin,stdout,stderr = s.exec_command('awk -F \'\"\' \'/info/{print $4}\' SanServer/ServerConfig.xml SanServer/ServerConfig_kuaqu.xml')
	else:
		stdin,stdout,stderr = s.exec_command('awk -F \'\"\'  \'/info/{print $4}\' SanServer/ServerConfig.xml')
	conprocs = set()
	for conproc in stdout.readlines():
		conprocs.add(conproc) 
	
	stdin,stdout,stderr = s.exec_command('ps x | grep \'\-d\' | grep -v grep | awk  -F \"-n\" \'{print $2}\'')
	nowprocs = set()
	for nowproc in stdout.readlines():
		nowprocs.add(nowproc)
		lostprocs = conprocs - nowprocs
	s.close
#	print len(lostprocs)
	if  len(lostprocs) != 0 :
		lost_list = []
		for lost in lostprocs:
			lost_list.append(lost)


#		print lost_list
		name_lost[username] = lost_list
#		print name_lost

def main():
	for pl_z in usernamelist:
		username = "_%s_%s" %(pl_z[0],pl_z[1])
		ssh(username,pl_z[1])
#	print name_lost
	judge(name_lost)


if __name__ == '__main__':
	main()


#	profile.run( "main()" )


