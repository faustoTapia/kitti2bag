#!/usr/bin/env python

from setuptools import setup

setup(
    name='kitti2bag',
    version='1.5',
    description='Convert KITTI dataset to ROS bag file the easy way!',
    author='Tomas Krejci',
    author_email='tomas@krej.ci',
    url='https://github.com/faustoTapia/kitti2bag.git@bug_fix_odom_p',
    download_url = 'https://github.com/faustoTapia/kitti2bag/archive/1.5.zip',
    keywords = ['dataset', 'ros', 'rosbag', 'kitti'],
    entry_points = {
        'console_scripts': ['kitti2bag=kitti2bag.__main__:main'],
    },
    install_requires=['pykitti', 'progressbar2']
)
