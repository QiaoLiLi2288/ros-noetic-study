[1] 四元数 -> RPY角 
[2] 




[1]
def quat_to_angle(quat):
  import PyKDL
  rot = PyKDL.Rotation.Quaternion(quat.x, quat.y, quat.z, quat.w)
  return rot.GetRPY()[2]
