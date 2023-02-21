from setuptools import setup, find_packages
import pathlib


HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text(encoding="utf8")

setup(
	name="PyTai",
	version="0.1",
	author="MagMigo",
	description="HMtai python port.",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/MagM1go/pytai",
	packages=find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3.10.0",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.7',
)