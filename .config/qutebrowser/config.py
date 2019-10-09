# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'file://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')

# Bindings for normal mode
config.bind('e', 'hint links spawn mpv {hint-url}')
config.bind('E', 'spawn mpv {url}')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
config.bind('<Space>p', 'open -p')
config.bind('<Space>m', 'tab-mute')
config.bind('<Space>F', 'spawn palemoon {url}')
config.bind('<Space>f', 'hint links run spawn palemoon {hint-url}')
config.bind('<Space>dh', 'hint links run download -d ~/pix/hen {hint-url}')
config.bind('<Space>dm', 'hint links run download -d ~/pix/meme {hint-url}')
config.bind('<Space>dt', 'hint links run download -d ~/pix/tmp {hint-url}')
config.bind('<Space>dc', 'hint links run download -d ~/pix/moe {hint-url}')

# Basics
config.set('content.notifications', False)
config.set('content.pdfjs', True)
config.set('downloads.location.directory', '/home/finn/etc/')
config.set('downloads.location.prompt', False)
config.set('downloads.remove_finished', 1000)
config.set('tabs.position', 'top')
config.set('tabs.select_on_remove', 'last-used')

# External configuration
c.url.searchengines =   {"DEFAULT": "https://start.duckduckgo.com/?q={}", 
                        "a": "https://wiki.archlinux.org/?search={}",
                        "y": "https://www.youtube.com/results?search_query={}",
                        "4": "https://boards.4channel.org/{}/",
			"r": "https://www.reddit.com/r/{}/",
			"g": "https://github.com/search?q={}"}

# jmatrix
# import sys, os
# sys.path.append(os.path.join(sys.path[0], 'jmatrix'))
# config.source("jmatrix/jmatrix/integrations/qutebrowser.py")

# qutenyan
config.source('qutenyan/nyan.py')
 
