from pygal_maps_world.maps import World

wm = World()
wm.title = '北美洲国家人口分布'
wm.add("北美", {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('na_populations.svg')