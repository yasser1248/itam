from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in itam/__init__.py
from itam import __version__ as version

setup(
	name="itam",
	version=version,
	description="IT Assets Management",
	author="IT Systematic",
	author_email="ahmeddesoky412@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
