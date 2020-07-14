# __author__    = 'Fabian'
# __project__   = Snippet
# __file__      = remote_display.py
# __version__   = 0.1

# Tkinter per Remote ausführen


import os

if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
