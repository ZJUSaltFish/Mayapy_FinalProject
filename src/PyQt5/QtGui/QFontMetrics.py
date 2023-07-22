# encoding: utf-8
# module PyQt5.QtGui
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QFontMetrics(__sip.simplewrapper):
    """
    QFontMetrics(a0: QFont)
    QFontMetrics(a0: QFont, pd: QPaintDevice)
    QFontMetrics(a0: QFontMetrics)
    """
    def ascent(self): # real signature unknown; restored from __doc__
        """ ascent(self) -> int """
        return 0

    def averageCharWidth(self): # real signature unknown; restored from __doc__
        """ averageCharWidth(self) -> int """
        return 0

    def boundingRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        boundingRect(self, text: str) -> QRect
        boundingRect(self, rect: QRect, flags: int, text: str, tabStops: int = 0, tabArray: typing.Optional[Optional[List[int]]] = 0) -> QRect
        boundingRect(self, x: int, y: int, width: int, height: int, flags: int, text: str, tabStops: int = 0, tabArray: typing.Optional[Optional[List[int]]] = 0) -> QRect
        """
        pass

    def boundingRectChar(self, a0): # real signature unknown; restored from __doc__
        """ boundingRectChar(self, a0: str) -> QRect """
        pass

    def capHeight(self): # real signature unknown; restored from __doc__
        """ capHeight(self) -> int """
        return 0

    def descent(self): # real signature unknown; restored from __doc__
        """ descent(self) -> int """
        return 0

    def elidedText(self, text, mode, width, flags=0): # real signature unknown; restored from __doc__
        """ elidedText(self, text: str, mode: Qt.TextElideMode, width: int, flags: int = 0) -> str """
        return ""

    def fontDpi(self): # real signature unknown; restored from __doc__
        """ fontDpi(self) -> float """
        return 0.0

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def horizontalAdvance(self, a0, length=-1): # real signature unknown; restored from __doc__
        """ horizontalAdvance(self, a0: str, length: int = -1) -> int """
        return 0

    def inFont(self, a0): # real signature unknown; restored from __doc__
        """ inFont(self, a0: str) -> bool """
        return False

    def inFontUcs4(self, character): # real signature unknown; restored from __doc__
        """ inFontUcs4(self, character: int) -> bool """
        return False

    def leading(self): # real signature unknown; restored from __doc__
        """ leading(self) -> int """
        return 0

    def leftBearing(self, a0): # real signature unknown; restored from __doc__
        """ leftBearing(self, a0: str) -> int """
        return 0

    def lineSpacing(self): # real signature unknown; restored from __doc__
        """ lineSpacing(self) -> int """
        return 0

    def lineWidth(self): # real signature unknown; restored from __doc__
        """ lineWidth(self) -> int """
        return 0

    def maxWidth(self): # real signature unknown; restored from __doc__
        """ maxWidth(self) -> int """
        return 0

    def minLeftBearing(self): # real signature unknown; restored from __doc__
        """ minLeftBearing(self) -> int """
        return 0

    def minRightBearing(self): # real signature unknown; restored from __doc__
        """ minRightBearing(self) -> int """
        return 0

    def overlinePos(self): # real signature unknown; restored from __doc__
        """ overlinePos(self) -> int """
        return 0

    def rightBearing(self, a0): # real signature unknown; restored from __doc__
        """ rightBearing(self, a0: str) -> int """
        return 0

    def size(self, flags, text, tabStops=0, tabArray, Optional=None, List=None, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ size(self, flags: int, text: str, tabStops: int = 0, tabArray: typing.Optional[Optional[List[int]]] = 0) -> QSize """
        pass

    def strikeOutPos(self): # real signature unknown; restored from __doc__
        """ strikeOutPos(self) -> int """
        return 0

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QFontMetrics) """
        pass

    def tightBoundingRect(self, text): # real signature unknown; restored from __doc__
        """ tightBoundingRect(self, text: str) -> QRect """
        pass

    def underlinePos(self): # real signature unknown; restored from __doc__
        """ underlinePos(self) -> int """
        return 0

    def width(self, text, length=-1): # real signature unknown; restored from __doc__
        """ width(self, text: str, length: int = -1) -> int """
        return 0

    def widthChar(self, a0): # real signature unknown; restored from __doc__
        """ widthChar(self, a0: str) -> int """
        return 0

    def xHeight(self): # real signature unknown; restored from __doc__
        """ xHeight(self) -> int """
        return 0

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, a0, pd=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


