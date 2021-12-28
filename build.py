#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init
import datetime
use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.distutils")
name = "hello"
default_task = "publish"
version = datetime.datetime.now().strftime('%Y%m%d%H%M')
@init
def set_properties(project):
    project.set_property("publish_command", f"rm -rf target/dist/cicd; cp -r target/dist/cicd-{version} target/dist/cicd;")
