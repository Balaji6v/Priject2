# Base TV Class
class TV:
    def __init__(self, brand, price, inches):
        self.brand = brand
        self.price = price
        self.inches = inches
        self.channel = 1  # Default channel
        self.volume = 50  # Default volume
        self.is_on = False  # TV starts off
   #powen on and off
    def system_power(self):
        self.is_on = not self.is_on

   #volume increase and decrease
    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        power = "ON" if self.is_on else "OFF"
        return f"{self.brand} {power}, Channel: {self.channel}, Volume: {self.volume}"


# LED TV Class
class LedTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        return (
            f"{self.brand} LED TV\n"
            f"Screen Thickness: {self.screen_thickness}\n"
            f"Energy Usage: {self.energy_usage}W\n"
            f"Lifespan: {self.lifespan} hours\n"
            f"Refresh Rate: {self.refresh_rate} Hz\n"
        )


# Plasma TV Class
class PlasmaTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        return (
            f"{self.brand} Plasma TV\n"
            f"Screen Thickness: {self.screen_thickness}\n"
            f"Energy Usage: {self.energy_usage}W\n"
            f"Lifespan: {self.lifespan} hours\n"
            f"Refresh Rate: {self.refresh_rate} Hz\n"
        )
