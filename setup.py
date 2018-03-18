#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages

#import Lib
import LogsPSA
 
setup(
 
    #Lib name
    name='LogsPSA',
 
    # version
    version=LogsPSA.__version__,
 
   # Find all requested packages
    packages=find_packages(),
 
    #author name
    author="Thomas GRYSPEERDT",
 
    #author e-amil
    author_email="gryspeerdt.thomas@gmail.com",
 
    #short description
    description="Custom logs store object",
 
    #long description
    long_description=open('README.md').read(),
 
    # Vous pouvez rajouter une liste de dépendances pour votre lib
    # et même préciser une version. A l'installation, Python essayera de
    # les télécharger et les installer.
    #
    # Ex: ["gunicorn", "docutils >= 0.3", "lxml==0.5a7"]
    #
    # Dans notre cas on en a pas besoin, donc je le commente, mais je le
    # laisse pour que vous sachiez que ça existe car c'est très utile.
    # install_requires= ,
 
    # Active la prise en compte du fichier MANIFEST.in
    include_package_data=True,
 
    # github url
    url='https://github.com/Thomasgry/LogsPSA',
 
    # Metadatas
    classifiers=[
        "Programming Language :: Python",
        "License :: MIT Licence",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Topic :: Logging",
    ],
	#~ #entry point
    #~ entry_points = {
        #~ 'console_scripts': [
            #~ 'LogsPSA = sm_lib.core:proclamer',
            #~ 'LogsPSA = LogsPSA.LogPSA:proclamer',
        #~ ],
    #~ },
 
)
