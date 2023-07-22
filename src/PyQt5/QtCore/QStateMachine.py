# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QState import QState

class QStateMachine(QState):
    """
    QStateMachine(parent: typing.Optional[QObject] = None)
    QStateMachine(childMode: QState.ChildMode, parent: typing.Optional[QObject] = None)
    """
    def addDefaultAnimation(self, animation): # real signature unknown; restored from __doc__
        """ addDefaultAnimation(self, animation: QAbstractAnimation) """
        pass

    def addState(self, state): # real signature unknown; restored from __doc__
        """ addState(self, state: QAbstractState) """
        pass

    def cancelDelayedEvent(self, id): # real signature unknown; restored from __doc__
        """ cancelDelayedEvent(self, id: int) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearError(self): # real signature unknown; restored from __doc__
        """ clearError(self) """
        pass

    def configuration(self): # real signature unknown; restored from __doc__
        """ configuration(self) -> Set[QAbstractState] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultAnimations(self): # real signature unknown; restored from __doc__
        """ defaultAnimations(self) -> List[QAbstractAnimation] """
        return []

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QStateMachine.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: QEvent) -> bool """
        return False

    def eventFilter(self, watched, event): # real signature unknown; restored from __doc__
        """ eventFilter(self, watched: QObject, event: QEvent) -> bool """
        return False

    def globalRestorePolicy(self): # real signature unknown; restored from __doc__
        """ globalRestorePolicy(self) -> QState.RestorePolicy """
        pass

    def isAnimated(self): # real signature unknown; restored from __doc__
        """ isAnimated(self) -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def onEntry(self, event): # real signature unknown; restored from __doc__
        """ onEntry(self, event: QEvent) """
        pass

    def onExit(self, event): # real signature unknown; restored from __doc__
        """ onExit(self, event: QEvent) """
        pass

    def postDelayedEvent(self, event, delay): # real signature unknown; restored from __doc__
        """ postDelayedEvent(self, event: QEvent, delay: int) -> int """
        return 0

    def postEvent(self, event, priority=None): # real signature unknown; restored from __doc__
        """ postEvent(self, event: QEvent, priority: QStateMachine.EventPriority = QStateMachine.NormalPriority) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeDefaultAnimation(self, animation): # real signature unknown; restored from __doc__
        """ removeDefaultAnimation(self, animation: QAbstractAnimation) """
        pass

    def removeState(self, state): # real signature unknown; restored from __doc__
        """ removeState(self, state: QAbstractState) """
        pass

    def runningChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAnimated(self, enabled): # real signature unknown; restored from __doc__
        """ setAnimated(self, enabled: bool) """
        pass

    def setGlobalRestorePolicy(self, restorePolicy): # real signature unknown; restored from __doc__
        """ setGlobalRestorePolicy(self, restorePolicy: QState.RestorePolicy) """
        pass

    def setRunning(self, running): # real signature unknown; restored from __doc__
        """ setRunning(self, running: bool) """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def started(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def stopped(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    HighPriority = 1
    NoCommonAncestorForTransitionError = 3
    NoDefaultStateInHistoryStateError = 2
    NoError = 0
    NoInitialStateError = 1
    NormalPriority = 0
    StateMachineChildModeSetToParallelError = 4


