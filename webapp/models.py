from django.db import models
# from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

class Functionalarea(models.Model):
      name=models.CharField(max_length=500)

      def __str__(self):
         return self.name

class Rolename(models.Model):
    functionalarea=models.ForeignKey(Functionalarea, on_delete=models.CASCADE)
    name=models.CharField(max_length=500)
    def __str__(self):
         return self.name



class Record(models.Model):
    yesno_choice=[
        ("Yes", "Yes"),
        ("No", "No")
    ]

    registration_type=[
        ("Profit", "Profit"),
        ("Non Profit", "Non Profit")
    ]
    entry_level=[
        ("National", "National"),
        ("County", "County")
    ]
    partner_category=[
        ("Implementing", "Implementing"),
        ("Contracted", "Contracted"),
        ("Funder", "Funder")
    ]

    partnership_framework=[
        ("MOU", "National"),
        ("Implementation Letter", "Implementation Letter"),
        ("Letter of Intent", "Letter of Intent"),
        ("Partnership Agreement", "Partnership Agreement"),
        ("Implementation Letter", "Implementation Letter"),
        ("Contract", "Contract"),
        ("Other", "Other")
    ]

    county_choice=(
       ("All Counties", "All Counties"),
       ("Nairobi", "Nairobi"),
       ("Mombasa", "Mombasa"),
        ("Nakuru", "Nakuru")
    )

    entry_level=[
        ("National", "National"),
        ("County", "County")
    ]
   
   
    creation_date = models.DateTimeField(auto_now_add=True)
    stakeholder_name = models.CharField(max_length=100, blank=False, null=True)
    physical_location=models.TextField(blank=False, null=True)
    Primary_contact_tel=models.CharField(max_length=200, blank=False, null=True)
    year_of_registration=models.DateTimeField(blank=False, null=True)
    partner_category=models.CharField(choices=partner_category, null=True, blank=False)
    stakeholder_type = models.CharField(max_length=100, null=True, blank=False)
    # county = MultiSelectField(choices=county_choice, max_length=500)
    county = models.CharField(max_length=300, null=True, blank=False) 
    functionalarea = models.ForeignKey(Functionalarea, on_delete=models.SET_NULL, blank=False, null=True)
    rolename = models.ForeignKey(Rolename, on_delete=models.SET_NULL, blank=False, null=True)
    registration_type=models.CharField(choices=registration_type, null=True, blank=False)
    entry_level=models.CharField(choices=entry_level, null=True, blank=False)
    budget=models.CharField(max_length=200, null=True, blank=True)
    partnership_framework=models.CharField(choices=partnership_framework, null=True, blank=False)
    # hiv = models.CharField(choices=yesno_choice, null=True, blank=False)
    # malaria = models.CharField(choices=yesno_choice, null=True, blank=False)
    # fp = models.CharField(choices=yesno_choice, null=True, blank=False)
    # mnch = models.CharField(choices=yesno_choice, null=True, blank=False)
    # emms = models.CharField(choices=yesno_choice, null=True, blank=False)
    # emms = models.CharField(max_length=125)
    contact_email = models.CharField(max_length=125)
    notes = models.TextField(max_length=500)
    activity_reference = models.CharField(max_length=150)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

# class countym(models.Model):
#     county = models.CharField(max_length=30)

# class Recordm(models.Model):
#     county = models.CharField(max_length=50)
#     counties = models.ManyToManyField(countym)

#     def __str__(self):
#         return "%s (%s)" % (
#             self.name,
#             ", ".join(counties.name for counties in self.counties.all()),
#         )

    def __str__(self):

        return self.stakeholder_name + "   " + self.stakeholder_type
