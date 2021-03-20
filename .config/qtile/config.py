import os 
import re 
import socket 
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Click, Rule, Match 
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
# from libqtile.widget import Spacer 


###############################################################################
########                    Usefull function                         ##########
###############################################################################

@lazy.function
def window_to_prev_group(qtile):
  if qtile.currentWindow is not None:
    i = qtile.groups.index(qtile.currentGroup)
    qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
  if qtile.currentWindow is not None:
    i = qtile.groups.index(qtile.currentGroup)
    qtile.currentWindow.togroup(qtile.groups[i + 1].name)


###############################################################################
########                System and User Keybinding                   ##########
###############################################################################

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')


keys = [
  #############################################################################
  ########                     System Keybinding                     ##########
  #############################################################################

  # MULTIMEDIA KEYS
  # Increase/decrease brightness
  Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
  Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

  # Increase/decrease/mute volume
  Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
  Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
  Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

  Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
  Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
  Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
  Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

  # CHANGE FOCUS
  Key([mod], "k", lazy.layout.up()),
  Key([mod], "j", lazy.layout.down()),
  Key([mod], "h", lazy.layout.left()),
  Key([mod], "l", lazy.layout.right()),
  Key([mod], "Up", lazy.layout.up()),
  Key([mod], "Down", lazy.layout.down()),
  Key([mod], "Left", lazy.layout.left()),
  Key([mod], "Right", lazy.layout.right()),

  # RESIZE UP, DOWN, LEFT, RIGHT
  Key([mod, "control"], "l",
    lazy.layout.grow_right(),
    lazy.layout.grow(),
    lazy.layout.increase_ratio(),
    lazy.layout.delete(),
  ),
  Key([mod, "control"], "h",
    lazy.layout.grow_left(),
    lazy.layout.shrink(),
    lazy.layout.decrease_ratio(),
    lazy.layout.add(),
  ),
  Key([mod, "control"], "k",
    lazy.layout.grow_up(),
    lazy.layout.grow(),
    lazy.layout.decrease_nmaster(),
  ),
  Key([mod, "control"], "j",
    lazy.layout.grow_down(),
    lazy.layout.shrink(),
    lazy.layout.increase_nmaster(),
  ),

  # QTILE LAYOUT KEYS
  Key([mod], "n", lazy.layout.normalize()),
  Key([mod], "space", lazy.next_layout()),
  Key([mod], "f", lazy.window.toggle_fullscreen()),

  # Toggle floating layout
  Key([mod, "shift"], "space", lazy.window.toggle_floating()),

  # FLIP LAYOUT FOR MONADTALL/MONADWIDE
  Key([mod, "shift"], "f", lazy.layout.flip()),

  # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
  Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
  Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
  Key([mod, "shift"], "Left", lazy.layout.swap_left()),
  Key([mod, "shift"], "Right", lazy.layout.swap_right()),

  # FLIP LAYOUT FOR BSP
  Key([mod, "mod1"], "k", lazy.layout.flip_up()),
  Key([mod, "mod1"], "j", lazy.layout.flip_down()),
  Key([mod, "mod1"], "l", lazy.layout.flip_right()),
  Key([mod, "mod1"], "h", lazy.layout.flip_left()),

  # MOVE WINDOWS UP OR DOWN BSP LAYOUT
  Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
  Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
  Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
  Key([mod, "shift"], "l", lazy.layout.shuffle_right()),


  #############################################################################
  ########                       User Keybinding                     ##########
  #############################################################################

  Key([mod, "shift"], "r", lazy.restart()),
  Key([mod, "shift"], "e", lazy.spawn('arcolinux-logout')),

  Key([mod,"shift"], "q", lazy.window.kill()),
  Key([mod], "Escape", lazy.spawn('xkill')),

  Key([mod],"p", lazy.spawn('pavucontrol')),

  # Program laucher
  Key([mod], "F2", lazy.spawn('xfce4-appfinder')),
  Key([mod], "F3", lazy.spawn('morc_menu')),
  Key([mod,"mod1"], "d", lazy.spawn(home+'/.conf/i3/scripts/dmenu_run_history\
    -i -nb "#191919" -nf "#fea63c" -sb "#fea63c" -sf "#191919" \
    -fn "NotoMonoRegular:bold:pixelsize=14"')),

  Key([mod], "d", lazy.spawn('rofi -show run -font "Noto Sans 13"')),
  Key([mod,"shift"], "d", lazy.spawn('rofi -show window -font "Noto Sans 13"')),

  Key([mod], "Return", lazy.spawn('alacritty')),
  Key([mod], "w", lazy.spawn('brave')),
  Key([mod,"shift"], "w", lazy.spawn('firefox')),
  Key([mod], "o", lazy.spawn('dolphin')),
  Key([mod], "x", lazy.spawn('evince')),


  #############################################################################
  ########                       Screenshots                         ##########
  #############################################################################

  Key([mod], "c", lazy.spawn('flameshot gui')),
  #TODO:- Completar


  #############################################################################
  ########                       Screenlayout                        ##########
  #############################################################################

  Key([mod], "F9", lazy.spawn('/f/dev/scripts/screenlayout/extendedL.sh')),
  Key([mod], "F10", lazy.spawn('/f/dev/scripts/screenlayout/normal.sh')),
  Key([mod], "F11", lazy.spawn('/f/dev/scripts/screenlayout/zoom.sh')),
  Key([mod], "F12", lazy.spawn('/f/dev/scripts/screenlayout/extendedR.sh')),
]


###############################################################################
########                    WORKSPACES (or Groups)                   ##########
###############################################################################

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

group_labels = [" 1", " 2", "  3", " 4", " 5", 
  " 6", " 7", " 8", " 9", " 10",]

group_layouts = ["max", "monadtall", "max", "max", 
  "max", "max", "max", "max", "max", "max",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", 
#"matrix", "monadtall", "bsp", "monadtall", "monadtall",]

# Builiding initial layout for each workspace
# With the arrays define above
for i in range(len(group_names)):
  groups.append(
    Group(
      name=group_names[i],
      layout=group_layouts[i].lower(),
      label=group_labels[i],
    ))

# Defining keys for workspace movement
for i in groups:
  keys.extend([
    #CHANGE WORKSPACES
    Key([mod], i.name, lazy.group[i.name].toscreen()),

    # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
    #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
    Key([mod, "shift"], 
      i.name, lazy.window.togroup(i.name) , 
      lazy.group[i.name].toscreen()),
    Key([mod, "control"], 
      i.name, lazy.window.togroup(i.name)),
  ])

keys.extend([
  Key([mod,"mod1"], "l", lazy.screen.next_group()),
  Key([mod,"mod1"], "h", lazy.screen.prev_group()),
  Key([mod],"Tab",lazy.screen.toggle_group()),
  Key([mod],"z",lazy.next_layout()),
  Key([mod],"e",lazy.prev_layout()),
])


###############################################################################
########               User prefered layouts and theming             ##########
###############################################################################

def init_layout_theme():
  return {
    "margin":5,
    "border_width":2,
    "border_focus": "#5e81ac",
    "border_normal": "#4c566a"
  }

layout_theme = init_layout_theme()

layouts = [
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
    layout.MonadTall(
      margin=5, 
      border_width=2, 
      border_focus="#5e81ac", 
      border_normal="#4c566a"
    ),
    layout.MonadWide(
      margin=5, 
      border_width=2, 
      border_focus="#5e81ac", 
      border_normal="#4c566a"
    ),
    layout.Bsp(**layout_theme),
    layout.Stack(**layout_theme),
]

###############################################################################
########                    Mouse configuration                      ##########
###############################################################################

mouse = [
  Drag([mod], "Button1", 
    lazy.window.set_position_floating(),
    start=lazy.window.get_position()
  ),
  Drag([mod], "Button3", 
    lazy.window.set_size_floating(),
    start=lazy.window.get_size()
  )
]


###############################################################################
########                    Workspaces assigment                      ##########
###############################################################################

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
@hook.subscribe.client_new
def assign_app_group(client):
  d = {}
  #########################################################
  ################ assgin apps to groups ##################
  #########################################################
  d["1"] = ["Brave", "Brave-browser","brave", "brave-browser", ]
  d["2"] = ["termite"]
  d["3"] = ["Code-oss", "Code",  "code-oss", "code", ]
  d["4"] = ["okular",]
  d["5"] = ["VirtualBox Manager", "VirtualBox Machine", 
            "virtualbox manager", "virtualbox machine",
            ]
  d["6"] = ["dolphin",]
  d["7"] = ["Vlc","vlc", "Mpv", "mpv","zoom","Skype" ]
  d["8"] = ["",]
  d["9"] = ["TelegramDesktop","telegram-desktop","Telegram"
            "facebookmessenger-nativefier-7ab88e",
            "whatsapp-nativefier-d40211" ]
  d["0"] = ["Spotify","spotify","Spotify Free","draw.io","obs",]
  ##########################################################
  wm_class = client.window.get_wm_class()[0]

  for i in range(len(d)):
    if wm_class in list(d.values())[i]:
      group = list(d.keys())[i]
      client.togroup(group)
      client.group.cmd_toscreen()


main = None

@hook.subscribe.startup_once
def start_once():
  home = os.path.expanduser('~')
  subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
  # Set the cursor to something sane in X
  subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
  if (window.window.get_wm_transient_for()
    or window.window.get_wm_type() in floating_types):
    window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
  *layout.Floating.default_float_rules,
  Match(title='Confirmation'),  # tastyworks exit box
  Match(title='Qalculate!'),  # qalculate-gtk
  Match(wm_class= 'arcolinux-welcome-app.py'),
  Match(wm_class= 'arcolinux-tweak-tool.py'),
  Match(wm_class= 'confirm'),
  Match(wm_class= 'pavucontrol'),
  Match(wm_class= 'dialog'),
  Match(wm_class= 'download'),
  Match(wm_class= 'error'),
  Match(wm_class= 'file_progress'),
  Match(wm_class= 'notification'),
  Match(wm_class= 'splash'),
  Match(wm_class= 'toolbar'),
  Match(wm_class= 'confirmreset'),
  Match(wm_class= 'makebranch'),
  Match(wm_class= 'maketag'),
  Match(wm_class= 'arandr'),
  Match(wm_class= 'feh'),
  Match(wm_class= 'galculator'),
  Match(wm_class= 'arcolinux-logout'),
  Match(wm_class= 'xfce4-terminal'),
  Match(wm_class= 'ssh-askpass'),
  Match(wm_class= 'Xfce4-appfinder'),
  Match(wm_type= 'branchdialog'),
  Match(wm_type= 'open file'),
  Match(title= 'Save File',role='GtkFileChooserDialog'),
  Match(title= 'Select one or more files to open'),
  Match(role='GtkFileChooserDialog'),
  Match(title='Chat'),
  Match(wm_type= 'pinentry'),
# ],fullscreen_border_width = 0, border_width = 0)
],fullscreen_border_width = 0)

auto_fullscreen = True

# focus_on_window_activation = "focus" # or smart
focus_on_window_activation = "smart"

wmname = "LG3D"

###############################################################################
########                    Widget config for the BAR                ##########
###############################################################################

def init_colors():
  return [
    ["#2F343F", "#2F343F"], # color 0
    ["#2F343F", "#2F343F"], # color 1
    ["#c0c5ce", "#c0c5ce"], # color 2
    ["#fba922", "#fba922"], # color 3
    ["#3384d0", "#3384d0"], # color 4
    ["#f3f4f5", "#f3f4f5"], # color 5
    ["#cd1f3f", "#cd1f3f"], # color 6
    ["#62FF00", "#62FF00"], # color 7
    ["#6790eb", "#6790eb"], # color 8
    ["#a9a9a9", "#a9a9a9"], # color 9
  ] 


colors = init_colors()

def init_widgets_defaults():
  return dict(font="Noto Sans",
    fontsize = 11,
    padding = 2,
    background=colors[1]
  )

widget_defaults = init_widgets_defaults()

def init_widgets_list():
  prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
  widgets_list = [
    widget.GroupBox(
      font="FontAwesome",
      fontsize = 12,
      margin_y = -1,
      margin_x = 0,
      padding_y = 6,
      padding_x = 5,
      borderwidth = 0,
      disable_drag = True,
      active = colors[9],
      inactive = colors[5],
      rounded = False,
      highlight_method = "text",
      this_current_screen_border = colors[8],
      foreground = colors[2],
      background = colors[1]
    ),
  ]

wmname = "LG3D"

###############################################################################
########                    Widget config for the BAR                ##########
###############################################################################

def init_colors():
  return [
    ["#2F343F", "#2F343F"], # color 0
    ["#2F343F", "#2F343F"], # color 1
    ["#c0c5ce", "#c0c5ce"], # color 2
    ["#fba922", "#fba922"], # color 3
    ["#3384d0", "#3384d0"], # color 4
    ["#f3f4f5", "#f3f4f5"], # color 5
    ["#cd1f3f", "#cd1f3f"], # color 6
    ["#62FF00", "#62FF00"], # color 7
    ["#6790eb", "#6790eb"], # color 8
    ["#a9a9a9", "#a9a9a9"], # color 9
  ] 


colors = init_colors()

def init_widgets_defaults():
  return dict(font="Noto Sans",
    fontsize = 11,
    padding = 2,
    background=colors[1]
  )

widget_defaults = init_widgets_defaults()

def init_widgets_list():
  prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
  widgets_list = [
    widget.GroupBox(
      font="FontAwesome",
      fontsize = 12,
      margin_y = -1,
      margin_x = 0,
      padding_y = 6,
      padding_x = 5,
      borderwidth = 0,
      disable_drag = True,
      active = colors[9],
      inactive = colors[5],
      rounded = False,
      highlight_method = "text",
      this_current_screen_border = colors[8],
      foreground = colors[2],
      background = colors[1]
    ),
    widget.Sep(
      linewidth = 1,
      padding = 10,
      foreground = colors[2],
      background = colors[1]
    ),
    widget.CurrentLayout(
      font = "Noto Sans Bold",
      foreground = colors[5],
      background = colors[1]
    ),
    widget.Sep(
      linewidth = 1,
      padding = 10,
      foreground = colors[2],
      background = colors[1]
    ),
    # widget.WindowName(font="Noto Sans",
      # fontsize = 12,
      # foreground = colors[5],
      # background = colors[1],
    # ),
    # widget.Net(
      # font="Noto Sans",
      # fontsize=12,
      # interface="enp0s25",
      # foreground=colors[2],
      # background=colors[1],
      # padding = 0,
    # ),
    # widget.Sep(
    #          linewidth = 1,
    #          padding = 10,
    #          foreground = colors[2],
    #          background = colors[1]
    #          ),
    # widget.NetGraph(
    #          font="Noto Sans",
    #          fontsize=12,
    #          bandwidth="down",
    #          interface="auto",
    #          fill_color = colors[8],
    #          foreground=colors[2],
    #          background=colors[1],
    #          graph_color = colors[8],
    #          border_color = colors[2],
    #          padding = 0,
    #          border_width = 1,
    #          line_width = 1,
    #          ),
    # widget.Sep(
    #          linewidth = 1,
    #          padding = 10,
    #          foreground = colors[2],
    #          background = colors[1]
    #          ),
    # # do not activate in Virtualbox - will break qtile
    # widget.ThermalSensor(
    #          foreground = colors[5],
    #          foreground_alert = colors[6],
    #          background = colors[1],
    #          metric = True,
    #          padding = 3,
    #          threshold = 80
    #          ),
    # # battery option 1  ArcoLinux Horizontal icons do not forget to import arcobattery at the top
    # widget.Sep(
    #          linewidth = 1,
    #          padding = 10,
    #          foreground = colors[2],
    #          background = colors[1]
    #          ),
    # arcobattery.BatteryIcon(
    #          padding=0,
    #          scale=0.7,
    #          y_poss=2,
    #          theme_path=home + "/.config/qtile/icons/battery_icons_horiz",
    #          update_interval = 5,
    #          background = colors[1]
    #          ),
    # # battery option 2  from Qtile
    # widget.Sep(
    #          linewidth = 1,
    #          padding = 10,
    #          foreground = colors[2],
    #          background = colors[1]
    #          ),
    # widget.Battery(
    #          font="Noto Sans",
    #          update_interval = 10,
    #          fontsize = 12,
    #          foreground = colors[5],
    #          background = colors[1],
    #          ),
    widget.TaskList(
      font = "Noto Sans Bold",
      borderwidth = 1,
      margin = 3,
      padding = 4,
    ),
    widget.TextBox(
      font="FontAwesome",
      text="  ",
      foreground=colors[3],
      background=colors[1],
      padding = 0,
      fontsize=16
    ),
    widget.DF(
      warn_space=10, 
      measure='G', 
      format=' {p}:{uf}{m}',
      update_interval=60,
      visible_on_warn = False,
      foreground = colors[5],
      partition="/",
      background=colors[1],
    ),
    widget.TextBox(
      font="FontAwesome",
      text="  ",
      foreground=colors[4],
      background=colors[1],
      padding = 0,
      fontsize=16
    ),
    widget.DF(
      warn_space=10, 
      visible_on_warn = False,
      measure='G', 
      format=' {p}:{uf}{m}',
      update_interval=60,
      foreground = colors[5],
      partition="/f",
      background=colors[1],
    ),
    widget.Sep(
      linewidth = 1,
      padding = 10,
      foreground = colors[2],
      background = colors[1]
    ),
    widget.TextBox(
      font="FontAwesome",
      text=" ",
      foreground=colors[3],
      background=colors[1],
      padding = 0,
      fontsize=16
    ),
    widget.Volume(),
    widget.Sep(
      linewidth = 1,
      padding = 10,
      foreground = colors[2],
      background = colors[1]
    ),
    widget.TextBox(
      font="FontAwesome",
      text="  ",
      foreground=colors[6],
      background=colors[1],
      padding = 0,
      fontsize=16
    ),
    widget.CPU(
      format = '{load_percent}%'
    ),
    # widget.CPUGraph(
      # border_color = colors[2],
      # #fill_color = colors[1],
      # #graph_color = colors[5],
      # background= colors[1],
      # border_width = 1,
      # line_width = 1,
      # core = "all",
      # type = "box" 
    # ),
    widget.Sep(
      linewidth = 1,
      padding = 10,
      foreground = colors[2],
      background = colors[1]
    ),
    widget.TextBox(
      font="FontAwesome",
      text="  ",
      foreground=colors[4],
      background=colors[1],
      padding = 0,
      fontsize=16
    ),
    widget.Memory(
      font="Noto Sans",
      format = '{MemPercent}%',
      update_interval = 1,
      fontsize = 12,
      foreground = colors[5],
      background = colors[1],
    ),
    widget.Sep(
      linewidth = 1,
      padding = 10,
      foreground = colors[2],
      background = colors[1]
    ),
    widget.TextBox(
      font="FontAwesome",
      text="  ",
      foreground=colors[3],
      background=colors[1],
      padding = 0,
      fontsize=16
    ),
    widget.Clock(
      foreground = colors[5],
      background = colors[1],
      fontsize = 12,
      format="%Y-%m-%d %H:%M"
    ),
    widget.Sep(
      linewidth = 1,
      padding = 10,
      foreground = colors[2],
      background = colors[1]
    ),
    widget.Systray(
      background=colors[1],
      icon_size=20,
      padding = 4
    ),
  ]
  return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
  widgets_screen1 = init_widgets_list()
  return widgets_screen1

def init_widgets_screen2():
  widgets_screen2 = init_widgets_list()
  return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
  return [
    Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26)),
    Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26))
  ]

screens = init_screens()

def switch_screens():
  @lazy.function
  def __inner(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)
  return __inner

keys.extend([
  Key([mod],"comma",switch_screens()),
  Key([mod],"period",lazy.next_screen()),
])

