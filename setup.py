from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='UUU',
    version='0.0.1',
    description='A small collection of general utility functions I hack together and use.',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='BSD License',
    readme = readme,
    packages=find_packages(include=['UwU']),
    author='Bela Tristan Leander Vogler',
    author_email='bela.vogler@uni-jena.de',
    keywords=['Utility', 'Functions', 'Miscellaneous', 'Windowing', 'QR Codes'],
    classifiers=[
    "Development Status :: 3 - Alpha",

    "Intended Audience :: Science/Research",
    "Topic :: Scientific/Engineering :: Bio-Informatics",

    "License :: OSI Approved :: BSD License",

    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    ],
    install_requires=['numpy', 'plotly', 'pandas', 'qrcode'],
    python_requires='>=3',
    url='https://github.com/Eggeling-Lab-Microscope-Software/utterly_useless_utilities'
)