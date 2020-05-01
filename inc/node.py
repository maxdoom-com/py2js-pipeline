#ifndef node.py
#define node.py

# ----------------------------------------------------------------------
# Node class... an abtraction to interface the dom.
# 
class Node:

    # ------------------------------------------------------------------
    # Binding to DOM nodes

    def dom_bind_to_node_by_selector(self, selector):
        self._node = document.querySelector(selector)
        self._node._object = self

    # ------------------------------------------------------------------
    # CSS Classes

    def dom_set_classes(self, classes):
        self._node.classList.value = ' '.join(classes)

    def dom_get_classes(self):
        return self._node.classList.valueOf()

    def dom_add_classes(self, classes):
        for class_ in classes:
            self._node.classList.add(class_)

    # ------------------------------------------------------------------
    # Hide/show

    def dom_hide(self):
        self._node.style.display = 'none'

    def dom_show(self):
        self._node.style.display = 'block'

#endif node.py
