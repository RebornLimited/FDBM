import setuptools
with open(r'E:\Alex\Python\DatabaseMaster\PyPi\README.md', 'r', encoding='utf-8') as fh:
	long_description = fh.read()

setuptools.setup(
	name='FastDBM',
	version='1.0.3',
	author='Reborn',
	author_email='mixamo2354@gmail.com',
	description='Manage your database in two lines of code.',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/RebornLimited/FastDBM',
	packages=['fastdbm'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)