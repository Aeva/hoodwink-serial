

# This file is part of Hoodwink-Serial.
#
# Hoodwink-Serial is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Hoodwink-Serial is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hoodwink-Serial.  If not, see
# <http://www.gnu.org/licenses/>.


class Serial(object):
    """Fake serial port object."""

    def __init__(self,
                 port = None,
                 baudrate=0,
                 timeout=None, **kargs):
        pass

    def open(self):
        pass

    def close(self):
        pass
    
    def read(self, size=1):
        pass

    def write(self, data):
        pass

    def flush(self):
        pass
    
    def setRTS(self, level=1):
        pass

    def setDTR(self, level=1):
        pass

    
