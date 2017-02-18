
   function editarArticulo(){
        var id= $('#id_articulo').val();
        var ruta= $('#abrirModal').attr("data-ajax-target");
        //var action=$('#formEditar').attr('action');
        $.ajax({
            url:ruta,
            type:'GET',
            data:{'id':id},
            success:function(res){
                var rutaEditar='/editarArticulo/'+id+'/';
                var obj= JSON.parse(res);
                $("#titulo").val(obj[0].fields.titulo);
                $("#contenido").val(obj[0].fields.contenido);
                $("#imagen").val(obj[0].fields.imagen);
                $("#fecha_publicacion").val(obj[0].fields.fecha_publicacion);
                $("#fecha_vencimiento").val(obj[0].fields.fecha_vencimiento);
                $('#formEditar').attr('action',rutaEditar);
                //alert($('#formEditar').attr('action'))
                alert(obj[0].fields.tag);
                $('#demo-default-modal').modal();
            }
        });



   };


