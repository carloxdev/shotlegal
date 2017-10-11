
/* ------------------------ LOAD ------------------------ */

window.paceOptions = {
    // Disable the 'elements' source
    elements: false,
    // Only show the progress on regular and ajax-y page navigation,
    // not every request
    restartOnRequestAfter: false,
    startOnPageLoad: false,
    ajax: {
      trackMethods: ['GET', 'POST', 'DELETE', 'PUT', 'PATCH']
    }
}

// $(document).ready(function () {
//
// })
