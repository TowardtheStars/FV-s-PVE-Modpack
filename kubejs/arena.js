
if (mod.isLoaded("customstartinggear")){
    subcommand = {
        'store': function (sender, args){
            if (args.size() == 1)
            {
                var server = sender.server;
                var entityList = server.getEntities(args[0]);
                entityList.forEach(function (e){
                    if (e.player){
                        server.runCommand("csg_kit add _arena_kit_" + e.name + " " + e.name)
                    }
                });
            }
        },

        'recover': function (sender, args){
            if (args.size() == 1)
            {
                var server = sender.server;
                var entityList = server.getEntities(args[0]);
                entityList.forEach(function (e){
                    if (e.player){
                        server.runCommand("csg_kit give _arena_kit_" + e.name + " " + e.name)
                    }
                });
            }
        }
    };

    help_msg = "";

    events.listen("command.registry", function(event){
        event
            .create("arena")
            .execute(function (sender, args){
                var player = sender.player;
                if (args.size() == 0)
                {
                    player.tell(help_msg);
                } else {
                    subcommand[args[0]](sender, args.subList(1, args.size()));
                }
            })
            .op()
            .add();
    });
}