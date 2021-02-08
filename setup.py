from setuptools import setup


setup(name='filecompare',
      version='0.1',
      description='A package for comparing text and JSON files.',
      url='https://git.ccfe.ac.uk/FISPACT-II/filecompare',
      author='UKAEA',
      author_email='thomas.stainer@ukaea.uk',
      license='',
      packages=[
            'filecompare',
            'filecompare.compare',
            'filecompare.tools',
            'filecompare.utils'
      ],
      install_requires=[],
      python_requires='>=3',
      scripts=['filecompare/tools/docompare.py'],
      setup_requires=['pytest-runner'],
      test_suite='tests.testsuite',
      tests_require=['pytest'],
      zip_safe=False)
