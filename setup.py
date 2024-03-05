import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="captchasolver",
    version="0.1.0",
    description="A simple CAPTCHA solver utility package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wuihee/captchasolver",
    author="Wuihee",
    author_email="wuihee@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    license="MIT",
    install_requires=["tensorflow", "opencv-python"],
    extras_requires={"dev": ["pytest"]},
)
