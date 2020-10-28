from arm.logicnode.arm_nodes import *


class RandomBooleanNode(ArmLogicTreeNode):
    """Generates a random boolean."""
    bl_idname = 'LNRandomBooleanNode'
    bl_label = 'Random Boolean'
    arm_version = 1

    def init(self, context):
        super(RandomBooleanNode, self).init(context)
        self.add_output('NodeSocketBool', 'Bool')
