"""
setup module
"""

from distutils.core import setup

# TEMPLATE
setup(
    name='maddendeavor-website',
    version='0.0',
    description='website for my business Maddendeavor, LLC',
    long_description=open('README.rst').read(),
    author='Christine Madden',
    license=open('LICENSE').read(),
    author_email='info@maddendeavor.com',
    packages=['maddendeavor_website'],
    install_requires=[
        "flask",
    ],
    entry_points={
        'console_scripts':
        [
            'maddendeavor_website = maddendeavor_website.__main__:main',
        ]
    }
)
