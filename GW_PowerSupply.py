"""
This class provides functions for communicating with GW Instek DC Power Supply.
It was specifically created for GW PSB2800L, but may be useful on other GW Power Supplies.

Developed by: Mahdi Hayati

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\                           CONTACT ME                         \\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\            gmail              \\   mahdihayati79@gmail.com   \\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\           GitHub              \\        MahdiHayati705       \\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""


import pyvisa


class GW_PSB2800L:

    def __init__(self, port : str):
        self.IDN = 'GW ,PSB-2800L , GEX132567,1.01/V2.05A\n'
        
        self.PS = pyvisa.ResourceManager().open_resource(port)
        self.PS.baud_rate = 57600

    def close(self):
        self.PS.close()

    def IDNCheck(self):
        """
        :return TRUE: Device is detected.
        :return FALSE: Device is not detected.
        """
        try:
            if self.PS.query('*IDN?') == self.IDN:  return 1
            else:                                   return 0
        except:                                     return 0

    def ON(self):
        """
        Turns output ON
        """
        command = ':OUTP 1'
        self.PS.write(command)

    def OFF(self):
        """
        Turns output OFF
        """
        command = ':OUTP 0'
        self.PS.write(command)

    def outputStatus(self):
        """
        :return TRUE: If output is ON
        :return FALSE: If output is OFF
        """
        command = ':OUTP?'
        status = self.PS.query(command)
        return bool(status)

    def voltage(self, value : float):
        """
        Sets the output voltage of power supply.
        
        :param value: voltage value (float) 
        """
        command = f":VOLT {str(value)}"
        self.PS.write(command)

    def readVoltage(self):
        """
        :return Output Voltage: returns output voltage (float)
        """
        command = ":VOLT?"
        value = self.PS.query(command)
        return float(value)
    
    def current(self, value : float):
        """
        Sets the output current of power supply.
        
        :param value: current value (float) 
        """
        command = f":CURR {str(value)}"
        self.PS.write(command)

    def readCurrent(self):
        """
        :return output Current: returns output current (float)
        """
        command = ":CURR?"
        value = self.PS.query(command)
        return float(value)
    
    def OVP(self, value : float):
        """
        Sets Over Voltage Protection

        :param value: Over Voltage Protection value (float) 
        """
        command = f":VOLT:PROT {str(value)}"
        self.PS.write(command)

    def readOVP(self):
        """
        :return Over Voltage Protection Value: (float)
        """
        command = ':VOLT:PROT?'
        value = self.PS.query(command)
        return float(value)

    def OCP(self, value : float):
        """
        Sets Over Current Protection

        :param value: Over Current Protection value (float) 
        """
        command = f":CURR:PROT {str(value)}"
        self.PS.write(command)

    def readOCP(self):
        """
        :return Over Current Protection Value: (float)
        """
        command = ':CURR:PROT?'
        value = self.PS.query(command)
        return float(value)
    
    def power(self, value : float):
        """
        Sets output power value

        :param value: Output power value (float)
        """
        command = f":POW {str(value)}"
        self.PS.write(command)
    
    def readPower(self):
        """
        :return Output Power: (float)
        """
        command = ":POW?"
        value = self.PS.query(command)
        return float(value)