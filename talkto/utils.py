import inspect


def _has_contribute_to_class(value):
    # Only call contribute_to_class() if it's bound.
    return not inspect.isclass(value) and hasattr(value, 'contribute_to_class')


def querydict_to_dict(query_dict):
    data = {}
    for key in query_dict.keys():
        try:
            v = query_dict.getlist(key)
            if len(v) == 1:
                v = v[0]
        except:
            v = query_dict.get(key)
        data[key] = v
    data.pop('csrfmiddlewaretoken') if data.get('csrfmiddlewaretoken') else data
    return data
