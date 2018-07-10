function loginBodyHandler(event, trigger, parent, closeFunction) {
    var triggerElement = document.getElementById(trigger);
    var parentElement = document.getElementById(parent);
    var childElements = parentElement.getElementsByTagName('*');
    var target = event.target;

    if (!target.isEqualNode(triggerElement) && !target.isEqualNode(parentElement)) {
        var isChild = false;
        for (var i = 0; i < childElements.length; ++i) {
            if (target.isEqualNode(childElements[i])) {
                isChild = true;
                break;
            }
        }
        if (!isChild) {
            closeFunction();
        }
    }
}


function openSideNav() {
    document.getElementById("side-navigation").style.width = "75vw";
    document.body.addEventListener("click", _sideNavCloseListener = function () {
        loginBodyHandler(event, "side-navigation-toggle", "side-navigation", closeSideNav)
    });
}

function closeSideNav() {
    document.getElementById("side-navigation").style.width = "0";
    document.body.removeEventListener("click", _sideNavCloseListener);
}
