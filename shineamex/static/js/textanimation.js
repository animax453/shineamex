var textAnimation = (function(parentElement){
	var obj={};
    obj.input = this.find(':input');
    obj.parentElement = parentElement || 'ul';

    obj.input.map(function(index,item) {
        switch(item.type) {

            case 'text':
            case 'password':
            case 'email':

                if(this.value == '') {
                    $(this).closest(obj.parentElement).removeClass('transform');
                }

                $(this)
                .on('focus',function(){
                    if($(this).val() == '') {
                       $(this).closest(obj.parentElement).addClass('transform');
                    }

                })
                .on('blur',function(){
                    if($(this).val() == '') {
                       $(this).closest(obj.parentElement).removeClass('transform');
                    }
                });
                break;


             case 'select-one':

                if(this.value != '') {
                    $(this).closest(obj.parentElement).find('.lbl').removeClass('displaynone');
                }

                $(this)
                .on('change',function(){
                    if($(this).val() != '') {
                        $(this).closest(obj.parentElement).find('.lbl').removeClass('displaynone');
                    } else {
                        $(this).closest(obj.parentElement).find('.lbl').addClass('displaynone');
                    }
                })

            default : {
                break;

            }
        }

    });

});

textAnimation.call($('.cls_txtanimation'),$('.input-field'));
