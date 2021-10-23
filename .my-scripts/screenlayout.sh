#!/usr/bin/env sh
#Author: Rodrigo Francisco
#Description: Diplay screenlayout selector
#Date: 22/10/2021

position=${1:-left-of} # left-of | right-of | above | below | normal(just main mon)

# Checks if option is valid
if [[ "${position}" != "left-of" && "$position" != "normal" && "${position}" != "right-of" 
  && "${position}" != "above" && "${position}" != "below" ]]; then
  echo "Invalid option"
  exit 400
fi

primary=$(xrandr --query | grep " primary" | cut -d" " -f1)
secondaries=$(xrandr --query | grep " connected" | grep -v "primary" | cut -d" " -f1)
monitors="${primary[*]} ${secondaries[*]}"

layout="xrandr"

# Turns off all secondary monitor and the primary remains
if [ "${position}" == "normal" ]; then
  for secondary in $secondaries; do
    layout="xrandr --output ${secondary} --off"
    echo "Exec: ${layout}"
    $layout;
  done
  exit
fi

# Sets primary and secondary monitor
# At the moment only considers all monitors are set to the left. 
# This will be fix as needed in the future
for monitor in $monitors; do
  resolution=$(xrandr | grep ${monitor} -A 1 | tail -1 | awk '{print $1}')
  mon_conf="--output ${monitor} --mode ${resolution}"

  if [ "${monitor}" != "${primary}" ]; then
    mon_conf="${mon_conf} --${position} ${primary}"
  fi
  layout="${layout} ${mon_conf}";
done;
echo "Exec: ${layout}"
$layout
