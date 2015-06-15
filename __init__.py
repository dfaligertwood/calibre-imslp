# -*- coding: utf-8 -*-

from calibre.customize import InterfaceActionBase

class InterfacePluginDemo(InterfaceActionBase):
    name                    = 'IMSLP search'
    description             = ("Searches IMSLP/Petrucci for keywords using "
                               "IMSLP opensearch. NB. This is *very* flawed "
                               "- IMSLP\'s search engine only recognises words "
                               "which appear in the title. It will not return "
                               "items appearing in compilations, for example."
    supported_platforms     = ['osx']
                            # Probably works on others. Not tested yet.
    author                  = 'Douglas Ligertwood'
    version                 = (1, 0, 0)
    minimum_calibre_bersion = (2, 30, 0)

    actual_plugin           = 'calibre_plugins.imslp.ui:PetrucciPlugin'
