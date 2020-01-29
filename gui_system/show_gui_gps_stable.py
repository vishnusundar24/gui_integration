import sys
from PyQt5.QtWidgets import QDialog, QApplication
from gps_stable_gui import *
import os
import csv
collecting = 0
vizon = 0
head_curr_lat, head_curr_lon = 0,0
tail_lat, tail_lon = 0,0
curr_pot_angle = 0
robot_heading, wheel_heading = 0,0
steering_cmd = 0
class MyForm(QDialog):
		def __init__(self):
			super().__init__()
			self.ui = Ui_Dialog()
			self.ui.setupUi(self)
			self.read_labels
			self.ui.launch_button.clicked.connect(self.read_labels)
			self.ui.launch_button.clicked.connect(self.write_labels)
			#self.ui.launch_button.clicked.connect(self.launch_file)
			#self.ui.pushrosrun steer_to_waypoint head_gps.py'Button.clicked.connect(self.collectData)
			#self.ui.pushButton_2.clicked.connect(self.stopCollect)
		#	self.ui.Exit.clicked.connect(self.killSwitch)
			self.show()
		def launch_file(self):
			os.system("gnome-terminal -e 'roslaunch gps_stble steer_to_waypoint.launch'")
			read_labels()
			#os.system("roslaunch realsense2_camera rs_camera.launch")
		def collectData(self):
			global collecting
			global vizon
			if collecting == 0:
				self.ui.collectLabel.setText("Collecting...")
				os.system("gnome-terminal -e 'python /home/wisser/catkin_ws/src/GPS-Nav/src/guiberry/logger.py'")
				collecting = 1
				#os.system("python /home/wisser/catkin_ws/src/data_for_randy/src/datetimetest.py")
			if vizon == 0:
				os.system("gnome-terminal -e 'rosrun image_view image_view image:=/camera/color/image_raw'")
				os.system("gnome-terminal -e 'firefox http://192.168.1.4'")
				vizon = 1
		def callback_head_gps(gps_head):
			global head_curr_lat
			global head_curr_lon
			head_curr_lat = gps_data.latitude
			head_curr_lon = gps_data.longitude
		def stopCollect(self):
			self.ui.collectLabel.setText("")
			os.system("gnome-terminal -e 'pkill -f logger.py'")
			#os.system("pkill python datetimetest.py")
			global collecting
			collecting = 0
		def killSwitch(self):
			os.system("gnome-terminal -e 'pkill terminal'")
			#os.system("pkill python")
		def read_labels(self):
			global head_curr_lat
			global head_curr_lon
			global tail_curr_lat
			global tail_curr_lon
			global curr_pot_angle
			global robot_heading
			global wheel_heading
			global steering_cmd
			with open('topic_log.csv', 'r') as readFile:
				reader = csv.reader(readFile)
				lines = list(reader)
				head_curr_lat = str(lines[0][1])
				head_curr_lon = str(lines[1][1])
				tail_curr_lat = str(lines[2][1])
				tail_curr_lon = str(lines[3][1])
				curr_pot_angle = str(lines[4][1])
				robot_heading = str(lines[5][1])
				wheel_heading = str(lines[6][1])
				steering_cmd = str(lines[7][1])
		def write_labels(self):
			global head_curr_lat
			global head_curr_lon
			global tail_curr_lat
			global tail_curr_lon
			global curr_pot_angle
			global robot_heading
			global wheel_heading
			global steering_cmd
			self.ui.head_lon.setText(head_curr_lon)
			self.ui.head_lat.setText(head_curr_lat)
			self.ui.tail_lon.setText(tail_curr_lon)
			self.ui.tail_lat.setText(tail_curr_lat)
			self.ui.pot_angle.setText(curr_pot_angle)
			self.ui.robot_heading.setText(robot_heading)
			self.ui.wheel_heading.setText(wheel_heading)
			self.ui.steering_cmd.setText(steering_cmd)

if __name__=="__main__":
	app = QApplication(sys.argv)
	w = MyForm()
	w.show()
	#read_labels(self)
	#write_labels(self)
	sys.exit(app.exec_())
