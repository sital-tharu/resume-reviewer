document.getElementById("uploadForm").onsubmit = function() {
    document.getElementById("spinner").style.display = "block";
};

window.onload = function() {
    document.getElementById("spinner").style.display = "none";
};