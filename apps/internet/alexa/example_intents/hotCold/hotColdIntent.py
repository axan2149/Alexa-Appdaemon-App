import appdaemon.plugins.hass.hassapi as hass
import random

class hotColdIntent(hass.Hass):

    def initialize(self):
        return

    def getIntentResponse(self, slots, devicename):
        if slots["feeling"].lower() == "kalt":
            for thermostat in self.args[devicename]["thermostats"]:
                valuenow = self.get_state(thermostat)
                self.run_in(self.set_thermostat_back,1880,thermostat=thermostat,oldvalue=valuenow)
                self.call_service("input_number/set_value", entity_id=thermostat, value=25.0)
            text = self.args["coldTextline"]
        elif slots["feeling"].lower() == "warm":
            for thermostat in self.args[self.devicename]["thermostats"]:
                valuenow = self.get_state(thermostat)
                self.run_in(self.set_thermostat_back,1880,thermostat=thermostat,oldvalue=valuenow)
                self.call_service("input_number/set_value", entity_id=thermostat, value=16.0)
            text = self.args["warmTextline"]
        else:
            text = self.args["Error"]
        return text 

    def set_thermostat_back(self,kwargs):
        self.call_service("input_number/set_value", entity_id=kwargs["thermostat"], value=kwargs["oldvalue"])
