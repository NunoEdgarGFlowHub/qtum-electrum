from qtum_electrum.plugins import hook
from qtum_electrum.util import print_msg
from .keepkey import KeepKeyPlugin
from ..hw_wallet import CmdLineHandler
from qtum_electrum.plugins import hook


class Plugin(KeepKeyPlugin):
    handler = CmdLineHandler()

    @hook
    def init_keystore(self, keystore):
        if not isinstance(keystore, self.keystore_class):
            return
        keystore.handler = self.handler
