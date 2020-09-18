#!/bin/zsh

# First we copy files
cp ~/.vimrc ~/.profile ~/.Xresources .

cp ~/.bashrc ~/.bash_history ~/.bash_profile .
cp ~/.zshrc ~/.zshenv ~/.zsh_history .

cp -r ~/.bin .
cp ~/.conkyrc .
cp ~/.fehbg .
cp ~/.gitconfig .

# Copyng directories
mkdir .config

cp -r ~/.config/i3 .config 
cp -r ~/.config/{termite,alacritty} .config 
cp -r ~/.config/mimeapps.list* .config 
cp -r ~/.config/autostart .config
cp -r ~/.config/ranger .config 
mkdir -p .config/Code\ -\ OSS/User/
cp -r ~/.config/Code\ -\ OSS/User/snippets .config/Code\ -\ OSS/User/
cp ~/.config/Code\ -\ OSS/User/settings.json .config/Code\ -\ OSS/User/
cp -r ~/.config/nano .config
cp -r ~/.config/neofetch .config
cp -r ~/.config/rofi .config
cp -r ~/.config/polybar .config
cp -r ~/.config/broot .config
cp -r ~/.config/conky .config
cp -r ~/.config/obs-studio .config
cp -r ~/.config/pcmanfm .config
cp -r ~/.config/rclone-browser .config
cp -r ~/.config/variety .config

cp -r ~/.images .
cp -r ~/.screenlayout .
cp -r ~/.scripts .
cp -r ~/.files .
