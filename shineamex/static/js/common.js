
/* Formset binding to referral form */


/* referral form validation */
$("#id_referralForm").validate({
		rules: {
			'name':'required',
			'contact_no': {
			    required:true,
			    number:true,
			    minlength:1,
			    maxlength:10

			},
			'email':{
			    required:true,
			    email:true
			},
			'organization':'required',
			'city':'required',
			'state':'required'
		},
		ignore: [],

		errorPlacement:function(error, element) {
			// error.appendTo($(element).parent());
		},
		onfocusout:function(element) {
				$(element).valid();
		},
		highlight:function(el) {
		    switch(el.type){
               case 'select-one':
                   $(el).parent().addClass('redborder');
               break;
               default:
                   $(el).addClass('redborder');
               break;
            }
	    },

		unhighlight:function(el){
            switch(el.type){
               case 'select-one':
                $(el).parent().removeClass('redborder');
               break;
               default:
                $(el).removeClass('redborder');
               break;
            }
		}
	});
	$(".cls_referral_name").each(function(){
      $(this).rules("add", {
          required:true
      });
    });
    $(".cls_referral_contactnum").each(function(){
      $(this).rules("add", {
          required:true,
          number:true,
          minlength:1,
          maxlength:10
      });
    });
    $(".cls_referral_email").each(function(){
      $(this).rules("add", {
          required:true,
          email:true
      });
    });
    $(".cls_referral_city").each(function(){
      $(this).rules("add", {
          required:true
      });
    });
    $(".cls_referral_org").each(function(){
      $(this).rules("add", {
          required:true
      });
    });
/* Referral form validation ends */

/*Application form validation */
 $("#id_applicationForm").validate({
		rules: {
			'name':'required',
			'contact_no': {
			    required:true,
			    number:true,
			    minlength:1,
			    maxlength:10

			},
			'email':{
			    required:true,
			    email:true
			},
			'organization':'required',
			'city':'required',
			'state':'required'
		},
		ignore: [],

		errorPlacement:function(error, element) {
			// error.appendTo($(element).parent());
		},
		onfocusout:function(element) {
				$(element).valid();
		},
		highlight:function(el) {
		    switch(el.type){
               case 'select-one':
                   $(el).parent().addClass('redborder');
               break;
               default:
                   $(el).addClass('redborder');
               break;
            }
	    },

		unhighlight:function(el){
            switch(el.type){
               case 'select-one':
                $(el).parent().removeClass('redborder');
               break;
               default:
                $(el).removeClass('redborder');
               break;
            }
		}
	});
/*Application form validation  end*/
	$(document).on('change','.selectboxdiv',function(){
	    $(this).next(".out").text($(this).find(":selected").text());
     });
