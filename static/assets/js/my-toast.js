"use strict";
!(function (o, t) {
    t(".eg-toastr-top-right").on("load", function (t) {
      t.preventDefault(),
        toastr.clear(),
        o.Toast("{{ message }}", "info", {
          position: "top-right",
        });
    }),
})(NioApp, jQuery);
