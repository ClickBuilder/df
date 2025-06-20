config.load_autoconfig(False)


# Интерфейс
c.statusbar.show = "in-mode"
c.tabs.show = "switching"
c.url.start_pages = ["about:blank"]
c.url.default_page = "about:blank"
c.confirm_quit = ["downloads"]

# Шрифты
c.fonts.default_family = "monospace"
c.fonts.default_size = "10pt"

# Темная тема (всё, что возможно)
config.set("colors.webpage.darkmode.enabled", True)
config.set("colors.webpage.preferred_color_scheme", "dark")
config.set("colors.webpage.darkmode.policy.images", "smart")

# Блокировка рекламы
config.set("content.blocking.enabled", True)
config.set("content.blocking.method", "adblock")
config.set("content.blocking.adblock.lists", [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt"
])

# Конфиденциальность и производительность
config.set("content.cookies.accept", "no-3rdparty")
config.set("content.autoplay", False)
config.set("content.notifications.enabled", False)
config.set("content.geolocation", False)

# Скачивания
config.set("downloads.remove_finished", 3000)

# Скролл
c.scrolling.bar = "never"
c.scrolling.smooth = True

# По умолчанию JS включен
config.set("content.javascript.enabled", True)

# Поисковики
c.url.searchengines = {
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "g": "https://www.google.com/search?q={}",
    "yt": "https://www.youtube.com/results?search_query={}",
    "gh": "https://github.com/search?q={}",
    "wiki": "https://en.wikipedia.org/wiki/{}",
    "aur": "https://aur.archlinux.org/packages/?O=0&K={}",
    "arch": "https://wiki.archlinux.org/?search={}"
}
c.aliases['off-arch'] = 'open file:///home/wex/offline-sites/archlinux.org/archlinux.org/index.html'




# Быстрые бинды
config.bind('<Ctrl+s>', 'download --mhtml')
config.bind('xx', 'tab-close')     # Закрыть вкладку
config.bind(';m', 'hint links spawn mpv {hint-url}')  # Открыть ссылку в mpv
config.bind(',M', 'spawn mpv {url}')                   # Открыть текущую страницу в mpv
config.bind('<Ctrl+y>', 'open https://www.youtube.com')
config.bind("xb", "config-cycle statusbar.show always never")
config.bind("xt", "config-cycle tabs.show always never")
config.bind("<Ctrl-h>", "tab-prev")
config.bind("<Ctrl-l>", "tab-next")
config.bind("<Ctrl-q>", "quit")
config.bind("ZZ", "quit")
config.bind("J", "tab-prev")
config.bind("K", "tab-next")
config.bind(";d", "hint links download")
config.bind(";m", "hint links spawn mpv {hint-url}")

