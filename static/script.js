const interval = setInterval(function () {
    updateList();
}, 5000);

function updateList() {
    //10000 = 10 seconds in millseconds
    // print('It'.concat(' is',' a',' great',' day.'));
    var timestamp = Date.now() - 10000;
    var url = 'https://slack.com/api/channels.history?token=xoxp-847971877056-847971877792-856975052375-2afbe577916e8940dc0e4b3bf3f4f3c6&channel=CQLEU7DMZ&count=1&pretty=1';
    var request = new XMLHttpRequest();
    request.open('GET', url);
    request.send();

    request.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            //console.log(request.responseText);
            console.log(timestamp);
        }

    };

}