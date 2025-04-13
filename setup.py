
from setuptools import setup, find_packages

setup(
    name="opencv_django_demo",
    version="0.1",
    packages=find_packages(),
    install_requires=["opencv-python", "numpy"],
    author="OpenCV Django Demo",
    description="Demo paket za detekciju ljudi uz pomoć OpenCV i integraciju s Django projektom.",
)
