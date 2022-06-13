# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbs

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class Attributes(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Attributes()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAttributes(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    # Attributes
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Attributes
    def Items(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .KeyValue import KeyValue
            obj = KeyValue()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Attributes
    def ItemsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Attributes
    def ItemsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0


def Start(builder): builder.StartObject(1)


def AttributesStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)


def AddItems(builder, items): builder.PrependUOffsetTRelativeSlot(0,
                                                                  flatbuffers.number_types.UOffsetTFlags.py_type(items),
                                                                  0)


def AttributesAddItems(builder, items):
    """This method is deprecated. Please switch to AddItems."""
    return AddItems(builder, items)


def StartItemsVector(builder, numElems): return builder.StartVector(4, numElems, 4)


def AttributesStartItemsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartItemsVector(builder, numElems)


def End(builder): return builder.EndObject()


def AttributesEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)