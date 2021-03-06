# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html
config.set('fonts.default_family', 'terminus')

config.set('content.javascript.enabled', True, 'file://*')
config.set('content.javascript.enabled', True, 'qute://*/*')
config.set('content.javascript.enabled', False, 'http://*')
config.set('content.javascript.enabled', False, 'https://*')
config.set('content.javascript.enabled', True, '*://boards.4chan.org/*')
config.set('content.javascript.enabled', True, '*://boards.4channel.org/*')
config.set('content.cookies.accept', 'no-3rdparty')

config.bind('e', 'hint links spawn mpv {hint-url}')
config.bind('E', 'spawn mpv {url}')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
config.bind('#', 'enter-mode set_mark')
config.bind('x', 'edit-url')
config.bind('X', 'hint links run edit-url -t {hint-url}')
config.bind('b', 'bookmark-load {}')
config.bind('B', 'bookmark-load -t {}')
config.bind('<Space>o', 'hint --rapid all tab-bg')
config.bind('<Space>p', 'open -p')
config.bind('<Space>m', 'tab-mute')
config.bind('<Space>dh', 'hint links run download -d ~/pix/hen "{hint-url}"')
config.bind('<Space>dm', 'hint links run download -d ~/pix/meme "{hint-url}"')
config.bind('<Space>dt', 'hint links run download -d ~/pix/tmp "{hint-url}"')
config.bind('<Space>dm', 'hint links run download -d ~/pix/moe "{hint-url}"')
config.bind('<Space>dc', 'hint links run download -d ~/pix/chan "{hint-url}"')
config.bind('<Space>dp', 'hint links run download -d ~/pdf "{hint-url}"')
config.bind('<Space>dy', 'hint links run spawn --verbose youtube-dl "{hint-url}"')
config.bind('<Space>a', 'spawn --verbose htmltopdf "{url}"')
config.bind('ac', 'hint links run spawn --verbose yt-channel-id "{hint-url}"')
config.bind('ay', 'hint links run spawn --verbose yt-audio-download "{hint-url}"')

config.set('content.notifications', False)
config.set('content.pdfjs', True)
config.set('downloads.location.directory', '/home/finn/www/')
config.set('downloads.location.prompt', False)
config.set('downloads.remove_finished', 1000)
config.set('tabs.position', 'top')
config.set('tabs.select_on_remove', 'last-used')
config.set('editor.command', ["st", "nvim", "{file}"])
config.set('completion.open_categories', ["quickmarks", "bookmarks", "history"])

c.url.searchengines =   {"DEFAULT": "https://start.duckduckgo.com/?q={}", 
                        "a": "https://wiki.archlinux.org/?search={}",
                        "y": "https://www.youtube.com/results?search_query={}",
                        "4": "https://boards.4channel.org/{}/",
                        "r": "https://www.reddit.com/r/{}/",
                        "g": "https://github.com/search?q={}",
                        "i": "https://yandex.com/images/search/?text={}"}

c.aliases =             {"q": "close",
                        "qa": "quit",
                        "w": "session-save",
                        "wq": "quit --save",
                        "wqa": "quit --save"}

# jmatrix
# import sys, os
# sys.path.append(os.path.join(sys.path[0], 'jmatrix'))
# config.source("jmatrix/jmatrix/integrations/qutebrowser.py")

# qutenyan
config.source('qutenyan/nyan.py')
