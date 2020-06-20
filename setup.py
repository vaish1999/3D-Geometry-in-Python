from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname("__file__"))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = '3dg',         
  packages = ['3dg'],   
  version = '0.1',      
  license='GPL 2.0',        
  description = 'Explore 3D geometry in python over here!',   
  author = 'Vaishakh Nargund',                  
  author_email = 'vaishakh.nargund1999@gmail.com', 
  long_description=long_description,
  long_description_content_type="text/markdown",     
  url = 'https://github.com/vaish1999/3D-Geometry-in-Python',  
  download_url = 'https://github.com/vaish1999/Calculus-in-python/archive/v1.4.tar.gz',   
  keywords = ['3d', 'geometry', 'line','plane','distance'],   
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
