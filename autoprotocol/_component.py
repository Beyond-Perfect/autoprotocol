# This file serves to provide an abstract base class which must be used for all hardware (sensor/actuator) classes

# The Confusing Bits:
#   The Pins Input:
#       Pins can be input to a component using the `pins` input as either an int representing a single pin OR
#       a dict representing a pins object containing the appropriate pin names as keys and the respective pin numbers
#       as values. In the first case, the `pin` is passed into the `Component` superclass as {'single': <pin_num>}

from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, is_pin_not_pins, pin_names):
        self._components = {}
        self._IS_PIN_NOT_PINS = is_pin_not_pins     # Boolean to indicate whether pin is set as int or dict
        self._PIN_NAMES = pin_names                 # List of names for pins ONLY IF `self._IS_PIN_NOT_PINS` is `False`

    @abstractmethod
    def register(self, *, pins=None, name):
        if pins is None:
            raise Exception("Pins must be specified to register components")
        elif self._IS_PIN_NOT_PINS and 'single' not in pins:
            raise Exception("Implementation of derived `register` method is incorrect. See autoprotocol/_component.py")
        elif self._IS_PIN_NOT_PINS and type(pins['single']) is not int:
            raise Exception("Pin must be integer representing number of pin")
        elif self._IS_PIN_NOT_PINS and pins in self._components.values():
            raise Exception("Cannot register component as given pin number is already registered")
        elif not self._IS_PIN_NOT_PINS:
            overlapping_pins = []
            for pin in pins.values():
                for component in self._components.values():
                    if pin in component.values():
                        overlapping_pins.append(pin)
            if len(overlapping_pins) > 1:
                raise Exception("Cannot register component as pins " + ", ".join(pins) + " are already registered")
            elif len(overlapping_pins) > 0:
                raise Exception("Cannot register component as pin " + overlapping_pins[0] + " is already registered")
        elif name in self._components:
            raise Exception("Cannot register component as given name (" + str(name) + ") is already registered")
        else:
            self._components[name] = pins

    @abstractmethod
    def deregister(self, *, name):
        if name not in self._components:
            raise Exception("Cannot deregister component as given name (" + str(name) + ") is not registered")
        else:
            del self._components[name]


# Example Implementation:
# class ExampleComponent(Component):
#     def __init__(self):
#         super().__init__(is_pin_not_pins=False, pin_names=['lions', 'tigers', 'bears'])
#
#     def register(self, *, pin=None, name):
#         super(ExampleComponent, self).register(name=name, pins={'single': pin})
#
#     def deregister(self, *, name):
#         super(ExampleComponent, self).deregister(name=name)
