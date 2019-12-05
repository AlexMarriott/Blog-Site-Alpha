const interval = setInterval(function () {
    var xmlHttp = new XMLHttpRequest();
    var slackMessages = document.getElementById('slack_messages');
    xmlHttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var i;
            for (i = 0; i < this.responseText.length; i++){
                console.log(i)
            }
        }
            //slackMessages.innerHTML += this.responseText
        };
    xmlHttp.open('GET', '/slack/channel_msg');
    xmlHttp.send();


}, 10000);