from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'sb3 vanilla rnn version'
LONG_DESCRIPTION = 'Stable Baseline 3 with vanilla RNN support from Torch.'

# Setting up
setup(
    name="sb3_rnn",
    version=VERSION,
    author="Matin Yousefabadi",
    author_email="<mtnusf97@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['stable-baselines3[extra]', 'sb3-contrib'],
    keywords=['python', 'rnn', 'RL'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)