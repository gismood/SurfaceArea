# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SurfaceArea
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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "Surface area of polygon"
def description():
    return "Surface area of polygon"
def version():
    return "Version 0.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load SurfaceArea class from file SurfaceArea
    from surfacearea import SurfaceArea
    return SurfaceArea(iface)
