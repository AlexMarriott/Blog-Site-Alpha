    const interval = setInterval(function() {
        updateList();
    }, 5000);

    function updateList(){
      var url = 'https://slack.com/api/channels.history?token=xoxp-847971877056-847971877792-856975052375-2afbe577916e8940dc0e4b3bf3f4f3c6&channel=CQLEU7DMZ&pretty=1';
      var request = new XMLHttpRequest();
        request.open('GET', url);
        request.send();

        request.onreadystatechange  = function(){
          if (this.readyState==4 && this.status==200){
            console.log(request.responseText);
          }

        };

    }