import csv
import pandas as pd
from job import Job


class JobManager:
    """
    Represents management of a simple job allocation system.

    This class stores multiple cases of job instances and objects, which allows the user ability to perform
    various tasks such as adding jobs, removing jobs, editing jobs, searching jobs (distinct) searches;
    search by name, category and/or rate, calculate total rates for each worker,allows the ability to
     load from any given file within the repository and save to any given repository

    Attributes include:
        __jobs: a form of name-mangling (encapsulation)
    """

    def __init__(self, jobs=None):
        """
        A constructor that initialises the JobManager object. The jobs parameter is optional.
        If a jobs value is not provided (i.e., None),
        then initialise the list of jobs objects to be an empty list,
        else, set it to the given list of jobs objects
        """
        if jobs == None:
            self.__jobs = [] # Empty List
        else:
            self.__jobs = jobs

    def get_jobs(self):
        """
        Returns a method to return the list of jobs objects.
        Returns:
            list: a list containing all the job objects.
        """
        return self.__jobs

    def __str__(self):
        """
        Returns a string representation of the job manager.
        Returns:
            str: a string showing all the list of job objects.
        """
        return f" {self.get_jobs()}"

    def __repr__(self):
        """
        Returns the formal string representation of the job manager.
        Returns:
            repr: a string representation suitable for developers for debugging.
        """
        return self.__str__()

    def add_job(self, job):
        """
        Returns a method which adds a job to the job manager if the worker is available.
        Returns:
            Job: The job object to add.
        """
        self.__jobs.append(job) # Stores the job into the list

    def remove_job(self, job):
        """
        Returns a method which removes an existing job from the job manager.
        Returns:
            Job: The job object to remove
        """
        self.__jobs.remove(job)

    def edit_job(self, old_job, new_job):
        """
        Returns a method which edits an existing job in the job manager if the worker is available.
        This method searches for the occurrence  of 'old_job' and replaces it with 'new_job'
        and prints a formatted string stating the old jobs name 'is being replaced by'
        by the new jobs name.

        Parameters:
            old_job: The job object being replaced
            new_job: The new job object being inserted in the new jobs place.
        """
        for i in range(len(self.__jobs)):
            if self.__jobs[i] == old_job:
                print(f"Old job {old_job.get_category()} is being replaced by {new_job.get_category()}")
                self.__jobs[i] = new_job
        return self.__jobs


    def search_by_category(self, category):
        """
        Returns a method which returns a list of all jobs that completely matches the given category (string).
        Returns:
            category (str): The job category to search for
        Raises:
            ValueError: If the category written is not a string
        """
        if not isinstance(category, str): # Value checks
            raise ValueError("category must be a string")

        existing_job = []
        for job in self.__jobs:
            if job.get_category() == category:
                existing_job.append(job)
        return existing_job


    def search_by_rate(self, rate):
        """
        Returns a method returns a list of all jobs that completely matches the given rate (float)
        Returns:
            rate (float): the rate of the worker

        Raises:
            TypeError: if the rate is not a float
            ValueError: if the rate is not positive
        """
        if not isinstance(rate, float):
            raise TypeError("rate must be a float")
        if rate <= 0:
            raise ValueError("rate can only be positive")

        existing_rate = []
        for job in self.__jobs:
            if job.get_rate() == rate:
                existing_rate.append(job)
        return existing_rate

    def search_by_name_and_date(self, name, date):
        """
        Returns a method returns a list of all jobs that completely matches the
         given name (string) and date (string)
        Returns:
            name (str) & date (str): name and date of the worker

        Raises:
            TypeError: if the name is not a string
            TypeError: if the date is not a string
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string") # Type checks
        elif not isinstance(date, str):
            raise TypeError("date must be a string") # Type checksa

        existing_name_date = []
        for job in self.__jobs:
            if job.get_name() == name and job.get_date() == date:
                existing_name_date.append(job)
        return existing_name_date

    def get_total_cost_per_name(self, names):
        """
        Returns a method returns a dictionary that maps each worker found in names (list of string)
        to the total cost (float) of the work allocated in the system for that worker.
        Returns:
            name (str) * rate (float) than displays their total wage
        """
        result = {}
        for job in self.__jobs:
            name = job.get_name()
            if name in names:
                hours = job.get_hours()
                rate = job.get_rate()
                if name not in result:
                    result[name] = hours * rate # Multiples hours with rate to calculate total cost
                else:
                    result[name] += (hours * rate)
        return result

    def get_category_count_per_name(self):
        """
        This method returns a dictionary that maps name (string) to a dictionary,
        that maps category (string) to the total number of jobs (int)
         of that category found in the system.
         Returns:
             name (str) & category (str): Total amount of times a worker has worked.
        """
        category_count = {
        }
        for job in self.__jobs:
            name = job.get_name()
            category = job.get_category()
            if name not in category_count:
                category_count[name] = set() # If the name is not seen before, it appends it to the dictionary

            category_count[name].add(category)

        for name in category_count: # Loops through each name in the category
            category_count[name] = len(category_count[name])
        return category_count

    file_name = "sample_data.csv" # csv file in use

    def load_from_file(self, file_name):
        """
        Returns a  method reads a csv file of job details and adds them to the list of job objects
        Returns:
            load_from_file which uses the panda library to load and store from the file of
            "sample_data.csv" assigned to 'file_name'
        """
        df = pd.read_csv(file_name)
        self.__jobs = []
        for _, row in df.iterrows(): # Loops through each row in the df (dataframe) and returns each row as a pair
            job = Job(
                row["name"],
                row["category"],
                row["rate"],
                row["date"],
                row["hours"] # Creates a new job instance by passing data from the CSV to the constructor
            )
            self.__jobs.append(job)

    def save_to_file(self, file_name):
        """
        Returns a method which writes to a csv file all job details found in the list of job objects
        Returns:
            save_to_file which you can add multiple job objects which when executed stores them into
            "sample_data.csv" allowing you to save from file
        save_to_file also inherits the same document of 'file_name' as "load_from_file"
        """
        df = pd.DataFrame([job.__dict__  for job in self.__jobs])
        df = df.rename(columns={"_Job__name": "name", "_Job__category": "category", "_Job__rate": "rate",
                           "_Job__date": "date", "_Job__hours": "hours"}) # Ensures each column has a title
        df.to_csv(file_name, index = False) # Ensures the index begins with 1 instead of 0 in the job list





