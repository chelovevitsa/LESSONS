$('#check').click(function(){
    var topic = $('#topic').val();
  
    $.get("http://www.omdbapi.com/?t=" + topic + "&apikey=ac2c0207", function(data, status){
      console.log(data);
  
    var list = $('#list');
    list.append('<li class="text"> Nazwa: ' + topic + "<img src=" + data.Poster + "></img>" + '</li>');
  
    });
  });
  