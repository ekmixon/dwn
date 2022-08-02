import os

from setuptools import setup, find_packages

from dwn import __version__


def _package_files(directory: str, suffix: str = None) -> list:
    """
        Get all of the file paths in the directory specified by suffix.
        :param directory:
        :return:
    """

    paths = []

    for (path, directories, filenames) in os.walk(directory):
        paths.extend(
            os.path.join('..', path, filename)
            for filename in filenames
            if suffix is not None
            and filename.endswith(suffix)
            or suffix is None
        )

    return paths


# here - where we are.
here = os.path.abspath(os.path.dirname(__file__))

# read the package requirements for install_requires
with open(os.path.join(here, 'requirements.txt'), 'r') as f:
    requirements = f.readlines()

# setup!
setup(
    name='dwn',
    author='Leon Jacobs',
    author_email='leon@sensepost.com',
    description='dwn, a docker pwn tool manager',
    license='GPL v3',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    url='https://github.com/sensepost/dwn',
    download_url=f'https://github.com/sensepost/dwn/archive/{__version__}.tar.gz',
    keywords=['docker', 'tool', 'pentest', 'framework'],
    version=__version__,
    package_data={
        '': _package_files(os.path.join(here, 'dwn/assets'))
        + _package_files(os.path.join(here, 'plans/'))
    },
    classifiers=[
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
    ],
    entry_points={
        'console_scripts': [
            'dwn = dwn.cli.cli:cli',
        ],
    },
)
