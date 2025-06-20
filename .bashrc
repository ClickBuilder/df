date +%d\|%m\|%y,\ %H:%M:%S
# If not running interactively, don't do anything
[[ $- != *i* ]] && return
alias \
	virc='nvim ~/.bashrc'\
	qute='qutebrowser'\
	vih='nvim ~/.config/hypr/hyprland.conf'\
	ls='ls --color=auto' \
	grep='grep --color=auto' \
    ..='cd ..' \
	vicfg='nvim ~/.config/nvim/init.lua' \
	vi='nvim' \
	upd='sudo pacman -Syu' \
	get='sudo pacman -S' \
	exercism='~/bin/exercism' \
	es='exercism submit *.sh' \
	gits='git status --untracked-files=no' \
	dm='~/scripts/dm.sh' \
	ms='~/scripts/ms.sh' \
    sm="sudo -E ~/scripts/sm.sh" \
    smcfg="nvim ~/.config/scripts/systemManagementOptions.conf" \
    vis="sudo -E nvim" \
    vic="nvim ~/.config/nvim/init.lua" \
    cdnvim="cd /home/ikillmylinux/.config/nvim/" \
    gety="yay -S" \
    ref="sudo reflector --latest 20 --sort rate --save /etc/pacman.d/mirrorlist && sudo pacman -Syu" \
    cal="export LC_TIME=ru_RU.UTF-8 && cal -3 && unset LC_TIME" \
    wip="cd $HOME/scripts/wip && nvim main.sh" \
    wkill="hyprctl kill" \
    gm="$HOME/scripts/gm.sh" \
    links="$HOME/scripts/links.sh" \
    torrc="sudo nvim /etc/tor/torrc" \
    mc="cd $HOME/.local/share/PrismLauncher/instances/" \
    st="cd $HOME/.local/share/Steam/steamapps/common/" \
    todo="nvim $HOME/todo" \
    pipereload="systemctl --user restart pipewire pipewire-pulse" \
    dc="ddg-chat" \
    # an="anicli-ru" \
    tt="$HOME/scripts/twitch-title.sh" \
    # qemu="$HOME/scripts/wip/qemu.sh" \
    # qemuv="$HOME/scripts/wip/qemu.sh -v" \
    # yay='https_proxy=socks5://127.0.0.1:9050 http_proxy=socks5://127.0.0.1:9050 yay' \

set -o vi
PS1='[\u@\h \W]\$ '

