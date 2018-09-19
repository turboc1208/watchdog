import appdaemon.plugins.hass.hassapi as hass
import datetime
import time
sinclude('../myappapi.pyi')
class watchdog(hass.Hass):

  def initialize(self):
    # self.LOGLEVEL="DEBUG"
    self.log("watchdog App")
    ADUtils=self.get_app("ADutils")
