#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}
run dex $HOME/.config/autostart/arcolinux-welcome-app.desktop
#run xrandr --output VGA-1 --primary --mode 1360x768 --pos 0x0 --rotate normal
#run xrandr --output HDMI2 --mode 1920x1080 --pos 1920x0 --rotate normal --output HDMI1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output VIRTUAL1 --off
#run caffeine
#run pamac-tray
run nm-applet
run variety
run xfce4-power-manager
run blueberry-tray
run /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1
run numlockx on
run volumeicon
feh --bg-fill /usr/share/backgrounds/arcolinux/arco-wallpaper.jpg &
run flameshot
run shutter --min_at_startup
#run nitrogen --restore
#run conky -c $HOME/.config/awesome/system-overview

#run applications from startup
#run dropbox
#run insync start
#run spotify
#run ckb-next -b

run telegram-desktop
run discord
run zoom
run skypeforlinux
run mailspring

run brave
