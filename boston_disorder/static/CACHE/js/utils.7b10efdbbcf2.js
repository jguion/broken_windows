// Generated by CoffeeScript 1.4.0
(function() {

  $(function() {
    return $("#change_map").click(function() {
      var url;
      url = window.location.pathname;
      if (url.indexOf("tree_map") !== -1) {
        url = url.replace("tree_map", "map");
      } else {
        url = url.replace("map", "tree_map");
      }
      return window.location.href = url;
    });
  });

  $(function() {
    return $("#census_tract").click(function() {
      var url;
      url = window.location.href;
      if (url.indexOf("?") === -1) {
        url += "?";
      }
      if (url.indexOf("granularity") !== -1) {
        url = url.replace(/granularity=.*?$/, "granularity=Census Tract&");
      } else {
        url += "&granularity=Census Tract";
      }
      return window.location.href = url;
    });
  });

  $(function() {
    return $("#block_group").click(function() {
      var url;
      url = window.location.href;
      if (url.indexOf("?") === -1) {
        url += "?";
      }
      if (url.indexOf("granularity") !== -1) {
        url = url.replace(/granularity=.*?$/, "granularity=Block Group&");
      } else {
        url += "&granularity=Block Group";
      }
      return window.location.href = url;
    });
  });

  $(function() {
    return $("#block").click(function() {
      var url;
      url = window.location.href;
      if (url.indexOf("?") === -1) {
        url += "?";
      }
      if (url.indexOf("granularity") !== -1) {
        url = url.replace(/granularity=.*?$/, "granularity=Block&");
      } else {
        url += "&granularity=Block";
      }
      return window.location.href = url;
    });
  });

  ({
    save_filter: function(text) {
      return $.ajaxQueue({
        url: window.location.pathname,
        type: "GET",
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
