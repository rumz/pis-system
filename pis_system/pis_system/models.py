from django.db import models

class Employee(models.Model):
  emp_id = models.CharField(max_length=9, primary_key=True)
  firstname = models.CharField(max_length=45)
  mi = models.CharField(max_length=1)
  lastname = models.CharField(max_length=45)
  position = models.CharField(max_length=45)
  address = models.CharField(max_length=100, blank=True)
  image_path = models.FileField(upload_to='templates/static/images/employees/')

  def __unicode__(self):
    return self.emp_id

class Employee_Account(models.Model):
  emp_id = models.OneToOneField(Employee)
  password = models.CharField(max_length=45)
  date_created = models.DateTimeField(auto_now=True, auto_now_add=True)
  account_privilege = models.IntegerField()

  def __unicode__(self):
    return self.password

class Student_Privilege(models.Model):
  priv_name = models.CharField(max_length=100) #scholar
  discount = models.FloatField(max_length=3) #discount

  def __unicode__(self):
    return self.priv_name

class Student(models.Model):
  acad_stat_choices = (('reg', 'Regular'),
                         ('ret', 'Retain')
                        )
  gender_choice = (('M', 'Male'),('F', 'Female'))
  stud_id = models.CharField(max_length=9, primary_key=True)
  firstname = models.CharField(max_length=45)
  mi = models.CharField(max_length=1)
  lastname = models.CharField(max_length=45)
  gender = models.CharField(max_length=1, choices=gender_choice)
  date_of_birth = models.DateField()
  date_admitted = models.DateField()
  mother_name = models.CharField(max_length=45)
  father_name = models.CharField(max_length=45)
  mother_occ = models.CharField(max_length=45, blank=True)  # mother occupation
  father_occ = models.CharField(max_length=45, blank=True)  # father occupation
  last_school_att = models.CharField(max_length=100, blank=True)
  last_school_att_add = models.CharField(max_length=100, blank=True)
  acad_status = models.CharField(max_length=45, choices=acad_stat_choices)
  image_path = models.FileField(upload_to='templates/static/images/students/')
  priv = models.ForeignKey(Student_Privilege)

  def __unicode__(self):
    return self.stud_id


class Bill_Item(models.Model):
  item_name = models.CharField(max_length=45) #misc or totu
  amount  = models.DecimalField(max_digits=7, decimal_places=2) #amount

  def __unicode__(self):
    return self.item_name

class Student_Bill_Account(models.Model):
  stud_id = models.ForeignKey(Student)
  emp_id = models.ForeignKey(Employee)
  total = models.DecimalField(max_digits=8, decimal_places=2)
  amount_tender = models.DecimalField(max_digits=8, decimal_places=2)
  balance = models.DecimalField(max_digits=8, decimal_places=2)
  school_year = models.CharField(max_length=9)
  year_level = models.IntegerField()
  date_received = models.DateTimeField(auto_now=True, auto_now_add=True)

  def __unicode__(self):
    return unicode(self.stud_id)

class Student_Bill_Breakdown(models.Model):
  sba_id = models.ForeignKey(Student_Bill_Account) #student billing account
  bill_item_id = models.ManyToManyField(Bill_Item)
  amount = models.DecimalField(max_digits=8, decimal_places=2)

  def __unicode__(self):
    return unicode(self.sba_id)

class Bill_Assign(models.Model):
  bill_item_id = models.ManyToManyField(Bill_Item)
  school_year = models.CharField(max_length=9)
  year_level = models.IntegerField()

  def __unicode__(self):
    return self.school_year

class Entrance_Fees(models.Model):
  bill_item_id = models.ForeignKey(Bill_Item)
  amount = models.DecimalField(max_digits=6, decimal_places=2)
  payee = models.CharField(max_length=45)
  date_recieved = models.DateTimeField(auto_now=True, auto_now_add=True)
  or_number = models.CharField(max_length=15)
  emp_id = models.ManyToManyField(Employee)

  def __unicode__(self):
    return self.payee


class Subject(models.Model):
  title = models.CharField(max_length=45)
  units = models.IntegerField()

  def __unicode__(self):
    return self.title

class Section(models.Model):
  name = models.CharField(max_length=45)
  room_no = models.IntegerField()

  def __unicode__(self):
    return self.name

class Student_Subjects(models.Model):
  subject_id = models.ManyToManyField(Subject)
  stud_id = models.ForeignKey(Student)
  section_id = models.ForeignKey(Section)
  emp_id = models.ForeignKey(Employee)
  year_level = models.IntegerField()
  school_year = models.CharField(max_length=9)
  time_fr = models.TimeField()
  time_to = models.TimeField()
  days = models.CharField(max_length=6)

  def __unicode__(self):
    return self.school_year

class Character_Rate(models.Model):

  character_choices = (('C','Cleanliness'),
                         ('CP','Courtesy and Politeness'),
                         ('HC','Helpfulness and Cooperativeness'),
                         ('I','Industriousness'),
                         ('LI','Leadership and Innitiative'),
                         ('O','Obedience'),
                         ('SC','Self Control'),
                         ('PP','Promptness and Punctuality'),
                         ('S','Sportmanship'),
                         ('TE','Thrift and Economy'),
                         ('MS','Modesty and Simplicity')
                        )

  stud_id = models.ForeignKey(Student)
  rate = models.FloatField(max_length=3)
  character = models.CharField(max_length=2,choices=character_choices)
  year_level = models.IntegerField()
  school_year = models.CharField(max_length=5)
  period = models.IntegerField()
  date_rated = models.DateTimeField(auto_now=True, auto_now_add=True)

  def __unicode__(self):
    return self.school_year

class Attendance(models.Model):
  stud_id = models.ForeignKey(Student)
  year_level = models.IntegerField()
  school_year = models.CharField(max_length=5)
  no_school_days = models.IntegerField()
  no_school_days_tardy = models.IntegerField()
  no_school_days_present = models.IntegerField()
  month = models.CharField(max_length=9)

  def __unicode__(self):
    return self.school_year



