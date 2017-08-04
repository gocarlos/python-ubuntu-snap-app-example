# python-ubuntu-snap-app-example

Example of a very simple python app packaged as snap app

[![Build Status](https://travis-ci.org/gocarlos/python-ubuntu-snap-app-example.svg?branch=master)](https://travis-ci.org/gocarlos/python-ubuntu-snap-app-example)

[![Snap Status](https://build.snapcraft.io/badge/gocarlos/python-ubuntu-snap-app-example.svg)](https://build.snapcraft.io/user/gocarlos/python-ubuntu-snap-app-example)

## snap build instructions

``` bash
# clone app
git clone git@github.com:gocarlos/python-ubuntu-snap-app-example.git
cd python-ubuntu-snap-app-example
# build app
snapcraft
# install app
sudo snap install mygreatapp_1.0_amd64.snap --devmode
# run the app, or search for mygreatapp, it should show a python icon.
mygreatapp
```
If you like it clone/share/star it and do a great app :)



PS: you can also install it by tipping:
```bash
sudo snap install mygreatapp --edge --devmode
```
