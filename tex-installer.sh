#! /bin/bash

#remember to change the permissions of this file to be executable
#with the command `chmod 744 tex-installer.sh` to allow the file to be ran

#this updates your distro packages to the most recent version.
#Depending on how long ago this has been ran, it could potentially
#take a while, so edit this out if this is time sensitive
sudo apt update
sudo apt upgrade -y

#this command installs LaTeX. it will take a while to run, it's a big package
sudo apt install texlive-full -y

#this installs emacs. If you don't want a dedicated LaTeX editor,
#emacs will keep you covered. To install an emacs TeX extension,
#launch emacs and press alt-x, go to the package auctex, select it with i,
#and press x to install
sudo apt install emacs -y

#this installs a LaTeX editor. It's the only one I've looked at,
#but I will include other packages in the comments below. Just replace
#texmaker for which ever package you choose 
sudo apt install texmaker -y

#other options include:
#lyx texstudio gummi texpen texworks kile ktikz latexila

#this is how to launch texmaker from the terminal
texmaker
