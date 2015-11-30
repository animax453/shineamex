#python imports

#django imports

#local imports

#inter app imports

#third party imports

FA_CHOICES = ((0,"Not Mentioned"),)

FA_K2V = {tup[0]:tup[1] for tup in FA_CHOICES}

EXP_CHOICES = ((0,"Not Mentioned"),)

EXP_K2V = {tup[0]:tup[1] for tup in EXP_CHOICES}

LOCATION_CHOICES = ((-1,"Select City"),
				(0,"Not Mentioned"),
				(1,"Delhi"), 
				(2,"Gurgaon"), 
				(3,"Jaipur"), 
				(4,"Chandigarh"), 
				(5,"Kolkata"), 
				(6,"Bangalore"), 
				(7,"Chennai"), 
				(8,"Hyderabad"), 
				(9,"Coimbatore"), 
				(10,"Mumbai"), 
				(11,"Pune"), 
				(12,"Ahmedabad"), 
				(13,"Surat"), 
				(14,"Vadodara"), 
				(15,"Indore"),)


SALARY_CHOICES = ((0,"Not Mentioned"),)

SALARY_K2V = {tup[0]:tup[1] for tup in SALARY_CHOICES}

LOCATION_K2V = {tup[0]:tup[1] for tup in LOCATION_CHOICES}

CANDIDATE_CITY_CHOICES = LOCATION_CHOICES

CANDIDATE_STATE_CHOICES = ((0,"Not Mentioned"),)
