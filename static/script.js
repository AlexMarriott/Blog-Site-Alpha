// Used to check the latest slack message and post it to the contact page. 
const interval = setInterval(getSlackMessages, 10000);

function getSlackMessages(){
        var pollhttp = new XMLHttpRequest();
    var node = document.getElementById("slack_list");
    var slackMessages = document.getElementById("slack_messages").getElementsByTagName("li");
    var latest_message = slackMessages[slackMessages.length - 1].innerText;
    pollhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            if (this.responseText !== latest_message) {
                var entry = document.createElement('li');
                entry.appendChild(document.createTextNode(this.responseText));
                node.appendChild(entry);
            }
        }
    };
    pollhttp.open('GET', '/slack/channel_msg');
    pollhttp.send();
}
function sendMessage() {
    var msg = document.getElementById("slack_message").value;
    var xmlHttp = new XMLHttpRequest();
    var url = '/contact/post_to_slack/' + msg;
    console.log(msg);
    console.log(url);
    xmlHttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            getSlackMessages()
        }
    };
    xmlHttp.open('POST', '/contact/post_to_slack/' + msg);
    xmlHttp.send();

}