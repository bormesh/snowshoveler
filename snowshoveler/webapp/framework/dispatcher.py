# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf-8:
# -*- coding: utf-8 -*-

import logging

from horsemeat.webapp import dispatcher

from snowshoveler.webapp.framework import request

log = logging.getLogger(__name__)

class Dispatcher(dispatcher.Dispatcher):

    request_class = request.Request

    def make_handlers(self):

        log.info('Making snowshoveler handlers...')

        self.handlers.extend(self.make_handlers_from_module_string(
            'snowshoveler.webapp.mockups.handlers'))

        self.handlers.extend(self.make_handlers_from_module_string(
            'snowshoveler.webapp.dashboard.handlers'))

        self.handlers.extend(self.make_handlers_from_module_string(
            'snowshoveler.webapp.snowshoveler.handlers'))

        self.handlers.extend(self.make_handlers_from_module_string(
            'snowshoveler.webapp.notfound.handlers'))

    @property
    def error_page(self):

        log.debug("Getting error template...")

        j = self.cw.get_jinja2_environment()

        t = j.get_template('snowshoveler/error.html')

        return t

