# coding:utf-8
"""
    blog 文章发布
"""
from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd,lcd,env
from fabric.contrib.console import confirm

# TODO
# 需要配置服务器 host password 路径等
#
env.hosts = ['sp.lfate.com',]
env.user = 'root'
env.password = "~/.ssh/id_rsa.pub"

def add(filename):
    """
        git add {filename}
    """
    with settings(warn_only=True):
        command = "git add {filename}".format(filename=filename)
        local(command)


def commit(message):
    """
        git commit -m {message}
    """
    with settings(warn_only=True):
        command = "git commit -m '{message}'".format(message=message)
        local(command)


def lpush(remote='origin', branch='master', filename="./*", message="update"):
    """
         上传
        add(filename)
        commit(message)
        git push remote branch
    """
    with settings(warn_only=True):
        add(filename)
        commit(message)
        command = "git push {remote} {branch}".format(
            remote=remote, branch=branch)
        local(command)


def preview():
    """
        预览
        cd lfate.com
        hugo
    """
    with settings(warn_only=True):
        with lcd('../lfate.com/'):
            command = "hugo --config local_config.toml"
            local(command)


def public():
    """
        发布
        cd hucher.com
        git pull
        hugo
    """
    with settings(warn_only=True):
        with cd('/workspace/lfate/lfate.com/'):
            run("git pull")
            run("rm -rf public")
            run("hugo ")


def new(filename):
    """
        新建文档
        cd hucher.com
        hugo new {filename}
        macdown {filename}
    """
    with lcd('../lfate.com/'):
        local('pwd')
        new = "hugo new {filename}".format(filename=filename)
        # 需要安装macdown 编辑器
        _open = "subl content/{filename}".format(filename=filename)
        local(new)
        local(_open)


def deploy(host="localhost"):
    """
        配置nginx 服务
    """
    pass
