# First we copy files
cp ~/.vimrc ~/.profile ~/.bashrc ~/.zshrc ~/.zsh_history ~/.bash_history ~/.bash_profile ~/.Xresources ~/.zhistory .xinitrc .Xauthority .


# Copyng directories
cp -r ~/.i3/ .
mkdir .config
cp -r ~/.config/{i3,mimeapps.list,dmenu-recent} .config 
cp -r ~/.images .
