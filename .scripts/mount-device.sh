# Author: rhodfra@gmail.com
# Date: June 18, 2021
# Desc: Simple script to mount usb
action=${1:-"mount"} # Other action is: umount
id=${2:-"sdc1"}

case $action in
  "mount")
    echo "MOUNTING device"
    udisksctl mount -b "/dev/${id}"
    sudo systemctl start smb
  ;;
  "umount")
    echo "UMOUNTING device"
    sudo systemctl stop smb
    udisksctl unmount -b "/dev/${id}"
  ;;
  *)
    echo "Wrong option, bye"
    exit 1
  ;;
esac
