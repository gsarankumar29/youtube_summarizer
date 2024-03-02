// const btn = document.getElementById("summarise");
// btn.addEventListener("click", function() {
//     btn.disabled = true;
//     btn.innerHTML = "Summarising...";
//     chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
//         var url = tabs[0].url;
//         var xhr = new XMLHttpRequest();
//         xhr.open("GET", "http://127.0.0.1:5000/summarize?url=" + url, true);
//         xhr.onload = function() {
//             var text = xhr.responseText;
//             const p = document.getElementById("output");
//             p.innerHTML = text;
//             btn.disabled = false;
//             btn.innerHTML = "Summarise";
//         }
//         xhr.send();
//     });
// });

// popup.js

const btn = document.getElementById("summarise");
btn.addEventListener("click", function() {
    btn.disabled = true;
    btn.innerHTML = "Summarising...";
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
        var url = tabs[0].url;
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "http://127.0.0.1:5000/summarize", true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    var response = JSON.parse(xhr.responseText);
                    const p = document.getElementById("output");
                    p.innerHTML = response.summary;
                } else {
                    const p = document.getElementById("output");
                    p.innerHTML = "Error: " + xhr.statusText;
                }
                btn.disabled = false;
                btn.innerHTML = "Summarise";
            }
        };
        xhr.send(JSON.stringify({url: url}));
    });
});
