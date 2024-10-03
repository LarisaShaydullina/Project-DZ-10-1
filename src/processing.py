def filter_by_state(dict_id, state = 'EXECUTED'):
    dictionary_executed = []
    for index in dict_id:
        if index['state'] == state:
            dictionary_executed.append(index)
        #else:
            #dictionary_executed.append(index)
    return dictionary_executed


def sort_by_date(dict_id, ascending = True):
    return sorted(dictionary_id, key = lambda dict_id: dict_id['date'], reverse = ascending)