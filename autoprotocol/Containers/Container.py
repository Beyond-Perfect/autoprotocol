
    """
    This class represents every item on the deck.
    It maintains the hierarchy and provides means to:
    * traverse
    * retrieve items by name
    * calculate coordinates in different reference systems
    It should never be directly created; it is created by the system during
    labware load and when accessing wells.
    """
    #placeable.py---^ look into that file and funcs

class Container(type_c, action=None, location=default, sub_container=None):
'''
      param:: type_c [object] - The type_c parameter refers to the type of container, ie. deck, shake_flask...
      param:: action - The action parameter refers to the protocol function that will act on the container
      param:: location [str/int] or [list] - list representing coordinate location or variable with location
      param:: sub_container [object] - containers within a container, like wells within a plate
'''
  def __init__(self, type_c, action=None, location=default, sub_container=None,...):
    pass
