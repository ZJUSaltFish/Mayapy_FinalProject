# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QCameraFocus(__PySide2_QtCore.QObject):
    # no doc
    def customFocusPoint(self): # real signature unknown; restored from __doc__
        """ customFocusPoint(self) -> PySide2.QtCore.QPointF """
        pass

    def digitalZoom(self): # real signature unknown; restored from __doc__
        """ digitalZoom(self) -> float """
        return 0.0

    def digitalZoomChanged(self, *args, **kwargs): # real signature unknown
        pass

    def focusMode(self): # real signature unknown; restored from __doc__
        """ focusMode(self) -> PySide2.QtMultimedia.QCameraFocus.FocusModes """
        pass

    def focusPointMode(self): # real signature unknown; restored from __doc__
        """ focusPointMode(self) -> PySide2.QtMultimedia.QCameraFocus.FocusPointMode """
        pass

    def focusZones(self): # real signature unknown; restored from __doc__
        """ focusZones(self) -> typing.List[PySide2.QtMultimedia.QCameraFocusZone] """
        pass

    def focusZonesChanged(self, *args, **kwargs): # real signature unknown
        pass

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isFocusModeSupported(self, mode): # real signature unknown; restored from __doc__
        """ isFocusModeSupported(self, mode: PySide2.QtMultimedia.QCameraFocus.FocusModes) -> bool """
        return False

    def isFocusPointModeSupported(self, arg__1): # real signature unknown; restored from __doc__
        """ isFocusPointModeSupported(self, arg__1: PySide2.QtMultimedia.QCameraFocus.FocusPointMode) -> bool """
        return False

    def maximumDigitalZoom(self): # real signature unknown; restored from __doc__
        """ maximumDigitalZoom(self) -> float """
        return 0.0

    def maximumDigitalZoomChanged(self, *args, **kwargs): # real signature unknown
        pass

    def maximumOpticalZoom(self): # real signature unknown; restored from __doc__
        """ maximumOpticalZoom(self) -> float """
        return 0.0

    def maximumOpticalZoomChanged(self, *args, **kwargs): # real signature unknown
        pass

    def opticalZoom(self): # real signature unknown; restored from __doc__
        """ opticalZoom(self) -> float """
        return 0.0

    def opticalZoomChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setCustomFocusPoint(self, point): # real signature unknown; restored from __doc__
        """ setCustomFocusPoint(self, point: PySide2.QtCore.QPointF) -> None """
        pass

    def setFocusMode(self, mode): # real signature unknown; restored from __doc__
        """ setFocusMode(self, mode: PySide2.QtMultimedia.QCameraFocus.FocusModes) -> None """
        pass

    def setFocusPointMode(self, mode): # real signature unknown; restored from __doc__
        """ setFocusPointMode(self, mode: PySide2.QtMultimedia.QCameraFocus.FocusPointMode) -> None """
        pass

    def zoomTo(self, opticalZoom, digitalZoom): # real signature unknown; restored from __doc__
        """ zoomTo(self, opticalZoom: float, digitalZoom: float) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AutoFocus = PySide2.QtMultimedia.QCameraFocus.FocusMode.AutoFocus
    ContinuousFocus = PySide2.QtMultimedia.QCameraFocus.FocusMode.ContinuousFocus
    FocusMode = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraFocus.FocusMode'>"
    FocusModes = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraFocus.FocusModes'>"
    FocusPointAuto = PySide2.QtMultimedia.QCameraFocus.FocusPointMode.FocusPointAuto
    FocusPointCenter = PySide2.QtMultimedia.QCameraFocus.FocusPointMode.FocusPointCenter
    FocusPointCustom = PySide2.QtMultimedia.QCameraFocus.FocusPointMode.FocusPointCustom
    FocusPointFaceDetection = PySide2.QtMultimedia.QCameraFocus.FocusPointMode.FocusPointFaceDetection
    FocusPointMode = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraFocus.FocusPointMode'>"
    HyperfocalFocus = PySide2.QtMultimedia.QCameraFocus.FocusMode.HyperfocalFocus
    InfinityFocus = PySide2.QtMultimedia.QCameraFocus.FocusMode.InfinityFocus
    MacroFocus = PySide2.QtMultimedia.QCameraFocus.FocusMode.MacroFocus
    ManualFocus = PySide2.QtMultimedia.QCameraFocus.FocusMode.ManualFocus
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000188746A6F80>'


