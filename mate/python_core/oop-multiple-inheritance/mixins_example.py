class Transport:
    def __init__(self, name: str, start_point: str, speed: int) -> None:
        self.name = name
        self.start_point = start_point
        self.speed = speed

    @staticmethod
    def drive(start_point, end_point: str) -> None:
        print(f"From {start_point} to {end_point}")

    
class AlarmMixin:
    def __init__(self) -> None:
        self.turn_on_off = False

    def change_status(self) -> None:
        self.turn_on_off = False if self.turn_on_off else True
        if self.turn_on_off:
            print("Alarm is turned off")
        else:
            print("Alarm is turned on")


class AutoPilotMixin:
    def __init__(self, is_turned: bool) -> None:
        self.is_turned = is_turned
        
    def turn_on_off_auto_pilot(self) -> None:
        self.is_turned = False if self.is_turned else True


class RadioMixin:
    def __init__(self, radio_name: str) -> None:
        self.radio_name = radio_name
        self.radio_is_on = False

    def turn_on_off_radio(self) -> None:
        self.radio_is_on = False if self.radio_is_on else True


class Car(Transport, AlarmMixin, AutoPilotMixin, RadioMixin):
    def __init__(self, name: str, start_point: str, speed: int):
        super().__init__(name, start_point, speed)


vito = Car("Mersedes Vito", "Kiev", 100)
vito.change_status()
