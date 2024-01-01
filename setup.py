from setuptools import find_packages, setup

setup(
    name="captchasolver",
    version="0.1.0",
    description="A simple CAPTCHA solver utility package.",
    author="Wuihee",
    author_email="wuihee@gmail.com",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "tensorflow",
        "opencv-python",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
