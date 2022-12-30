"""Discover chessnut Air devices.
See pdf file Chessnut_comunications.pdf 
for more information."""

import asyncio
import logging


from bleak import BleakScanner, BleakClient
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
from constants import DEVICELIST


class GetChessnutAirDevices:
        
    def __init__(self, timeout=10.0):
        self.deviceNameList = DEVICELIST # valid device names
        self.device = self.advertisement_data = None


    def filter_by_name(
        self,
        device: BLEDevice,
        advertisement_data: AdvertisementData,
    ) -> None:
        """Callback for each discovered device.
        return True if the device name is in the list of valid device names"""
        if any(ext in device.name for ext in self.deviceNameList):
            self.device = device            
            return True
        else:
            return False

    async def discover(self, timeout=10.0):
        """Scan for chessnut Air devices"""
        print("scanning, please wait...")
        await BleakScanner.find_device_by_filter(
            self.filter_by_name)
        if self.device is None:
            print("No chessnut Air devices found")
            return

        print("done scanning")



#if __name__ == "__main__":
#    connect = GetChessnutAirDevices()
#    asyncio.run(connect.discover())
