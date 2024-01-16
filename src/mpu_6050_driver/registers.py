PWR_MGMT_1   = 0x6B
PWR_MGMT_2   = 0x6C
SMPRT_DIV    = 0x19 # Register 25 – Sample Rate Divider SMPRT_DIV
# Sample Rate = Gyroscope Output Rate / (1 + SMPLRT_DIV)
CONFIG       = 0x1A # Register 26 – Configuration - This register configures the external Frame Synchronization (FSYNC) EXT_SYNC_SET pin sampling 
# and the Digital Low Pass Filter (DLPF) DLPF_CFG setting for both the gyroscopes and accelerometers.

GYRO_CONFIG  = 0x1B # Register 27 – Gyroscope Configuration - used to trigger gyroscope self-test and configure the gyroscopes’ full scale range
 # 24 bits 3-4 -> bin 11 FS_SEL=3 range +-2000 ; bin 10 ->2 range +-1000 ; bin 01 ->1 range +-500 ; bin 00 ->0  range +-250
ACCEL_CONFIG = 0x1C # Register 28 – Accelerometer Configuration
 # Same as for gyro: 3 +-16g ; 2 +-8g ; 1 +-4g ; 0 +- 2g
INT_ENABLE   = 0x38

ACCEL_XOUT_H = 0x3B
ACCEL_XOUT_L = 0x3C
ACCEL_YOUT_H = 0x3D
ACCEL_YOUT_L = 0x3E
ACCEL_ZOUT_H = 0x3F
ACCEL_ZOUT_L = 0x40


GYRO_XOUT_H = 0x43
GYRO_XOUT_L = 0x44
GYRO_YOUT_H = 0x45
GYRO_YOUT_L = 0x46
GYRO_ZOUT_H = 0x47
GYRO_ZOUT_L = 0x48

TEMP_H = 0x41
TEMP_L = 0x42
