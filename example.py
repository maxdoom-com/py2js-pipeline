#include inc/node.py

class Example(Node):
    def __init__(self, selector):
        self.dom_bind_to_node_by_selector(selector)
        print(self._node)
        self.dom_set_classes(['blue'])

# some raw js...
# RawJS("""/* foo */""")
