
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='qctrl-open-controls',
    version='1.2.1',
    description='Q-CTRL Open Controls',
    python_requires='>=3.7.3',
    project_urls={'repository': 'https://github.com/qctrl/python-open-controls'},
    author='Q-CTRL',
    author_email='support@q-ctrl.com',
    license='Apache-2.0',
    keywords='quantum computing open source engineering',
    classifiers=['Development Status :: 5 - Production/Stable', 'Environment :: Console', 'Intended Audience :: Developers', 'Intended Audience :: Education', 'Intended Audience :: Science/Research', 'License :: OSI Approved :: Apache Software License', 'Natural Language :: English', 'Operating System :: OS Independent', 'Programming Language :: Python :: 3.6', 'Topic :: Scientific/Engineering :: Physics', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Embedded Systems', 'Topic :: System :: Distributed Computing'],
    packages=['qctrlopencontrols', 'qctrlopencontrols.base', 'qctrlopencontrols.cirq', 'qctrlopencontrols.driven_controls', 'qctrlopencontrols.dynamic_decoupling_sequences', 'qctrlopencontrols.exceptions', 'qctrlopencontrols.globals', 'qctrlopencontrols.pyquil', 'qctrlopencontrols.qiskit'],
    package_data={},
    install_requires=['cirq==0.*,>=0.5.0', 'numpy==1.*,>=1.16.0', 'pyquil==2.*,>=2.9.0', 'qiskit-ibmq-provider==0.*,>=0.2.2', 'qiskit-terra==0.*,>=0.8.1', 'scipy==1.*,>=1.3.0'],
    extras_require={'dev': ['pylama', 'pylint', 'pylint-runner', 'pytest']},
)
