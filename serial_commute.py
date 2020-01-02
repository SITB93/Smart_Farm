import serial
import time
import shutil
import os
import write_excel

dev_path = 'COM4'
baudrate = 9600
arduino = serial.Serial(dev_path,baudrate)
today = '0_0_0'
now = time.gmtime(time.time())
idx = 0
xlsx_path = ''

while(1):
	check_today = '{}_{}_{}'.format(now.tm_year,now.tm_mon,now.tm_mday)
	if not today == check_today:
		xlsx_path = os.path.join('F:\\OneDrive - sch.ac.kr\\자료_연구실\\프로젝트\\스마트팜_프로젝트\\logging\\{}.xlsx'.format(check_today))
		shutil.copy("F:\\OneDrive - sch.ac.kr\\자료_연구실\\프로젝트\\스마트팜_프로젝트\\logging\\sample.xlsx", "{}".format(xlsx_path))
		idx = 0

	try:
		y = arduino.readline()
		value = y.decode()[:-2]
		idx += 1
		print(value)
		write_excel.write(idx, xlsx_path,value)

	except serial.serialutil.SerialException:
		print("no Data")

	today = '{}_{}_{}'.format(now.tm_year, now.tm_mon, now.tm_mday)

	