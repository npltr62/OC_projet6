import platform
def get_like_distro():
    info = platform.freedesktop_os_release()
    print(info)
    ids = [info["ID"]]
    if "ID_LIKE" in info:
        # ids are space separated and ordered by precedence
        ids.extend(info["ID_LIKE"].split())
    return info
get_like_distro()