from setuptools import setup

setup(
    name='neon-fake-ua',

    version='1.0.0',

    description='Use a random User-Agent provided by fake-useragent '
                'for every request unless playwright is active',
    long_description=open('README.rst').read(),

    keywords='scrapy proxy user-agent web-scraping',
    license='MIT License',

    author='Alexander Afanasyev',
    author_email='me@alecxe.me',
    maintainer='Jayden Edara',
    maintainer_email='aedara@uw.edu',

    url='https://github.com/alecxe/neon-fake-ua',
    python_requires=">=3.5",

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Scrapy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        'Topic :: Internet :: WWW/HTTP',
    ],
    packages=[
        'neon_fake_ua',
    ],
    install_requires=[
        'fake-useragent',
        'faker'
    ],
)
