/**
 * Created by JYC103 on 2015/9/24.
 */
$(document).ready(function(){
   $("#deletepost").click(function(){
      $post("delete/{{post.id}}"),
      {
          id:"{{post.id}}"
      },
          function(){
              alert("delete post {{post.id}}")
          };
   });
});