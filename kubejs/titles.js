titles_json_path = "./local/titles.json"


var json_titles = {};
try{
    json_titles = json.read(titles_json_path)
}catch (any){
    json.write(titles_json_path, {})
    json_titles = {}
}

function save_titles()
{
    json.write(titles_json_path, json_titles);
}

function get_player_title_info(player)
{
    json_titles = get_json_titles();
    if (player.toString() in json_titles)
    {
        return json_titles[player.toString()];
    }else
    {
        json_titles[player.toString()] = {};
        save_titles();
        return {};
    }
}


if (mod.isloaded("ftbutilities"))
{
    // For admin
    function command_titles_admin(sender, args){
        var subcommand = {
            "list": function(player_name){
                if ()
            }, 
            "give": function(player_name, title){
                
            }, 
            "take": function(player_name, title){

            }
        }
        subcommand[args[0]](args.slice(1))
    }

    // For player
    function command_titles(sender, args){
        var subcommand = {
            "list": function(player){
                var title_list = get_player_title_info(player)["list"]
                for (var i = 0; i < title_list.length; i ++){
                    player.tell(String(i) + ". " + title)
                }
            }, 
            "get": function(player){
                player.tell("Your cuurent title:")
                player.tell(get_player_title_info(player)["current"])
            }, 
            "set": function(player, idx){
                var info = get_player_title_info(player)
                var list = info["list"]
                if (idx >= 0 && idx < list.length)
                {
                    info["current"] = list[idx]
                    json.write(json_titles, json_titles)
                }
            },
            "clear": function(player){
                get_player_title_info(player)['current'] = ''
                save_titles()
                sender.server.runCommand(command("nick", ))
            }
        }
        if (args.length >= 1){
            subcommand[args[0]](sender.player, args.slice(1))
        }else{
            sender.player.tell("/titles get   显示当前称号");
        }
    }

    events.listen("command.registry", function (event){
        event
            .create('titles_admin')
            .op()
            .execute(command_titles)
            .add()

        event
            .create('titles')
            .execute(command_title)
            .add()
    })

}else {
    utils.server.tell("Title system is currently disabled.")
    utils.server.tell("Please install FTB Utilities to get access to title system.")
}
