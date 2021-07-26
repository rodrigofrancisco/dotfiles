#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#Set your native resolution IF it does not exist in xrandr
#More info in the script
#run $HOME/.config/qtile/scripts/set-screen-resolution-in-virtualbox.sh

#Find out your monitor name with xrandr or arandr (save and you get this line)
#xrandr --output eDP1 --primary --mode 1920x1080 --pos 0x0 --rotate normal
/f/dev/scripts/screenlayout/normal.sh &

#change your keyboard if you need it
#setxkbmap -layout be

#autostart ArcoLinux Welcome App
run dex $HOME/.config/autostart/arcolinux-welcome-app.desktop &

#Some ways to set your wallpaper besides variety or nitrogen
#feh --bg-fill /usr/share/backgrounds/arcolinux/arco-wallpaper.jpg &
nitrogen --restore &
#start the conky to learn the shortcuts
#(conky -c $HOME/.config/qtile/scripts/system-overview) &

#start sxhkd to replace Qtile native key-bindings
#run sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &


#starting utility applications at boot time
#run pamac-tray &
#picom --config $HOME/.config/qtile/scripts/picom.conf &
#run variety &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
numlockx on &
run nm-applet &
run xfce4-power-manager &
blueberry-tray &
run volumeicon &

#starting user applications at boot time
#nitrogen --restore &
#run caffeine -a &
#run vivaldi-stable &
#run firefox &
#run thunar &
#run dropbox &
#run insync start &
#run spotify &
#run atom &
#run shutter --min_at_startup &
#run flameshot &

#run telegram-desktop &
#run discord &
#run zoom &
#run skypeforlinux &

#run brave &
