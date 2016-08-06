# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
# from .zotero import zot

import markdown

ZOTERO_RE = r'\[zotero\:(?P<ref>[A-Z0-9]*)\|(?P<backup>[^\]]*?)\]'

class ZoteroPattern(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        # mla = zot.top(itemKey=m.group(2), format='json', include='bib', style="mla")[0]["bib"]
        # json = zot.top(itemKey=m.group(2))[0]
        mla = "a"
        json = {{"data":{"date":"a"}}, {"links":{"alternate":"b"}}}
        tstring = json["data"]["creators"][0]["lastName"] + ", " + json["data"]["date"]
        link = json["links"]["alternate"]["href"]
        el = markdown.util.etree.Element("a")
        el.attrib["id"] = m.group(2)
        el.attrib["class"] = "zotero-span"
        el.attrib["data-toggle"] = "popover"
        el.attrib["data-trigger"] = "mouseenter"
        el.attrib["title"] = mla
        el.attrib["data-content"] = link
        el.text = "[" + tstring + "]"
        return el

class ZoteroTreeProcessor(markdown.treeprocessors.Treeprocessor):
    def run(self, tree):
        # Get all tags
        zotero_tags = []
        for el in tree.iter():
            try:
                if el.attrib["class"] == "zotero-span":
                    if el.attrib["id"] not in zotero_tags:
                        zotero_tags.append(el.attrib["id"])
            except KeyError:
                pass
        # Append something
        if zotero_tags:
            div = markdown.util.etree.Element("div")
            div.text = ""
            for tag in zotero_tags:
                print tag
                div.text += tag + " "
            tree.append(div)
        return tree


class ZoteroExtension(markdown.Extension):

    """ Images plugin markdown extension for django-wiki. """

    def extendMarkdown(self, md, md_globals):
        """ Insert ImagePreprocessor before ReferencePreprocessor. """
        # md.preprocessors.add('dw-zotero', ZoteroPreprocessor(md), '>html_block')
        zot_pattern = ZoteroPattern(ZOTERO_RE, markdown_instance=md)
        zot_pattern.md = md
        md.inlinePatterns.add('dw-zotero-pattern', zot_pattern, "<reference")
        print("extension loaded")
        zot_tree = ZoteroTreeProcessor(md)
        md.treeprocessors.add("dw-zotero-bibtex", zot_tree, "_end")
        # md.postprocessors.add('dw-zotero-summary', ZoteroPostprocessor(md), '>raw_html')


def makeExtension():
    return ZoteroExtension()

# class ZoteroPostprocessor(markdown.postprocessors.Postprocessor):
#
#     def run(self, text):
#         return text