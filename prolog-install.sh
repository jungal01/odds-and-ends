#!/bin/bash
# I wrote this solely to install prolog for my programming languages class.
# this will only work on linux distros based on ubuntu/debian
sudo apt -add-repository ppa:swi-prolog/stable
sudo apt update
sudo apt install swi-prolog
