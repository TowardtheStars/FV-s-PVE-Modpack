
var ticker = 0;
events.listen("server.tick", function(event){
	ticker += 1;
	(ticker%1200 == 0)?event.server.runCommand("/whitelist reload"):0;
});

