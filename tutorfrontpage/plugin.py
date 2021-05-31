from glob import glob
import os
import pkg_resources

from .__about__ import __version__

templates = pkg_resources.resource_filename(
    "tutorfrontpage", "templates"
)

config = {
    "add": {
        "SECRET_KEY": "{{ 24|random_string }}",
    },
# Django application need this configurations
# After installation of plugin, run:
# "tutor config save --set frontpage_HOST=frontpage.{{LMS_HOST}}" and the others
    "defaults": {
        "HOST": "frontpage.{{ LMS_HOST }}",
        "DOCKER_REGISTRY": "{{ DOCKER_REGISTRY }}",
        "DOCKER_IMAGE": "muratp/frontpage",
        "MYSQL_HOST": "mysql",
        "MYSQL_PORT": 3306,
        "MYSQL_DATABASE": "frontpage",
        "MYSQL_USERNAME": "frontpage",
        "MYSQL_PASSWORD": "frontpage"
    }

}

hooks = {

     "init": ["mysql","lms","frontpage"],   
# Pull and build docker containers
    "build-image": {"frontpage": "muratp/frontpage"},
    "remote-image": {"frontpage": "muratp/frontpage"},
# Initial all services
    
}

def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename(
        "tutorfrontpage", "patches"
    )
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
