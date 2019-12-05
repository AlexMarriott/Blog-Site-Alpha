// Used to check the latest slack message and post it to the contact page. 
const interval = setInterval(function () {
    var xmlHttp = new XMLHttpRequest();
    var node = document.getElementById("slack_list");
    var slackMessages = document.getElementById("slack_messages").getElementsByTagName("li");
    var latest_message = slackMessages[slackMessages.length-1].innerText;
    xmlHttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            if (this.responseText !== latest_message){
                var entry = document.createElement('li');
                entry.appendChild(document.createTextNode(this.responseText));
                node.appendChild(entry);
            }
        }
        };
    xmlHttp.open('GET', '/slack/channel_msg');
    xmlHttp.send();

}, 10000);
