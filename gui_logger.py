#Author: Vishnusundar Somasundaram


import rospy
import csv
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import NavSatStatus
from std_msgs.msg import Float64
head_curr_lat, head_curr_lon = 0,0
tail_curr_lat, tail_curr_lon = 0,0
curr_pot_angle = 0
robot_heading, wheel_heading = 0,0
steering_cmd = 0
def callback_head_gps(gps_head):
	global head_curr_lat
	global head_curr_lon
	head_curr_lat = gps_head.latitude
	head_curr_lon = gps_head.longitude

def callback_tail_gps(gps_tail):
	print ("2")
	global tail_curr_lat
	global tail_curr_lon
	tail_curr_lat = gps_tail.latitude
	tail_curr_lon = gps_tail.longitude
	print (tail_curr_lat)


def callback_pot_angle(pot_angle):
	global  curr_pot_angle
	curr_pot_angle = pot_angle.data
	write_labels()

def write_labels():
	#print ("3")
	global head_curr_lat
	global head_curr_lon
	global tail_curr_lat
	global tail_curr_lon
	global curr_pot_angle
	global robot_heading
	global wheel_heading
	global steering_cmd
	csvData = [['Head_lat', head_curr_lat], ['Head_lon', head_curr_lon], ['Tail_lat',tail_curr_lat], ['Tail_lon',tail_curr_lon],["Pot_Angle", curr_pot_angle],["Robot Heading", robot_heading]["Wheel Heading",wheel_heading]["Steering Cmd",steering_cmd]]
	with open('topic_log.csv', 'w') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerows(csvData)
	csvFile.close()

def read_labels():
	with open('person.csv', 'r') as readFile:
		reader = csv.reader(readFile)
		lines = list(reader)
		name = str(lines[0][1])
		print(type(name))
		print (name)

if __name__ == '__main__':
	rospy.init_node('gui_logger', anonymous=True)
	#rospy.Subscriber("/camera/color/image_raw", Image, logger)
	rospy.Subscriber("gps_head", NavSatFix, callback_head_gps)
	rospy.Subscriber("gps_tail", NavSatFix, callback_tail_gps)
	rospy.Subscriber("pot_angle", Float64, callback_pot_angle)

	rospy.spin()


#read_labels()
