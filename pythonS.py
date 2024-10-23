class HomeAutomation:
    def __init__(self):
        self.lights_on = False
        self.temperature = 20  # Default temperature in Celsius

    def toggle_lights(self):
        self.lights_on = not self.lights_on
        state = "on" if self.lights_on else "off"
        print(f"Lights turned {state}.")

    def set_temperature(self, temp):
        if 16 <= temp <= 30:  # Assuming a safe range for temperature
            self.temperature = temp
            print(f"Temperature set to {self.temperature}°C.")
        else:
            print("Please set the temperature between 16°C and 30°C.")

    def show_status(self):
        lights_state = "on" if self.lights_on else "off"
        print(f"Lights: {lights_state}, Temperature: {self.temperature}°C")

if __name__ == "__main__":
    home = HomeAutomation()

    while True:
        print("\nHome Automation Menu:")
        print("1. Toggle Lights")
        print("2. Set Temperature")
        print("3. Show Status")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            home.toggle_lights()
        elif choice == '2':
            try:
                temp = int(input("Enter desired temperature (16-30°C): "))
                home.set_temperature(temp)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            home.show_status()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
