# -*- coding: utf-8 -*-

# Progress Bar Add-on for Anki
#
# Copyright (C) 2017-2021  Aristotelis P. <https://glutanimate.com/>
#                          and contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the license file that accompanied this program.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License that
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.

"""
Initializes add-on components.
"""


from ._version import __version__  # noqa: F401

from .libaddon import maybeVendorTyping

maybeVendorTyping()


def initialize_addon():
    """Initializes add-on after performing a few checks
    
    Allows more fine-grained control over add-on execution, which can
    be helpful when implementing workarounds for Anki bugs (e.g. the module
    import bug present in all Anki 2.1 versions up to 2.1.14)
    """

    from .libaddon import checkFor2114ImportError
    from .consts import ADDON

    if not checkFor2114ImportError(ADDON.NAME):
        return False

    from .consts import ADDON
    from .libaddon.consts import setAddonProperties

    setAddonProperties(ADDON)

    # from .libaddon.debug import maybeStartDebugging

    # maybeStartDebugging()

    from . import progress # noqa


initialize_addon()
