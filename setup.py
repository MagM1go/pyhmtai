from setuptools import setup, find_packages
import pathlib


HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text(encoding="utf8")

setup(
	name="pyhmtai",
	version="0.1.6",
	author="MagMigo",
	description="HMtai python port.",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/MagM1go/pyhmtai",
	packages=find_packages(),
	python_requires='>=3.7',
)