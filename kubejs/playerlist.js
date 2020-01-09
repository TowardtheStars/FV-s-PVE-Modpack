
// Add a command to see who is online

events.listen("command.registry", function(event){
    event.create("playerlist")
        .execute(function(sender, args){
            sender.server.players.forEach(function(element) {
               sender.tell(element.name) 
            });
        })
        .add();
});
