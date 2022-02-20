# The MIT License (MIT)
#
# Copyright (c) 2014 Christian Stade-Schuldt
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Library to work with a Piko inverter from Kostal."""

import urllib.request as urllib
import time

class Piko():
    def __init__(self, host=None, username='pvserver', password='pvwr'):
        self.host = host
        self.username = username
        self.password = password
        self.lastUpdate = 0
        self.data = null

    def get_logdaten_dat(self):
        pass

    def get_current_power(self):
        """returns the current power in W"""
        return int(getField(self._get_raw_content(), 'current'))

    def get_total_energy(self):
        """returns the total energy in kWh"""
        return int(getField(self._get_raw_content(), 'total energy'))

    def get_daily_energy(self):
        """returns the daily energy in kWh"""
        return int(getField(self._get_raw_content(), 'daily energy'))
        
    def getField(html, name):
        start = html.find(name + '</td>')
        start = html.find('F">', start) + 3
        end = html.find('</td>', start)
        value = html[start: end].strip()
        if value.find('x') == -1:
            return value
        else:
            return 0

    def _get_raw_content(self):
        if time.time() < self.lastUpdate + MIN_TIME_BETWEEN_UPDATES and self.data != null:
            return self.data
        self.lastUpdate = time.time()
    
        url = "http://" + self.host;
        print("Opening " + url);
    
        passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, url, self.username, self.password)
        authhandler = urllib.request.HTTPBasicAuthHandler(passman)
        opener = urllib.request.build_opener(authhandler)
        urllib.request.install_opener(opener)

        res = urllib.request.urlopen(url)
        html = res.read().decode('utf-8')
        
        self.data = html
        return html
