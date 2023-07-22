# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QAbstractScrollArea import QAbstractScrollArea

class QPlainTextEdit(QAbstractScrollArea):
    """
    QPlainTextEdit(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QPlainTextEdit(self, text: str, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def anchorAt(self, pos): # real signature unknown; restored from __doc__
        """ anchorAt(self, pos: PySide2.QtCore.QPoint) -> str """
        return ""

    def appendHtml(self, html): # real signature unknown; restored from __doc__
        """ appendHtml(self, html: str) -> None """
        pass

    def appendPlainText(self, text): # real signature unknown; restored from __doc__
        """ appendPlainText(self, text: str) -> None """
        pass

    def backgroundVisible(self): # real signature unknown; restored from __doc__
        """ backgroundVisible(self) -> bool """
        return False

    def blockBoundingGeometry(self, block): # real signature unknown; restored from __doc__
        """ blockBoundingGeometry(self, block: PySide2.QtGui.QTextBlock) -> PySide2.QtCore.QRectF """
        pass

    def blockBoundingRect(self, block): # real signature unknown; restored from __doc__
        """ blockBoundingRect(self, block: PySide2.QtGui.QTextBlock) -> PySide2.QtCore.QRectF """
        pass

    def blockCount(self): # real signature unknown; restored from __doc__
        """ blockCount(self) -> int """
        return 0

    def blockCountChanged(self, *args, **kwargs): # real signature unknown
        pass

    def canInsertFromMimeData(self, source): # real signature unknown; restored from __doc__
        """ canInsertFromMimeData(self, source: PySide2.QtCore.QMimeData) -> bool """
        return False

    def canPaste(self): # real signature unknown; restored from __doc__
        """ canPaste(self) -> bool """
        return False

    def centerCursor(self): # real signature unknown; restored from __doc__
        """ centerCursor(self) -> None """
        pass

    def centerOnScroll(self): # real signature unknown; restored from __doc__
        """ centerOnScroll(self) -> bool """
        return False

    def changeEvent(self, e): # real signature unknown; restored from __doc__
        """ changeEvent(self, e: PySide2.QtCore.QEvent) -> None """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def contentOffset(self): # real signature unknown; restored from __doc__
        """ contentOffset(self) -> PySide2.QtCore.QPointF """
        pass

    def contextMenuEvent(self, e): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, e: PySide2.QtGui.QContextMenuEvent) -> None """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> None """
        pass

    def copyAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def createMimeDataFromSelection(self): # real signature unknown; restored from __doc__
        """ createMimeDataFromSelection(self) -> PySide2.QtCore.QMimeData """
        pass

    def createStandardContextMenu(self): # real signature unknown; restored from __doc__
        """
        createStandardContextMenu(self) -> PySide2.QtWidgets.QMenu
        createStandardContextMenu(self, position: PySide2.QtCore.QPoint) -> PySide2.QtWidgets.QMenu
        """
        pass

    def currentCharFormat(self): # real signature unknown; restored from __doc__
        """ currentCharFormat(self) -> PySide2.QtGui.QTextCharFormat """
        pass

    def cursorForPosition(self, pos): # real signature unknown; restored from __doc__
        """ cursorForPosition(self, pos: PySide2.QtCore.QPoint) -> PySide2.QtGui.QTextCursor """
        pass

    def cursorPositionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def cursorRect(self): # real signature unknown; restored from __doc__
        """
        cursorRect(self) -> PySide2.QtCore.QRect
        cursorRect(self, cursor: PySide2.QtGui.QTextCursor) -> PySide2.QtCore.QRect
        """
        pass

    def cursorWidth(self): # real signature unknown; restored from __doc__
        """ cursorWidth(self) -> int """
        return 0

    def cut(self): # real signature unknown; restored from __doc__
        """ cut(self) -> None """
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> PySide2.QtGui.QTextDocument """
        pass

    def documentTitle(self): # real signature unknown; restored from __doc__
        """ documentTitle(self) -> str """
        return ""

    def doSetTextCursor(self, cursor): # real signature unknown; restored from __doc__
        """ doSetTextCursor(self, cursor: PySide2.QtGui.QTextCursor) -> None """
        pass

    def dragEnterEvent(self, e): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, e: PySide2.QtGui.QDragEnterEvent) -> None """
        pass

    def dragLeaveEvent(self, e): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, e: PySide2.QtGui.QDragLeaveEvent) -> None """
        pass

    def dragMoveEvent(self, e): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, e: PySide2.QtGui.QDragMoveEvent) -> None """
        pass

    def dropEvent(self, e): # real signature unknown; restored from __doc__
        """ dropEvent(self, e: PySide2.QtGui.QDropEvent) -> None """
        pass

    def ensureCursorVisible(self): # real signature unknown; restored from __doc__
        """ ensureCursorVisible(self) -> None """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def extraSelections(self): # real signature unknown; restored from __doc__
        """ extraSelections(self) -> typing.List[PySide2.QtWidgets.QTextEdit.ExtraSelection] """
        pass

    def find(self, exp, options=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        find(self, exp: PySide2.QtCore.QRegExp, options: PySide2.QtGui.QTextDocument.FindFlags = Default(QTextDocument.FindFlags)) -> bool
        find(self, exp: PySide2.QtCore.QRegularExpression, options: PySide2.QtGui.QTextDocument.FindFlags = Default(QTextDocument.FindFlags)) -> bool
        find(self, exp: str, options: PySide2.QtGui.QTextDocument.FindFlags = Default(QTextDocument.FindFlags)) -> bool
        """
        pass

    def firstVisibleBlock(self): # real signature unknown; restored from __doc__
        """ firstVisibleBlock(self) -> PySide2.QtGui.QTextBlock """
        pass

    def focusInEvent(self, e): # real signature unknown; restored from __doc__
        """ focusInEvent(self, e: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOutEvent(self, e): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, e: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def getPaintContext(self): # real signature unknown; restored from __doc__
        """ getPaintContext(self) -> PySide2.QtGui.QAbstractTextDocumentLayout.PaintContext """
        pass

    def inputMethodEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, arg__1: PySide2.QtGui.QInputMethodEvent) -> None """
        pass

    def inputMethodQuery(self, property): # real signature unknown; restored from __doc__
        """
        inputMethodQuery(self, property: PySide2.QtCore.Qt.InputMethodQuery) -> typing.Any
        inputMethodQuery(self, query: PySide2.QtCore.Qt.InputMethodQuery, argument: typing.Any) -> typing.Any
        """
        pass

    def insertFromMimeData(self, source): # real signature unknown; restored from __doc__
        """ insertFromMimeData(self, source: PySide2.QtCore.QMimeData) -> None """
        pass

    def insertPlainText(self, text): # real signature unknown; restored from __doc__
        """ insertPlainText(self, text: str) -> None """
        pass

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def isUndoRedoEnabled(self): # real signature unknown; restored from __doc__
        """ isUndoRedoEnabled(self) -> bool """
        return False

    def keyPressEvent(self, e): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, e: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def keyReleaseEvent(self, e): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, e: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def lineWrapMode(self): # real signature unknown; restored from __doc__
        """ lineWrapMode(self) -> PySide2.QtWidgets.QPlainTextEdit.LineWrapMode """
        pass

    def loadResource(self, type, name): # real signature unknown; restored from __doc__
        """ loadResource(self, type: int, name: PySide2.QtCore.QUrl) -> typing.Any """
        pass

    def maximumBlockCount(self): # real signature unknown; restored from __doc__
        """ maximumBlockCount(self) -> int """
        return 0

    def mergeCurrentCharFormat(self, modifier): # real signature unknown; restored from __doc__
        """ mergeCurrentCharFormat(self, modifier: PySide2.QtGui.QTextCharFormat) -> None """
        pass

    def modificationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, e): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, e: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseMoveEvent(self, e): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, e: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mousePressEvent(self, e): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, e: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseReleaseEvent(self, e): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, e: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def moveCursor(self, operation, mode=None): # real signature unknown; restored from __doc__
        """ moveCursor(self, operation: PySide2.QtGui.QTextCursor.MoveOperation, mode: PySide2.QtGui.QTextCursor.MoveMode = PySide2.QtGui.QTextCursor.MoveMode.MoveAnchor) -> None """
        pass

    def overwriteMode(self): # real signature unknown; restored from __doc__
        """ overwriteMode(self) -> bool """
        return False

    def paintEvent(self, e): # real signature unknown; restored from __doc__
        """ paintEvent(self, e: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def paste(self): # real signature unknown; restored from __doc__
        """ paste(self) -> None """
        pass

    def placeholderText(self): # real signature unknown; restored from __doc__
        """ placeholderText(self) -> str """
        return ""

    def print_(self, printer): # real signature unknown; restored from __doc__
        """ print_(self, printer: PySide2.QtGui.QPagedPaintDevice) -> None """
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ redo(self) -> None """
        pass

    def redoAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, e): # real signature unknown; restored from __doc__
        """ resizeEvent(self, e: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def scrollContentsBy(self, dx, dy): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, dx: int, dy: int) -> None """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ selectAll(self) -> None """
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setBackgroundVisible(self, visible): # real signature unknown; restored from __doc__
        """ setBackgroundVisible(self, visible: bool) -> None """
        pass

    def setCenterOnScroll(self, enabled): # real signature unknown; restored from __doc__
        """ setCenterOnScroll(self, enabled: bool) -> None """
        pass

    def setCurrentCharFormat(self, format): # real signature unknown; restored from __doc__
        """ setCurrentCharFormat(self, format: PySide2.QtGui.QTextCharFormat) -> None """
        pass

    def setCursorWidth(self, width): # real signature unknown; restored from __doc__
        """ setCursorWidth(self, width: int) -> None """
        pass

    def setDocument(self, document): # real signature unknown; restored from __doc__
        """ setDocument(self, document: PySide2.QtGui.QTextDocument) -> None """
        pass

    def setDocumentTitle(self, title): # real signature unknown; restored from __doc__
        """ setDocumentTitle(self, title: str) -> None """
        pass

    def setExtraSelections(self, selections, PySide2_QtWidgets_QTextEdit_ExtraSelection=None): # real signature unknown; restored from __doc__
        """ setExtraSelections(self, selections: typing.Sequence[PySide2.QtWidgets.QTextEdit.ExtraSelection]) -> None """
        pass

    def setLineWrapMode(self, mode): # real signature unknown; restored from __doc__
        """ setLineWrapMode(self, mode: PySide2.QtWidgets.QPlainTextEdit.LineWrapMode) -> None """
        pass

    def setMaximumBlockCount(self, maximum): # real signature unknown; restored from __doc__
        """ setMaximumBlockCount(self, maximum: int) -> None """
        pass

    def setOverwriteMode(self, overwrite): # real signature unknown; restored from __doc__
        """ setOverwriteMode(self, overwrite: bool) -> None """
        pass

    def setPlaceholderText(self, placeholderText): # real signature unknown; restored from __doc__
        """ setPlaceholderText(self, placeholderText: str) -> None """
        pass

    def setPlainText(self, text): # real signature unknown; restored from __doc__
        """ setPlainText(self, text: str) -> None """
        pass

    def setReadOnly(self, ro): # real signature unknown; restored from __doc__
        """ setReadOnly(self, ro: bool) -> None """
        pass

    def setTabChangesFocus(self, b): # real signature unknown; restored from __doc__
        """ setTabChangesFocus(self, b: bool) -> None """
        pass

    def setTabStopDistance(self, distance): # real signature unknown; restored from __doc__
        """ setTabStopDistance(self, distance: float) -> None """
        pass

    def setTabStopWidth(self, width): # real signature unknown; restored from __doc__
        """ setTabStopWidth(self, width: int) -> None """
        pass

    def setTextCursor(self, cursor): # real signature unknown; restored from __doc__
        """ setTextCursor(self, cursor: PySide2.QtGui.QTextCursor) -> None """
        pass

    def setTextInteractionFlags(self, flags): # real signature unknown; restored from __doc__
        """ setTextInteractionFlags(self, flags: PySide2.QtCore.Qt.TextInteractionFlags) -> None """
        pass

    def setUndoRedoEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setUndoRedoEnabled(self, enable: bool) -> None """
        pass

    def setWordWrapMode(self, policy): # real signature unknown; restored from __doc__
        """ setWordWrapMode(self, policy: PySide2.QtGui.QTextOption.WrapMode) -> None """
        pass

    def showEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ showEvent(self, arg__1: PySide2.QtGui.QShowEvent) -> None """
        pass

    def tabChangesFocus(self): # real signature unknown; restored from __doc__
        """ tabChangesFocus(self) -> bool """
        return False

    def tabStopDistance(self): # real signature unknown; restored from __doc__
        """ tabStopDistance(self) -> float """
        return 0.0

    def tabStopWidth(self): # real signature unknown; restored from __doc__
        """ tabStopWidth(self) -> int """
        return 0

    def textChanged(self, *args, **kwargs): # real signature unknown
        pass

    def textCursor(self): # real signature unknown; restored from __doc__
        """ textCursor(self) -> PySide2.QtGui.QTextCursor """
        pass

    def textInteractionFlags(self): # real signature unknown; restored from __doc__
        """ textInteractionFlags(self) -> PySide2.QtCore.Qt.TextInteractionFlags """
        pass

    def timerEvent(self, e): # real signature unknown; restored from __doc__
        """ timerEvent(self, e: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ toPlainText(self) -> str """
        return ""

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) -> None """
        pass

    def undoAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def updateRequest(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, e): # real signature unknown; restored from __doc__
        """ wheelEvent(self, e: PySide2.QtGui.QWheelEvent) -> None """
        pass

    def wordWrapMode(self): # real signature unknown; restored from __doc__
        """ wordWrapMode(self) -> PySide2.QtGui.QTextOption.WrapMode """
        pass

    def zoomIn(self, range=1): # real signature unknown; restored from __doc__
        """ zoomIn(self, range: int = 1) -> None """
        pass

    def zoomInF(self, range): # real signature unknown; restored from __doc__
        """ zoomInF(self, range: float) -> None """
        pass

    def zoomOut(self, range=1): # real signature unknown; restored from __doc__
        """ zoomOut(self, range: int = 1) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    LineWrapMode = None # (!) real value is "<class 'PySide2.QtWidgets.QPlainTextEdit.LineWrapMode'>"
    NoWrap = PySide2.QtWidgets.QPlainTextEdit.LineWrapMode.NoWrap
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50816580>'
    WidgetWidth = PySide2.QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth


