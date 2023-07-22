# encoding: utf-8
# module PyQt5.QtXml
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


from .QXmlContentHandler import QXmlContentHandler

from .QXmlErrorHandler import QXmlErrorHandler

from .QXmlDTDHandler import QXmlDTDHandler

from .QXmlEntityResolver import QXmlEntityResolver

from .QXmlLexicalHandler import QXmlLexicalHandler

from .QXmlDeclHandler import QXmlDeclHandler

class QXmlDefaultHandler(QXmlContentHandler, QXmlErrorHandler, QXmlDTDHandler, QXmlEntityResolver, QXmlLexicalHandler, QXmlDeclHandler):
    """ QXmlDefaultHandler() """
    def attributeDecl(self, eName, aName, type, valueDefault, value): # real signature unknown; restored from __doc__
        """ attributeDecl(self, eName: str, aName: str, type: str, valueDefault: str, value: str) -> bool """
        return False

    def characters(self, ch): # real signature unknown; restored from __doc__
        """ characters(self, ch: str) -> bool """
        return False

    def comment(self, ch): # real signature unknown; restored from __doc__
        """ comment(self, ch: str) -> bool """
        return False

    def endCDATA(self): # real signature unknown; restored from __doc__
        """ endCDATA(self) -> bool """
        return False

    def endDocument(self): # real signature unknown; restored from __doc__
        """ endDocument(self) -> bool """
        return False

    def endDTD(self): # real signature unknown; restored from __doc__
        """ endDTD(self) -> bool """
        return False

    def endElement(self, namespaceURI, localName, qName): # real signature unknown; restored from __doc__
        """ endElement(self, namespaceURI: str, localName: str, qName: str) -> bool """
        return False

    def endEntity(self, name): # real signature unknown; restored from __doc__
        """ endEntity(self, name: str) -> bool """
        return False

    def endPrefixMapping(self, prefix): # real signature unknown; restored from __doc__
        """ endPrefixMapping(self, prefix: str) -> bool """
        return False

    def error(self, exception): # real signature unknown; restored from __doc__
        """ error(self, exception: QXmlParseException) -> bool """
        return False

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def externalEntityDecl(self, name, publicId, systemId): # real signature unknown; restored from __doc__
        """ externalEntityDecl(self, name: str, publicId: str, systemId: str) -> bool """
        return False

    def fatalError(self, exception): # real signature unknown; restored from __doc__
        """ fatalError(self, exception: QXmlParseException) -> bool """
        return False

    def ignorableWhitespace(self, ch): # real signature unknown; restored from __doc__
        """ ignorableWhitespace(self, ch: str) -> bool """
        return False

    def internalEntityDecl(self, name, value): # real signature unknown; restored from __doc__
        """ internalEntityDecl(self, name: str, value: str) -> bool """
        return False

    def notationDecl(self, name, publicId, systemId): # real signature unknown; restored from __doc__
        """ notationDecl(self, name: str, publicId: str, systemId: str) -> bool """
        return False

    def processingInstruction(self, target, data): # real signature unknown; restored from __doc__
        """ processingInstruction(self, target: str, data: str) -> bool """
        return False

    def resolveEntity(self, publicId, systemId): # real signature unknown; restored from __doc__
        """ resolveEntity(self, publicId: str, systemId: str) -> Tuple[bool, QXmlInputSource] """
        pass

    def setDocumentLocator(self, locator): # real signature unknown; restored from __doc__
        """ setDocumentLocator(self, locator: QXmlLocator) """
        pass

    def skippedEntity(self, name): # real signature unknown; restored from __doc__
        """ skippedEntity(self, name: str) -> bool """
        return False

    def startCDATA(self): # real signature unknown; restored from __doc__
        """ startCDATA(self) -> bool """
        return False

    def startDocument(self): # real signature unknown; restored from __doc__
        """ startDocument(self) -> bool """
        return False

    def startDTD(self, name, publicId, systemId): # real signature unknown; restored from __doc__
        """ startDTD(self, name: str, publicId: str, systemId: str) -> bool """
        return False

    def startElement(self, namespaceURI, localName, qName, atts): # real signature unknown; restored from __doc__
        """ startElement(self, namespaceURI: str, localName: str, qName: str, atts: QXmlAttributes) -> bool """
        return False

    def startEntity(self, name): # real signature unknown; restored from __doc__
        """ startEntity(self, name: str) -> bool """
        return False

    def startPrefixMapping(self, prefix, uri): # real signature unknown; restored from __doc__
        """ startPrefixMapping(self, prefix: str, uri: str) -> bool """
        return False

    def unparsedEntityDecl(self, name, publicId, systemId, notationName): # real signature unknown; restored from __doc__
        """ unparsedEntityDecl(self, name: str, publicId: str, systemId: str, notationName: str) -> bool """
        return False

    def warning(self, exception): # real signature unknown; restored from __doc__
        """ warning(self, exception: QXmlParseException) -> bool """
        return False

    def __init__(self): # real signature unknown; restored from __doc__
        pass


