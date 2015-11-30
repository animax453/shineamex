#python imports

#django imports
from django import template

#local imports
from job.choices import *

#inter app imports

#third party imports

register = template.Library()

@register.filter
def key_value(key,key_type):
    type_mapping = {'loc':LOCATION_K2V,
                    'exp':EXP_K2V,
                    'fa':FA_K2V,
                    'sal':SALARY_K2V,
                    }
                    
    k2v_dict = type_mapping.get(key_type)
    if not k2v_dict:
        return None

    return k2v_dict.get(key)