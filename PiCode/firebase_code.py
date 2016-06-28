import os
import glob
import subprocess
import calendar
import time
import urllib2
import json
import serial

ser = serial.Serial('/dev/ttyACM0', 115200)	
url = 'https://ualberta-ecocar.firebaseio.com/readings.json'


while 1:
	x=ser.readline()
	postdata = {
    		'time': str(calendar.timegm(time.gmtime())),
    		'data': x
    		"""
    		'fc_error' : x[0]
			'fc_state' : x[2]
			'fc_purge_count' : x[4]
			'fc_time_between_last_purges' : x[6]
			'fc_energy_since_last_purge' : x[8]
			'fc_total_energy' : x[10]
			'fc_charge_since_last_purge' : x[12]
			'fc_total_charge' : x[14]
			'fc_volt' : x[16]
			'fc_curr' : x[18]
			'fc_capvolt' : x[20]
			'fc_temp' : x[22]
			'fc_opttemp' : x[24]
			'fc_pres' : x[26]
			'fc_fan_speed' : x[28]
			'fc_start_relay' : x[30]
			'fc_res_relay' : x[32]
			'fc_cap_relay' : x[34]
			'fc_motor_relay' : x[36]
			'fc_purge_valve' : x[38]
			'fc_h2_valve' : x[40]
			"""
		}
 
	req = urllib2.Request(url)
	req.add_header('Content-Type','application/json')
	data = json.dumps(postdata)
 
	response = urllib2.urlopen(req,data)
	



