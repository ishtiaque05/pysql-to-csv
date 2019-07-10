#!usr/bin/python
from setuptools import setup, find_packages
setup(
		name='sql-to-csv',
		description='An application for converting sql to csv',
		version='0.10',
		packages=find_packages(),
		python_requires='>=3.6',
		test_suite="tests",
		entry_points={
			'console_scripts': [
				'pysql-to-csv=pysql_to_csv:runner',
				'dump-to-csv=mysqldump_to_csv:runner'
			]
		}
	)


