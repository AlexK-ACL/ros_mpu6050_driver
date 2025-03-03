#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['mpu6050_driver_py'],
    scripts=['scripts/imu_node.py'],
    package_dir={'': 'src'},
    install_requires=['rospkg'],
    )

setup(**d)
