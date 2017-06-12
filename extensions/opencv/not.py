#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Not class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.plugin import Plugin


class Not(Plugin):
    """
    This class contains methods related the Not class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        Plugin.__init__(self)

        # Appearance
        self.help = "Realiza a negação lógica de uma imagem. " + \
            "Corresponde à negativa da imagem."
        self.label = "Not"
        self.color = "10:180:10:150"
        self.in_ports = [{"type":"mosaicode.extensions.c.ports.image",
                          "name":"input_image",
                          "label":"Input Image"}
                         ]
        self.out_ports = [{"type":"mosaicode.extensions.c.ports.image",
                           "name":"output_image",
                           "label":"Output Image"}]
        self.group = "Arithmetic and logical operations"

        self.codes[1] = "IplImage * block$id$_img_i0 = NULL;\n" + \
                    "IplImage * block$id$_img_o0 = NULL;\n"

        self.codes[2] = \
            'if(block$id$_img_i0){\n' + \
            'block$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            'cvNot(block$id$_img_i0, block$id$_img_o0);\n' + \
            '}\n'

        self.codes[3] = "cvReleaseImage(&block$id$_img_i0);\n" + \
                       "cvReleaseImage(&block$id$_img_o0);\n"


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
