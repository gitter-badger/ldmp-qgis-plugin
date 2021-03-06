# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LDMP - A QGIS plugin
 This plugin supports monitoring and reporting of land degradation to the UNCCD 
 and in support of the SDG Land Degradation Neutrality (LDN) target.
                              -------------------
        begin                : 2017-05-23
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Conservation International
        email                : GEF-LDMP@conservation.org
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui

from LDMP.gui.DlgAbout import Ui_DlgAbout as UiDialog

class DlgAbout(QtGui.QDialog, UiDialog):
    def __init__(self, parent=None):
        """Constructor."""
        super(DlgAbout, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        VS_logo = QtGui.QPixmap(':/plugins/LDMP/icons/VS_logo.png')
        self.VS_logo.setPixmap(VS_logo)
        self.VS_logo.show()
        
        CI_logo = QtGui.QPixmap(':/plugins/LDMP/icons/CI_logo.png')
        self.CI_logo.setPixmap(CI_logo)
        self.CI_logo.show()
