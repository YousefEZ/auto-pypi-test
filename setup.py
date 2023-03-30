from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Twine-Test',
    author="Yousef Zaher",
    author_email="syberprojects@gmail.com",
    url="https://github.com/YousefEZ/discord-qalib",
    version='0.0.1',
    description='A twine upload test',
    packages=find_packages(exclude=("test*",)),
    license='MIT',
    python_requires='>=3.8.0',
    install_requires=requirements,
)