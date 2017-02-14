from setuptools import setup

setup(name='trello_connect',
      version='0.3',
      description='Dump trello board to the console.',
      author='Derek Jensen',
      author_email='derek@dpjensen.net',
      packages=['trello_connect'],
      scripts=['bin/trelloDump'],
        install_requires=[
            'toml',
            'certifi'
      ],
      zip_safe=True)
