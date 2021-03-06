from arm.logicnode.arm_nodes import *

class SurfaceNode(ArmLogicTreeNode):
    """Activates the output on the given touch event."""
    bl_idname = 'LNMergedSurfaceNode'
    bl_label = 'Touch'
    arm_section = 'surface'
    arm_version = 1

    property0: EnumProperty(
        items = [('started', 'Started', 'The screen surface starts to be touched'),
                 ('down', 'Down', 'The screen surface is touched'),
                 ('released', 'Released', 'The screen surface stops being touched'),
                 ('moved', 'Moved', 'Moved')],
        name='', default='down')

    def init(self, context):
        super(SurfaceNode, self).init(context)
        self.add_output('ArmNodeSocketAction', 'Out')
        self.add_output('NodeSocketBool', 'State')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')
