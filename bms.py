import time
import random

class BatteryManagementSystem:
    def __init__(self):
        self.battery_voltage = 12.5  
        self.battery_temperature = 25  
        self.battery_charge = 85  
        self.min_voltage = 11.0  
        self.max_voltage = 14.5  
        self.max_temperature = 50  
        self.min_temperature = 0  
        self.min_charge = 20 
    
    def get_battery_status(self):
        self.battery_voltage = random.uniform(10.5, 15.0)
        self.battery_temperature = random.uniform(-5, 60)
        self.battery_charge = random.randint(10, 100)
        
        return {
            "voltage": self.battery_voltage,
            "temperature": self.battery_temperature,
            "charge": self.battery_charge
        }
    
    def check_battery_conditions(self):
        status = self.get_battery_status()
        voltage = status["voltage"]
        temperature = status["temperature"]
        charge = status["charge"]
        
       
        if voltage < self.min_voltage:
            print("⚠️ Warning: Low Voltage Detected!")
        elif voltage > self.max_voltage:
            print("⚠️ Warning: High Voltage Detected!")
        
        if temperature < self.min_temperature:
            print("⚠️ Warning: Low Temperature Detected!")
        elif temperature > self.max_temperature:
            print("⚠️ Warning: High Temperature Detected!")
        
       
        if charge < self.min_charge:
            print("⚠️ Warning: Low Battery Charge Detected!")
        
        
        print(f"Current Voltage: {voltage:.2f}V, Temperature: {temperature:.2f}°C, Charge: {charge}%")
    
    def notify(self):
       
        while True:
            self.check_battery_conditions()
            time.sleep(5)  


if __name__ == "__main__":
    bms = BatteryManagementSystem()
    bms.notify()
