#!/usr/bin/python
# Filename: ndpromp_joint_emg.py

from __future__ import print_function

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import scipy.signal as signal
import ipromps
# import rospy

plt.close('all')    # close all windows
len_normal = 101    # the len of normalized traj
nrDemo = 20         # number of trajectoreis for training


#########################################
# load EMG date sets
#########################################
print('loading EMG data sets of aluminum hold task')
# read emg csv files of aluminum_hold
dir_prefix = '../../recorder/datasets/imu_emg_joint_3_task/aluminum_hold/csv/'
train_set_aluminum_hold_emg_00_pd = pd.read_csv(dir_prefix + '2017-07-09-09-57-38-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_01_pd = pd.read_csv(dir_prefix + '2017-07-09-09-57-55-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_02_pd = pd.read_csv(dir_prefix + '2017-07-09-09-58-24-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_03_pd = pd.read_csv(dir_prefix + '2017-07-09-09-58-51-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_04_pd = pd.read_csv(dir_prefix + '2017-07-09-09-59-13-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_05_pd = pd.read_csv(dir_prefix + '2017-07-09-10-00-01-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_06_pd = pd.read_csv(dir_prefix + '2017-07-09-10-01-08-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_07_pd = pd.read_csv(dir_prefix + '2017-07-09-10-01-38-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_08_pd = pd.read_csv(dir_prefix + '2017-07-09-10-02-08-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_09_pd = pd.read_csv(dir_prefix + '2017-07-09-10-02-29-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_10_pd = pd.read_csv(dir_prefix + '2017-07-09-10-02-52-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_11_pd = pd.read_csv(dir_prefix + '2017-07-09-10-03-26-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_12_pd = pd.read_csv(dir_prefix + '2017-07-09-10-03-43-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_13_pd = pd.read_csv(dir_prefix + '2017-07-09-10-04-17-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_14_pd = pd.read_csv(dir_prefix + '2017-07-09-10-04-36-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_15_pd = pd.read_csv(dir_prefix + '2017-07-09-10-04-57-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_16_pd = pd.read_csv(dir_prefix + '2017-07-09-10-05-20-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_17_pd = pd.read_csv(dir_prefix + '2017-07-09-10-05-46-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_18_pd = pd.read_csv(dir_prefix + '2017-07-09-10-06-07-myo_raw_emg_pub.csv')
train_set_aluminum_hold_emg_19_pd = pd.read_csv(dir_prefix + '2017-07-09-10-06-36-myo_raw_emg_pub.csv')
test_set_aluminum_hold_emg_pd = pd.read_csv(dir_prefix + '2017-07-09-10-07-04-myo_raw_emg_pub.csv')
# invert the object to float32 for easy computing
train_set_aluminum_hold_emg_00 = np.float32(train_set_aluminum_hold_emg_00_pd.values[:,5:13])
train_set_aluminum_hold_emg_01 = np.float32(train_set_aluminum_hold_emg_01_pd.values[:,5:13])
train_set_aluminum_hold_emg_02 = np.float32(train_set_aluminum_hold_emg_02_pd.values[:,5:13])
train_set_aluminum_hold_emg_03 = np.float32(train_set_aluminum_hold_emg_03_pd.values[:,5:13])
train_set_aluminum_hold_emg_04 = np.float32(train_set_aluminum_hold_emg_04_pd.values[:,5:13])
train_set_aluminum_hold_emg_05 = np.float32(train_set_aluminum_hold_emg_05_pd.values[:,5:13])
train_set_aluminum_hold_emg_06 = np.float32(train_set_aluminum_hold_emg_06_pd.values[:,5:13])
train_set_aluminum_hold_emg_07 = np.float32(train_set_aluminum_hold_emg_07_pd.values[:,5:13])
train_set_aluminum_hold_emg_08 = np.float32(train_set_aluminum_hold_emg_08_pd.values[:,5:13])
train_set_aluminum_hold_emg_09 = np.float32(train_set_aluminum_hold_emg_09_pd.values[:,5:13])
train_set_aluminum_hold_emg_10 = np.float32(train_set_aluminum_hold_emg_10_pd.values[:,5:13])
train_set_aluminum_hold_emg_11 = np.float32(train_set_aluminum_hold_emg_11_pd.values[:,5:13])
train_set_aluminum_hold_emg_12 = np.float32(train_set_aluminum_hold_emg_12_pd.values[:,5:13])
train_set_aluminum_hold_emg_13 = np.float32(train_set_aluminum_hold_emg_13_pd.values[:,5:13])
train_set_aluminum_hold_emg_14 = np.float32(train_set_aluminum_hold_emg_14_pd.values[:,5:13])
train_set_aluminum_hold_emg_15 = np.float32(train_set_aluminum_hold_emg_15_pd.values[:,5:13])
train_set_aluminum_hold_emg_16 = np.float32(train_set_aluminum_hold_emg_16_pd.values[:,5:13])
train_set_aluminum_hold_emg_17 = np.float32(train_set_aluminum_hold_emg_17_pd.values[:,5:13])
train_set_aluminum_hold_emg_18 = np.float32(train_set_aluminum_hold_emg_18_pd.values[:,5:13])
train_set_aluminum_hold_emg_19 = np.float32(train_set_aluminum_hold_emg_19_pd.values[:,5:13])
test_set_aluminum_hold_emg = np.float32(test_set_aluminum_hold_emg_pd.values[:,5:13])
#########################################################################################################
print('loading EMG data sets of spanner handover task')
# read emg csv files of spanner_handover
dir_prefix = '../../recorder/datasets/imu_emg_joint_3_task/spanner_handover/csv/'
train_set_spanner_handover_emg_00_pd = pd.read_csv(dir_prefix + '2017-07-09-09-29-42-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_01_pd = pd.read_csv(dir_prefix + '2017-07-09-09-30-17-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_02_pd = pd.read_csv(dir_prefix + '2017-07-09-09-30-41-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_03_pd = pd.read_csv(dir_prefix + '2017-07-09-09-31-03-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_04_pd = pd.read_csv(dir_prefix + '2017-07-09-09-31-23-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_05_pd = pd.read_csv(dir_prefix + '2017-07-09-09-31-40-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_06_pd = pd.read_csv(dir_prefix + '2017-07-09-09-32-24-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_07_pd = pd.read_csv(dir_prefix + '2017-07-09-09-32-43-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_08_pd = pd.read_csv(dir_prefix + '2017-07-09-09-33-04-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_09_pd = pd.read_csv(dir_prefix + '2017-07-09-09-33-23-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_10_pd = pd.read_csv(dir_prefix + '2017-07-09-09-33-40-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_11_pd = pd.read_csv(dir_prefix + '2017-07-09-09-34-00-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_12_pd = pd.read_csv(dir_prefix + '2017-07-09-09-34-32-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_13_pd = pd.read_csv(dir_prefix + '2017-07-09-09-34-49-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_14_pd = pd.read_csv(dir_prefix + '2017-07-09-09-35-11-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_15_pd = pd.read_csv(dir_prefix + '2017-07-09-09-35-49-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_16_pd = pd.read_csv(dir_prefix + '2017-07-09-09-36-19-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_17_pd = pd.read_csv(dir_prefix + '2017-07-09-09-36-38-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_18_pd = pd.read_csv(dir_prefix + '2017-07-09-09-36-58-myo_raw_emg_pub.csv')
train_set_spanner_handover_emg_19_pd = pd.read_csv(dir_prefix + '2017-07-09-09-37-16-myo_raw_emg_pub.csv')
test_set_spanner_handover_emg_pd = pd.read_csv(dir_prefix + '2017-07-09-09-37-41-myo_raw_emg_pub.csv')
# invert the object to float32 for easy computing
train_set_spanner_handover_emg_00 = np.float32(train_set_spanner_handover_emg_00_pd.values[:,5:13])
train_set_spanner_handover_emg_01 = np.float32(train_set_spanner_handover_emg_01_pd.values[:,5:13])
train_set_spanner_handover_emg_02 = np.float32(train_set_spanner_handover_emg_02_pd.values[:,5:13])
train_set_spanner_handover_emg_03 = np.float32(train_set_spanner_handover_emg_03_pd.values[:,5:13])
train_set_spanner_handover_emg_04 = np.float32(train_set_spanner_handover_emg_04_pd.values[:,5:13])
train_set_spanner_handover_emg_05 = np.float32(train_set_spanner_handover_emg_05_pd.values[:,5:13])
train_set_spanner_handover_emg_06 = np.float32(train_set_spanner_handover_emg_06_pd.values[:,5:13])
train_set_spanner_handover_emg_07 = np.float32(train_set_spanner_handover_emg_07_pd.values[:,5:13])
train_set_spanner_handover_emg_08 = np.float32(train_set_spanner_handover_emg_08_pd.values[:,5:13])
train_set_spanner_handover_emg_09 = np.float32(train_set_spanner_handover_emg_09_pd.values[:,5:13])
train_set_spanner_handover_emg_10 = np.float32(train_set_spanner_handover_emg_10_pd.values[:,5:13])
train_set_spanner_handover_emg_11 = np.float32(train_set_spanner_handover_emg_11_pd.values[:,5:13])
train_set_spanner_handover_emg_12 = np.float32(train_set_spanner_handover_emg_12_pd.values[:,5:13])
train_set_spanner_handover_emg_13 = np.float32(train_set_spanner_handover_emg_13_pd.values[:,5:13])
train_set_spanner_handover_emg_14 = np.float32(train_set_spanner_handover_emg_14_pd.values[:,5:13])
train_set_spanner_handover_emg_15 = np.float32(train_set_spanner_handover_emg_15_pd.values[:,5:13])
train_set_spanner_handover_emg_16 = np.float32(train_set_spanner_handover_emg_16_pd.values[:,5:13])
train_set_spanner_handover_emg_17 = np.float32(train_set_spanner_handover_emg_17_pd.values[:,5:13])
train_set_spanner_handover_emg_18 = np.float32(train_set_spanner_handover_emg_18_pd.values[:,5:13])
train_set_spanner_handover_emg_19 = np.float32(train_set_spanner_handover_emg_19_pd.values[:,5:13])
test_set_spanner_handover_emg = np.float32(test_set_spanner_handover_emg_pd.values[:,5:13])
#############################################################################################################
print('loading EMG data sets of tape hold task')
# read emg csv files of tape_hold
dir_prefix = '../../recorder/datasets/imu_emg_joint_3_task/tape_hold/csv/'
train_set_tape_hold_emg_00_pd = pd.read_csv(dir_prefix + '2017-07-09-10-14-01-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_01_pd = pd.read_csv(dir_prefix + '2017-07-09-10-14-22-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_02_pd = pd.read_csv(dir_prefix + '2017-07-09-10-14-43-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_03_pd = pd.read_csv(dir_prefix + '2017-07-09-10-15-47-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_04_pd = pd.read_csv(dir_prefix + '2017-07-09-10-16-04-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_05_pd = pd.read_csv(dir_prefix + '2017-07-09-10-16-22-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_06_pd = pd.read_csv(dir_prefix + '2017-07-09-10-16-40-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_07_pd = pd.read_csv(dir_prefix + '2017-07-09-10-16-56-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_08_pd = pd.read_csv(dir_prefix + '2017-07-09-10-17-13-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_09_pd = pd.read_csv(dir_prefix + '2017-07-09-10-17-48-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_10_pd = pd.read_csv(dir_prefix + '2017-07-09-10-18-04-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_11_pd = pd.read_csv(dir_prefix + '2017-07-09-10-18-33-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_12_pd = pd.read_csv(dir_prefix + '2017-07-09-10-18-49-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_13_pd = pd.read_csv(dir_prefix + '2017-07-09-10-19-05-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_14_pd = pd.read_csv(dir_prefix + '2017-07-09-10-19-22-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_15_pd = pd.read_csv(dir_prefix + '2017-07-09-10-19-51-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_16_pd = pd.read_csv(dir_prefix + '2017-07-09-10-20-08-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_17_pd = pd.read_csv(dir_prefix + '2017-07-09-10-20-26-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_18_pd = pd.read_csv(dir_prefix + '2017-07-09-10-20-44-myo_raw_emg_pub.csv')
train_set_tape_hold_emg_19_pd = pd.read_csv(dir_prefix + '2017-07-09-10-21-03-myo_raw_emg_pub.csv')
test_set_tape_hold_emg_pd = pd.read_csv(dir_prefix + '2017-07-09-10-21-22-myo_raw_emg_pub.csv')
# invert the object to float32 for easy computing
train_set_tape_hold_emg_00 = np.float32(train_set_tape_hold_emg_00_pd.values[:,5:13])
train_set_tape_hold_emg_01 = np.float32(train_set_tape_hold_emg_01_pd.values[:,5:13])
train_set_tape_hold_emg_02 = np.float32(train_set_tape_hold_emg_02_pd.values[:,5:13])
train_set_tape_hold_emg_03 = np.float32(train_set_tape_hold_emg_03_pd.values[:,5:13])
train_set_tape_hold_emg_04 = np.float32(train_set_tape_hold_emg_04_pd.values[:,5:13])
train_set_tape_hold_emg_05 = np.float32(train_set_tape_hold_emg_05_pd.values[:,5:13])
train_set_tape_hold_emg_06 = np.float32(train_set_tape_hold_emg_06_pd.values[:,5:13])
train_set_tape_hold_emg_07 = np.float32(train_set_tape_hold_emg_07_pd.values[:,5:13])
train_set_tape_hold_emg_08 = np.float32(train_set_tape_hold_emg_08_pd.values[:,5:13])
train_set_tape_hold_emg_09 = np.float32(train_set_tape_hold_emg_09_pd.values[:,5:13])
train_set_tape_hold_emg_10 = np.float32(train_set_tape_hold_emg_10_pd.values[:,5:13])
train_set_tape_hold_emg_11 = np.float32(train_set_tape_hold_emg_11_pd.values[:,5:13])
train_set_tape_hold_emg_12 = np.float32(train_set_tape_hold_emg_12_pd.values[:,5:13])
train_set_tape_hold_emg_13 = np.float32(train_set_tape_hold_emg_13_pd.values[:,5:13])
train_set_tape_hold_emg_14 = np.float32(train_set_tape_hold_emg_14_pd.values[:,5:13])
train_set_tape_hold_emg_15 = np.float32(train_set_tape_hold_emg_15_pd.values[:,5:13])
train_set_tape_hold_emg_16 = np.float32(train_set_tape_hold_emg_16_pd.values[:,5:13])
train_set_tape_hold_emg_17 = np.float32(train_set_tape_hold_emg_17_pd.values[:,5:13])
train_set_tape_hold_emg_18 = np.float32(train_set_tape_hold_emg_18_pd.values[:,5:13])
train_set_tape_hold_emg_19 = np.float32(train_set_tape_hold_emg_19_pd.values[:,5:13])
test_set_tape_hold_emg = np.float32(test_set_tape_hold_emg_pd.values[:,5:13])

##############################################################################################################
##############################################################################################################
#########################################
# load IMU date sets
#########################################
print('loading IMU data sets of aluminum hold task')
# read imu csv files of aluminum_hold
dir_prefix = '../../recorder/datasets/imu_emg_joint_3_task/aluminum_hold/csv/'
train_set_aluminum_hold_imu_00_pd = pd.read_csv(dir_prefix + '2017-07-09-09-57-38-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_01_pd = pd.read_csv(dir_prefix + '2017-07-09-09-57-55-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_02_pd = pd.read_csv(dir_prefix + '2017-07-09-09-58-24-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_03_pd = pd.read_csv(dir_prefix + '2017-07-09-09-58-51-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_04_pd = pd.read_csv(dir_prefix + '2017-07-09-09-59-13-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_05_pd = pd.read_csv(dir_prefix + '2017-07-09-10-00-01-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_06_pd = pd.read_csv(dir_prefix + '2017-07-09-10-01-08-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_07_pd = pd.read_csv(dir_prefix + '2017-07-09-10-01-38-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_08_pd = pd.read_csv(dir_prefix + '2017-07-09-10-02-08-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_09_pd = pd.read_csv(dir_prefix + '2017-07-09-10-02-29-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_10_pd = pd.read_csv(dir_prefix + '2017-07-09-10-02-52-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_11_pd = pd.read_csv(dir_prefix + '2017-07-09-10-03-26-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_12_pd = pd.read_csv(dir_prefix + '2017-07-09-10-03-43-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_13_pd = pd.read_csv(dir_prefix + '2017-07-09-10-04-17-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_14_pd = pd.read_csv(dir_prefix + '2017-07-09-10-04-36-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_15_pd = pd.read_csv(dir_prefix + '2017-07-09-10-04-57-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_16_pd = pd.read_csv(dir_prefix + '2017-07-09-10-05-20-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_17_pd = pd.read_csv(dir_prefix + '2017-07-09-10-05-46-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_18_pd = pd.read_csv(dir_prefix + '2017-07-09-10-06-07-myo_raw_imu_pub (copy).csv')
train_set_aluminum_hold_imu_19_pd = pd.read_csv(dir_prefix + '2017-07-09-10-06-36-myo_raw_imu_pub (copy).csv')
test_set_aluminum_hold_imu_pd = pd.read_csv(dir_prefix + '2017-07-09-10-07-04-myo_raw_imu_pub (copy).csv')
# invert the object to float32 for easy computing
train_set_aluminum_hold_imu_00 = np.float32(train_set_aluminum_hold_imu_00_pd.values[:,:])
train_set_aluminum_hold_imu_01 = np.float32(train_set_aluminum_hold_imu_01_pd.values[:,:])
train_set_aluminum_hold_imu_02 = np.float32(train_set_aluminum_hold_imu_02_pd.values[:,:])
train_set_aluminum_hold_imu_03 = np.float32(train_set_aluminum_hold_imu_03_pd.values[:,:])
train_set_aluminum_hold_imu_04 = np.float32(train_set_aluminum_hold_imu_04_pd.values[:,:])
train_set_aluminum_hold_imu_05 = np.float32(train_set_aluminum_hold_imu_05_pd.values[:,:])
train_set_aluminum_hold_imu_06 = np.float32(train_set_aluminum_hold_imu_06_pd.values[:,:])
train_set_aluminum_hold_imu_07 = np.float32(train_set_aluminum_hold_imu_07_pd.values[:,:])
train_set_aluminum_hold_imu_08 = np.float32(train_set_aluminum_hold_imu_08_pd.values[:,:])
train_set_aluminum_hold_imu_09 = np.float32(train_set_aluminum_hold_imu_09_pd.values[:,:])
train_set_aluminum_hold_imu_10 = np.float32(train_set_aluminum_hold_imu_10_pd.values[:,:])
train_set_aluminum_hold_imu_11 = np.float32(train_set_aluminum_hold_imu_11_pd.values[:,:])
train_set_aluminum_hold_imu_12 = np.float32(train_set_aluminum_hold_imu_12_pd.values[:,:])
train_set_aluminum_hold_imu_13 = np.float32(train_set_aluminum_hold_imu_13_pd.values[:,:])
train_set_aluminum_hold_imu_14 = np.float32(train_set_aluminum_hold_imu_14_pd.values[:,:])
train_set_aluminum_hold_imu_15 = np.float32(train_set_aluminum_hold_imu_15_pd.values[:,:])
train_set_aluminum_hold_imu_16 = np.float32(train_set_aluminum_hold_imu_16_pd.values[:,:])
train_set_aluminum_hold_imu_17 = np.float32(train_set_aluminum_hold_imu_17_pd.values[:,:])
train_set_aluminum_hold_imu_18 = np.float32(train_set_aluminum_hold_imu_18_pd.values[:,:])
train_set_aluminum_hold_imu_19 = np.float32(train_set_aluminum_hold_imu_19_pd.values[:,:])
test_set_aluminum_hold_imu = np.float32(test_set_aluminum_hold_imu_pd.values[:,:])
#########################################################################################################
print('loading IMU data sets of spanner handover task')
# read imu csv files of spanner_handover
dir_prefix = '../../recorder/datasets/imu_emg_joint_3_task/spanner_handover/csv/'
train_set_spanner_handover_imu_00_pd = pd.read_csv(dir_prefix + '2017-07-09-09-29-42-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_01_pd = pd.read_csv(dir_prefix + '2017-07-09-09-30-17-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_02_pd = pd.read_csv(dir_prefix + '2017-07-09-09-30-41-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_03_pd = pd.read_csv(dir_prefix + '2017-07-09-09-31-03-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_04_pd = pd.read_csv(dir_prefix + '2017-07-09-09-31-23-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_05_pd = pd.read_csv(dir_prefix + '2017-07-09-09-31-40-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_06_pd = pd.read_csv(dir_prefix + '2017-07-09-09-32-24-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_07_pd = pd.read_csv(dir_prefix + '2017-07-09-09-32-43-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_08_pd = pd.read_csv(dir_prefix + '2017-07-09-09-33-04-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_09_pd = pd.read_csv(dir_prefix + '2017-07-09-09-33-23-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_10_pd = pd.read_csv(dir_prefix + '2017-07-09-09-33-40-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_11_pd = pd.read_csv(dir_prefix + '2017-07-09-09-34-00-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_12_pd = pd.read_csv(dir_prefix + '2017-07-09-09-34-32-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_13_pd = pd.read_csv(dir_prefix + '2017-07-09-09-34-49-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_14_pd = pd.read_csv(dir_prefix + '2017-07-09-09-35-11-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_15_pd = pd.read_csv(dir_prefix + '2017-07-09-09-35-49-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_16_pd = pd.read_csv(dir_prefix + '2017-07-09-09-36-19-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_17_pd = pd.read_csv(dir_prefix + '2017-07-09-09-36-38-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_18_pd = pd.read_csv(dir_prefix + '2017-07-09-09-36-58-myo_raw_imu_pub (copy).csv')
train_set_spanner_handover_imu_19_pd = pd.read_csv(dir_prefix + '2017-07-09-09-37-16-myo_raw_imu_pub (copy).csv')
test_set_spanner_handover_imu_pd = pd.read_csv(dir_prefix + '2017-07-09-09-37-41-myo_raw_imu_pub (copy).csv')
# invert the object to float32 for easy computing
train_set_spanner_handover_imu_00 = np.float32(train_set_spanner_handover_imu_00_pd.values[:,:])
train_set_spanner_handover_imu_01 = np.float32(train_set_spanner_handover_imu_01_pd.values[:,:])
train_set_spanner_handover_imu_02 = np.float32(train_set_spanner_handover_imu_02_pd.values[:,:])
train_set_spanner_handover_imu_03 = np.float32(train_set_spanner_handover_imu_03_pd.values[:,:])
train_set_spanner_handover_imu_04 = np.float32(train_set_spanner_handover_imu_04_pd.values[:,:])
train_set_spanner_handover_imu_05 = np.float32(train_set_spanner_handover_imu_05_pd.values[:,:])
train_set_spanner_handover_imu_06 = np.float32(train_set_spanner_handover_imu_06_pd.values[:,:])
train_set_spanner_handover_imu_07 = np.float32(train_set_spanner_handover_imu_07_pd.values[:,:])
train_set_spanner_handover_imu_08 = np.float32(train_set_spanner_handover_imu_08_pd.values[:,:])
train_set_spanner_handover_imu_09 = np.float32(train_set_spanner_handover_imu_09_pd.values[:,:])
train_set_spanner_handover_imu_10 = np.float32(train_set_spanner_handover_imu_10_pd.values[:,:])
train_set_spanner_handover_imu_11 = np.float32(train_set_spanner_handover_imu_11_pd.values[:,:])
train_set_spanner_handover_imu_12 = np.float32(train_set_spanner_handover_imu_12_pd.values[:,:])
train_set_spanner_handover_imu_13 = np.float32(train_set_spanner_handover_imu_13_pd.values[:,:])
train_set_spanner_handover_imu_14 = np.float32(train_set_spanner_handover_imu_14_pd.values[:,:])
train_set_spanner_handover_imu_15 = np.float32(train_set_spanner_handover_imu_15_pd.values[:,:])
train_set_spanner_handover_imu_16 = np.float32(train_set_spanner_handover_imu_16_pd.values[:,:])
train_set_spanner_handover_imu_17 = np.float32(train_set_spanner_handover_imu_17_pd.values[:,:])
train_set_spanner_handover_imu_18 = np.float32(train_set_spanner_handover_imu_18_pd.values[:,:])
train_set_spanner_handover_imu_19 = np.float32(train_set_spanner_handover_imu_19_pd.values[:,:])
test_set_spanner_handover_imu = np.float32(test_set_spanner_handover_imu_pd.values[:,:])
#############################################################################################################
print('loading IMU data sets of tape hold task')
# read imu csv files of tape_hold
dir_prefix = '../../recorder/datasets/imu_emg_joint_3_task/tape_hold/csv/'
train_set_tape_hold_imu_00_pd = pd.read_csv(dir_prefix + '2017-07-09-10-14-01-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_01_pd = pd.read_csv(dir_prefix + '2017-07-09-10-14-22-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_02_pd = pd.read_csv(dir_prefix + '2017-07-09-10-14-43-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_03_pd = pd.read_csv(dir_prefix + '2017-07-09-10-15-47-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_04_pd = pd.read_csv(dir_prefix + '2017-07-09-10-16-04-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_05_pd = pd.read_csv(dir_prefix + '2017-07-09-10-16-22-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_06_pd = pd.read_csv(dir_prefix + '2017-07-09-10-16-40-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_07_pd = pd.read_csv(dir_prefix + '2017-07-09-10-16-56-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_08_pd = pd.read_csv(dir_prefix + '2017-07-09-10-17-13-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_09_pd = pd.read_csv(dir_prefix + '2017-07-09-10-17-48-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_10_pd = pd.read_csv(dir_prefix + '2017-07-09-10-18-04-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_11_pd = pd.read_csv(dir_prefix + '2017-07-09-10-18-33-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_12_pd = pd.read_csv(dir_prefix + '2017-07-09-10-18-49-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_13_pd = pd.read_csv(dir_prefix + '2017-07-09-10-19-05-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_14_pd = pd.read_csv(dir_prefix + '2017-07-09-10-19-22-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_15_pd = pd.read_csv(dir_prefix + '2017-07-09-10-19-51-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_16_pd = pd.read_csv(dir_prefix + '2017-07-09-10-20-08-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_17_pd = pd.read_csv(dir_prefix + '2017-07-09-10-20-26-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_18_pd = pd.read_csv(dir_prefix + '2017-07-09-10-20-44-myo_raw_imu_pub (copy).csv')
train_set_tape_hold_imu_19_pd = pd.read_csv(dir_prefix + '2017-07-09-10-21-03-myo_raw_imu_pub (copy).csv')
test_set_tape_hold_imu_pd = pd.read_csv(dir_prefix + '2017-07-09-10-21-22-myo_raw_imu_pub (copy).csv')
# invert the object to float32 for easy computing
train_set_tape_hold_imu_00 = np.float32(train_set_tape_hold_imu_00_pd.values[:,:])
train_set_tape_hold_imu_01 = np.float32(train_set_tape_hold_imu_01_pd.values[:,:])
train_set_tape_hold_imu_02 = np.float32(train_set_tape_hold_imu_02_pd.values[:,:])
train_set_tape_hold_imu_03 = np.float32(train_set_tape_hold_imu_03_pd.values[:,:])
train_set_tape_hold_imu_04 = np.float32(train_set_tape_hold_imu_04_pd.values[:,:])
train_set_tape_hold_imu_05 = np.float32(train_set_tape_hold_imu_05_pd.values[:,:])
train_set_tape_hold_imu_06 = np.float32(train_set_tape_hold_imu_06_pd.values[:,:])
train_set_tape_hold_imu_07 = np.float32(train_set_tape_hold_imu_07_pd.values[:,:])
train_set_tape_hold_imu_08 = np.float32(train_set_tape_hold_imu_08_pd.values[:,:])
train_set_tape_hold_imu_09 = np.float32(train_set_tape_hold_imu_09_pd.values[:,:])
train_set_tape_hold_imu_10 = np.float32(train_set_tape_hold_imu_10_pd.values[:,:])
train_set_tape_hold_imu_11 = np.float32(train_set_tape_hold_imu_11_pd.values[:,:])
train_set_tape_hold_imu_12 = np.float32(train_set_tape_hold_imu_12_pd.values[:,:])
train_set_tape_hold_imu_13 = np.float32(train_set_tape_hold_imu_13_pd.values[:,:])
train_set_tape_hold_imu_14 = np.float32(train_set_tape_hold_imu_14_pd.values[:,:])
train_set_tape_hold_imu_15 = np.float32(train_set_tape_hold_imu_15_pd.values[:,:])
train_set_tape_hold_imu_16 = np.float32(train_set_tape_hold_imu_16_pd.values[:,:])
train_set_tape_hold_imu_17 = np.float32(train_set_tape_hold_imu_17_pd.values[:,:])
train_set_tape_hold_imu_18 = np.float32(train_set_tape_hold_imu_18_pd.values[:,:])
train_set_tape_hold_imu_19 = np.float32(train_set_tape_hold_imu_19_pd.values[:,:])
test_set_tape_hold_imu = np.float32(test_set_tape_hold_imu_pd.values[:,:])
##############################################################################################################
##############################################################################################################
#########################################
# load Pose date sets
#########################################
print('loading pose data sets of aluminum hold task')
# read pose csv files of aluminum_hold
dir_prefix = '../../recorder/datasets/imu_emg_joint_3_task/aluminum_hold/csv/'
train_set_aluminum_hold_pose_00_pd = pd.read_csv(dir_prefix + '2017-07-09-09-57-38-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_01_pd = pd.read_csv(dir_prefix + '2017-07-09-09-57-55-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_02_pd = pd.read_csv(dir_prefix + '2017-07-09-09-58-24-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_03_pd = pd.read_csv(dir_prefix + '2017-07-09-09-58-51-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_04_pd = pd.read_csv(dir_prefix + '2017-07-09-09-59-13-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_05_pd = pd.read_csv(dir_prefix + '2017-07-09-10-00-01-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_06_pd = pd.read_csv(dir_prefix + '2017-07-09-10-01-08-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_07_pd = pd.read_csv(dir_prefix + '2017-07-09-10-01-38-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_08_pd = pd.read_csv(dir_prefix + '2017-07-09-10-02-08-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_09_pd = pd.read_csv(dir_prefix + '2017-07-09-10-02-29-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_10_pd = pd.read_csv(dir_prefix + '2017-07-09-10-02-52-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_11_pd = pd.read_csv(dir_prefix + '2017-07-09-10-03-26-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_12_pd = pd.read_csv(dir_prefix + '2017-07-09-10-03-43-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_13_pd = pd.read_csv(dir_prefix + '2017-07-09-10-04-17-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_14_pd = pd.read_csv(dir_prefix + '2017-07-09-10-04-36-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_15_pd = pd.read_csv(dir_prefix + '2017-07-09-10-04-57-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_16_pd = pd.read_csv(dir_prefix + '2017-07-09-10-05-20-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_17_pd = pd.read_csv(dir_prefix + '2017-07-09-10-05-46-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_18_pd = pd.read_csv(dir_prefix + '2017-07-09-10-06-07-robot-limb-left-endpoint_state.csv')
train_set_aluminum_hold_pose_19_pd = pd.read_csv(dir_prefix + '2017-07-09-10-06-36-robot-limb-left-endpoint_state.csv')
test_set_aluminum_hold_pose_pd = pd.read_csv(dir_prefix + '2017-07-09-10-07-04-robot-limb-left-endpoint_state.csv')
# invert the object to float32 for easy computing
train_set_aluminum_hold_pose_00 = np.float32(train_set_aluminum_hold_pose_00_pd.values[:,5:12])
train_set_aluminum_hold_pose_01 = np.float32(train_set_aluminum_hold_pose_01_pd.values[:,5:12])
train_set_aluminum_hold_pose_02 = np.float32(train_set_aluminum_hold_pose_02_pd.values[:,5:12])
train_set_aluminum_hold_pose_03 = np.float32(train_set_aluminum_hold_pose_03_pd.values[:,5:12])
train_set_aluminum_hold_pose_04 = np.float32(train_set_aluminum_hold_pose_04_pd.values[:,5:12])
train_set_aluminum_hold_pose_05 = np.float32(train_set_aluminum_hold_pose_05_pd.values[:,5:12])
train_set_aluminum_hold_pose_06 = np.float32(train_set_aluminum_hold_pose_06_pd.values[:,5:12])
train_set_aluminum_hold_pose_07 = np.float32(train_set_aluminum_hold_pose_07_pd.values[:,5:12])
train_set_aluminum_hold_pose_08 = np.float32(train_set_aluminum_hold_pose_08_pd.values[:,5:12])
train_set_aluminum_hold_pose_09 = np.float32(train_set_aluminum_hold_pose_09_pd.values[:,5:12])
train_set_aluminum_hold_pose_10 = np.float32(train_set_aluminum_hold_pose_10_pd.values[:,5:12])
train_set_aluminum_hold_pose_11 = np.float32(train_set_aluminum_hold_pose_11_pd.values[:,5:12])
train_set_aluminum_hold_pose_12 = np.float32(train_set_aluminum_hold_pose_12_pd.values[:,5:12])
train_set_aluminum_hold_pose_13 = np.float32(train_set_aluminum_hold_pose_13_pd.values[:,5:12])
train_set_aluminum_hold_pose_14 = np.float32(train_set_aluminum_hold_pose_14_pd.values[:,5:12])
train_set_aluminum_hold_pose_15 = np.float32(train_set_aluminum_hold_pose_15_pd.values[:,5:12])
train_set_aluminum_hold_pose_16 = np.float32(train_set_aluminum_hold_pose_16_pd.values[:,5:12])
train_set_aluminum_hold_pose_17 = np.float32(train_set_aluminum_hold_pose_17_pd.values[:,5:12])
train_set_aluminum_hold_pose_18 = np.float32(train_set_aluminum_hold_pose_18_pd.values[:,5:12])
train_set_aluminum_hold_pose_19 = np.float32(train_set_aluminum_hold_pose_19_pd.values[:,5:12])
test_set_aluminum_hold_pose = np.float32(test_set_aluminum_hold_pose_pd.values[:,5:12])
#########################################################################################################
print('loading Pose data sets of spanner handover task')
# read pose csv files of spanner_handover
dir_prefix = '../../recorder/datasets/imu_emg_joint_3_task/spanner_handover/csv/'
train_set_spanner_handover_pose_00_pd = pd.read_csv(dir_prefix + '2017-07-09-09-29-42-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_01_pd = pd.read_csv(dir_prefix + '2017-07-09-09-30-17-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_02_pd = pd.read_csv(dir_prefix + '2017-07-09-09-30-41-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_03_pd = pd.read_csv(dir_prefix + '2017-07-09-09-31-03-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_04_pd = pd.read_csv(dir_prefix + '2017-07-09-09-31-23-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_05_pd = pd.read_csv(dir_prefix + '2017-07-09-09-31-40-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_06_pd = pd.read_csv(dir_prefix + '2017-07-09-09-32-24-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_07_pd = pd.read_csv(dir_prefix + '2017-07-09-09-32-43-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_08_pd = pd.read_csv(dir_prefix + '2017-07-09-09-33-04-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_09_pd = pd.read_csv(dir_prefix + '2017-07-09-09-33-23-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_10_pd = pd.read_csv(dir_prefix + '2017-07-09-09-33-40-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_11_pd = pd.read_csv(dir_prefix + '2017-07-09-09-34-00-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_12_pd = pd.read_csv(dir_prefix + '2017-07-09-09-34-32-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_13_pd = pd.read_csv(dir_prefix + '2017-07-09-09-34-49-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_14_pd = pd.read_csv(dir_prefix + '2017-07-09-09-35-11-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_15_pd = pd.read_csv(dir_prefix + '2017-07-09-09-35-49-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_16_pd = pd.read_csv(dir_prefix + '2017-07-09-09-36-19-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_17_pd = pd.read_csv(dir_prefix + '2017-07-09-09-36-38-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_18_pd = pd.read_csv(dir_prefix + '2017-07-09-09-36-58-robot-limb-left-endpoint_state.csv')
train_set_spanner_handover_pose_19_pd = pd.read_csv(dir_prefix + '2017-07-09-09-37-16-robot-limb-left-endpoint_state.csv')
test_set_spanner_handover_pose_pd = pd.read_csv(dir_prefix + '2017-07-09-09-37-41-robot-limb-left-endpoint_state.csv')
# invert the object to float32 for easy computing
train_set_spanner_handover_pose_00 = np.float32(train_set_spanner_handover_pose_00_pd.values[:,5:12])
train_set_spanner_handover_pose_01 = np.float32(train_set_spanner_handover_pose_01_pd.values[:,5:12])
train_set_spanner_handover_pose_02 = np.float32(train_set_spanner_handover_pose_02_pd.values[:,5:12])
train_set_spanner_handover_pose_03 = np.float32(train_set_spanner_handover_pose_03_pd.values[:,5:12])
train_set_spanner_handover_pose_04 = np.float32(train_set_spanner_handover_pose_04_pd.values[:,5:12])
train_set_spanner_handover_pose_05 = np.float32(train_set_spanner_handover_pose_05_pd.values[:,5:12])
train_set_spanner_handover_pose_06 = np.float32(train_set_spanner_handover_pose_06_pd.values[:,5:12])
train_set_spanner_handover_pose_07 = np.float32(train_set_spanner_handover_pose_07_pd.values[:,5:12])
train_set_spanner_handover_pose_08 = np.float32(train_set_spanner_handover_pose_08_pd.values[:,5:12])
train_set_spanner_handover_pose_09 = np.float32(train_set_spanner_handover_pose_09_pd.values[:,5:12])
train_set_spanner_handover_pose_10 = np.float32(train_set_spanner_handover_pose_10_pd.values[:,5:12])
train_set_spanner_handover_pose_11 = np.float32(train_set_spanner_handover_pose_11_pd.values[:,5:12])
train_set_spanner_handover_pose_12 = np.float32(train_set_spanner_handover_pose_12_pd.values[:,5:12])
train_set_spanner_handover_pose_13 = np.float32(train_set_spanner_handover_pose_13_pd.values[:,5:12])
train_set_spanner_handover_pose_14 = np.float32(train_set_spanner_handover_pose_14_pd.values[:,5:12])
train_set_spanner_handover_pose_15 = np.float32(train_set_spanner_handover_pose_15_pd.values[:,5:12])
train_set_spanner_handover_pose_16 = np.float32(train_set_spanner_handover_pose_16_pd.values[:,5:12])
train_set_spanner_handover_pose_17 = np.float32(train_set_spanner_handover_pose_17_pd.values[:,5:12])
train_set_spanner_handover_pose_18 = np.float32(train_set_spanner_handover_pose_18_pd.values[:,5:12])
train_set_spanner_handover_pose_19 = np.float32(train_set_spanner_handover_pose_19_pd.values[:,5:12])
test_set_spanner_handover_pose = np.float32(test_set_spanner_handover_pose_pd.values[:,5:12])
#############################################################################################################
print('loading Pose data sets of tape hold task')
# read pose csv files of tape_hold
dir_prefix = '../../recorder/datasets/imu_emg_joint_3_task/tape_hold/csv/'
train_set_tape_hold_pose_00_pd = pd.read_csv(dir_prefix + '2017-07-09-10-14-01-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_01_pd = pd.read_csv(dir_prefix + '2017-07-09-10-14-22-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_02_pd = pd.read_csv(dir_prefix + '2017-07-09-10-14-43-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_03_pd = pd.read_csv(dir_prefix + '2017-07-09-10-15-47-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_04_pd = pd.read_csv(dir_prefix + '2017-07-09-10-16-04-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_05_pd = pd.read_csv(dir_prefix + '2017-07-09-10-16-22-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_06_pd = pd.read_csv(dir_prefix + '2017-07-09-10-16-40-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_07_pd = pd.read_csv(dir_prefix + '2017-07-09-10-16-56-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_08_pd = pd.read_csv(dir_prefix + '2017-07-09-10-17-13-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_09_pd = pd.read_csv(dir_prefix + '2017-07-09-10-17-48-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_10_pd = pd.read_csv(dir_prefix + '2017-07-09-10-18-04-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_11_pd = pd.read_csv(dir_prefix + '2017-07-09-10-18-33-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_12_pd = pd.read_csv(dir_prefix + '2017-07-09-10-18-49-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_13_pd = pd.read_csv(dir_prefix + '2017-07-09-10-19-05-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_14_pd = pd.read_csv(dir_prefix + '2017-07-09-10-19-22-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_15_pd = pd.read_csv(dir_prefix + '2017-07-09-10-19-51-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_16_pd = pd.read_csv(dir_prefix + '2017-07-09-10-20-08-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_17_pd = pd.read_csv(dir_prefix + '2017-07-09-10-20-26-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_18_pd = pd.read_csv(dir_prefix + '2017-07-09-10-20-44-robot-limb-left-endpoint_state.csv')
train_set_tape_hold_pose_19_pd = pd.read_csv(dir_prefix + '2017-07-09-10-21-03-robot-limb-left-endpoint_state.csv')
test_set_tape_hold_pose_pd = pd.read_csv(dir_prefix + '2017-07-09-10-21-22-robot-limb-left-endpoint_state.csv')
# invert the object to float32 for easy computing
train_set_tape_hold_pose_00 = np.float32(train_set_tape_hold_pose_00_pd.values[:,5:12])
train_set_tape_hold_pose_01 = np.float32(train_set_tape_hold_pose_01_pd.values[:,5:12])
train_set_tape_hold_pose_02 = np.float32(train_set_tape_hold_pose_02_pd.values[:,5:12])
train_set_tape_hold_pose_03 = np.float32(train_set_tape_hold_pose_03_pd.values[:,5:12])
train_set_tape_hold_pose_04 = np.float32(train_set_tape_hold_pose_04_pd.values[:,5:12])
train_set_tape_hold_pose_05 = np.float32(train_set_tape_hold_pose_05_pd.values[:,5:12])
train_set_tape_hold_pose_06 = np.float32(train_set_tape_hold_pose_06_pd.values[:,5:12])
train_set_tape_hold_pose_07 = np.float32(train_set_tape_hold_pose_07_pd.values[:,5:12])
train_set_tape_hold_pose_08 = np.float32(train_set_tape_hold_pose_08_pd.values[:,5:12])
train_set_tape_hold_pose_09 = np.float32(train_set_tape_hold_pose_09_pd.values[:,5:12])
train_set_tape_hold_pose_10 = np.float32(train_set_tape_hold_pose_10_pd.values[:,5:12])
train_set_tape_hold_pose_11 = np.float32(train_set_tape_hold_pose_11_pd.values[:,5:12])
train_set_tape_hold_pose_12 = np.float32(train_set_tape_hold_pose_12_pd.values[:,5:12])
train_set_tape_hold_pose_13 = np.float32(train_set_tape_hold_pose_13_pd.values[:,5:12])
train_set_tape_hold_pose_14 = np.float32(train_set_tape_hold_pose_14_pd.values[:,5:12])
train_set_tape_hold_pose_15 = np.float32(train_set_tape_hold_pose_15_pd.values[:,5:12])
train_set_tape_hold_pose_16 = np.float32(train_set_tape_hold_pose_16_pd.values[:,5:12])
train_set_tape_hold_pose_17 = np.float32(train_set_tape_hold_pose_17_pd.values[:,5:12])
train_set_tape_hold_pose_18 = np.float32(train_set_tape_hold_pose_18_pd.values[:,5:12])
train_set_tape_hold_pose_19 = np.float32(train_set_tape_hold_pose_19_pd.values[:,5:12])
test_set_tape_hold_pose = np.float32(test_set_tape_hold_pose_pd.values[:,5:12])
##############################################################################################################
##############################################################################################################


# #########################################
# # plot raw data
# #########################################
# plt.figure(0)
# for ch_ex in range(8):
#    plt.subplot(421+ch_ex)
#    plt.plot(range(len(train_set_aluminum_hold_emg_00)), train_set_aluminum_hold_emg_00[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_01)), train_set_aluminum_hold_emg_01[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_02)), train_set_aluminum_hold_emg_02[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_03)), train_set_aluminum_hold_emg_03[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_04)), train_set_aluminum_hold_emg_04[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_05)), train_set_aluminum_hold_emg_05[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_06)), train_set_aluminum_hold_emg_06[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_07)), train_set_aluminum_hold_emg_07[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_08)), train_set_aluminum_hold_emg_08[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_09)), train_set_aluminum_hold_emg_09[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_10)), train_set_aluminum_hold_emg_10[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_11)), train_set_aluminum_hold_emg_11[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_12)), train_set_aluminum_hold_emg_12[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_13)), train_set_aluminum_hold_emg_13[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_14)), train_set_aluminum_hold_emg_14[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_15)), train_set_aluminum_hold_emg_15[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_16)), train_set_aluminum_hold_emg_16[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_17)), train_set_aluminum_hold_emg_17[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_18)), train_set_aluminum_hold_emg_18[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_emg_19)), train_set_aluminum_hold_emg_19[:,ch_ex])
# plt.figure(1)
# for ch_ex in range(8):
#    plt.subplot(421+ch_ex)
#    plt.plot(range(len(train_set_spanner_handover_emg_00)), train_set_spanner_handover_emg_00[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_01)), train_set_spanner_handover_emg_01[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_02)), train_set_spanner_handover_emg_02[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_03)), train_set_spanner_handover_emg_03[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_04)), train_set_spanner_handover_emg_04[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_05)), train_set_spanner_handover_emg_05[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_06)), train_set_spanner_handover_emg_06[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_07)), train_set_spanner_handover_emg_07[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_08)), train_set_spanner_handover_emg_08[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_09)), train_set_spanner_handover_emg_09[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_10)), train_set_spanner_handover_emg_10[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_11)), train_set_spanner_handover_emg_11[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_12)), train_set_spanner_handover_emg_12[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_13)), train_set_spanner_handover_emg_13[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_14)), train_set_spanner_handover_emg_14[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_15)), train_set_spanner_handover_emg_15[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_16)), train_set_spanner_handover_emg_16[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_17)), train_set_spanner_handover_emg_17[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_18)), train_set_spanner_handover_emg_18[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_emg_19)), train_set_spanner_handover_emg_19[:,ch_ex])
# plt.figure(2)
# for ch_ex in range(8):
#    plt.subplot(421+ch_ex)
#    plt.plot(range(len(train_set_tape_hold_emg_00)), train_set_tape_hold_emg_00[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_01)), train_set_tape_hold_emg_01[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_02)), train_set_tape_hold_emg_02[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_03)), train_set_tape_hold_emg_03[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_04)), train_set_tape_hold_emg_04[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_05)), train_set_tape_hold_emg_05[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_06)), train_set_tape_hold_emg_06[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_07)), train_set_tape_hold_emg_07[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_08)), train_set_tape_hold_emg_08[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_09)), train_set_tape_hold_emg_09[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_10)), train_set_tape_hold_emg_10[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_11)), train_set_tape_hold_emg_11[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_12)), train_set_tape_hold_emg_12[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_13)), train_set_tape_hold_emg_13[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_14)), train_set_tape_hold_emg_14[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_15)), train_set_tape_hold_emg_15[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_16)), train_set_tape_hold_emg_16[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_17)), train_set_tape_hold_emg_17[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_18)), train_set_tape_hold_emg_18[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_emg_19)), train_set_tape_hold_emg_19[:,ch_ex])
# ###########################################################################################
# plt.figure(3)
# for ch_ex in range(4):
#    plt.subplot(411+ch_ex)
#    plt.plot(range(len(train_set_aluminum_hold_imu_00)), train_set_aluminum_hold_imu_00[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_01)), train_set_aluminum_hold_imu_01[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_02)), train_set_aluminum_hold_imu_02[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_03)), train_set_aluminum_hold_imu_03[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_04)), train_set_aluminum_hold_imu_04[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_05)), train_set_aluminum_hold_imu_05[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_06)), train_set_aluminum_hold_imu_06[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_07)), train_set_aluminum_hold_imu_07[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_08)), train_set_aluminum_hold_imu_08[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_09)), train_set_aluminum_hold_imu_09[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_10)), train_set_aluminum_hold_imu_10[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_11)), train_set_aluminum_hold_imu_11[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_12)), train_set_aluminum_hold_imu_12[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_13)), train_set_aluminum_hold_imu_13[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_14)), train_set_aluminum_hold_imu_14[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_15)), train_set_aluminum_hold_imu_15[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_16)), train_set_aluminum_hold_imu_16[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_17)), train_set_aluminum_hold_imu_17[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_18)), train_set_aluminum_hold_imu_18[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_imu_19)), train_set_aluminum_hold_imu_19[:,ch_ex])
# plt.figure(4)
# for ch_ex in range(4):
#    plt.subplot(411+ch_ex)
#    plt.plot(range(len(train_set_spanner_handover_imu_00)), train_set_spanner_handover_imu_00[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_01)), train_set_spanner_handover_imu_01[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_02)), train_set_spanner_handover_imu_02[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_03)), train_set_spanner_handover_imu_03[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_04)), train_set_spanner_handover_imu_04[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_05)), train_set_spanner_handover_imu_05[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_06)), train_set_spanner_handover_imu_06[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_07)), train_set_spanner_handover_imu_07[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_08)), train_set_spanner_handover_imu_08[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_09)), train_set_spanner_handover_imu_09[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_10)), train_set_spanner_handover_imu_10[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_11)), train_set_spanner_handover_imu_11[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_12)), train_set_spanner_handover_imu_12[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_13)), train_set_spanner_handover_imu_13[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_14)), train_set_spanner_handover_imu_14[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_15)), train_set_spanner_handover_imu_15[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_16)), train_set_spanner_handover_imu_16[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_17)), train_set_spanner_handover_imu_17[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_18)), train_set_spanner_handover_imu_18[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_imu_19)), train_set_spanner_handover_imu_19[:,ch_ex])
# plt.figure(5)
# for ch_ex in range(4):
#    plt.subplot(411+ch_ex)
#    plt.plot(range(len(train_set_tape_hold_imu_00)), train_set_tape_hold_imu_00[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_01)), train_set_tape_hold_imu_01[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_02)), train_set_tape_hold_imu_02[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_03)), train_set_tape_hold_imu_03[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_04)), train_set_tape_hold_imu_04[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_05)), train_set_tape_hold_imu_05[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_06)), train_set_tape_hold_imu_06[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_07)), train_set_tape_hold_imu_07[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_08)), train_set_tape_hold_imu_08[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_09)), train_set_tape_hold_imu_09[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_10)), train_set_tape_hold_imu_10[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_11)), train_set_tape_hold_imu_11[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_12)), train_set_tape_hold_imu_12[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_13)), train_set_tape_hold_imu_13[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_14)), train_set_tape_hold_imu_14[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_15)), train_set_tape_hold_imu_15[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_16)), train_set_tape_hold_imu_16[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_17)), train_set_tape_hold_imu_17[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_18)), train_set_tape_hold_imu_18[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_imu_19)), train_set_tape_hold_imu_19[:,ch_ex])
# ###########################################################################################
# plt.figure(6)
# for ch_ex in range(7):
#    plt.subplot(711+ch_ex)
#    plt.plot(range(len(train_set_aluminum_hold_pose_00)), train_set_aluminum_hold_pose_00[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_01)), train_set_aluminum_hold_pose_01[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_02)), train_set_aluminum_hold_pose_02[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_03)), train_set_aluminum_hold_pose_03[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_04)), train_set_aluminum_hold_pose_04[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_05)), train_set_aluminum_hold_pose_05[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_06)), train_set_aluminum_hold_pose_06[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_07)), train_set_aluminum_hold_pose_07[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_08)), train_set_aluminum_hold_pose_08[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_09)), train_set_aluminum_hold_pose_09[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_10)), train_set_aluminum_hold_pose_10[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_11)), train_set_aluminum_hold_pose_11[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_12)), train_set_aluminum_hold_pose_12[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_13)), train_set_aluminum_hold_pose_13[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_14)), train_set_aluminum_hold_pose_14[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_15)), train_set_aluminum_hold_pose_15[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_16)), train_set_aluminum_hold_pose_16[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_17)), train_set_aluminum_hold_pose_17[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_18)), train_set_aluminum_hold_pose_18[:,ch_ex])
#    plt.plot(range(len(train_set_aluminum_hold_pose_19)), train_set_aluminum_hold_pose_19[:,ch_ex])
# plt.figure(7)
# for ch_ex in range(7):
#    plt.subplot(711+ch_ex)
#    plt.plot(range(len(train_set_spanner_handover_pose_00)), train_set_spanner_handover_pose_00[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_01)), train_set_spanner_handover_pose_01[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_02)), train_set_spanner_handover_pose_02[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_03)), train_set_spanner_handover_pose_03[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_04)), train_set_spanner_handover_pose_04[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_05)), train_set_spanner_handover_pose_05[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_06)), train_set_spanner_handover_pose_06[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_07)), train_set_spanner_handover_pose_07[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_08)), train_set_spanner_handover_pose_08[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_09)), train_set_spanner_handover_pose_09[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_10)), train_set_spanner_handover_pose_10[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_11)), train_set_spanner_handover_pose_11[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_12)), train_set_spanner_handover_pose_12[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_13)), train_set_spanner_handover_pose_13[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_14)), train_set_spanner_handover_pose_14[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_15)), train_set_spanner_handover_pose_15[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_16)), train_set_spanner_handover_pose_16[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_17)), train_set_spanner_handover_pose_17[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_18)), train_set_spanner_handover_pose_18[:,ch_ex])
#    plt.plot(range(len(train_set_spanner_handover_pose_19)), train_set_spanner_handover_pose_19[:,ch_ex])
# plt.figure(8)
# for ch_ex in range(7):
#    plt.subplot(711+ch_ex)
#    plt.plot(range(len(train_set_tape_hold_pose_00)), train_set_tape_hold_pose_00[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_01)), train_set_tape_hold_pose_01[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_02)), train_set_tape_hold_pose_02[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_03)), train_set_tape_hold_pose_03[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_04)), train_set_tape_hold_pose_04[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_05)), train_set_tape_hold_pose_05[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_06)), train_set_tape_hold_pose_06[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_07)), train_set_tape_hold_pose_07[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_08)), train_set_tape_hold_pose_08[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_09)), train_set_tape_hold_pose_09[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_10)), train_set_tape_hold_pose_10[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_11)), train_set_tape_hold_pose_11[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_12)), train_set_tape_hold_pose_12[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_13)), train_set_tape_hold_pose_13[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_14)), train_set_tape_hold_pose_14[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_15)), train_set_tape_hold_pose_15[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_16)), train_set_tape_hold_pose_16[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_17)), train_set_tape_hold_pose_17[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_18)), train_set_tape_hold_pose_18[:,ch_ex])
#    plt.plot(range(len(train_set_tape_hold_pose_19)), train_set_tape_hold_pose_19[:,ch_ex])



#########################################
# resampling the EMG data for experiencing the same duration
#########################################
# rospy.loginfo('normalizing data into same duration')
print('normalizing EMG data into same duration of aluminum_hold')
# resampling emg signals of aluminum_hold
train_set_aluminum_hold_emg_norm00=np.array([]);train_set_aluminum_hold_emg_norm01=np.array([]);train_set_aluminum_hold_emg_norm02=np.array([]);train_set_aluminum_hold_emg_norm03=np.array([]);train_set_aluminum_hold_emg_norm04=np.array([]);
train_set_aluminum_hold_emg_norm05=np.array([]);train_set_aluminum_hold_emg_norm06=np.array([]);train_set_aluminum_hold_emg_norm07=np.array([]);train_set_aluminum_hold_emg_norm08=np.array([]);train_set_aluminum_hold_emg_norm09=np.array([]);
train_set_aluminum_hold_emg_norm10=np.array([]);train_set_aluminum_hold_emg_norm11=np.array([]);train_set_aluminum_hold_emg_norm12=np.array([]);train_set_aluminum_hold_emg_norm13=np.array([]);train_set_aluminum_hold_emg_norm14=np.array([]);
train_set_aluminum_hold_emg_norm15=np.array([]);train_set_aluminum_hold_emg_norm16=np.array([]);train_set_aluminum_hold_emg_norm17=np.array([]);train_set_aluminum_hold_emg_norm18=np.array([]);train_set_aluminum_hold_emg_norm19=np.array([]);
test_set_aluminum_hold_emg_norm=np.array([]);
for ch_ex in range(8):
    train_set_aluminum_hold_emg_norm00 = np.hstack(( train_set_aluminum_hold_emg_norm00, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_00)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_00),1.), train_set_aluminum_hold_emg_00[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm01 = np.hstack(( train_set_aluminum_hold_emg_norm01, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_01)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_01),1.), train_set_aluminum_hold_emg_01[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm02 = np.hstack(( train_set_aluminum_hold_emg_norm02, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_02)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_02),1.), train_set_aluminum_hold_emg_02[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm03 = np.hstack(( train_set_aluminum_hold_emg_norm03, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_03)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_03),1.), train_set_aluminum_hold_emg_03[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm04 = np.hstack(( train_set_aluminum_hold_emg_norm04, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_04)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_04),1.), train_set_aluminum_hold_emg_04[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm05 = np.hstack(( train_set_aluminum_hold_emg_norm05, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_05)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_05),1.), train_set_aluminum_hold_emg_05[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm06 = np.hstack(( train_set_aluminum_hold_emg_norm06, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_06)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_06),1.), train_set_aluminum_hold_emg_06[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm07 = np.hstack(( train_set_aluminum_hold_emg_norm07, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_07)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_07),1.), train_set_aluminum_hold_emg_07[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm08 = np.hstack(( train_set_aluminum_hold_emg_norm08, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_08)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_08),1.), train_set_aluminum_hold_emg_08[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm09 = np.hstack(( train_set_aluminum_hold_emg_norm09, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_09)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_09),1.), train_set_aluminum_hold_emg_09[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm10 = np.hstack(( train_set_aluminum_hold_emg_norm10, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_10)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_10),1.), train_set_aluminum_hold_emg_10[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm11 = np.hstack(( train_set_aluminum_hold_emg_norm11, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_11)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_11),1.), train_set_aluminum_hold_emg_11[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm12 = np.hstack(( train_set_aluminum_hold_emg_norm12, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_12)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_12),1.), train_set_aluminum_hold_emg_12[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm13 = np.hstack(( train_set_aluminum_hold_emg_norm13, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_13)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_13),1.), train_set_aluminum_hold_emg_13[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm14 = np.hstack(( train_set_aluminum_hold_emg_norm14, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_14)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_14),1.), train_set_aluminum_hold_emg_14[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm15 = np.hstack(( train_set_aluminum_hold_emg_norm15, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_15)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_15),1.), train_set_aluminum_hold_emg_15[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm16 = np.hstack(( train_set_aluminum_hold_emg_norm16, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_16)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_16),1.), train_set_aluminum_hold_emg_16[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm17 = np.hstack(( train_set_aluminum_hold_emg_norm17, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_17)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_17),1.), train_set_aluminum_hold_emg_17[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm18 = np.hstack(( train_set_aluminum_hold_emg_norm18, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_18)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_18),1.), train_set_aluminum_hold_emg_18[:,ch_ex]) ))
    train_set_aluminum_hold_emg_norm19 = np.hstack(( train_set_aluminum_hold_emg_norm19, np.interp(np.linspace(0, len(train_set_aluminum_hold_emg_19)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_emg_19),1.), train_set_aluminum_hold_emg_19[:,ch_ex]) ))
    test_set_aluminum_hold_emg_norm = np.hstack(( test_set_aluminum_hold_emg_norm, np.interp(np.linspace(0, len(test_set_aluminum_hold_emg)-1, len_normal), np.arange(0,len(test_set_aluminum_hold_emg),1.), test_set_aluminum_hold_emg[:,ch_ex]) ))
train_set_aluminum_hold_emg_norm00 = train_set_aluminum_hold_emg_norm00.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm01 = train_set_aluminum_hold_emg_norm01.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm02 = train_set_aluminum_hold_emg_norm02.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm03 = train_set_aluminum_hold_emg_norm03.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm04 = train_set_aluminum_hold_emg_norm04.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm05 = train_set_aluminum_hold_emg_norm05.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm06 = train_set_aluminum_hold_emg_norm06.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm07 = train_set_aluminum_hold_emg_norm07.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm08 = train_set_aluminum_hold_emg_norm08.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm09 = train_set_aluminum_hold_emg_norm09.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm10 = train_set_aluminum_hold_emg_norm10.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm11 = train_set_aluminum_hold_emg_norm11.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm12 = train_set_aluminum_hold_emg_norm12.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm13 = train_set_aluminum_hold_emg_norm13.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm14 = train_set_aluminum_hold_emg_norm14.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm15 = train_set_aluminum_hold_emg_norm15.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm16 = train_set_aluminum_hold_emg_norm16.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm17 = train_set_aluminum_hold_emg_norm17.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm18 = train_set_aluminum_hold_emg_norm18.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm19 = train_set_aluminum_hold_emg_norm19.reshape(8,len_normal).T
test_set_aluminum_hold_emg_norm = test_set_aluminum_hold_emg_norm.reshape(8,len_normal).T
train_set_aluminum_hold_emg_norm_full = np.array([train_set_aluminum_hold_emg_norm00,train_set_aluminum_hold_emg_norm01,train_set_aluminum_hold_emg_norm02,train_set_aluminum_hold_emg_norm03,train_set_aluminum_hold_emg_norm04,
                                    train_set_aluminum_hold_emg_norm05,train_set_aluminum_hold_emg_norm06,train_set_aluminum_hold_emg_norm07,train_set_aluminum_hold_emg_norm08,train_set_aluminum_hold_emg_norm09,
                                    train_set_aluminum_hold_emg_norm10,train_set_aluminum_hold_emg_norm11,train_set_aluminum_hold_emg_norm12,train_set_aluminum_hold_emg_norm13,train_set_aluminum_hold_emg_norm14,
                                    train_set_aluminum_hold_emg_norm15,train_set_aluminum_hold_emg_norm16,train_set_aluminum_hold_emg_norm17,train_set_aluminum_hold_emg_norm18,train_set_aluminum_hold_emg_norm19])
##########################################################################################
print('normalizing EMG data into same duration of spanner_handove')
# resampling emg signals of aluminum_hold
train_set_spanner_handover_emg_norm00=np.array([]);train_set_spanner_handover_emg_norm01=np.array([]);train_set_spanner_handover_emg_norm02=np.array([]);train_set_spanner_handover_emg_norm03=np.array([]);train_set_spanner_handover_emg_norm04=np.array([]);
train_set_spanner_handover_emg_norm05=np.array([]);train_set_spanner_handover_emg_norm06=np.array([]);train_set_spanner_handover_emg_norm07=np.array([]);train_set_spanner_handover_emg_norm08=np.array([]);train_set_spanner_handover_emg_norm09=np.array([]);
train_set_spanner_handover_emg_norm10=np.array([]);train_set_spanner_handover_emg_norm11=np.array([]);train_set_spanner_handover_emg_norm12=np.array([]);train_set_spanner_handover_emg_norm13=np.array([]);train_set_spanner_handover_emg_norm14=np.array([]);
train_set_spanner_handover_emg_norm15=np.array([]);train_set_spanner_handover_emg_norm16=np.array([]);train_set_spanner_handover_emg_norm17=np.array([]);train_set_spanner_handover_emg_norm18=np.array([]);train_set_spanner_handover_emg_norm19=np.array([]);
test_set_spanner_handover_emg_norm=np.array([]);
for ch_ex in range(8):
    train_set_spanner_handover_emg_norm00 = np.hstack(( train_set_spanner_handover_emg_norm00, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_00)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_00),1.), train_set_spanner_handover_emg_00[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm01 = np.hstack(( train_set_spanner_handover_emg_norm01, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_01)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_01),1.), train_set_spanner_handover_emg_01[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm02 = np.hstack(( train_set_spanner_handover_emg_norm02, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_02)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_02),1.), train_set_spanner_handover_emg_02[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm03 = np.hstack(( train_set_spanner_handover_emg_norm03, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_03)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_03),1.), train_set_spanner_handover_emg_03[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm04 = np.hstack(( train_set_spanner_handover_emg_norm04, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_04)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_04),1.), train_set_spanner_handover_emg_04[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm05 = np.hstack(( train_set_spanner_handover_emg_norm05, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_05)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_05),1.), train_set_spanner_handover_emg_05[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm06 = np.hstack(( train_set_spanner_handover_emg_norm06, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_06)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_06),1.), train_set_spanner_handover_emg_06[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm07 = np.hstack(( train_set_spanner_handover_emg_norm07, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_07)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_07),1.), train_set_spanner_handover_emg_07[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm08 = np.hstack(( train_set_spanner_handover_emg_norm08, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_08)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_08),1.), train_set_spanner_handover_emg_08[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm09 = np.hstack(( train_set_spanner_handover_emg_norm09, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_09)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_09),1.), train_set_spanner_handover_emg_09[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm10 = np.hstack(( train_set_spanner_handover_emg_norm10, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_10)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_10),1.), train_set_spanner_handover_emg_10[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm11 = np.hstack(( train_set_spanner_handover_emg_norm11, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_11)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_11),1.), train_set_spanner_handover_emg_11[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm12 = np.hstack(( train_set_spanner_handover_emg_norm12, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_12)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_12),1.), train_set_spanner_handover_emg_12[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm13 = np.hstack(( train_set_spanner_handover_emg_norm13, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_13)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_13),1.), train_set_spanner_handover_emg_13[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm14 = np.hstack(( train_set_spanner_handover_emg_norm14, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_14)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_14),1.), train_set_spanner_handover_emg_14[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm15 = np.hstack(( train_set_spanner_handover_emg_norm15, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_15)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_15),1.), train_set_spanner_handover_emg_15[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm16 = np.hstack(( train_set_spanner_handover_emg_norm16, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_16)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_16),1.), train_set_spanner_handover_emg_16[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm17 = np.hstack(( train_set_spanner_handover_emg_norm17, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_17)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_17),1.), train_set_spanner_handover_emg_17[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm18 = np.hstack(( train_set_spanner_handover_emg_norm18, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_18)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_18),1.), train_set_spanner_handover_emg_18[:,ch_ex]) ))
    train_set_spanner_handover_emg_norm19 = np.hstack(( train_set_spanner_handover_emg_norm19, np.interp(np.linspace(0, len(train_set_spanner_handover_emg_19)-1, len_normal), np.arange(0,len(train_set_spanner_handover_emg_19),1.), train_set_spanner_handover_emg_19[:,ch_ex]) ))
    test_set_spanner_handover_emg_norm = np.hstack(( test_set_spanner_handover_emg_norm, np.interp(np.linspace(0, len(test_set_spanner_handover_emg)-1, len_normal), np.arange(0,len(test_set_spanner_handover_emg),1.), test_set_spanner_handover_emg[:,ch_ex]) ))
train_set_spanner_handover_emg_norm00 = train_set_spanner_handover_emg_norm00.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm01 = train_set_spanner_handover_emg_norm01.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm02 = train_set_spanner_handover_emg_norm02.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm03 = train_set_spanner_handover_emg_norm03.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm04 = train_set_spanner_handover_emg_norm04.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm05 = train_set_spanner_handover_emg_norm05.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm06 = train_set_spanner_handover_emg_norm06.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm07 = train_set_spanner_handover_emg_norm07.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm08 = train_set_spanner_handover_emg_norm08.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm09 = train_set_spanner_handover_emg_norm09.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm10 = train_set_spanner_handover_emg_norm10.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm11 = train_set_spanner_handover_emg_norm11.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm12 = train_set_spanner_handover_emg_norm12.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm13 = train_set_spanner_handover_emg_norm13.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm14 = train_set_spanner_handover_emg_norm14.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm15 = train_set_spanner_handover_emg_norm15.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm16 = train_set_spanner_handover_emg_norm16.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm17 = train_set_spanner_handover_emg_norm17.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm18 = train_set_spanner_handover_emg_norm18.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm19 = train_set_spanner_handover_emg_norm19.reshape(8,len_normal).T
test_set_spanner_handover_emg_norm = test_set_spanner_handover_emg_norm.reshape(8,len_normal).T
train_set_spanner_handover_emg_norm_full = np.array([train_set_spanner_handover_emg_norm00,train_set_spanner_handover_emg_norm01,train_set_spanner_handover_emg_norm02,train_set_spanner_handover_emg_norm03,train_set_spanner_handover_emg_norm04,
                                    train_set_spanner_handover_emg_norm05,train_set_spanner_handover_emg_norm06,train_set_spanner_handover_emg_norm07,train_set_spanner_handover_emg_norm08,train_set_spanner_handover_emg_norm09,
                                    train_set_spanner_handover_emg_norm10,train_set_spanner_handover_emg_norm11,train_set_spanner_handover_emg_norm12,train_set_spanner_handover_emg_norm13,train_set_spanner_handover_emg_norm14,
                                    train_set_spanner_handover_emg_norm15,train_set_spanner_handover_emg_norm16,train_set_spanner_handover_emg_norm17,train_set_spanner_handover_emg_norm18,train_set_spanner_handover_emg_norm19])
##########################################################################################
print('normalizing EMG data into same duration of tape_hold')
# resampling emg signals of aluminum_hold
train_set_tape_hold_emg_norm00=np.array([]);train_set_tape_hold_emg_norm01=np.array([]);train_set_tape_hold_emg_norm02=np.array([]);train_set_tape_hold_emg_norm03=np.array([]);train_set_tape_hold_emg_norm04=np.array([]);
train_set_tape_hold_emg_norm05=np.array([]);train_set_tape_hold_emg_norm06=np.array([]);train_set_tape_hold_emg_norm07=np.array([]);train_set_tape_hold_emg_norm08=np.array([]);train_set_tape_hold_emg_norm09=np.array([]);
train_set_tape_hold_emg_norm10=np.array([]);train_set_tape_hold_emg_norm11=np.array([]);train_set_tape_hold_emg_norm12=np.array([]);train_set_tape_hold_emg_norm13=np.array([]);train_set_tape_hold_emg_norm14=np.array([]);
train_set_tape_hold_emg_norm15=np.array([]);train_set_tape_hold_emg_norm16=np.array([]);train_set_tape_hold_emg_norm17=np.array([]);train_set_tape_hold_emg_norm18=np.array([]);train_set_tape_hold_emg_norm19=np.array([]);
test_set_tape_hold_emg_norm=np.array([]);
for ch_ex in range(8):
    train_set_tape_hold_emg_norm00 = np.hstack(( train_set_tape_hold_emg_norm00, np.interp(np.linspace(0, len(train_set_tape_hold_emg_00)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_00),1.), train_set_tape_hold_emg_00[:,ch_ex]) ))
    train_set_tape_hold_emg_norm01 = np.hstack(( train_set_tape_hold_emg_norm01, np.interp(np.linspace(0, len(train_set_tape_hold_emg_01)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_01),1.), train_set_tape_hold_emg_01[:,ch_ex]) ))
    train_set_tape_hold_emg_norm02 = np.hstack(( train_set_tape_hold_emg_norm02, np.interp(np.linspace(0, len(train_set_tape_hold_emg_02)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_02),1.), train_set_tape_hold_emg_02[:,ch_ex]) ))
    train_set_tape_hold_emg_norm03 = np.hstack(( train_set_tape_hold_emg_norm03, np.interp(np.linspace(0, len(train_set_tape_hold_emg_03)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_03),1.), train_set_tape_hold_emg_03[:,ch_ex]) ))
    train_set_tape_hold_emg_norm04 = np.hstack(( train_set_tape_hold_emg_norm04, np.interp(np.linspace(0, len(train_set_tape_hold_emg_04)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_04),1.), train_set_tape_hold_emg_04[:,ch_ex]) ))
    train_set_tape_hold_emg_norm05 = np.hstack(( train_set_tape_hold_emg_norm05, np.interp(np.linspace(0, len(train_set_tape_hold_emg_05)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_05),1.), train_set_tape_hold_emg_05[:,ch_ex]) ))
    train_set_tape_hold_emg_norm06 = np.hstack(( train_set_tape_hold_emg_norm06, np.interp(np.linspace(0, len(train_set_tape_hold_emg_06)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_06),1.), train_set_tape_hold_emg_06[:,ch_ex]) ))
    train_set_tape_hold_emg_norm07 = np.hstack(( train_set_tape_hold_emg_norm07, np.interp(np.linspace(0, len(train_set_tape_hold_emg_07)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_07),1.), train_set_tape_hold_emg_07[:,ch_ex]) ))
    train_set_tape_hold_emg_norm08 = np.hstack(( train_set_tape_hold_emg_norm08, np.interp(np.linspace(0, len(train_set_tape_hold_emg_08)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_08),1.), train_set_tape_hold_emg_08[:,ch_ex]) ))
    train_set_tape_hold_emg_norm09 = np.hstack(( train_set_tape_hold_emg_norm09, np.interp(np.linspace(0, len(train_set_tape_hold_emg_09)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_09),1.), train_set_tape_hold_emg_09[:,ch_ex]) ))
    train_set_tape_hold_emg_norm10 = np.hstack(( train_set_tape_hold_emg_norm10, np.interp(np.linspace(0, len(train_set_tape_hold_emg_10)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_10),1.), train_set_tape_hold_emg_10[:,ch_ex]) ))
    train_set_tape_hold_emg_norm11 = np.hstack(( train_set_tape_hold_emg_norm11, np.interp(np.linspace(0, len(train_set_tape_hold_emg_11)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_11),1.), train_set_tape_hold_emg_11[:,ch_ex]) ))
    train_set_tape_hold_emg_norm12 = np.hstack(( train_set_tape_hold_emg_norm12, np.interp(np.linspace(0, len(train_set_tape_hold_emg_12)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_12),1.), train_set_tape_hold_emg_12[:,ch_ex]) ))
    train_set_tape_hold_emg_norm13 = np.hstack(( train_set_tape_hold_emg_norm13, np.interp(np.linspace(0, len(train_set_tape_hold_emg_13)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_13),1.), train_set_tape_hold_emg_13[:,ch_ex]) ))
    train_set_tape_hold_emg_norm14 = np.hstack(( train_set_tape_hold_emg_norm14, np.interp(np.linspace(0, len(train_set_tape_hold_emg_14)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_14),1.), train_set_tape_hold_emg_14[:,ch_ex]) ))
    train_set_tape_hold_emg_norm15 = np.hstack(( train_set_tape_hold_emg_norm15, np.interp(np.linspace(0, len(train_set_tape_hold_emg_15)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_15),1.), train_set_tape_hold_emg_15[:,ch_ex]) ))
    train_set_tape_hold_emg_norm16 = np.hstack(( train_set_tape_hold_emg_norm16, np.interp(np.linspace(0, len(train_set_tape_hold_emg_16)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_16),1.), train_set_tape_hold_emg_16[:,ch_ex]) ))
    train_set_tape_hold_emg_norm17 = np.hstack(( train_set_tape_hold_emg_norm17, np.interp(np.linspace(0, len(train_set_tape_hold_emg_17)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_17),1.), train_set_tape_hold_emg_17[:,ch_ex]) ))
    train_set_tape_hold_emg_norm18 = np.hstack(( train_set_tape_hold_emg_norm18, np.interp(np.linspace(0, len(train_set_tape_hold_emg_18)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_18),1.), train_set_tape_hold_emg_18[:,ch_ex]) ))
    train_set_tape_hold_emg_norm19 = np.hstack(( train_set_tape_hold_emg_norm19, np.interp(np.linspace(0, len(train_set_tape_hold_emg_19)-1, len_normal), np.arange(0,len(train_set_tape_hold_emg_19),1.), train_set_tape_hold_emg_19[:,ch_ex]) ))
    test_set_tape_hold_emg_norm = np.hstack(( test_set_tape_hold_emg_norm, np.interp(np.linspace(0, len(test_set_tape_hold_emg)-1, len_normal), np.arange(0,len(test_set_tape_hold_emg),1.), test_set_tape_hold_emg[:,ch_ex]) ))
train_set_tape_hold_emg_norm00 = train_set_tape_hold_emg_norm00.reshape(8,len_normal).T
train_set_tape_hold_emg_norm01 = train_set_tape_hold_emg_norm01.reshape(8,len_normal).T
train_set_tape_hold_emg_norm02 = train_set_tape_hold_emg_norm02.reshape(8,len_normal).T
train_set_tape_hold_emg_norm03 = train_set_tape_hold_emg_norm03.reshape(8,len_normal).T
train_set_tape_hold_emg_norm04 = train_set_tape_hold_emg_norm04.reshape(8,len_normal).T
train_set_tape_hold_emg_norm05 = train_set_tape_hold_emg_norm05.reshape(8,len_normal).T
train_set_tape_hold_emg_norm06 = train_set_tape_hold_emg_norm06.reshape(8,len_normal).T
train_set_tape_hold_emg_norm07 = train_set_tape_hold_emg_norm07.reshape(8,len_normal).T
train_set_tape_hold_emg_norm08 = train_set_tape_hold_emg_norm08.reshape(8,len_normal).T
train_set_tape_hold_emg_norm09 = train_set_tape_hold_emg_norm09.reshape(8,len_normal).T
train_set_tape_hold_emg_norm10 = train_set_tape_hold_emg_norm10.reshape(8,len_normal).T
train_set_tape_hold_emg_norm11 = train_set_tape_hold_emg_norm11.reshape(8,len_normal).T
train_set_tape_hold_emg_norm12 = train_set_tape_hold_emg_norm12.reshape(8,len_normal).T
train_set_tape_hold_emg_norm13 = train_set_tape_hold_emg_norm13.reshape(8,len_normal).T
train_set_tape_hold_emg_norm14 = train_set_tape_hold_emg_norm14.reshape(8,len_normal).T
train_set_tape_hold_emg_norm15 = train_set_tape_hold_emg_norm15.reshape(8,len_normal).T
train_set_tape_hold_emg_norm16 = train_set_tape_hold_emg_norm16.reshape(8,len_normal).T
train_set_tape_hold_emg_norm17 = train_set_tape_hold_emg_norm17.reshape(8,len_normal).T
train_set_tape_hold_emg_norm18 = train_set_tape_hold_emg_norm18.reshape(8,len_normal).T
train_set_tape_hold_emg_norm19 = train_set_tape_hold_emg_norm19.reshape(8,len_normal).T
test_set_tape_hold_emg_norm = test_set_tape_hold_emg_norm.reshape(8,len_normal).T
train_set_tape_hold_emg_norm_full = np.array([train_set_tape_hold_emg_norm00,train_set_tape_hold_emg_norm01,train_set_tape_hold_emg_norm02,train_set_tape_hold_emg_norm03,train_set_tape_hold_emg_norm04,
                                    train_set_tape_hold_emg_norm05,train_set_tape_hold_emg_norm06,train_set_tape_hold_emg_norm07,train_set_tape_hold_emg_norm08,train_set_tape_hold_emg_norm09,
                                    train_set_tape_hold_emg_norm10,train_set_tape_hold_emg_norm11,train_set_tape_hold_emg_norm12,train_set_tape_hold_emg_norm13,train_set_tape_hold_emg_norm14,
                                    train_set_tape_hold_emg_norm15,train_set_tape_hold_emg_norm16,train_set_tape_hold_emg_norm17,train_set_tape_hold_emg_norm18,train_set_tape_hold_emg_norm19])


#########################################
# resampling the IMU data for experiencing the same duration
#########################################
# rospy.loginfo('normalizing data into same duration')
print('normalizing IMU data into same duration of aluminum_hold')
# resampling imu signals of aluminum_hold
train_set_aluminum_hold_imu_norm00=np.array([]);train_set_aluminum_hold_imu_norm01=np.array([]);train_set_aluminum_hold_imu_norm02=np.array([]);train_set_aluminum_hold_imu_norm03=np.array([]);train_set_aluminum_hold_imu_norm04=np.array([]);
train_set_aluminum_hold_imu_norm05=np.array([]);train_set_aluminum_hold_imu_norm06=np.array([]);train_set_aluminum_hold_imu_norm07=np.array([]);train_set_aluminum_hold_imu_norm08=np.array([]);train_set_aluminum_hold_imu_norm09=np.array([]);
train_set_aluminum_hold_imu_norm10=np.array([]);train_set_aluminum_hold_imu_norm11=np.array([]);train_set_aluminum_hold_imu_norm12=np.array([]);train_set_aluminum_hold_imu_norm13=np.array([]);train_set_aluminum_hold_imu_norm14=np.array([]);
train_set_aluminum_hold_imu_norm15=np.array([]);train_set_aluminum_hold_imu_norm16=np.array([]);train_set_aluminum_hold_imu_norm17=np.array([]);train_set_aluminum_hold_imu_norm18=np.array([]);train_set_aluminum_hold_imu_norm19=np.array([]);
test_set_aluminum_hold_imu_norm=np.array([]);
for ch_ex in range(4):
    train_set_aluminum_hold_imu_norm00 = np.hstack(( train_set_aluminum_hold_imu_norm00, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_00)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_00),1.), train_set_aluminum_hold_imu_00[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm01 = np.hstack(( train_set_aluminum_hold_imu_norm01, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_01)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_01),1.), train_set_aluminum_hold_imu_01[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm02 = np.hstack(( train_set_aluminum_hold_imu_norm02, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_02)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_02),1.), train_set_aluminum_hold_imu_02[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm03 = np.hstack(( train_set_aluminum_hold_imu_norm03, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_03)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_03),1.), train_set_aluminum_hold_imu_03[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm04 = np.hstack(( train_set_aluminum_hold_imu_norm04, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_04)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_04),1.), train_set_aluminum_hold_imu_04[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm05 = np.hstack(( train_set_aluminum_hold_imu_norm05, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_05)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_05),1.), train_set_aluminum_hold_imu_05[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm06 = np.hstack(( train_set_aluminum_hold_imu_norm06, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_06)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_06),1.), train_set_aluminum_hold_imu_06[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm07 = np.hstack(( train_set_aluminum_hold_imu_norm07, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_07)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_07),1.), train_set_aluminum_hold_imu_07[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm08 = np.hstack(( train_set_aluminum_hold_imu_norm08, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_08)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_08),1.), train_set_aluminum_hold_imu_08[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm09 = np.hstack(( train_set_aluminum_hold_imu_norm09, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_09)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_09),1.), train_set_aluminum_hold_imu_09[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm10 = np.hstack(( train_set_aluminum_hold_imu_norm10, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_10)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_10),1.), train_set_aluminum_hold_imu_10[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm11 = np.hstack(( train_set_aluminum_hold_imu_norm11, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_11)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_11),1.), train_set_aluminum_hold_imu_11[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm12 = np.hstack(( train_set_aluminum_hold_imu_norm12, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_12)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_12),1.), train_set_aluminum_hold_imu_12[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm13 = np.hstack(( train_set_aluminum_hold_imu_norm13, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_13)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_13),1.), train_set_aluminum_hold_imu_13[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm14 = np.hstack(( train_set_aluminum_hold_imu_norm14, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_14)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_14),1.), train_set_aluminum_hold_imu_14[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm15 = np.hstack(( train_set_aluminum_hold_imu_norm15, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_15)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_15),1.), train_set_aluminum_hold_imu_15[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm16 = np.hstack(( train_set_aluminum_hold_imu_norm16, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_16)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_16),1.), train_set_aluminum_hold_imu_16[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm17 = np.hstack(( train_set_aluminum_hold_imu_norm17, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_17)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_17),1.), train_set_aluminum_hold_imu_17[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm18 = np.hstack(( train_set_aluminum_hold_imu_norm18, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_18)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_18),1.), train_set_aluminum_hold_imu_18[:,ch_ex]) ))
    train_set_aluminum_hold_imu_norm19 = np.hstack(( train_set_aluminum_hold_imu_norm19, np.interp(np.linspace(0, len(train_set_aluminum_hold_imu_19)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_imu_19),1.), train_set_aluminum_hold_imu_19[:,ch_ex]) ))
    test_set_aluminum_hold_imu_norm = np.hstack(( test_set_aluminum_hold_imu_norm, np.interp(np.linspace(0, len(test_set_aluminum_hold_imu)-1, len_normal), np.arange(0,len(test_set_aluminum_hold_imu),1.), test_set_aluminum_hold_imu[:,ch_ex]) ))
train_set_aluminum_hold_imu_norm00 = train_set_aluminum_hold_imu_norm00.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm01 = train_set_aluminum_hold_imu_norm01.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm02 = train_set_aluminum_hold_imu_norm02.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm03 = train_set_aluminum_hold_imu_norm03.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm04 = train_set_aluminum_hold_imu_norm04.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm05 = train_set_aluminum_hold_imu_norm05.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm06 = train_set_aluminum_hold_imu_norm06.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm07 = train_set_aluminum_hold_imu_norm07.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm08 = train_set_aluminum_hold_imu_norm08.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm09 = train_set_aluminum_hold_imu_norm09.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm10 = train_set_aluminum_hold_imu_norm10.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm11 = train_set_aluminum_hold_imu_norm11.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm12 = train_set_aluminum_hold_imu_norm12.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm13 = train_set_aluminum_hold_imu_norm13.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm14 = train_set_aluminum_hold_imu_norm14.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm15 = train_set_aluminum_hold_imu_norm15.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm16 = train_set_aluminum_hold_imu_norm16.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm17 = train_set_aluminum_hold_imu_norm17.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm18 = train_set_aluminum_hold_imu_norm18.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm19 = train_set_aluminum_hold_imu_norm19.reshape(4,len_normal).T
test_set_aluminum_hold_imu_norm = test_set_aluminum_hold_imu_norm.reshape(4,len_normal).T
train_set_aluminum_hold_imu_norm_full = np.array([train_set_aluminum_hold_imu_norm00,train_set_aluminum_hold_imu_norm01,train_set_aluminum_hold_imu_norm02,train_set_aluminum_hold_imu_norm03,train_set_aluminum_hold_imu_norm04,
                                    train_set_aluminum_hold_imu_norm05,train_set_aluminum_hold_imu_norm06,train_set_aluminum_hold_imu_norm07,train_set_aluminum_hold_imu_norm08,train_set_aluminum_hold_imu_norm09,
                                    train_set_aluminum_hold_imu_norm10,train_set_aluminum_hold_imu_norm11,train_set_aluminum_hold_imu_norm12,train_set_aluminum_hold_imu_norm13,train_set_aluminum_hold_imu_norm14,
                                    train_set_aluminum_hold_imu_norm15,train_set_aluminum_hold_imu_norm16,train_set_aluminum_hold_imu_norm17,train_set_aluminum_hold_imu_norm18,train_set_aluminum_hold_imu_norm19])
##########################################################################################
print('normalizing IMU data into same duration of spanner_handove')
# resampling imu signals of aluminum_hold
train_set_spanner_handover_imu_norm00=np.array([]);train_set_spanner_handover_imu_norm01=np.array([]);train_set_spanner_handover_imu_norm02=np.array([]);train_set_spanner_handover_imu_norm03=np.array([]);train_set_spanner_handover_imu_norm04=np.array([]);
train_set_spanner_handover_imu_norm05=np.array([]);train_set_spanner_handover_imu_norm06=np.array([]);train_set_spanner_handover_imu_norm07=np.array([]);train_set_spanner_handover_imu_norm08=np.array([]);train_set_spanner_handover_imu_norm09=np.array([]);
train_set_spanner_handover_imu_norm10=np.array([]);train_set_spanner_handover_imu_norm11=np.array([]);train_set_spanner_handover_imu_norm12=np.array([]);train_set_spanner_handover_imu_norm13=np.array([]);train_set_spanner_handover_imu_norm14=np.array([]);
train_set_spanner_handover_imu_norm15=np.array([]);train_set_spanner_handover_imu_norm16=np.array([]);train_set_spanner_handover_imu_norm17=np.array([]);train_set_spanner_handover_imu_norm18=np.array([]);train_set_spanner_handover_imu_norm19=np.array([]);
test_set_spanner_handover_imu_norm=np.array([]);
for ch_ex in range(4):
    train_set_spanner_handover_imu_norm00 = np.hstack(( train_set_spanner_handover_imu_norm00, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_00)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_00),1.), train_set_spanner_handover_imu_00[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm01 = np.hstack(( train_set_spanner_handover_imu_norm01, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_01)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_01),1.), train_set_spanner_handover_imu_01[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm02 = np.hstack(( train_set_spanner_handover_imu_norm02, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_02)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_02),1.), train_set_spanner_handover_imu_02[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm03 = np.hstack(( train_set_spanner_handover_imu_norm03, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_03)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_03),1.), train_set_spanner_handover_imu_03[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm04 = np.hstack(( train_set_spanner_handover_imu_norm04, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_04)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_04),1.), train_set_spanner_handover_imu_04[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm05 = np.hstack(( train_set_spanner_handover_imu_norm05, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_05)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_05),1.), train_set_spanner_handover_imu_05[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm06 = np.hstack(( train_set_spanner_handover_imu_norm06, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_06)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_06),1.), train_set_spanner_handover_imu_06[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm07 = np.hstack(( train_set_spanner_handover_imu_norm07, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_07)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_07),1.), train_set_spanner_handover_imu_07[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm08 = np.hstack(( train_set_spanner_handover_imu_norm08, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_08)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_08),1.), train_set_spanner_handover_imu_08[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm09 = np.hstack(( train_set_spanner_handover_imu_norm09, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_09)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_09),1.), train_set_spanner_handover_imu_09[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm10 = np.hstack(( train_set_spanner_handover_imu_norm10, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_10)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_10),1.), train_set_spanner_handover_imu_10[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm11 = np.hstack(( train_set_spanner_handover_imu_norm11, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_11)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_11),1.), train_set_spanner_handover_imu_11[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm12 = np.hstack(( train_set_spanner_handover_imu_norm12, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_12)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_12),1.), train_set_spanner_handover_imu_12[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm13 = np.hstack(( train_set_spanner_handover_imu_norm13, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_13)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_13),1.), train_set_spanner_handover_imu_13[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm14 = np.hstack(( train_set_spanner_handover_imu_norm14, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_14)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_14),1.), train_set_spanner_handover_imu_14[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm15 = np.hstack(( train_set_spanner_handover_imu_norm15, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_15)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_15),1.), train_set_spanner_handover_imu_15[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm16 = np.hstack(( train_set_spanner_handover_imu_norm16, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_16)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_16),1.), train_set_spanner_handover_imu_16[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm17 = np.hstack(( train_set_spanner_handover_imu_norm17, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_17)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_17),1.), train_set_spanner_handover_imu_17[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm18 = np.hstack(( train_set_spanner_handover_imu_norm18, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_18)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_18),1.), train_set_spanner_handover_imu_18[:,ch_ex]) ))
    train_set_spanner_handover_imu_norm19 = np.hstack(( train_set_spanner_handover_imu_norm19, np.interp(np.linspace(0, len(train_set_spanner_handover_imu_19)-1, len_normal), np.arange(0,len(train_set_spanner_handover_imu_19),1.), train_set_spanner_handover_imu_19[:,ch_ex]) ))
    test_set_spanner_handover_imu_norm = np.hstack(( test_set_spanner_handover_imu_norm, np.interp(np.linspace(0, len(test_set_spanner_handover_imu)-1, len_normal), np.arange(0,len(test_set_spanner_handover_imu),1.), test_set_spanner_handover_imu[:,ch_ex]) ))
train_set_spanner_handover_imu_norm00 = train_set_spanner_handover_imu_norm00.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm01 = train_set_spanner_handover_imu_norm01.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm02 = train_set_spanner_handover_imu_norm02.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm03 = train_set_spanner_handover_imu_norm03.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm04 = train_set_spanner_handover_imu_norm04.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm05 = train_set_spanner_handover_imu_norm05.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm06 = train_set_spanner_handover_imu_norm06.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm07 = train_set_spanner_handover_imu_norm07.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm08 = train_set_spanner_handover_imu_norm08.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm09 = train_set_spanner_handover_imu_norm09.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm10 = train_set_spanner_handover_imu_norm10.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm11 = train_set_spanner_handover_imu_norm11.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm12 = train_set_spanner_handover_imu_norm12.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm13 = train_set_spanner_handover_imu_norm13.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm14 = train_set_spanner_handover_imu_norm14.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm15 = train_set_spanner_handover_imu_norm15.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm16 = train_set_spanner_handover_imu_norm16.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm17 = train_set_spanner_handover_imu_norm17.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm18 = train_set_spanner_handover_imu_norm18.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm19 = train_set_spanner_handover_imu_norm19.reshape(4,len_normal).T
test_set_spanner_handover_imu_norm = test_set_spanner_handover_imu_norm.reshape(4,len_normal).T
train_set_spanner_handover_imu_norm_full = np.array([train_set_spanner_handover_imu_norm00,train_set_spanner_handover_imu_norm01,train_set_spanner_handover_imu_norm02,train_set_spanner_handover_imu_norm03,train_set_spanner_handover_imu_norm04,
                                    train_set_spanner_handover_imu_norm05,train_set_spanner_handover_imu_norm06,train_set_spanner_handover_imu_norm07,train_set_spanner_handover_imu_norm08,train_set_spanner_handover_imu_norm09,
                                    train_set_spanner_handover_imu_norm10,train_set_spanner_handover_imu_norm11,train_set_spanner_handover_imu_norm12,train_set_spanner_handover_imu_norm13,train_set_spanner_handover_imu_norm14,
                                    train_set_spanner_handover_imu_norm15,train_set_spanner_handover_imu_norm16,train_set_spanner_handover_imu_norm17,train_set_spanner_handover_imu_norm18,train_set_spanner_handover_imu_norm19])
##########################################################################################
print('normalizing IMU data into same duration of tape_hold')
# resampling imu signals of aluminum_hold
train_set_tape_hold_imu_norm00=np.array([]);train_set_tape_hold_imu_norm01=np.array([]);train_set_tape_hold_imu_norm02=np.array([]);train_set_tape_hold_imu_norm03=np.array([]);train_set_tape_hold_imu_norm04=np.array([]);
train_set_tape_hold_imu_norm05=np.array([]);train_set_tape_hold_imu_norm06=np.array([]);train_set_tape_hold_imu_norm07=np.array([]);train_set_tape_hold_imu_norm08=np.array([]);train_set_tape_hold_imu_norm09=np.array([]);
train_set_tape_hold_imu_norm10=np.array([]);train_set_tape_hold_imu_norm11=np.array([]);train_set_tape_hold_imu_norm12=np.array([]);train_set_tape_hold_imu_norm13=np.array([]);train_set_tape_hold_imu_norm14=np.array([]);
train_set_tape_hold_imu_norm15=np.array([]);train_set_tape_hold_imu_norm16=np.array([]);train_set_tape_hold_imu_norm17=np.array([]);train_set_tape_hold_imu_norm18=np.array([]);train_set_tape_hold_imu_norm19=np.array([]);
test_set_tape_hold_imu_norm=np.array([]);
for ch_ex in range(4):
    train_set_tape_hold_imu_norm00 = np.hstack(( train_set_tape_hold_imu_norm00, np.interp(np.linspace(0, len(train_set_tape_hold_imu_00)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_00),1.), train_set_tape_hold_imu_00[:,ch_ex]) ))
    train_set_tape_hold_imu_norm01 = np.hstack(( train_set_tape_hold_imu_norm01, np.interp(np.linspace(0, len(train_set_tape_hold_imu_01)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_01),1.), train_set_tape_hold_imu_01[:,ch_ex]) ))
    train_set_tape_hold_imu_norm02 = np.hstack(( train_set_tape_hold_imu_norm02, np.interp(np.linspace(0, len(train_set_tape_hold_imu_02)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_02),1.), train_set_tape_hold_imu_02[:,ch_ex]) ))
    train_set_tape_hold_imu_norm03 = np.hstack(( train_set_tape_hold_imu_norm03, np.interp(np.linspace(0, len(train_set_tape_hold_imu_03)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_03),1.), train_set_tape_hold_imu_03[:,ch_ex]) ))
    train_set_tape_hold_imu_norm04 = np.hstack(( train_set_tape_hold_imu_norm04, np.interp(np.linspace(0, len(train_set_tape_hold_imu_04)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_04),1.), train_set_tape_hold_imu_04[:,ch_ex]) ))
    train_set_tape_hold_imu_norm05 = np.hstack(( train_set_tape_hold_imu_norm05, np.interp(np.linspace(0, len(train_set_tape_hold_imu_05)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_05),1.), train_set_tape_hold_imu_05[:,ch_ex]) ))
    train_set_tape_hold_imu_norm06 = np.hstack(( train_set_tape_hold_imu_norm06, np.interp(np.linspace(0, len(train_set_tape_hold_imu_06)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_06),1.), train_set_tape_hold_imu_06[:,ch_ex]) ))
    train_set_tape_hold_imu_norm07 = np.hstack(( train_set_tape_hold_imu_norm07, np.interp(np.linspace(0, len(train_set_tape_hold_imu_07)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_07),1.), train_set_tape_hold_imu_07[:,ch_ex]) ))
    train_set_tape_hold_imu_norm08 = np.hstack(( train_set_tape_hold_imu_norm08, np.interp(np.linspace(0, len(train_set_tape_hold_imu_08)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_08),1.), train_set_tape_hold_imu_08[:,ch_ex]) ))
    train_set_tape_hold_imu_norm09 = np.hstack(( train_set_tape_hold_imu_norm09, np.interp(np.linspace(0, len(train_set_tape_hold_imu_09)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_09),1.), train_set_tape_hold_imu_09[:,ch_ex]) ))
    train_set_tape_hold_imu_norm10 = np.hstack(( train_set_tape_hold_imu_norm10, np.interp(np.linspace(0, len(train_set_tape_hold_imu_10)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_10),1.), train_set_tape_hold_imu_10[:,ch_ex]) ))
    train_set_tape_hold_imu_norm11 = np.hstack(( train_set_tape_hold_imu_norm11, np.interp(np.linspace(0, len(train_set_tape_hold_imu_11)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_11),1.), train_set_tape_hold_imu_11[:,ch_ex]) ))
    train_set_tape_hold_imu_norm12 = np.hstack(( train_set_tape_hold_imu_norm12, np.interp(np.linspace(0, len(train_set_tape_hold_imu_12)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_12),1.), train_set_tape_hold_imu_12[:,ch_ex]) ))
    train_set_tape_hold_imu_norm13 = np.hstack(( train_set_tape_hold_imu_norm13, np.interp(np.linspace(0, len(train_set_tape_hold_imu_13)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_13),1.), train_set_tape_hold_imu_13[:,ch_ex]) ))
    train_set_tape_hold_imu_norm14 = np.hstack(( train_set_tape_hold_imu_norm14, np.interp(np.linspace(0, len(train_set_tape_hold_imu_14)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_14),1.), train_set_tape_hold_imu_14[:,ch_ex]) ))
    train_set_tape_hold_imu_norm15 = np.hstack(( train_set_tape_hold_imu_norm15, np.interp(np.linspace(0, len(train_set_tape_hold_imu_15)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_15),1.), train_set_tape_hold_imu_15[:,ch_ex]) ))
    train_set_tape_hold_imu_norm16 = np.hstack(( train_set_tape_hold_imu_norm16, np.interp(np.linspace(0, len(train_set_tape_hold_imu_16)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_16),1.), train_set_tape_hold_imu_16[:,ch_ex]) ))
    train_set_tape_hold_imu_norm17 = np.hstack(( train_set_tape_hold_imu_norm17, np.interp(np.linspace(0, len(train_set_tape_hold_imu_17)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_17),1.), train_set_tape_hold_imu_17[:,ch_ex]) ))
    train_set_tape_hold_imu_norm18 = np.hstack(( train_set_tape_hold_imu_norm18, np.interp(np.linspace(0, len(train_set_tape_hold_imu_18)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_18),1.), train_set_tape_hold_imu_18[:,ch_ex]) ))
    train_set_tape_hold_imu_norm19 = np.hstack(( train_set_tape_hold_imu_norm19, np.interp(np.linspace(0, len(train_set_tape_hold_imu_19)-1, len_normal), np.arange(0,len(train_set_tape_hold_imu_19),1.), train_set_tape_hold_imu_19[:,ch_ex]) ))
    test_set_tape_hold_imu_norm = np.hstack(( test_set_tape_hold_imu_norm, np.interp(np.linspace(0, len(test_set_tape_hold_imu)-1, len_normal), np.arange(0,len(test_set_tape_hold_imu),1.), test_set_tape_hold_imu[:,ch_ex]) ))
train_set_tape_hold_imu_norm00 = train_set_tape_hold_imu_norm00.reshape(4,len_normal).T
train_set_tape_hold_imu_norm01 = train_set_tape_hold_imu_norm01.reshape(4,len_normal).T
train_set_tape_hold_imu_norm02 = train_set_tape_hold_imu_norm02.reshape(4,len_normal).T
train_set_tape_hold_imu_norm03 = train_set_tape_hold_imu_norm03.reshape(4,len_normal).T
train_set_tape_hold_imu_norm04 = train_set_tape_hold_imu_norm04.reshape(4,len_normal).T
train_set_tape_hold_imu_norm05 = train_set_tape_hold_imu_norm05.reshape(4,len_normal).T
train_set_tape_hold_imu_norm06 = train_set_tape_hold_imu_norm06.reshape(4,len_normal).T
train_set_tape_hold_imu_norm07 = train_set_tape_hold_imu_norm07.reshape(4,len_normal).T
train_set_tape_hold_imu_norm08 = train_set_tape_hold_imu_norm08.reshape(4,len_normal).T
train_set_tape_hold_imu_norm09 = train_set_tape_hold_imu_norm09.reshape(4,len_normal).T
train_set_tape_hold_imu_norm10 = train_set_tape_hold_imu_norm10.reshape(4,len_normal).T
train_set_tape_hold_imu_norm11 = train_set_tape_hold_imu_norm11.reshape(4,len_normal).T
train_set_tape_hold_imu_norm12 = train_set_tape_hold_imu_norm12.reshape(4,len_normal).T
train_set_tape_hold_imu_norm13 = train_set_tape_hold_imu_norm13.reshape(4,len_normal).T
train_set_tape_hold_imu_norm14 = train_set_tape_hold_imu_norm14.reshape(4,len_normal).T
train_set_tape_hold_imu_norm15 = train_set_tape_hold_imu_norm15.reshape(4,len_normal).T
train_set_tape_hold_imu_norm16 = train_set_tape_hold_imu_norm16.reshape(4,len_normal).T
train_set_tape_hold_imu_norm17 = train_set_tape_hold_imu_norm17.reshape(4,len_normal).T
train_set_tape_hold_imu_norm18 = train_set_tape_hold_imu_norm18.reshape(4,len_normal).T
train_set_tape_hold_imu_norm19 = train_set_tape_hold_imu_norm19.reshape(4,len_normal).T
test_set_tape_hold_imu_norm = test_set_tape_hold_imu_norm.reshape(4,len_normal).T
train_set_tape_hold_imu_norm_full = np.array([train_set_tape_hold_imu_norm00,train_set_tape_hold_imu_norm01,train_set_tape_hold_imu_norm02,train_set_tape_hold_imu_norm03,train_set_tape_hold_imu_norm04,
                                    train_set_tape_hold_imu_norm05,train_set_tape_hold_imu_norm06,train_set_tape_hold_imu_norm07,train_set_tape_hold_imu_norm08,train_set_tape_hold_imu_norm09,
                                    train_set_tape_hold_imu_norm10,train_set_tape_hold_imu_norm11,train_set_tape_hold_imu_norm12,train_set_tape_hold_imu_norm13,train_set_tape_hold_imu_norm14,
                                    train_set_tape_hold_imu_norm15,train_set_tape_hold_imu_norm16,train_set_tape_hold_imu_norm17,train_set_tape_hold_imu_norm18,train_set_tape_hold_imu_norm19])

#########################################
# resampling the Pose data for experiencing the same duration
#########################################
# rospy.loginfo('normalizing data into same duration')
print('normalizing Pose data into same duration of aluminum_hold')
# resampling signals of aluminum_hold
train_set_aluminum_hold_pose_norm00=np.array([]);train_set_aluminum_hold_pose_norm01=np.array([]);train_set_aluminum_hold_pose_norm02=np.array([]);train_set_aluminum_hold_pose_norm03=np.array([]);train_set_aluminum_hold_pose_norm04=np.array([]);
train_set_aluminum_hold_pose_norm05=np.array([]);train_set_aluminum_hold_pose_norm06=np.array([]);train_set_aluminum_hold_pose_norm07=np.array([]);train_set_aluminum_hold_pose_norm08=np.array([]);train_set_aluminum_hold_pose_norm09=np.array([]);
train_set_aluminum_hold_pose_norm10=np.array([]);train_set_aluminum_hold_pose_norm11=np.array([]);train_set_aluminum_hold_pose_norm12=np.array([]);train_set_aluminum_hold_pose_norm13=np.array([]);train_set_aluminum_hold_pose_norm14=np.array([]);
train_set_aluminum_hold_pose_norm15=np.array([]);train_set_aluminum_hold_pose_norm16=np.array([]);train_set_aluminum_hold_pose_norm17=np.array([]);train_set_aluminum_hold_pose_norm18=np.array([]);train_set_aluminum_hold_pose_norm19=np.array([]);
test_set_aluminum_hold_pose_norm=np.array([]);
for ch_ex in range(7):
    train_set_aluminum_hold_pose_norm00 = np.hstack(( train_set_aluminum_hold_pose_norm00, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_00)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_00),1.), train_set_aluminum_hold_pose_00[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm01 = np.hstack(( train_set_aluminum_hold_pose_norm01, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_01)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_01),1.), train_set_aluminum_hold_pose_01[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm02 = np.hstack(( train_set_aluminum_hold_pose_norm02, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_02)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_02),1.), train_set_aluminum_hold_pose_02[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm03 = np.hstack(( train_set_aluminum_hold_pose_norm03, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_03)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_03),1.), train_set_aluminum_hold_pose_03[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm04 = np.hstack(( train_set_aluminum_hold_pose_norm04, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_04)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_04),1.), train_set_aluminum_hold_pose_04[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm05 = np.hstack(( train_set_aluminum_hold_pose_norm05, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_05)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_05),1.), train_set_aluminum_hold_pose_05[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm06 = np.hstack(( train_set_aluminum_hold_pose_norm06, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_06)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_06),1.), train_set_aluminum_hold_pose_06[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm07 = np.hstack(( train_set_aluminum_hold_pose_norm07, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_07)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_07),1.), train_set_aluminum_hold_pose_07[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm08 = np.hstack(( train_set_aluminum_hold_pose_norm08, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_08)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_08),1.), train_set_aluminum_hold_pose_08[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm09 = np.hstack(( train_set_aluminum_hold_pose_norm09, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_09)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_09),1.), train_set_aluminum_hold_pose_09[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm10 = np.hstack(( train_set_aluminum_hold_pose_norm10, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_10)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_10),1.), train_set_aluminum_hold_pose_10[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm11 = np.hstack(( train_set_aluminum_hold_pose_norm11, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_11)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_11),1.), train_set_aluminum_hold_pose_11[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm12 = np.hstack(( train_set_aluminum_hold_pose_norm12, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_12)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_12),1.), train_set_aluminum_hold_pose_12[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm13 = np.hstack(( train_set_aluminum_hold_pose_norm13, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_13)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_13),1.), train_set_aluminum_hold_pose_13[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm14 = np.hstack(( train_set_aluminum_hold_pose_norm14, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_14)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_14),1.), train_set_aluminum_hold_pose_14[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm15 = np.hstack(( train_set_aluminum_hold_pose_norm15, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_15)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_15),1.), train_set_aluminum_hold_pose_15[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm16 = np.hstack(( train_set_aluminum_hold_pose_norm16, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_16)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_16),1.), train_set_aluminum_hold_pose_16[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm17 = np.hstack(( train_set_aluminum_hold_pose_norm17, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_17)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_17),1.), train_set_aluminum_hold_pose_17[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm18 = np.hstack(( train_set_aluminum_hold_pose_norm18, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_18)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_18),1.), train_set_aluminum_hold_pose_18[:,ch_ex]) ))
    train_set_aluminum_hold_pose_norm19 = np.hstack(( train_set_aluminum_hold_pose_norm19, np.interp(np.linspace(0, len(train_set_aluminum_hold_pose_19)-1, len_normal), np.arange(0,len(train_set_aluminum_hold_pose_19),1.), train_set_aluminum_hold_pose_19[:,ch_ex]) ))
    test_set_aluminum_hold_pose_norm = np.hstack(( test_set_aluminum_hold_pose_norm, np.interp(np.linspace(0, len(test_set_aluminum_hold_pose)-1, len_normal), np.arange(0,len(test_set_aluminum_hold_pose),1.), test_set_aluminum_hold_pose[:,ch_ex]) ))
train_set_aluminum_hold_pose_norm00 = train_set_aluminum_hold_pose_norm00.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm01 = train_set_aluminum_hold_pose_norm01.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm02 = train_set_aluminum_hold_pose_norm02.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm03 = train_set_aluminum_hold_pose_norm03.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm04 = train_set_aluminum_hold_pose_norm04.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm05 = train_set_aluminum_hold_pose_norm05.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm06 = train_set_aluminum_hold_pose_norm06.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm07 = train_set_aluminum_hold_pose_norm07.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm08 = train_set_aluminum_hold_pose_norm08.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm09 = train_set_aluminum_hold_pose_norm09.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm10 = train_set_aluminum_hold_pose_norm10.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm11 = train_set_aluminum_hold_pose_norm11.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm12 = train_set_aluminum_hold_pose_norm12.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm13 = train_set_aluminum_hold_pose_norm13.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm14 = train_set_aluminum_hold_pose_norm14.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm15 = train_set_aluminum_hold_pose_norm15.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm16 = train_set_aluminum_hold_pose_norm16.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm17 = train_set_aluminum_hold_pose_norm17.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm18 = train_set_aluminum_hold_pose_norm18.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm19 = train_set_aluminum_hold_pose_norm19.reshape(7,len_normal).T
test_set_aluminum_hold_pose_norm = test_set_aluminum_hold_pose_norm.reshape(7,len_normal).T
train_set_aluminum_hold_pose_norm_full = np.array([train_set_aluminum_hold_pose_norm00,train_set_aluminum_hold_pose_norm01,train_set_aluminum_hold_pose_norm02,train_set_aluminum_hold_pose_norm03,train_set_aluminum_hold_pose_norm04,
                                    train_set_aluminum_hold_pose_norm05,train_set_aluminum_hold_pose_norm06,train_set_aluminum_hold_pose_norm07,train_set_aluminum_hold_pose_norm08,train_set_aluminum_hold_pose_norm09,
                                    train_set_aluminum_hold_pose_norm10,train_set_aluminum_hold_pose_norm11,train_set_aluminum_hold_pose_norm12,train_set_aluminum_hold_pose_norm13,train_set_aluminum_hold_pose_norm14,
                                    train_set_aluminum_hold_pose_norm15,train_set_aluminum_hold_pose_norm16,train_set_aluminum_hold_pose_norm17,train_set_aluminum_hold_pose_norm18,train_set_aluminum_hold_pose_norm19])
##########################################################################################
print('normalizing Pose data into same duration of spanner_handove')
# resampling pose signals of aluminum_hold
train_set_spanner_handover_pose_norm00=np.array([]);train_set_spanner_handover_pose_norm01=np.array([]);train_set_spanner_handover_pose_norm02=np.array([]);train_set_spanner_handover_pose_norm03=np.array([]);train_set_spanner_handover_pose_norm04=np.array([]);
train_set_spanner_handover_pose_norm05=np.array([]);train_set_spanner_handover_pose_norm06=np.array([]);train_set_spanner_handover_pose_norm07=np.array([]);train_set_spanner_handover_pose_norm08=np.array([]);train_set_spanner_handover_pose_norm09=np.array([]);
train_set_spanner_handover_pose_norm10=np.array([]);train_set_spanner_handover_pose_norm11=np.array([]);train_set_spanner_handover_pose_norm12=np.array([]);train_set_spanner_handover_pose_norm13=np.array([]);train_set_spanner_handover_pose_norm14=np.array([]);
train_set_spanner_handover_pose_norm15=np.array([]);train_set_spanner_handover_pose_norm16=np.array([]);train_set_spanner_handover_pose_norm17=np.array([]);train_set_spanner_handover_pose_norm18=np.array([]);train_set_spanner_handover_pose_norm19=np.array([]);
test_set_spanner_handover_pose_norm=np.array([]);
for ch_ex in range(7):
    train_set_spanner_handover_pose_norm00 = np.hstack(( train_set_spanner_handover_pose_norm00, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_00)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_00),1.), train_set_spanner_handover_pose_00[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm01 = np.hstack(( train_set_spanner_handover_pose_norm01, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_01)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_01),1.), train_set_spanner_handover_pose_01[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm02 = np.hstack(( train_set_spanner_handover_pose_norm02, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_02)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_02),1.), train_set_spanner_handover_pose_02[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm03 = np.hstack(( train_set_spanner_handover_pose_norm03, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_03)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_03),1.), train_set_spanner_handover_pose_03[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm04 = np.hstack(( train_set_spanner_handover_pose_norm04, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_04)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_04),1.), train_set_spanner_handover_pose_04[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm05 = np.hstack(( train_set_spanner_handover_pose_norm05, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_05)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_05),1.), train_set_spanner_handover_pose_05[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm06 = np.hstack(( train_set_spanner_handover_pose_norm06, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_06)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_06),1.), train_set_spanner_handover_pose_06[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm07 = np.hstack(( train_set_spanner_handover_pose_norm07, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_07)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_07),1.), train_set_spanner_handover_pose_07[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm08 = np.hstack(( train_set_spanner_handover_pose_norm08, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_08)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_08),1.), train_set_spanner_handover_pose_08[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm09 = np.hstack(( train_set_spanner_handover_pose_norm09, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_09)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_09),1.), train_set_spanner_handover_pose_09[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm10 = np.hstack(( train_set_spanner_handover_pose_norm10, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_10)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_10),1.), train_set_spanner_handover_pose_10[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm11 = np.hstack(( train_set_spanner_handover_pose_norm11, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_11)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_11),1.), train_set_spanner_handover_pose_11[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm12 = np.hstack(( train_set_spanner_handover_pose_norm12, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_12)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_12),1.), train_set_spanner_handover_pose_12[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm13 = np.hstack(( train_set_spanner_handover_pose_norm13, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_13)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_13),1.), train_set_spanner_handover_pose_13[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm14 = np.hstack(( train_set_spanner_handover_pose_norm14, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_14)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_14),1.), train_set_spanner_handover_pose_14[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm15 = np.hstack(( train_set_spanner_handover_pose_norm15, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_15)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_15),1.), train_set_spanner_handover_pose_15[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm16 = np.hstack(( train_set_spanner_handover_pose_norm16, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_16)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_16),1.), train_set_spanner_handover_pose_16[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm17 = np.hstack(( train_set_spanner_handover_pose_norm17, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_17)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_17),1.), train_set_spanner_handover_pose_17[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm18 = np.hstack(( train_set_spanner_handover_pose_norm18, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_18)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_18),1.), train_set_spanner_handover_pose_18[:,ch_ex]) ))
    train_set_spanner_handover_pose_norm19 = np.hstack(( train_set_spanner_handover_pose_norm19, np.interp(np.linspace(0, len(train_set_spanner_handover_pose_19)-1, len_normal), np.arange(0,len(train_set_spanner_handover_pose_19),1.), train_set_spanner_handover_pose_19[:,ch_ex]) ))
    test_set_spanner_handover_pose_norm = np.hstack(( test_set_spanner_handover_pose_norm, np.interp(np.linspace(0, len(test_set_spanner_handover_pose)-1, len_normal), np.arange(0,len(test_set_spanner_handover_pose),1.), test_set_spanner_handover_pose[:,ch_ex]) ))
train_set_spanner_handover_pose_norm00 = train_set_spanner_handover_pose_norm00.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm01 = train_set_spanner_handover_pose_norm01.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm02 = train_set_spanner_handover_pose_norm02.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm03 = train_set_spanner_handover_pose_norm03.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm04 = train_set_spanner_handover_pose_norm04.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm05 = train_set_spanner_handover_pose_norm05.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm06 = train_set_spanner_handover_pose_norm06.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm07 = train_set_spanner_handover_pose_norm07.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm08 = train_set_spanner_handover_pose_norm08.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm09 = train_set_spanner_handover_pose_norm09.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm10 = train_set_spanner_handover_pose_norm10.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm11 = train_set_spanner_handover_pose_norm11.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm12 = train_set_spanner_handover_pose_norm12.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm13 = train_set_spanner_handover_pose_norm13.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm14 = train_set_spanner_handover_pose_norm14.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm15 = train_set_spanner_handover_pose_norm15.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm16 = train_set_spanner_handover_pose_norm16.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm17 = train_set_spanner_handover_pose_norm17.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm18 = train_set_spanner_handover_pose_norm18.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm19 = train_set_spanner_handover_pose_norm19.reshape(7,len_normal).T
test_set_spanner_handover_pose_norm = test_set_spanner_handover_pose_norm.reshape(7,len_normal).T
train_set_spanner_handover_pose_norm_full = np.array([train_set_spanner_handover_pose_norm00,train_set_spanner_handover_pose_norm01,train_set_spanner_handover_pose_norm02,train_set_spanner_handover_pose_norm03,train_set_spanner_handover_pose_norm04,
                                    train_set_spanner_handover_pose_norm05,train_set_spanner_handover_pose_norm06,train_set_spanner_handover_pose_norm07,train_set_spanner_handover_pose_norm08,train_set_spanner_handover_pose_norm09,
                                    train_set_spanner_handover_pose_norm10,train_set_spanner_handover_pose_norm11,train_set_spanner_handover_pose_norm12,train_set_spanner_handover_pose_norm13,train_set_spanner_handover_pose_norm14,
                                    train_set_spanner_handover_pose_norm15,train_set_spanner_handover_pose_norm16,train_set_spanner_handover_pose_norm17,train_set_spanner_handover_pose_norm18,train_set_spanner_handover_pose_norm19])
##########################################################################################
print('normalizing Pose data into same duration of tape_hold')
# resampling pose signals of aluminum_hold
train_set_tape_hold_pose_norm00=np.array([]);train_set_tape_hold_pose_norm01=np.array([]);train_set_tape_hold_pose_norm02=np.array([]);train_set_tape_hold_pose_norm03=np.array([]);train_set_tape_hold_pose_norm04=np.array([]);
train_set_tape_hold_pose_norm05=np.array([]);train_set_tape_hold_pose_norm06=np.array([]);train_set_tape_hold_pose_norm07=np.array([]);train_set_tape_hold_pose_norm08=np.array([]);train_set_tape_hold_pose_norm09=np.array([]);
train_set_tape_hold_pose_norm10=np.array([]);train_set_tape_hold_pose_norm11=np.array([]);train_set_tape_hold_pose_norm12=np.array([]);train_set_tape_hold_pose_norm13=np.array([]);train_set_tape_hold_pose_norm14=np.array([]);
train_set_tape_hold_pose_norm15=np.array([]);train_set_tape_hold_pose_norm16=np.array([]);train_set_tape_hold_pose_norm17=np.array([]);train_set_tape_hold_pose_norm18=np.array([]);train_set_tape_hold_pose_norm19=np.array([]);
test_set_tape_hold_pose_norm=np.array([]);
for ch_ex in range(7):
    train_set_tape_hold_pose_norm00 = np.hstack(( train_set_tape_hold_pose_norm00, np.interp(np.linspace(0, len(train_set_tape_hold_pose_00)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_00),1.), train_set_tape_hold_pose_00[:,ch_ex]) ))
    train_set_tape_hold_pose_norm01 = np.hstack(( train_set_tape_hold_pose_norm01, np.interp(np.linspace(0, len(train_set_tape_hold_pose_01)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_01),1.), train_set_tape_hold_pose_01[:,ch_ex]) ))
    train_set_tape_hold_pose_norm02 = np.hstack(( train_set_tape_hold_pose_norm02, np.interp(np.linspace(0, len(train_set_tape_hold_pose_02)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_02),1.), train_set_tape_hold_pose_02[:,ch_ex]) ))
    train_set_tape_hold_pose_norm03 = np.hstack(( train_set_tape_hold_pose_norm03, np.interp(np.linspace(0, len(train_set_tape_hold_pose_03)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_03),1.), train_set_tape_hold_pose_03[:,ch_ex]) ))
    train_set_tape_hold_pose_norm04 = np.hstack(( train_set_tape_hold_pose_norm04, np.interp(np.linspace(0, len(train_set_tape_hold_pose_04)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_04),1.), train_set_tape_hold_pose_04[:,ch_ex]) ))
    train_set_tape_hold_pose_norm05 = np.hstack(( train_set_tape_hold_pose_norm05, np.interp(np.linspace(0, len(train_set_tape_hold_pose_05)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_05),1.), train_set_tape_hold_pose_05[:,ch_ex]) ))
    train_set_tape_hold_pose_norm06 = np.hstack(( train_set_tape_hold_pose_norm06, np.interp(np.linspace(0, len(train_set_tape_hold_pose_06)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_06),1.), train_set_tape_hold_pose_06[:,ch_ex]) ))
    train_set_tape_hold_pose_norm07 = np.hstack(( train_set_tape_hold_pose_norm07, np.interp(np.linspace(0, len(train_set_tape_hold_pose_07)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_07),1.), train_set_tape_hold_pose_07[:,ch_ex]) ))
    train_set_tape_hold_pose_norm08 = np.hstack(( train_set_tape_hold_pose_norm08, np.interp(np.linspace(0, len(train_set_tape_hold_pose_08)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_08),1.), train_set_tape_hold_pose_08[:,ch_ex]) ))
    train_set_tape_hold_pose_norm09 = np.hstack(( train_set_tape_hold_pose_norm09, np.interp(np.linspace(0, len(train_set_tape_hold_pose_09)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_09),1.), train_set_tape_hold_pose_09[:,ch_ex]) ))
    train_set_tape_hold_pose_norm10 = np.hstack(( train_set_tape_hold_pose_norm10, np.interp(np.linspace(0, len(train_set_tape_hold_pose_10)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_10),1.), train_set_tape_hold_pose_10[:,ch_ex]) ))
    train_set_tape_hold_pose_norm11 = np.hstack(( train_set_tape_hold_pose_norm11, np.interp(np.linspace(0, len(train_set_tape_hold_pose_11)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_11),1.), train_set_tape_hold_pose_11[:,ch_ex]) ))
    train_set_tape_hold_pose_norm12 = np.hstack(( train_set_tape_hold_pose_norm12, np.interp(np.linspace(0, len(train_set_tape_hold_pose_12)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_12),1.), train_set_tape_hold_pose_12[:,ch_ex]) ))
    train_set_tape_hold_pose_norm13 = np.hstack(( train_set_tape_hold_pose_norm13, np.interp(np.linspace(0, len(train_set_tape_hold_pose_13)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_13),1.), train_set_tape_hold_pose_13[:,ch_ex]) ))
    train_set_tape_hold_pose_norm14 = np.hstack(( train_set_tape_hold_pose_norm14, np.interp(np.linspace(0, len(train_set_tape_hold_pose_14)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_14),1.), train_set_tape_hold_pose_14[:,ch_ex]) ))
    train_set_tape_hold_pose_norm15 = np.hstack(( train_set_tape_hold_pose_norm15, np.interp(np.linspace(0, len(train_set_tape_hold_pose_15)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_15),1.), train_set_tape_hold_pose_15[:,ch_ex]) ))
    train_set_tape_hold_pose_norm16 = np.hstack(( train_set_tape_hold_pose_norm16, np.interp(np.linspace(0, len(train_set_tape_hold_pose_16)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_16),1.), train_set_tape_hold_pose_16[:,ch_ex]) ))
    train_set_tape_hold_pose_norm17 = np.hstack(( train_set_tape_hold_pose_norm17, np.interp(np.linspace(0, len(train_set_tape_hold_pose_17)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_17),1.), train_set_tape_hold_pose_17[:,ch_ex]) ))
    train_set_tape_hold_pose_norm18 = np.hstack(( train_set_tape_hold_pose_norm18, np.interp(np.linspace(0, len(train_set_tape_hold_pose_18)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_18),1.), train_set_tape_hold_pose_18[:,ch_ex]) ))
    train_set_tape_hold_pose_norm19 = np.hstack(( train_set_tape_hold_pose_norm19, np.interp(np.linspace(0, len(train_set_tape_hold_pose_19)-1, len_normal), np.arange(0,len(train_set_tape_hold_pose_19),1.), train_set_tape_hold_pose_19[:,ch_ex]) ))
    test_set_tape_hold_pose_norm = np.hstack(( test_set_tape_hold_pose_norm, np.interp(np.linspace(0, len(test_set_tape_hold_pose)-1, len_normal), np.arange(0,len(test_set_tape_hold_pose),1.), test_set_tape_hold_pose[:,ch_ex]) ))
train_set_tape_hold_pose_norm00 = train_set_tape_hold_pose_norm00.reshape(7,len_normal).T
train_set_tape_hold_pose_norm01 = train_set_tape_hold_pose_norm01.reshape(7,len_normal).T
train_set_tape_hold_pose_norm02 = train_set_tape_hold_pose_norm02.reshape(7,len_normal).T
train_set_tape_hold_pose_norm03 = train_set_tape_hold_pose_norm03.reshape(7,len_normal).T
train_set_tape_hold_pose_norm04 = train_set_tape_hold_pose_norm04.reshape(7,len_normal).T
train_set_tape_hold_pose_norm05 = train_set_tape_hold_pose_norm05.reshape(7,len_normal).T
train_set_tape_hold_pose_norm06 = train_set_tape_hold_pose_norm06.reshape(7,len_normal).T
train_set_tape_hold_pose_norm07 = train_set_tape_hold_pose_norm07.reshape(7,len_normal).T
train_set_tape_hold_pose_norm08 = train_set_tape_hold_pose_norm08.reshape(7,len_normal).T
train_set_tape_hold_pose_norm09 = train_set_tape_hold_pose_norm09.reshape(7,len_normal).T
train_set_tape_hold_pose_norm10 = train_set_tape_hold_pose_norm10.reshape(7,len_normal).T
train_set_tape_hold_pose_norm11 = train_set_tape_hold_pose_norm11.reshape(7,len_normal).T
train_set_tape_hold_pose_norm12 = train_set_tape_hold_pose_norm12.reshape(7,len_normal).T
train_set_tape_hold_pose_norm13 = train_set_tape_hold_pose_norm13.reshape(7,len_normal).T
train_set_tape_hold_pose_norm14 = train_set_tape_hold_pose_norm14.reshape(7,len_normal).T
train_set_tape_hold_pose_norm15 = train_set_tape_hold_pose_norm15.reshape(7,len_normal).T
train_set_tape_hold_pose_norm16 = train_set_tape_hold_pose_norm16.reshape(7,len_normal).T
train_set_tape_hold_pose_norm17 = train_set_tape_hold_pose_norm17.reshape(7,len_normal).T
train_set_tape_hold_pose_norm18 = train_set_tape_hold_pose_norm18.reshape(7,len_normal).T
train_set_tape_hold_pose_norm19 = train_set_tape_hold_pose_norm19.reshape(7,len_normal).T
test_set_tape_hold_pose_norm = test_set_tape_hold_pose_norm.reshape(7,len_normal).T
train_set_tape_hold_pose_norm_full = np.array([train_set_tape_hold_pose_norm00,train_set_tape_hold_pose_norm01,train_set_tape_hold_pose_norm02,train_set_tape_hold_pose_norm03,train_set_tape_hold_pose_norm04,
                                    train_set_tape_hold_pose_norm05,train_set_tape_hold_pose_norm06,train_set_tape_hold_pose_norm07,train_set_tape_hold_pose_norm08,train_set_tape_hold_pose_norm09,
                                    train_set_tape_hold_pose_norm10,train_set_tape_hold_pose_norm11,train_set_tape_hold_pose_norm12,train_set_tape_hold_pose_norm13,train_set_tape_hold_pose_norm14,
                                    train_set_tape_hold_pose_norm15,train_set_tape_hold_pose_norm16,train_set_tape_hold_pose_norm17,train_set_tape_hold_pose_norm18,train_set_tape_hold_pose_norm19])



#########################################
# plot EMG norm data
#########################################
# plot the norm emg data of aluminum_hold
plt.figure(10)
for ch_ex in range(8):
   plt.subplot(421+ch_ex)
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm00[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm01[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm02[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm03[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm04[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm05[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm06[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm07[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm08[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm09[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm10[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm11[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm12[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm13[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm14[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm15[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm16[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm17[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm18[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_aluminum_hold_emg_norm19[:,ch_ex])
# plot the norm emg data of spanner_handover
plt.figure(11)
for ch_ex in range(8):
   plt.subplot(421+ch_ex)
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm00[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm01[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm02[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm03[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm04[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm05[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm06[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm07[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm08[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm09[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm10[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm11[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm12[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm13[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm14[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm15[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm16[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm17[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm18[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_spanner_handover_emg_norm19[:,ch_ex])
# plot the norm emg data of tape_hold
plt.figure(12)
for ch_ex in range(8):
   plt.subplot(421+ch_ex)
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm00[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm01[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm02[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm03[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm04[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm05[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm06[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm07[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm08[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm09[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm10[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm11[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm12[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm13[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm14[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm15[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm16[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm17[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm18[:,ch_ex])
   plt.plot(np.arange(0,1.01,0.01), train_set_tape_hold_emg_norm19[:,ch_ex])

#########################################
# plot IMU norm data
#########################################
# plot the norm imu data of aluminum_hold
plt.figure(13)
for ch_ex in range(4):
   plt.subplot(411 + ch_ex)
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm00[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm01[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm02[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm03[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm04[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm05[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm06[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm07[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm08[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm09[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm10[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm11[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm12[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm13[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm14[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm15[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm16[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm17[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm18[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_imu_norm19[:, ch_ex])
# plot the norm imu data of spanner_handover
plt.figure(14)
for ch_ex in range(4):
   plt.subplot(411 + ch_ex)
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm00[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm01[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm02[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm03[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm04[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm05[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm06[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm07[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm08[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm09[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm10[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm11[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm12[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm13[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm14[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm15[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm16[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm17[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm18[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_imu_norm19[:, ch_ex])
# plot the norm imu data of tape_hold
plt.figure(15)
for ch_ex in range(4):
   plt.subplot(411 + ch_ex)
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm00[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm01[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm02[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm03[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm04[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm05[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm06[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm07[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm08[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm09[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm10[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm11[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm12[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm13[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm14[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm15[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm16[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm17[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm18[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_imu_norm19[:, ch_ex])

#########################################
# plot Pose norm data
#########################################
# plot the norm pose data of aluminum_hold
plt.figure(16)
for ch_ex in range(7):
   plt.subplot(711 + ch_ex)
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm00[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm01[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm02[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm03[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm04[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm05[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm06[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm07[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm08[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm09[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm10[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm11[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm12[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm13[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm14[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm15[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm16[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm17[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm18[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_aluminum_hold_pose_norm19[:, ch_ex])
# plot the norm pose data of spanner_handover
plt.figure(17)
for ch_ex in range(7):
   plt.subplot(711 + ch_ex)
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm00[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm01[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm02[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm03[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm04[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm05[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm06[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm07[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm08[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm09[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm10[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm11[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm12[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm13[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm14[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm15[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm16[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm17[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm18[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_spanner_handover_pose_norm19[:, ch_ex])
# plot the norm pose data of tape_hold
plt.figure(18)
for ch_ex in range(7):
   plt.subplot(711 + ch_ex)
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm00[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm01[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm02[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm03[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm04[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm05[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm06[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm07[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm08[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm09[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm10[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm11[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm12[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm13[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm14[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm15[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm16[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm17[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm18[:, ch_ex])
   plt.plot(np.arange(0, 1.01, 0.01), train_set_tape_hold_pose_norm19[:, ch_ex])




# # create a n-dimensional iProMP
# ipromp = ipromps.IProMP(num_joints=15, nrBasis=31, sigma=0.05, num_samples=101)
#
# # add demostration
# for idx in range(0, nrDemo):
#     demo_temp = np.hstack([train_set_emg_norm_full[idx], train_set_joint_norm_full[idx]])
#     ipromp.add_demonstration(demo_temp)
#
# # plot the prior distributioin
# plt.figure(4)
# for i in range(8):
#     plt.subplot(421+i)
#     ipromp.promps[i].plot(np.arange(0,1.01,0.01), color='g', legend="Prior of Joints");
# plt.figure(5)
# for i in range(7):
#     plt.subplot(711+i)
#     ipromp.promps[8+i].plot(np.arange(0,1.01,0.01), color='g', legend="Prior of Joints");
#
#
# # filter emg and joint data
# # test_set_emg_norm_filtered = signal.medfilt(test_set_emg_norm, [11,1])
# # test_set_emg_norm_filtered = test_set_emg_norm
# test_set_emg_norm_filtered = train_set_emg_norm14
# # test_set_joint_norm_filtered = signal.medfilt(test_set_joint_norm, [5,1])
# # test_set_joint_norm_filtered = test_set_joint_norm
# test_set_joint_norm_filtered = train_set_joint_norm14
# test_set_joint_norm_filtered_zero = np.zeros([101,7])
#
# # stack emg and joint data as a new matrix
# test_set_norm_filtered = np.hstack((test_set_emg_norm_filtered, test_set_joint_norm_filtered_zero))
#
# # add via point as observation
# ipromp.add_viapoint(0.00, test_set_norm_filtered[0,:], 250)
# ipromp.add_viapoint(0.02, test_set_norm_filtered[2,:], 250)
# ipromp.add_viapoint(0.04, test_set_norm_filtered[4,:], 250)
# ipromp.add_viapoint(0.06, test_set_norm_filtered[6,:], 250)
# ipromp.add_viapoint(0.08, test_set_norm_filtered[8,:], 250)
# ipromp.add_viapoint(0.18, test_set_norm_filtered[18,:], 250)
# ipromp.add_viapoint(0.28, test_set_norm_filtered[28,:], 250)
# ipromp.add_viapoint(0.40, test_set_norm_filtered[40,:], 250)
# ipromp.add_viapoint(0.50, test_set_norm_filtered[50,:], 250)
#
# # plot the updated distribution
# plt.figure(4)
# for i in range(8):
#     plt.subplot(421+i);
#     plt.plot(ipromp.x, test_set_emg_norm_filtered[:,i], color='r', linewidth=3, label="EMGs Ground True");
#     ipromp.promps[i].plot_updated(ipromp.x, color='b', legend="the updated distribution");
# plt.figure(5)
# for i in range(7):
#     plt.subplot(711+i);
#     plt.plot(ipromp.x, test_set_joint_norm_filtered[:,i], color='r', linewidth=3, label="Joints Ground True");
#     ipromp.promps[8+i].plot_updated(ipromp.x, color='b', via_show=False, legend="the updated distribution");
#
# ipromp.add_obs(t=0.00, obsy=test_set_norm_filtered[0,:], sigmay=250)
# ipromp.add_obs(t=0.08, obsy=test_set_norm_filtered[8,:], sigmay=250)
# prob = ipromp.prob_obs()
# print('the probability of observation based on the prior is ', prob)

plt.show()