# -*- coding: utf-8 -*-
from odoo import models, fields
class agenda(models.Model):

    #_name es el nombre de referencia del modelo: nombreDelModulo.nombreDeLaClase
    _name = 'agenda.agenda'
    _description = 'Representa cada uno de los registros de la agenda'
    _order = 'name'

    #Los campos indican qué almacena el objeto y dónde
    #name es un nombre especial que Odoo usará para referenciar el objeto
    name = fields.Char('Nombre', required = True, help='Nombre del contacto')
    telefono = fields.Char('Teléfono', required = True, size=9, help='9 dígitos')

