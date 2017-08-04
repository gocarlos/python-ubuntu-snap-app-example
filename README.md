# python-ubuntu-snap-app-example

Example of a very simple python app packaged as snap app

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
If you like it clone/share/start it and do a great app :)
