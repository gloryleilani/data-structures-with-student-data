"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    
    cohort_data_file = open(filename)
    
    houses_with_dups = []

    for line in cohort_data_file:
      line = line.rstrip()
      cohort_data_tokens = line.split("|") #The split method returns a list 
      
      first_name, last_name, house, adviser, cohort_name = cohort_data_tokens  
      
      if house != "":
        houses_with_dups.append(house) 

    houses = set(houses_with_dups)

    #print(houses)
    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """
    
    cohort_data_file = open(filename)
    
    students = []

    for line in cohort_data_file:
      line = line.rstrip()
      cohort_data_tokens = line.split("|") #The split method returns a list 
      
      #first_name, last_name, house, adviser, cohort_name = cohort_data_tokens 
      first_name = cohort_data_tokens[0]
      last_name = cohort_data_tokens[1]
      house = cohort_data_tokens[2]
      cohort_name = cohort_data_tokens[4]


      if house != "":
        #print("cohort passed in", cohort)
        #print("cohort_name", cohort_name)
        if cohort_name == cohort:
          students.append(first_name+ " " + last_name)
        
        elif cohort == "" or cohort == "All":
          students.append(first_name + " " + last_name)


    #print("LL students", students)
    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    cohort_data_file = open(filename)

    
    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []
    

    for line in cohort_data_file:
      line = line.rstrip()
      cohort_data_tokens = line.split("|")

      first_name, last_name, house, adviser, cohort_name = cohort_data_tokens 

      if house == "Dumbledore's Army":
        dumbledores_army.append(first_name + " " + last_name)
      
      elif house == "Gryffindor":
        gryffindor.append(first_name + " " + last_name)
      
      elif house == "Hufflepuff":
        hufflepuff.append(first_name + " " + last_name)
      
      elif house == "Ravenclaw":
        ravenclaw.append(first_name + " " + last_name)  
      
      elif house == "Slytherin":
        slytherin.append(first_name + " " + last_name)   
      
      elif house == "Ravenclaw":
        ravenclaw.append(first_name + " " + last_name)   
      
      elif cohort_name == "G":
        ghosts.append(first_name + " " + last_name) 
      
      elif cohort_name == "I":
        instructors.append(first_name + " " + last_name) 
      
      else:
        print("Not found.")

    rosters = [sorted(dumbledores_army), sorted(gryffindor), sorted(hufflepuff), 
               sorted(ravenclaw), sorted(slytherin), sorted(ghosts), 
               sorted(instructors)]

    #print(rosters)
    return rosters


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    cohort_data_file = open(filename)

    all_data = []

    for line in cohort_data_file:
      line = line.rstrip()
      cohort_data_tokens = line.split("|") #The split method returns a list 
      
      first_name, last_name, house, adviser, cohort_name = cohort_data_tokens 

      full_name = first_name + " " + last_name
      cohort_member = (full_name, house, adviser, cohort_name)
      all_data.append(cohort_member)
    
    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    cohort_data_file= open(filename)
    for line in cohort_data_file:
      line = line.rstrip()
      cohort_data_tokens = line.split("|")

      first_name, last_name, house, adviser, cohort_name = cohort_data_tokens

      full_name = first_name + " " + last_name

      if full_name == name:
        return cohort_name

    if name in cohort_data_tokens:
      print ("")

    else:
      return None



def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    cohort_data_file = open(filename)
      
    set_of_unique_last_names = []
    last_names_dups_only = []

    for line in cohort_data_file:
      line = line.rstrip()
      cohort_data_tokens = line.split("|")

      first_name, last_name, house, adviser, cohort_name = cohort_data_tokens
        
      if not last_name in set_of_unique_last_names:
        set_of_unique_last_names.append(last_name)

      else: 
        last_names_dups_only.append(last_name)

    last_names_dups_only = set(last_names_dups_only)
    
    return last_names_dups_only


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    cohort_data_file = open(filename)
    cohort = ""
    house_name = ""
    cohort_members = []
    housemates = []

    for line in cohort_data_file:
      line = line.rstrip()
      cohort_data_tokens = line.split("|")

      first_name, last_name, house, adviser, cohort_name = cohort_data_tokens

      full_name = first_name + " " + last_name

      if full_name == name:
        cohort = cohort_name 
        house_name = house

        #print("full name:", full_name)
        #print("cohort:", cohort_name)

      cohort_member = (full_name, house, adviser, cohort_name)
      cohort_members.append(cohort_member)

    #print("cohort members:", cohort_members)
    #print("cohort:", cohort)

    for cohort_member in cohort_members:
      #print("cohort member:", cohort_member)
      if cohort_member[3] == cohort and cohort_member[0] != name and cohort_member[1] == house_name:
        housemates.append(cohort_member[0])
      
      #print("housemates:", housemates)

    housemates = set(housemates)

    return housemates

##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
