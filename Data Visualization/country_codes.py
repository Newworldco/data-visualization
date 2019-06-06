from pygal_maps_world.maps import COUNTRIES


def get_country_code(country_name):
    """根据指定的国家， 返回国别码"""
    for code, name in COUNTRIES.items():
        if country_name == name:
            return code
    return None
