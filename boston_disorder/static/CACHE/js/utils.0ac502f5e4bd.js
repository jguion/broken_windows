// Generated by CoffeeScript 1.4.0
(function() {

  $(function() {
    return $("#filter").click(function() {
      alert("HERE");
      return false;
    });
  });

  $("#filter").click(function() {
    alert("HERE");
    return false;
  });

  ({
    save_filter: function(text) {
      return $.ajaxQueue({
        url: window.location.pathname,
        data: text,
        type: "POST",
        success: function() {
          return console.log("success");
        },
        error: function(data) {
          return alert("Save Failed: " + data.responseText);
        },
        complete: function() {
          return window.location.reload();
        }
      });
    }
  });

}).call(this);