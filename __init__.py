# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TreeSpeciesIdentificator
                                 A QGIS plugin
 This plugin helps to identify the spicies of trees.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-05-12
        copyright            : (C) 2022 by Ninel V
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
    """Load TreeSpeciesIdentificator class from file TreeSpeciesIdentificator.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .tree_species_identificator import TreeSpeciesIdentificator
    return TreeSpeciesIdentificator(iface)
