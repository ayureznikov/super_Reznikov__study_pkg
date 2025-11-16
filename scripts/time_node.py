#!/usr/bin/env python3
import rospy
from datetime import datetime

def main():
    rospy.init_node('time_publisher_node')
    
    rate = rospy.Rate(0.2)

    rospy.loginfo("Time publisher node started! Press Ctrl+C to stop.")

    while not rospy.is_shutdown():
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        rospy.loginfo(f"Current time: {formatted_time}")

        rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass