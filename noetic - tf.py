[1 - get tf transform]   
# Find out if the robot uses /base_link or /base_footprint
try:
    self.tf_listener.waitForTransform(self.odom_frame, '/base_footprint', rospy.Time(), rospy.Duration(1.0))
    self.base_frame = '/base_footprint'
except (tf.Exception, tf.ConnectivityException, tf.LookupException):
    try:
        self.tf_listener.waitForTransform(self.odom_frame, '/base_link', rospy.Time(), rospy.Duration(1.0))
        self.base_frame = '/base_link'
    except (tf.Exception, tf.ConnectivityException, tf.LookupException):
        rospy.loginfo("Cannot find transform between /odom and /base_link or /base_footprint")
        rospy.signal_shutdown("tf Exception") 
        
# Get the current transform between the odom and base frames
try:
    (trans, rot)  = self.tf_listener.lookupTransform(self.odom_frame, self.base_frame, rospy.Time(0))
except (tf.Exception, tf.ConnectivityException, tf.LookupException):
    rospy.loginfo("TF Exception")
    
[2 - ]
