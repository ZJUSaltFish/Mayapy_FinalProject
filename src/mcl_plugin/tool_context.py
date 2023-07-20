import threading
import time

import maya.cmds as cmds
import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui


from marching_cube import MarchingCube

from threading import Thread, Event
from time import sleep
import asyncio


from enum import Enum
class BrushTypes(Enum):
    sphere = 'mcl_sphere_brush'
    cube = 'mcl_cube_brush'
    
class LandscapeTool(omui.MPxContext):
    """
    This is a class defining Marching Cubes Landscape Editor
    It dont works. I dont understand
    """
    TOOL_NAME = 'mcltool'

    def __init__(self):
        super(LandscapeTool, self).__init__()


    def __del__(self):
        pass

    def stringClassName(self):
        """
        This function is called by mels to determine the unique name of the tool
        :return: MString
        """
        return self.TOOL_NAME

    def toolOnSetup(self):
        om.MGlobal.displayInfo(self.TOOL_NAME + " is activated.")

    def toolOffCleanup(self):
        om.MGlobal.displayInfo(self.TOOL_NAME + " is stopped.")

    def doPress(self, event, view, _):
        print("Pressed")

class BrushTool():
    CONTEXT_NAME = "BrushContext"

    def __init__(self):
        # initialize variables
        self.MC = MarchingCube()
        self._brush_name = 'mcl_brush'
        self._brush_mat = self._create_brush_mat()
        self._brush_type = BrushTypes.sphere
        self._brush_radius = 0
        self._brush_strength = 0
        self._brush_hardness = 0
        # python multi-thread for controlling maya brush. Ugly but I dont have better way.
        self._brush_event = Event()
        #self._brush_async = None
        #self._event_loop = asyncio.new_event_loop()
        cmds.draggerContext(self.CONTEXT_NAME, initialize=self._switch_on, finalize=self._switch_off, edit=False,
                            image1='commandButton.png', dragCommand = self._ray_check, pressCommand = self._ray_check)
    def enable(self, *brush_type):
        """
        This function is used when clicking "Tool" button on GUI
        It will create a new tool instance
        :param BrushTypes.brush_type:
        :return:
        """
        # update brush type
        self._brush_type = brush_type
        # activate the tool
        cmds.setToolTo(self.CONTEXT_NAME)

    def _switch_on(self):
        """
        This function is used to create a new tool instance
        automatically called when switching to mcltool
        :return:
        """
        # create new brush object
        self._new_brush(self._brush_type)

        # killing old brush controller thread in case the user clicked twice
        #if self._brush_async is not None:
        #    self._brush_async.cancel()
        #self._brush_async = self._event_loop.create_task(self._brush_async_control())
        #print("created")
        #asyncio.run(self._brush_async_control())
        #self._brush_event.set()
        # new event
        #self._brush_event = Event()
        # new controller thread
        #Thread(target=self._brush_threading, args=(self._brush_event,)).start()

    def _switch_off(self):
        """
        This function is used to delete current tool instance
        automatically called when switching off
        :return:
        """
        if cmds.objExists(self._brush_name):
            cmds.delete(self._brush_name)
        #self._brush_async.cancel()
        #self._brush_event.set()

    def set_radius(self, radius):
        self._brush_radius = radius
        if self._brush_type == BrushTypes.sphere:
            # Find the node that builds the sphere brush
            build_node = None
            history = cmds.listHistory(self._brush_name)
            print(history)
            for node in history:
                if cmds.nodeType(node) == 'makeNurbSphere':
                    build_node = node
                    break
            cmds.setAttr(build_node + '.radius', radius)

    def set_hardness(self, hardness):
        self._brush_hardness = hardness

    def set_strength(self, strength):
        self._brush_strength = strength
        cmds.setAttr('%s.transparency' % self._brush_mat, 1 - strength, 1 - strength, 1 - strength, type="double3")

    def _ray_check(self):
        mouse_pos = cmds.draggerContext(self.CONTEXT_NAME, query=True, dragPoint=True)

        viewport_pos = om.MPoint(mouse_pos[0], mouse_pos[1], 0)

        #projection_matrix = om.MMatrix(omui.M3dView().active3dView().projectionMatrix())

        ray_source = om.MPoint()
        ray_direction = om.MVector()
        omui.M3dView().active3dView().viewToWorld(int(viewport_pos[0]), int(viewport_pos[1]), ray_source, ray_direction)

        selection_list = om.MGlobal.getActiveSelectionList()

        intersect_point = om.MFloatPoint()

        hit = False
        selec_iter = om.MItSelectionList(selection_list)

        while not selec_iter.isDone():
            dag_path = selec_iter.getDagPath()
            fn_mesh = om.MFnMesh(dag_path)

            hit_return = fn_mesh.closestIntersection(om.MFloatPoint(ray_source), om.MFloatVector(ray_direction),
                                                     om.MSpace.kWorld, 1000, False)
            if hit_return:
                hit = True
                intersect_point = hit_return[0]
                break

            selec_iter.next()

        if hit:
            #print("Intersection Point: ", intersect_point)
            #do something else
            self._render_brush(location = intersect_point)
            (x,y,z,t) = intersect_point
            self.MC.addPoint(om.MPoint(x,y,z),self._brush_radius,0)
            # self.MC.render()
        else:
            self._hide_brush()

    async def _brush_async_control(self):
        while True:
            print("Check")
            self._ray_check()
            await asyncio.sleep(0.05)

    def _brush_threading(self, event):
        while True:
            print(cmds.draggerContext(self.CONTEXT_NAME, query = True, dragPoint = True))
            sleep(0.05)
            if event.isSet():
                break

    def _render_brush(self, *, location):
        """
        If no brush created: create a brush at location
        If brush exists: show it, then move to location
        :param location: (floatX, floatY, floatZ)
        :return: None
        """
        if cmds.objExists(self._brush_name) :
            cmds.showHidden(self._brush_name)
            cmds.move(location[0], location[1], location[2], self._brush_name, absolute=True, worldSpace=True)
            cmds.refresh()

    def _hide_brush(self):
        if cmds.objExists(self._brush_name):
            cmds.hide(self._brush_name)

    def _new_brush(self, *brush_type):
        # delete old brush object
        if cmds.objExists(self._brush_name):
            cmds.delete(self._brush_name)
        # create new brush object
        if brush_type == BrushTypes.cube:
            self._brush_type = BrushTypes.cube
            pass
        else:
            # 创建默认的球体
            sphereRadius = 1
            sphereStrength = 0.5
            cmds.sphere(name = self._brush_name, radius=sphereRadius)
            # 将材质赋给球体,并使其不可选中
            cmds.select(self._brush_name)
            cmds.sets(forceElement='%sSG' % self._brush_mat)
            # 设置球体的默认透明度值
            cmds.setAttr('%s.transparency' % self._brush_mat, sphereStrength, sphereStrength, sphereStrength, type="double3")
            # 将该物体设置为不可选中
            cmds.setAttr(self._brush_name + ".overrideEnabled", 1)
            cmds.setAttr(self._brush_name + ".overrideDisplayType", 2)
            cmds.select(clear=True)
            # make sure self._brush_type is not None
            self._brush_type = BrushTypes.sphere


    def _create_brush_mat(self):
        """
        Create a lambert material
        return: material shading node (cmds.shadingNode)
        """
        mat = cmds.shadingNode('lambert', asShader=True, name="mat")
        cmds.sets(name='%sSG' % mat, renderable=True, noSurfaceShader=True, empty=True)
        cmds.connectAttr('%s.outColor' % mat, '%sSG.surfaceShader' % mat)
        return mat

