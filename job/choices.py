#python imports

#django imports

#local imports

#inter app imports

#third party imports

FA_CHOICES = ((0,"Not Mentioned"),)

FA_K2V = {tup[0]:tup[1] for tup in FA_CHOICES}

EXP_CHOICES = ((0,"Not Mentioned"),)

EXP_K2V = {tup[0]:tup[1] for tup in EXP_CHOICES}

SALARY_CHOICES = ((0,"Not Mentioned"),)

SALARY_K2V = {tup[0]:tup[1] for tup in SALARY_CHOICES}

LOCATION_CHOICES = ((0,"Not Mentioned"),)

LOCATION_K2V = {tup[0]:tup[1] for tup in LOCATION_CHOICES}

CANDIDATE_CITY_CHOICES = ((-1,'Select City'),(0,"Not Mentioned"),(1,"Delhi"),(2,"Mumbai"))

CANDIDATE_STATE_CHOICES = ((-1,'Select State'),(0,"Not Mentioned"))