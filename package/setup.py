from setuptools import setup
import streamsx.geospatial
setup(
  name = 'streamsx.geospatial',
  packages = ['streamsx.geospatial'],
  include_package_data=True,
  version = streamsx.geospatial.__version__,
  description = 'Geospatial integration for IBM Streams',
  long_description = open('DESC.txt').read(),
  author = 'IBM Streams @ github.com',
  author_email = 'hegermar@de.ibm.com',
  license='Apache License - Version 2.0',
  url = 'https://github.com/IBMStreams/pypi.streamsx.geospatial',
  keywords = ['streams', 'ibmstreams', 'streaming', 'analytics', 'streaming-analytics', 'geospatial'],
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
  install_requires=['streamsx>=1.14.6'],
  
  test_suite='nose.collector',
  tests_require=['nose']
)
