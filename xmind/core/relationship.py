#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
    xmind.core.relationship
    ~~~~~~~~~~~~~~~~~~~


    :copyright:
    :license:
"""

__author__ = "aiqi@xmind.net <Woody Ai>"

from . import const

from .mixin import WorkbookMixinElement
from .topic import TopicElement
from .title import TitleElement


class RelationshipElement(WorkbookMixinElement):
    TAG_NAME = const.TAG_RELATIONSHIP

    def __init__(self, node=None, ownerWorkbook=None):
        super(RelationshipElement, self).__init__(node, ownerWorkbook)

        self.addIdAttribute(const.ATTR_ID)

    def _get_title(self):
        return self.getFirstChildNodeByTagName(const.TAG_TITLE)

    def _find_end_point_old(self, id):
        owner_workbook = self.getOwnerWorkbook()
        if owner_workbook is None:
            return

        end_point = owner_workbook.getElementById(id)
        if end_point is None:
            return

        if end_point.tagName == const.TAG_TOPIC:
            return TopicElement(end_point, owner_workbook)
            
    def _find_end_point(self, id):
        owner_document = self.getOwnerDocument()
        if owner_document is None:
            return

        topic_elems  = owner_document.getElementsByTagName(const.TAG_TOPIC)
        found = [x for x in topic_elems if (x.getAttribute('id') == id)]
        if len(found) < 1:
            return
        return TopicElement(found[0], self.getOwnerWorkbook())

    def getEnd1ID(self):
        return self.getAttribute(const.ATTR_END1)

    def setEnd1ID(self, id):
        self.setAttribute(const.ATTR_END1, id)
        self.updateModifiedTime()

    def getEnd2ID(self):
        return self.getAttribute(const.ATTR_END2)

    def setEnd2ID(self, id):
        self.setAttribute(const.ATTR_END2, id)
        self.updateModifiedTime()

    def getEnd1(self):
        return self._find_end_point(self.getEnd1ID())

    def getEnd2(self):
        return self._find_end_point(self.getEnd2ID())

    def getTitle(self):
        title = self._get_title()
        if title:
            title = TitleElement(title, self.getOwnerWorkbook())
            return title.getTextContent()

    def setTitle(self, text):
        _title = self._get_title()
        title = TitleElement(_title, self.getOwnerWorkbook())
        title.setTextContent(text)

        if _title is None:
            self.appendChild(title)

        self.updateModifiedTime()


class RelationshipsElement(WorkbookMixinElement):
    TAG_NAME = const.TAG_RELATIONSHIPS

    def __init__(self, node=None, ownerWorkbook=None):
        super(RelationshipsElement, self).__init__(node, ownerWorkbook)


def main():
    pass

if __name__ == "__main__":
    main()
