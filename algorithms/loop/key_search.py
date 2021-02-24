class Box:
    '''
    Can hold a key and/or other boxes inside.
    '''
    def __init__(self, items=[]):
        self.items = items

    def __str__(self):
        return 'box'

class Key:
    '''
    Item being searched for.
    '''
    def __str__(self):
        return 'key'

def key_search(item):
    '''
    Looks for key in a box.
    '''
    pile = []
    items = item.items

    if items == []:
        return None

    if len(items) > 0:
        pile.extend(items)

    while len(pile) > 0:
        pile_item = pile.pop(0)

        if str(pile_item) == 'key':
            return str(pile_item)

        if str(pile_item) == 'box':
            pile.extend(pile_item.items)

    return None
