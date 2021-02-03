#!/bin/bash
if pgrep -x "picom" > /dev/null
then
	killall picom
else
	#picom -b --config ~/.config/awesome/picom.conf
  # Trying picom fork from jonaburg
  picom --config ~/.config/i3/picom-jonaburg.conf
fi
