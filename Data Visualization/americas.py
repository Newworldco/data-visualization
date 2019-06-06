from pygal_maps_world.maps import World

wm = World()
wm.title = 'North, Central, and 南非'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br'])

wm.render_to_file('america.svg')