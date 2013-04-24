#!/usr/bin/env python
#-*- conding: utf-8 -*-

import sys
import datetime
import getinfo

#now = datetime.datetime.now()
#Date = now.strftime('%Y-%m-%d %H:%M:%S')
#print Date

'''init date => version if version has same change,then change the value init'''
change_d = '2013-04-26 00:00:00'
init_d = datetime.datetime.strptime(change_d,'%Y-%m-%d %H:%M:%S')
init_version = 85




def count_Along(open_day_str):
	open_day = datetime.datetime.strptime(open_day_str,'%Y-%m-%d %H:%M:%S')
	#open_day = datetime.datetime.strptime(open_day_str,'%Y-%m-%d')
	Along = open_day - init_d
	return Along




def select_version(Days):
	if Days > 0:
		print 'After now version,%d days' %(Days)
		change_ver = Days / 7
		version = init_version + change_ver
		return version
	else:
		Days = - Days
		print 'Before now version,%d days' %(Days)
		change_ver = Days / 7
		version = init_version - change_ver
		return version

def main(plant,zone):
	open_day_str = getinfo.getzoneinfo(plant,zone,'/serverInfo.cfg','opentime')
	#print open_day_str
	Along = count_Along(open_day_str)
	version = select_version(Along.days)
	version = "v%d" %(version)
	print version
	return version

if __name__ == '__main__':
	plant = sys.argv[1]
	zone = sys.argv[2]
	main(plant,zone)
