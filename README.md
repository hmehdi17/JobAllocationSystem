Job Allocation System - Overview
================
This project consisted of a simple job allocation system in Python using two main classes:
Job - Represents a single allocated job
JobManager - Manages the list of jobs presented and provides various methods for searching 
editing, saving and loading jobs into the respective files.

This system allows the functionality of retrieving all jobs and their details from the application with the validation
of ensuring name is a string, category is a string, rate is a float, date is a string and hours is an integer.
Furthermore, the system only allows positive values for rate and hours and ensures that the system cannot allocate more
than 6 hours of work per job.
The system also allows the ability for you to add, edit and delete job instances whilst also allowing you to search
the jobs by either category or rate which outputs all the matching job instances.
This system is built in such a way where you are able to calculate the total cost of the allocated worker and gives
you the ability to store data such as loading and saving to a csv file.

Required Installations
================
Please make sure to install the following modules before running & testing the program:
Panda3D - Write 'pip install panda3d' in the Terminal to install panda so you can run
'load_from_file' and 'save_to_file'

PyTest - Write 'pip install pytest' in the Terminal to actually perform the tests in 'test_job.py'
and 'test_job_manager.py'.

Usage
================
You are able to run the PyTests by pressing the green play button on the top of screen, this will run all the tests 
written and displays the results of them in the Terminal either saying 'name_of_test' 'PASSED' or 'FAILED' but in this case
all of them have passed.

You are able to substitute some of the tests to your liking giving you more immersion over this system,
I will provide the following which you are able to change yourself to see how the program works.

1 - def_test_edit_jobs() - Line 93 - test_job_manager.py
You are able to substitute 'old_job' and 'new_job' with any of the 8 instances presented on the top of the file 
simply, just copy and paste one for 'old_job' such as job5 and one for 'new_job' such as job7, and copy
them (excluding job(x), x being the job number assigned to like job(7)) just include "Job(....)" as shown on the ones
already being tested on.
After you change the jobs to your liking, you are able to execute the program and see the new display message of job5 
being replaced by job7.

2 - def test_total_cost_per_name() - Line 224 - test_job_manager.py
You are able to find the various total costs (rates) for any worker, you can either add more job instances from the list
provided on the top of the page or simply change the name of the worker already provided in the job instances such as
instead of 'Marc Velti' written on line 251 and 253, you can change it to 'Simonette Thirkettle' on both lines and it would
output the total cost of Simonette Thirkettle when you execute the program.

3 - def test_save_to_file() - Line 320 - test_job_manager.py 
You are able to save various job instances into 'sample_data.csv' by simply adding more job instances with the rest of 
the job instances in test_save_to_file. There are already 3 job instances saved to the relevant csv file, so you are able
to pick one or more other job instances from the top of the page copy and paste them under the last job instance being job3
in this case, than write the valid assertions for them under the last assertion in the exact same way but changing the job
number. For example if you chose the job4 instance copy and pasted it than for the assertion you would write 
assert (job4 in jobmanager_new.get_jobs()) run the test than open the "sample_data.csv" file in the repository than you will see
the new job added essentially saved to file.










