function searchStudent(form){
  var search_text;
  search_text = $('#'+ form + " #seach_student").val();
  var itemSelect;
  itemSelect = $ ('#item_search_filters').val();
  var item;

  if(itemSelect=='id_num'){
      item='stud_id'
  }else if(itemSelect=='last_name'){
      item='lastname'
  }else if(itemSelect=='first_name'){
      item='firstname'
  }

    $.get('/billing/searchstudent', {_search: search_text, _type:item}, function(data){

      $('#stud_list ').html(data);
    });


}

function getStudent(id){

  $.get('/billing/getstudent', {_stud: id }, function(data){

      $('#stud_info').html(data);

  });

  $.get('/billing/getbill', {_bill: id }, function(data){
      $('#bill_info').html(data);
  });

}