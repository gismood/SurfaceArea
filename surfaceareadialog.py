# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SurfaceAreaDialog
                                 A QGIS plugin
 Surface area of polygon
                             -------------------
        begin                : 2012-10-12
        copyright            : (C) 2012 by Johannes Staffans / Gismood
        email                : johannes@bitrite.fi
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_surfacearea import Ui_SurfaceArea
# create the dialog for zoom to point
class SurfaceAreaDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_SurfaceArea()
        self.ui.setupUi(self)
