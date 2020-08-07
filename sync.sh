# First we copy files
cp ~/.vimrc ~/.profile ~/.bashrc ~/.zshrc ~/.zsh_history ~/.bash_history ~/.bash_profile ~/.Xresources ~/.zhistory ~/.xinitrc ~/.Xauthority .


# Copyng directories
cp -r ~/.i3/ .
mkdir .config
cp -r ~/.config/{mimeapps.list,dmenu-recent,ranger} .config 
cp -r ~/.images .
cp -r ~/.screenlayout .
