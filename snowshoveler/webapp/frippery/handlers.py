#vim: set expandtab ts=4 sw=4 filetype=python:

import logging

from snowshoveler.webapp.framework.handler import Handler
from snowshoveler.webapp.framework.response import Response

log = logging.getLogger(__name__)

module_template_prefix = 'snowshoveler'
module_template_package = 'snowshoveler.webapp.snowshoveler.templates'

__all__ = ['Splash']

class Splash(Handler):

    route_strings = set(['GET /'])
    route = Handler.check_route_strings

    def handle(self, req):
        return Response.tmpl('snowshoveler/splash.html')
