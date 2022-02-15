
/*
Confirm that the user wants to delete a recipe and delete it if so.
Args:
  recipe_delete_url: string. The URL endpoint to delete a given recipe.
*/
function confirm_delete(recipe_delete_url){
    var delete_confirmed = confirm("Delete this question?")
    if (delete_confirmed){
        window.location.href = recipe_delete_url;
    }
  }

 