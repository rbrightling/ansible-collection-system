""" RKHunter Ansible Jinja Filters """
__metaclass__ = type


def option(value, join=" ", boolean="binary"):
    if value is True:
        return {"binary": 1, "text": "yes"}.get(boolean)
    elif value is False:
        return {"binary": 0, "text": "no"}.get(boolean)
    elif type(value) is list:
        return join.join(value)
    else:
        return value


class FilterModule(object):

    def filters(self):
        return {
            'rkhunter_conf_option': option,
        }
