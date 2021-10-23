#!/usr/bin/env sh
#Author: Rodrigo Francisco
#Description: Diplay screenlayout selector
#Date: 22/10/2021

position=${1:-left-of} # left-of | right-of | above | below | duplicate | normal(just main mon)
resolution_dup=${2} # Required if $position=duplicate

# Checks if option is valid
if [[ "$position" != "normal" && "${position}" != "duplicate" && "${position}" != "left-of" && "
  ${position}" != "right-of" && "${position}" != "above" && "${position}" != "below" ]]; then
  echo "Invalid option"
  exit 400
fi

if [ "${position}" == "duplicate" ] && [ -z "${resolution_dup}" ]; then
  echo "Resolution needed"
  exit 400
fi

primary=$(xrandr --query | grep " primary" | cut -d" " -f1)
secondaries=$(xrandr --query | grep " connected" | grep -v "primary" | cut -d" " -f1)
monitors="${primary[*]} ${secondaries[*]}"

layout="xrandr"

case $position in
  "normal")
    # Turns off all secondary monitor and the primary remains
    for secondary in $secondaries; do
      layout="xrandr --output ${secondary} --off"
      echo "Exec: ${layout}"
      $layout;
    done
    exit
    ;;
  "duplicate")
    resolution_main=$(xrandr | grep \* | awk '{print $1}' | head -1)
    resolution_main_array=(`echo $resolution_main | tr 'x' ' '`)
    x_main=${resolution_main_array[0]}
    y_main=${resolution_main_array[1]}

    resolution_dup_array=(`echo $resolution_dup | tr 'x' ' '`)
    x_dup=${resolution_dup_array[0]}
    y_dup=${resolution_dup_array[1]}

    scale_x=$(echo "scale=2 ; $x_main / $x_dup" | bc)
    scale_y=$(echo "scale=2 ; $y_main / $y_dup" | bc)
    for secondary in $secondaries; do
      layout="xrandr --output ${secondary} --mode ${resolution_dup} --same-as ${primary} --scale ${scale_x}x${scale_y}"
      echo "Exec: ${layout}"
      $layout;
    done

    ;;
  *)
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
    ;;
esac



