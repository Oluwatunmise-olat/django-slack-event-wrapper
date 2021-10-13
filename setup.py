from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: Unix',
    'Operating System :: MacOS :: MacOS X',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='django_slack_event_wrapper',
    version='0.1.12',
    description='This is a django wrapper to handle slack events and slash commands.',
    author='Oluwatunmise Olatunbosun',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    url='',
    author_email='oluwatunmiseolatunbosun2001@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['slack', 'slack events', 'django',
              'slack django wrapper', 'event', 'slack django events'],
    packages=find_packages(),
    install_requires=[
        'aiohttp>=3.7.4.post0',
        'asgiref>=3.4.1',
        'async-timeout==3.0.1',
        'attrs>=21.2.0',
        'chardet>=4.0.0',
        'Django>=3.2.8',
        'django-rest-framework>=0.1.0',
        'djangorestframework>=3.12.4',
        'idna>=3.2',
        'multidict>=5.2.0',
        'python-dotenv>=0.19.1',
        'pytz>=2021.3',
        'sqlparse>=0.4.2',
        'typing-extensions>=3.10.0.2',
        'yarl>=1.7.0'
    ]
)
