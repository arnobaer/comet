from setuptools import setup, find_packages

setup(
    name='comet',
    version='0.1.0',
    author="Bernhard Arnold",
    author_email="bernhard.arnold@oeaw.ac.at",
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'PyVISA',
        'PyVISA-py',
        'PyVISA-sim',
        'Pint>=0.9',
        'PyQt5',
        'PyQt5-sip',
        'pyqtgraph',
    ],
    package_data={
        'comet': [
            'assets/icons/*.svg',
            'widgets/*.ui',
        ],
    },
    test_suite='tests',
    license="GPLv3",
)
