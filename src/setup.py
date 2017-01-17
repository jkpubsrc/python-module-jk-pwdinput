from setuptools import setup


def readme():
	with open('README.rst') as f:
		return f.read()


setup(name='jk_pwdinput',
	version='0.2017.1.17',
	description='Provides the capability to read a passwords from STDIN. In contrast to typical password input in this case for every character pressed an asterisk is displayed.',
	author='Jürgen Knauth',
	author_email='pubsrc@binary-overflow.de',
	license='Apache 2.0',
	url='https://github.com/jkpubsrc/python-module-jk-pwdinput',
	download_url='https://github.com/jkpubsrc/python-module-jk-pwdinput/tarball/0.2017.1.17',
	keywords=['password', 'security'],
	packages=['jk_pwdinput'],
	install_requires=[
		"readchar"
	],
	include_package_data=True,
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Programming Language :: Python :: 3.5',
		'License :: OSI Approved :: Apache Software License'
	],
	long_description=readme(),
	zip_safe=False)

