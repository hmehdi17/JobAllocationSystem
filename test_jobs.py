from job_manager import JobManager
from job import Job
import pytest

# Normal Job instances For Testing
job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)
job4 = Job("Lawrence Matten", "Research Activities", 13.76, "08/08/2024", 5)
job5 = Job("Kelsey Nelson", "Pilot", 25.50, "02/01/2025", 6)

#Equal Jobs
job6 = Job("Lawrence Matten", "Research Activities", 13.76, "08/08/2024", 5)
job7 = Job("Lawrence Matten", "Research Activities", 13.76, "08/08/2024", 5)

#Hash Jobs
job8 = Job("Xanthe Woodard", "Customer Service", 13.58, "25/08/2024", 3)
job9 = Job("Lawrence Matten", "Operational", 13.60, "17/07/2024", 4)
jobmanager = JobManager()


# Test that gets the name within each Job object
def test_get_name():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)
    job4 = Job("Lawrence Matten", "Research Activities", 13.76, "08/08/2024", 5)

    assert job1.get_name() == "Simonette Thirkettle" # Job instance assertions used for testing
    assert job2.get_name() == "Corissa Seid"
    assert job3.get_name() == "Marc Velti"
    assert job4.get_name() == "Lawrence Matten"

# Test that gets the empty string for 'name'
def test_get_empty_name():
    empty_name_job1 = Job("", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    empty_name_job2 = Job("", "Technical", 13.76, "31/07/2024", 2)
    empty_name_job3 = Job("", "Administration", 17.19, "09/07/2024", 3)

    assert empty_name_job1.get_name() == ""
    assert empty_name_job2.get_name() == ""
    assert empty_name_job3.get_name() == ""

# Test that executes a TypeError when 'name' is not a string rather an integer (i.e '313')
def test_get_name_invalid_type():
    with pytest.raises(TypeError, match="name must be a string"): # Type Checks
        Job(313, "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    with pytest.raises(TypeError, match="name must be a string"): # Type Checks
         Job(212, "Technical", 13.76, "31/07/2024", 2)
    with pytest.raises(TypeError, match="name must be a string"): # Type Checks
        Job(111, "Administration", 17.19, "09/07/2024", 3)


# Test that gets the category within each Job object
def test_get_category():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)
    job4 = Job("Lawrence Matten", "Research Activities", 13.76, "08/08/2024", 5)

    assert job1.get_category() == "Teaching and Learning Activities"
    assert job2.get_category() == "Technical"
    assert job3.get_category() == "Administration"
    assert job4.get_category() == "Research Activities"

# Test that gets the empty string for 'category' name
def test_get_empty_category():
    empty_category_name1 = Job("Simonette Thirkettle", "", 13.45, "03/08/2024", 1)
    empty_category_name2 = Job("Corissa Seid", "", 13.76, "31/07/2024", 2)
    empty_category_name3 = Job("Marc Velti", "", 17.19, "09/07/2024", 3)

    assert empty_category_name1.get_category() == "" # Empty string for Category Test
    assert empty_category_name2.get_category() == ""
    assert empty_category_name3.get_category() == ""

# Test that executes a TypeError when 'category' is not a string rather an integer (i.e '313')
def test_get_category_invalid_type():
    with pytest.raises(TypeError, match="category must be a string"):
        Job("Simonette Thirkettle", 313, 13.45, "03/08/2024", 1)
    with pytest.raises(TypeError, match="category must be a string"):
        Job("Corissa Seid", 212, 13.76, "31/07/2024", 2)
    with pytest.raises(TypeError, match="category must be a string"):
        Job("Marc Velti", 111, 17.19, "09/07/2024", 3)

# Test that gets the rate within each Job object
def test_get_rate():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)
    job4 = Job("Lawrence Matten", "Research Activities", 13.76, "08/08/2024", 5)

    assert job1.get_rate() == 13.45
    assert job2.get_rate() == 13.76
    assert job3.get_rate() == 17.19
    assert job4.get_rate() == 13.76

#Test that executes TypeError when 'rate' is not a float rather than an integer (i.e 13.35 -> 13)
def test_rate_must_be_float():
        with pytest.raises(TypeError, match="rate must be a float"):
            Job("Simonette Thirkettle", "Teaching and Learning Activities", 13, "01/01/2024", 1)
        with pytest.raises(TypeError, match="rate must be a float"):
            Job("Corissa Seid", "Technical", 13, "31/07/2024", 2)
        with pytest.raises(TypeError, match="rate must be a float"):
            Job("Marc Velti", "Administration", 17, "09/07/2024", 3)

#Test that executes ValueError when 'rate' is not positive rather negative (i,e 13.45 -> -13.0)
def test_rate_must_be_positive():
    with pytest.raises(ValueError, match="rate can only be positive"): # Value Checks
        Job("Simonette Thirkettle", "Teaching and Learning Activities", -13.0, "01/01/2024", 1)
    with pytest.raises(ValueError, match="rate can only be positive"): # Value Checks
        Job("Corissa Seid", "Technical", -13.0, "31/07/2024", 2)
    with pytest.raises(ValueError, match="rate can only be positive"): # Value Checks
        Job("Marc Velti", "Administration", -17.0, "09/07/2024", 3)

# Test that gets the rate within each Job object
def test_get_date():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)
    job4 = Job("Lawrence Matten", "Research Activities", 13.76, "08/08/2024", 5)

    assert job1.get_date() == "03/08/2024"
    assert job2.get_date() == "31/07/2024"
    assert job3.get_date() == "09/07/2024"
    assert job4.get_date() == "08/08/2024"

#Test that executes TypeError when 'date' is not a string rather an integer (i.e "31/07/2024" -> 31072024)
def test_get_date_invalid_type():
        with pytest.raises(TypeError, match="date must be a string"):
            Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, 20240101, 1)
        with pytest.raises(TypeError, match="date must be a string"):
            Job("Corissa Seid", "Technical", 13.76, 31072024, 2)

# Test that gets the hours within each Job object
def test_get_hours():
    job1 = Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1)
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)
    job3 = Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3)
    job4 = Job("Lawrence Matten", "Research Activities", 13.76, "08/08/2024", 5)
    job5 = Job("Kelsey Nelson", "Pilot", 25.50, "02/01/2025", 6)

    assert job1.get_hours() == 1 # Retrieving Hours
    assert job2.get_hours() == 2
    assert job3.get_hours() == 3
    assert job4.get_hours() == 5
    assert job5.get_hours() == 6

#Test that executes ValueError when 'hours' is not an integer rather float (i.e 1 -> 1.10)
def test_hours_must_be_integer():
    with pytest.raises(ValueError, match="hours must be a integer"):
        Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 1.10)
    with pytest.raises(ValueError, match="hours must be a integer"):
        Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2.20)
    with pytest.raises(ValueError, match="hours must be a integer"):
        Job("Marc Velti", "Administration", 17.19, "09/07/2024", 3.30)

#Test that executes ValueError when 'hours' is not positive rather negative (i.e 1 -> -1)
def test_hours_can_be_only_positive():
    with pytest.raises(ValueError, match="hours can only be positive"):
        Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", -1)
    with pytest.raises(ValueError, match="hours can only be positive"):
         Job("Corissa Seid", "Technical", 13.76, "31/07/2024", -2)
    with pytest.raises(ValueError, match="hours can only be positive"):
        Job("Marc Velti", "Administration", 17.19, "09/07/2024", -3)

#Test that executes ValueError when 'hours' is out of range between 1 and 6 hours (i,e 15<6)
def test_hours_out_of_range():
    with pytest.raises(ValueError, match="hours can only be between 1 and 6"):
        Job("Simonette Thirkettle", "Teaching and Learning Activities", 13.45, "03/08/2024", 15)
    with pytest.raises(ValueError, match="hours can only be between 1 and 6"):
         Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 7)
    with pytest.raises(ValueError, match="hours can only be between 1 and 6"):
        Job("Marc Velti", "Administration", 17.19, "09/07/2024", 10)

# Test that tests and compares the equality of jobs
def test_equality_of_jobs_true():
    job6 = Job("Lawrence Matten", "Research Activities", 13.76, "08/08/2024", 5)
    job7 = Job("Lawrence Matten", "Research Activities", 13.76, "08/08/2024", 5)

    assert job6 == job7 # Compares if the two jobs are equal

# Test that tests and compares inequal jobs
def test_equality_of_jobs_false():
    job6 = Job("Lawrence Matten", "Research Activities", 13.77, "08/08/2024", 5)
    job7 = Job("Lawrence Matten", "Research Activities", 13.76, "08/08/2024", 5)

    assert job6 != job7 # Compares if the two jobs are not equal

# Test that tests the has of jobs and outputs their unique hash-key
def test_hash_of_jobs():
    job8 = Job("Xanthe Woodard", "Customer Service", 13.58, "25/08/2024", 3)
    job9 = Job("Lawrence Matten", "Operational", 13.60, "17/07/2024", 4)

    assert job8.__hash__() != job9.__hash__()
    print()
    print(job8.__hash__()) # Displays the unique hash value for the job
    print(job9.__hash__())

# Test that outputs the string format(str) of the job object
def test_str():
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)

    Anticipated = "Job(Corissa Seid, Technical, 13.76, 31/07/2024, 2)"

    assert str(job2) == Anticipated # Checks if the job instance matches to a str format

# Test that outputs the repr format of the job object
def test_repr():
    job2 = Job("Corissa Seid", "Technical", 13.76, "31/07/2024", 2)

    Anticipated = "Job(Corissa Seid, Technical, 13.76, 31/07/2024, 2)"

    assert repr(job2) == Anticipated # Checks if the job instance matches to a repr format













