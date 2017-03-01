
   $("select.one").select2({width: '100%'});
   $("select.many").select2({multiple:true, width: '100%'});

   $("#demo-panel-alert").click(function(){
        if ($('#activado').val() == 1){
            $('#activado').val('0') ;
        }else{
            $('#activado').val('1') ;
        }
   });

   function desactivar(){
        var activado= $('#activado').val();
        var id= $('#id_articulo').val();
        var ruta= $('#demo-panel-alert').attr("data-ajax-target");
        $.ajax({
            url:ruta,
            type:'GET',
            data:{'id':id,'activado':activado},
            success:function(res){
               alert(res);
            }
        });
   }

   function abrirModal(){
        $("#demo-default-modal").modal();
   }




