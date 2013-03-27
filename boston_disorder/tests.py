"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from crime.models import Crime
from django.db.models import Min, Max, Count

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

 	def crime_test(self):
 		crime_data = Crime.objects.all()
    	min_date = Crime.objects.all().aggregate(Min('fromdate'))
    	max_date = Crime.objects.all().aggregate(Max('fromdate'))
    	print "Min date %s , Max date %s"%(min_date,max_date)
    
    	crime_neighborhoods = Crime.objects.values('neighborhood').annotate(Count('pk')).order_by('pk__count')
    
    	specific_neighborhood_crime = Crime.objects.filter(neighborhood='MID DORCHESTER').values('crimecode_description').annotate(Count('pk')).order_by('pk__count')
    
    	weapons = Crime.objects.values('weapon_type').annotate(Count('pk')).order_by('pk__count')
    

    	for item in crime_neighborhoods:
        	print item
