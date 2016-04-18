class Author:
  def __init__(self, first_name, last_nam, year_born):
    self.first_name = first_name
    self.last_nam = last_nam
    self.year_born = year_born

  def get_full_name(self):
    return self.first_name + " " + self.last_nam

author = Author("Douglas", "Adams", 1952)
# Author { first_name: 'Douglas', last_nam: 'Adams', year_born: 1952 }

author.first_name = "Doug"
# Author { first_name: 'Doug', last_nam: 'Adams', year_born: 1952 }

fullName = author.get_full_name()
# "Doug Adams"
