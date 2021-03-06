# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import rj.site


class RjSiteLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=rj.site)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'rj.site:default')


RJ_SITE_FIXTURE = RjSiteLayer()


RJ_SITE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(RJ_SITE_FIXTURE,),
    name='RjSiteLayer:IntegrationTesting'
)


RJ_SITE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(RJ_SITE_FIXTURE,),
    name='RjSiteLayer:FunctionalTesting'
)


RJ_SITE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        RJ_SITE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='RjSiteLayer:AcceptanceTesting'
)
