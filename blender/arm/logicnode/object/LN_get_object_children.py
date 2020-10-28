from arm.logicnode.arm_nodes import *

class GetChildrenNode(ArmLogicTreeNode):
    """Returns the children of the given object."""
    bl_idname = 'LNGetChildrenNode'
    bl_label = 'Get Object Children'
    arm_section = 'relations'
    arm_version = 1

    def init(self, context):
        super(GetChildrenNode, self).init(context)
        self.add_input('ArmNodeSocketObject', 'Parent')
        self.add_output('ArmNodeSocketArray', 'Children')
