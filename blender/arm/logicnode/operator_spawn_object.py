import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class SpawnObjectNode(Node, ArmLogicTreeNode):
    '''Spawn object node'''
    bl_idname = 'LNSpawnObjectNode'
    bl_label = 'Spawn Object'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('ArmNodeSocketOperator', 'In')
        self.inputs.new('ArmNodeSocketObject', 'Object')
        self.inputs.new('NodeSocketShader', 'Tansform')
        self.outputs.new('ArmNodeSocketOperator', 'Out')
        self.outputs.new('ArmNodeSocketObject', 'Object')

add_node(SpawnObjectNode, category='Operator')