class Event:
    """
    Represents a calendar event.

    Attributes:
        title (str): The title of the event.
        date (datetime.date): The date of the event.
        start_time (datetime.time): The start time of the event.
        end_time (datetime.time): The end time of the event.
        description (str): A description of the event.
        participants (list of str): A list of participants.
    """

    def __init__(self, title, date, start_time, end_time, description='', participants=None):
        """
        Initializes a new Event instance.

        Args:
            title (str): The title of the event.
            date (datetime.date): The date of the event.
            start_time (datetime.time): The start time of the event.
            end_time (datetime.time): The end time of the event.
            description (str, optional): A description of the event.
            participants (list of str, optional): A list of participants.
        """
        # TODO: Initialize the event attributes
        pass

    def conflicts_with(self, other_event):
        """
        Determines if this event conflicts with another event.

        Args:
            other_event (Event): The other event to check against.

        Returns:
            bool: True if there is a conflict, False otherwise.
        """
        # TODO: Check if events are on the same date
        # If so, check if the time intervals overlap
        pass

    def __str__(self):
        """
        Returns a string representation of the event.

        Returns:
            str: The string representation of the event.
        """
        # TODO: Format the event details into a string
        pass
