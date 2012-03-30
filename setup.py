from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='datastore-client',
      version=version,
      description="Python client for CKAN DataStore and ElasticSearch",
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Database"],
      keywords='datastore rest api tables csv json',
      author='Open Knowledge Foundation',
      author_email='info@okfn.org',
      url='http://okfn.org',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      ],
      entry_points="""
      """,
      )
