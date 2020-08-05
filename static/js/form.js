$(function () {
function processForm (e) {

      var formData = {firstName: $("#firstName").val(),
      lastName: $("#lastName").val() }

      $.ajax({
          url: "/process",
          type: "POST",
          data: formData,
          success: function (data) {
                      $("#output").html(data);

                   },
          error: function (errorThrown) {
                        console.log(errorThrown);

                 }

      });

      e.preventDefault();

}
  $("#flask").submit(processForm);

  });
