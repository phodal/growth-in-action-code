from fabric.api import local

def test():
    local("./manage.py test test")
    # local("git add -p && git commit")
    # local("git push")
