#!/usr/bin/env python
# coding:utf-8


# -------------------------------------------------------------------------------------------------------
class A(object):
    """
    standard attribute access is the normal way of accessing attributes
    """
    def __init__(self, x=None):
        self._x = x
        pass

    def getx(self):
        print '(getx)'
        return self._x

    def setx(self, value):
        print '(setx)'
        self._x = value

    def delx(self):
        print '(delx)'
        del self._x

    """
    class property([fget[, fset[, fdel[, doc]]]])
        Return a property attribute for new-style classes (classes that derive from object).
        fget is a function for getting an attribute value.
        fset is a function for setting an attribute value.
        fdel is a function for deleting an attribute value.
        And doc creates a docstring for the attribute.
    If c is an instance of C,
        c.x
            will invoke the getter,
        c.x = value
            will invoke the setter,
        del c.x
            will invoke the deleter.
    """
    x = property(fget=getx, fset=setx, fdel=delx, doc='I am the "x" property')

    print property, type(property)
    # <type 'property'> <type 'type'>
    print x, type(x)
    # <property object at 0x1060bae68> <type 'property'>
# -------------------------------------------------------------------------------------------------------
class B(object):
    """
    A property object has getter, setter, and deleter methods usable as decorators
    that create a copy of the property with the corresponding accessor function set to the decorated function.
    """
    def __init__(self, x=None):
        self._x = x
        pass

    @property
    def x(self):
        print '(getter)'
        return self._x

    # @x.getter
    # def x(self):
    #     """
    #     Be sure to give the additional functions the same name as the original property (x in this case.)
    #     """
    #     print '(getter)'
    #     return self._x

    @x.setter
    def x(self, value):
        """
        Be sure to give the additional functions the same name as the original property (x in this case.)
        """
        print '(setter)'
        self._x = value

    @x.deleter
    def x(self):
        """
        Be sure to give the additional functions the same name as the original property (x in this case.)
        """
        print '(deleter)'
        del self._x
# -------------------------------------------------------------------------------------------------------
a = A(9)

a.x
# (getx)
a.x = 99
# (setx)
del a.x
# (delx)
# -------------------------------------------------------------------------------------------------------
b = B(9)

b.x
# (getter)
b.x = 99
# (setter)
del b.x
# (deleter)
# -------------------------------------------------------------------------------------------------------
