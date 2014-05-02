#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
    xmind.core.style
    ~~~~~~~~~~~~~~~~~~~

    :mod:``xmind.core.style`` implements the command XMind
    manipulations.

    :copyright:
    :license:
"""

__author__ = "Roc<rocaltair@gmail.com>"

from . import Document
from . import const
from . import Element

STYLE_TOPIC_SHAPE_UNDERLINE = "org.xmind.topicShape.underline"
STYLE_TOPIC_SHAPE_DIAMOND = "org.xmind.topicShape.diamond"

class StylesBookDocument(Document):
	"""`StylesBookDocument` as central object correspond XMind stylebook.
	"""
	def __init__(self, node=None, path=None):
		"""  Construct new `StylesBookDocument` object
		:param node:    pass DOM node object and parse as `StylesBookDocument`
				object. if node not given then created new one.

		:param path:    set workbook will to be placed.
		"""
		super(StylesBookDocument, self).__init__(node)
		self._path = path
		stylesBookNode = self.getFirstChildNodeByTagName(const.TAG_STYLESBOOK)
		self._styleMap = {}
		stylesBookElement = StylesBookElement(stylesBookNode)
		stylesDomNode = stylesBookElement.getFirstChildNodeByTagName(const.TAG_STYLES)
		for styleDomNode in stylesDomNode.childNodes:
			style = StyleElement(styleDomNode)
			styleId = style.getID()
			self._styleMap[styleId] = style
	
	def getStyleElementMap(self):
		return self._styleMap

class StylesBookElement(Element):
	def __init__(self, node=None, ownerStylesBook=None):
		super(StylesBookElement, self).__init__(node)
        	self._owner_stylesbook = ownerStylesBook

class StyleElement(Element):
	"""`StyleElement` for `style`
	`const.TAG_TOPIC_PROPERTIES` names:
		`const.ATTR_SHAPE_CLASS`:
			`style.STYLE_TOPIC_SHAPE_UNDERLINE`
			`style.STYLE_TOPIC_SHAPE_DIAMOND`

		`const.ATTR_STYLE_COLOR`:
			"#FF0000"
	"""
	TAG_NAME = const.TAG_STYLE
	def __init__(self, node=None, ownerStylesBook=None):
		super(StyleElement, self).__init__(node)
        	self._owner_stylesbook = ownerStylesBook

	def getID(self):
		return self.getAttribute(const.ATTR_ID)

	def getPropertyByName(self, attrName):
		"""see `const.TAG_TOPIC_PROPERTIES` names and values
		"""
		propertiesDomNode = self.getFirstChildNodeByTagName(const.TAG_TOPIC_PROPERTIES)
        	if not propertiesDomNode.hasAttribute(attrName):
			return None
		return propertiesDomNode.getAttribute(attrName)

def main():
	pass

if __name__ == "__main__":
	main()

