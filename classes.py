class Television:
    """
    A class representing details for a television object
    """

    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self, channel=MIN_CHANNEL, volume=MIN_VOLUME, status=False) -> None:
        """
        Constructor to create initial version of a television object
        :param channel: Television's channel
        :param volume: Television's volume
        :param status: Television's status on/off

        """
        self.__channel = channel
        self.__volume = volume
        self.__status = status

    def power(self) -> None:
        """
        Method used to turn the TV on/off.

        """
        if not self.__status:
            self.__status = True
        elif self.__status:
            self.__status = False

    def channel_up(self) -> None:
        """
        Method used to adjust the TV channel by incrementing its value
        If the channel is increased at its maximum, it will roll over to the lowest channel
        Only works when the television status is on
        """
        if self.__status:
            if Television.MIN_CHANNEL <= self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            elif self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method should be used to adjust the TV channel by decrementing its value
        If the channel is decreased at its minimum, it will roll over to the highest channel
        Only works when the television status is on
        """
        if self.__status:
            if Television.MIN_CHANNEL < self.__channel <= Television.MAX_CHANNEL:
                self.__channel -= 1
            elif self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method used to adjust the TV volume by incrementing its value
        Will only increase until it reaches MAX_VOLUME
        Only works when the television status is on
        """
        if self.__status:
            if self.__volume != Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method used to adjust the TV volume by decrementing its value
        Will only decrease until it reaches MIN_VOLUME
        Only works when the television status is on
        """
        if self.__status:
            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method used to return the television's status
        """
        return f'TV Status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

