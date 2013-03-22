# -*-coding: UTF-8 -*-
# Run these commands with fab

import os
from fabric.api import local, settings, abort, run, cd, env, sudo, prefix
from fabric.contrib.console import confirm
from fabric.contrib.files import exists, put

import logging
logging.basicConfig(level=logging.WARN)

env.hosts = ['texturejam@spreadsite.org']

def update_requirements():
    local("pip freeze | egrep -v 'Fabric|pycrypto|ssh' > REQUIREMENTS")

def update_patches_pack():
    local('cp -p ../texturepacker/minecraft/maps/* .')
    local('script/mkpatchrx')
    local('maketexture patches.tprx')

def create_test_pack():
    local('script/mkrecipe --local')
    local('maketexture --out=foo/PixelCraftVr11+Patches.zip base=file://foo/PixelCraftVr11.zip rx/upgrade-release-13.tprx')
    local('cp foo/PixelCraftVr11+Patches.zip ~/Library/Application\\ Support/minecraft/texturepacks')

def create_production_recipes():
    with open('VERSION', 'r') as strm:
        n = int(strm.read())
    with open('VERSION', 'w') as strm:
        strm.write('%03d' % (n + 1))
    local('script/mkrecipe')

def deploy_patches_pack():
    put('patches.zip', 'static/texturepacks')

def deploy_recipes():
    with cd('data/textureupdater'):
        run('git pull')
    with prefix('. ~/virtualenvs/texturejam/bin/activate'):
        with cd('Sites/texturejam'):
            run('./manage.py updatespecs ~/data/textureupdater/rx')

def deploy():
    update_patches_pack()
    deploy_patches_pack()
    create_production_recipes()
    deploy_recipes()
