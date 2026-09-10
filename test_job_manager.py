from job_manager import JobManager
from job import Job
import pytest
import pandas as pd


job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)
job4 = Job("Lawrence Matten", "Research Activities", 13.76, "08/08/2024", 5)
job5 = Job("Simonette Thirkettle", "Operational", 15.47, "02/08/2024", 6)
job6 = Job("Corissa Seid", "Operational", 13.58, "06/07/2024", 3)
job7 = Job("Marc Velti", "Senior Invigilation", 17.19, "20/07/2024", 5)
job8 = Job("Kelsey Nelson", "Pilot", 25.50, "02/01/2025", 6)

# Test which gets the jobs
def test_get_jobs():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])
    assert jobmanager.get_jobs() == [job1, job2, job3] # Job instance assertions used for testing

# Test which gets the job within an empty list
def test_get_jobs_empty():
    jobmanager = JobManager()
    assert jobmanager.get_jobs() == []

# Test which gets the job with the correct object
def test_get_jobs_correct_object():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)

    jobmanager = JobManager([job1]) # Initialises the JobManager class with the job

    job_list = jobmanager.get_jobs() # Retrieving the Job

    assert isinstance(job_list[0], Job)

# Test which outputs the job str representation
def test_get_jobs_str():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)

    Anticipated = "Job(Simonette Thirkettle, Teaching and Learning Activities, 13.45, 03/08/2024, 1)"

    assert str(job1) == Anticipated

# Test which outputs the job repr representation
def test_get_jobs_repr():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)

    Anticipated = "Job(Simonette Thirkettle, Teaching and Learning Activities, 13.45, 03/08/2024, 1)"

    assert repr(job1) == Anticipated

# Test which adds given jobs to a list
def test_add_jobs():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager()
    jobmanager.add_job(job1)
    jobmanager.add_job(job2)
    jobmanager.add_job(job3)

    jobs_in_list = jobmanager.get_jobs()

    assert len(jobs_in_list) == 3
    assert jobs_in_list[0] == job1 # Adds job to the list in order by their index like 0 then 1 then 2
    assert jobs_in_list[1] == job2
    assert jobs_in_list[2] == job3

# Test which removes jobs from a given list
def test_remove_jobs():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])

    jobmanager.remove_job(job1)

    jobs_remaining = jobmanager.get_jobs()

    assert len(jobs_remaining) == 2
    assert job1 not in jobs_remaining # Ensures the non-relevant jobs do not appear into the answer

    assert job2 in jobs_remaining
    assert job3 in jobs_remaining

# Test which edits an existing job in the job manager if the worker is available with another job
def test_edit_jobs():
    new_job = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    old_job = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([new_job, old_job])

    result = jobmanager.edit_job(old_job, new_job)

    assert new_job in result
    assert old_job not in result # Ensures the non-relevant jobs do not appear into the answer

# Test which you can search by category
def test_search_by_category():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])

    result = jobmanager.search_by_category("Administration")

    assert len(result) == 1
    assert job1 not in result # Ensures the non-relevant jobs do not appear into the answer
    assert job2 not in result
    assert job3 in result

# Test which stores a category not found in the list, in a list, stored for future use
def test_search_by_category_none_found():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])

    result = jobmanager.search_by_category("Pilot")

    assert result == []

# Test which outputs a ValueError if category is anything but a string
def test_search_by_category_invalid_input():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])

    with pytest.raises(ValueError, match="category must be a string"):
        jobmanager.search_by_category(31301)


# Test which you can search by rate for a given worker
def test_search_by_rate():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])

    result = jobmanager.search_by_rate(13.45) # The rate we are searching by

    # Ensures only the job with the matching rate is returned, hence length of result is equal to 1
    assert len(result) == 1
    assert job1 in result
    assert job2 not in result
    assert job3 not in result

# Test which stores a rate not found in the list, in a list, stored for future use
def test_search_by_rate_none_found():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])

    result = jobmanager.search_by_rate(15.00)

    assert result == [] # Asserts result into the list

# Test which outputs a TypeError if rate is anything but a float
def test_search_by_rate_int():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])

    with pytest.raises(TypeError, match="rate must be a float"): # Type Check
        jobmanager.search_by_rate(13)

# Test which outputs a ValueError if rate is not positive
def test_search_by_rate_negative():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])

    with pytest.raises(ValueError, match="rate can only be positive"): # Value Check
        jobmanager.search_by_rate(-13.45)

# Test which you can search by the name and date of the worker
def test_search_by_name_and_date():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])

    result = jobmanager.search_by_name_and_date("Marc Velti", "09/07/2024")

    assert job1 not in result # Ensures the non-relevant jobs do not appear into the answer
    assert job2 not in result
    assert job3 in result

# Test which stores the name and date of the worker not found in the list, in a list,
# stored for future use
def test_search_by_name_and_date_none_found():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])

    result = jobmanager.search_by_name_and_date("Lawrence Matten", "08/08/2024")

    assert result == [] # Asserts name and date into the list

#Test which outputs a TypeError if name is not a string
def test_search_by_name_and_date_invalid_input_1():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])

    with pytest.raises(TypeError, match="name must be a string"):
        jobmanager.search_by_name_and_date(123, "31/07/2024")

# Test which outputs a TypeError if date is not a string
def test_search_by_name_and_date_invalid_input_2():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])

    with pytest.raises(TypeError, match="date must be a string"):
        jobmanager.search_by_name_and_date("Simonette Thirkettle", 31072024)

# Test which calculates the total rate of the worker on the amount of hours they have worked
def test_get_total_cost_per_name():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])

    result = jobmanager.get_total_cost_per_name(["Marc Velti"])

    print(f"Marc Velti: {result["Marc Velti"]:.2f}") # Prints the name of the worker and wage to 2 decimals places

# Test which calculates the total rate of multiple workers on the amount of hours they have worked
def test_get_total_cost_per_name_multiple():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])

    result1 = jobmanager.get_total_cost_per_name(["Simonette Thirkettle"])
    result2 = jobmanager.get_total_cost_per_name(["Corissa Seid"])

    print(f"Simonette Thirkettle: {result1["Simonette Thirkettle"]:.2f}") # Prints to 2 decimal places
    print(f"Corissa Seid: {result2["Corissa Seid"]:.2f}")

# Test which calculates the total rate of the worker not available
def test_total_cost_per_name_empty_name():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])
    assert jobmanager.get_total_cost_per_name([]) == {}

# Test which outputs how many different roles (category) each worker has
def test_get_category_count_per_name():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job5 = Job("Simonette Thirkettle", "Operational", 15.47, "02/08/2024", 6)

    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job6 = Job("Corissa Seid", "Operational", 13.58, "06/07/2024", 3)

    job8 = Job("Kelsey Nelson", "Pilot", 25.50, "02/01/2025", 6)

    jobmanager = JobManager([job1, job5, job2, job6, job8])

    result = jobmanager.get_category_count_per_name()

    assert result["Simonette Thirkettle"] == 2
    assert result["Corissa Seid"] == 2
    assert result["Kelsey Nelson"] == 1

# Test which outputs how many roles (category) the worker has if they are duplicates
def test_category_count_per_name_duplicate():
    job1 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)

    jobmanager = JobManager([job1, job2])
    result = jobmanager.get_category_count_per_name()

    assert result["Corissa Seid"] == 1

# Test which loads from file being 'file_name' and stores them
def test_load_from_file():
    file_name = "sample_data.csv"
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])
    jobmanager.load_from_file(file_name)
    jobs = jobmanager.get_jobs()


# Test that saves job objects and instances to file_name ('sample_data.csv')
# Check 'sample_data.csv' for the results
def test_save_to_file():
    file_name = "sample_data.csv"
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)

    jobmanager = JobManager([job1, job2, job3])

    jobmanager.save_to_file(file_name)

    jobmanager_new = JobManager()
    jobmanager_new.load_from_file(file_name)

    assert (job1 in jobmanager_new.get_jobs()) # Asserts the job and details into the csv file
    assert (job2 in jobmanager_new.get_jobs())
    assert (job3 in jobmanager_new.get_jobs())


