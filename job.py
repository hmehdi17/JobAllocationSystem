class Job:
    """
    Represents a simple job allocation system containing details about the jobs.
    Each job object has details about the 'name', 'category', 'rate', 'date', and 'hours'.
    The class further includes various input invalidations (i.e 'TypeError' & 'Value Error'), accessors
    (getters), basic string representations (i.e 'str' and 'repr'), hash methods and equality methods.

    """

    def __init__(self, name, category, rate, date, hours):
        """
        This is the constructor which Initialise a Job object.

        Parameters:
        name (str): The job holder name.
        category (str): The job category (i.e Teaching or Technical).
        rate (float): The job rate (i.e 14.50 p/hour and must be positive & float).
        date (str): The job date which was performed.
        hours (integer(int)): The job allocated hours (must be positive and
         must be between 1 and 6 hours).

        Raises:
        TypeError: If the parameter has in invalid type such as name not being a string or rate
        not being a float.
        ValueError: If the parameter is not positive such as rate and/or hours is not positive or
        hours is outside the range of 1 and 6.
        """

        if not isinstance(name, str): # Type checks
            raise TypeError("name must be a string")

        if not isinstance(category, str): # Type checks
            raise TypeError("category must be a string")

        if not isinstance(rate, float): # Type checks
            raise TypeError("rate must be a float")
        if rate <= 0: # Value checks
            raise ValueError("rate can only be positive")

        if not isinstance(date, str): # Type checks
            raise TypeError("date must be a string")

        if not isinstance(hours, int): # Value checks
            raise ValueError("hours must be a integer")
        if hours <=0: # Value checks
            raise ValueError("hours can only be positive")
        if hours < 1 or hours > 6: # Value checks
            raise ValueError("hours can only be between 1 and 6")

        """
        These are the attributes being assigned with the use of name-mangling (encapsulation)
        which essentially makes the attributes private with the use of '__' after 'self.'
        """
        # Assign Attributes
        self.__name = name
        self.__category = category
        self.__rate = rate
        self.__date = date
        self.__hours = hours


    def get_name(self):
        """
        Returns the name of the person assigned to the job.
        Returns:
            str: The name of the allocated person.
        """
        return self.__name

    def get_category(self):
        """
        Returns the category (Type) of the job.
        Returns:
            str: the category of the job.
        """
        return self.__category

    def get_rate(self):
        """
        Returns the hourly rate of the job.
        Returns:
            float: the rate per hour of the job (must be positive).
        """
        return self.__rate

    def get_date(self):
        """
        Returns the date of the job (date which the job was performed).
        Returns:
            str: the date of the job.
        """
        return self.__date

    def get_hours(self):
        """
        Returns the number of hours the job was done in.
        Returns:
            int: the number of hours the job was done in.
        """
        return self.__hours

    def __eq__(self, other):
        """
        Compares if two jobs are equal
        Jobs are considered equal if they have the same 'name', 'category', 'rate', 'date'
        and hours.
        Returns True if all attributes are identical, False if they aren't.

        Parameters:
            'other': the other object instance the job(s) is compared with
        Returns:
            bool: True if the jobs are equal, False if otherwise.
        """
        if not isinstance(self, Job): # Compare Test
            return False
        else:
            return (self.__name==other.get_name() and
                    self.__category==other.get_category() and
                    self.__rate==other.get_rate() and
                    self.__date==other.get_date() and
                    self.__hours==other.get_hours())

    def __hash__(self):
        """
        Returns a hash value for the Job.
        The hash is based upon the 'name', 'category', 'rate', 'date' and hours of the job
        to ensure accuracy for the Job equality tests.
        Returns:
            int: Hash value for the Job object.
        """
        return hash((self.get_name(), self.get_category(), self.get_rate(), self.get_date(), self.get_hours()))

    def __str__(self):
        """
        Returns a readable user-friendly string representation of the Job instance,
        Suitable for CSV output.
        Returns:
            str: a string formatted comma-seperated showcasing the 'name', 'category', 'rate',
            'date' and hours of the job.
        """
        return f"Job({self.get_name()}, {self.get_category()}, {self.get_rate()}, {self.get_date()}, {self.get_hours()})"

    def __repr__(self):
        """
        Returns a formal string representation of the Job instance,
        Suitable for developer use for debugging or logs.
        Returns:
            str: A detailed string with attributed values in an readable format.
        """
        return self.__str__()










