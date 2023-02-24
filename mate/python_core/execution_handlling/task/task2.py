class SlowResponse(Exception):
    def __init__(self, name: str, response: int) -> None:
        self.name = name
        self.response = response

    def __str__(self) -> str:
        return f"Warning! {self.name} has a slow response of {self.response} ms."


class ExtraSlowResponse(SlowResponse):
    def __str__(self) -> str:
        return f"Alarm! {self.name} has a very slow response of {self.response} ms."


class DangerouslySlowResponse(ExtraSlowResponse):
    def __str__(self) -> str:
        return (f"Nuclear power station is under the danger! {self.name}"
                f" has a dangerously slow response of {self.response} ms.")


def check_device_response(device: dict) -> None:
    name = device["name"]
    response = device["response"]

    if response > 100:
        raise DangerouslySlowResponse(name=name, response=response)
    if response >= 76:
        raise ExtraSlowResponse(name=name, response=response)
    if response >= 51:
        raise SlowResponse(name=name, response=response)


def check_station_devices(devices: list[dict]) -> None:
    incorrect_count = 0
    for device in devices:
        try:
            check_device_response(device)
        except DangerouslySlowResponse as ex:
            print(ex, "We have a serious troubles!")
            incorrect_count += 1
        except ExtraSlowResponse as ex:
            print(ex, "Needs to be repaired!")
            incorrect_count += 1
        except SlowResponse as ex:
            print(ex, "Take attention!")
            incorrect_count += 1
    if incorrect_count == 0:
        print("Responses of all devices does not exceed the norm.")
