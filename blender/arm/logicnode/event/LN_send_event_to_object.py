from arm.logicnode.arm_nodes import *

class SendEventNode(ArmLogicTreeNode):
    """Sends the given event to the given object.

    @seeNode Send Event
    @seeNode On Event

    @input Event: the identifier of the event
    @input Object: the receiving object"""
    bl_idname = 'LNSendEventNode'
    bl_label = 'Send Event To Object'
    arm_section = 'custom'
    arm_version = 1

    def init(self, context):
        super(SendEventNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketString', 'Event')
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_output('ArmNodeSocketAction', 'Out')
