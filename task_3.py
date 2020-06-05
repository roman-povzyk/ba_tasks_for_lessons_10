class TVController:

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    def first_channel(self):
        return self.CHANNELS[0]

    def last_channel(self):
        return self.CHANNELS[-1]

    def turn_channel(self, number):
        self.number = number
        return self.CHANNELS[self.number - 1]

    def next_channel(self):
        return self.CHANNELS[self.number % 3]

    def previous_channel(self):
        return self.CHANNELS[self.number - 1]

    def current_channel(self):
        return self.CHANNELS[self.number - 1]

    def is_exist(self, num_name):
        self.num_name = num_name

        if str(self.num_name).isdigit():
            if num_name < len(self.CHANNELS) or num_name > len(self.CHANNELS):
                return "No"
            else:
                return "Yes"

        else:
            if self.num_name in self.CHANNELS:
                return "Yes"
            else:
                return "No"

controller = TVController()
print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
print(controller.is_exist("BBC"))



