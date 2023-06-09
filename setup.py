from setuptools import find_packages, setup

setup(
    name='Twine-Test',
    author="Yousef Zaher",
    author_email="syberprojects@gmail.com",
    long_description=open('README.md').read(),
    url="https://github.com/YousefEZ/twine-test",
    version="3.2.0",
    description='A twine upload test',
    packages=find_packages(exclude=("test*",)),
    license='MIT',
    python_requires='>=3.8.0',
    install_requires=[],
)