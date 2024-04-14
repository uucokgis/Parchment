def construct_sira_no_filter(min_sira_no=0, max_sira_no=-1):
    _dict = {
        "sira": {
            "$gt": min_sira_no,
        }
    }
    if max_sira_no > 0:
        _dict['sira']['$lt'] = max_sira_no

    return _dict
