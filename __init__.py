# -*- coding: utf-8 -*-
"""
/***************************************************************************
 cFGH
                                 A QGIS plugin
 Un plugon fantastique
                             -------------------
        begin                : 2015-12-04
        copyright            : (C) 2015 by Robin
        email                : robin.prest@anteagroup.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load cFGH class from file cFGH.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .fFGH import cFGH
    return cFGH(iface)
