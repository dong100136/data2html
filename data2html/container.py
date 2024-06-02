from .element import DElement
from typing import List


class DView:
    def __init__(self, title="empty title"):
        self.title = title
        self.child = []

    def add(self, ele: DElement):
        self.child.append(ele)

    def rend(self, data):
        pass

    def __str__(self):
        child_str = ["View("]
        for ele in self.child:
            tmp_str = str(ele)
            tmp_str = ["  " + t for t in tmp_str.split("\n")]
            child_str.extend(tmp_str)
        child_str.append(")")
        return "\n".join(child_str)


class DContainer(DElement):
    pass


class DTable(DContainer):
    def __init__(self, title="table"):
        self.title = title
        self.cols = []

    def add_col(self, ele:DElement, title="col"):
        self.cols.append(ele)

    def __str__(self):
        child_str = ["Table("]
        for col in self.cols:
            tmp_str = str(col)
            tmp_str = ["  " + t for t in tmp_str.split("\n")]
            child_str.extend(tmp_str)
        child_str.append(")")
        child_str = "\n".join(child_str)
        return child_str


class DStack(DContainer):
    def __init__(self, child: List[DElement], title="stack"):
        self.title = title
        self.child = child

    def __str__(self):
        child_str = ["Stack("]
        for ele in self.child:
            tmp_str = str(ele)
            tmp_str = ["  " + t for t in tmp_str.split("\n")]
            child_str.extend(tmp_str)
        child_str.append(")")
        child_str = "\n".join(child_str)
        return child_str
