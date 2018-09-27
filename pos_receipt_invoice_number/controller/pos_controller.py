# -*- coding: utf-8 -*
from odoo.http import request
from odoo.addons.bus.controllers.main import BusController
from odoo import api, http, SUPERUSER_ID
from odoo.addons.web.controllers.main import ensure_db, Home, Session, WebClient
from odoo.addons.point_of_sale.controllers.main import PosController
from odoo.addons.base.ir.ir_qweb import AssetsBundle
import json
import logging
import base64
import werkzeug.utils

_logger = logging.getLogger(__name__)
