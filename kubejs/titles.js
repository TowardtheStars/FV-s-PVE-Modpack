
var CURRENT = 'title_kjs.current_title';
var TITLE_LIST = 'title_kjs.list'

function getPlayerRank(player){
    return player.data.ftbutilities.rank;
}

function setTitle(player, title){
    if (title == null)
    {
        utils.server.runCommand(
            "ranks set_permission " + player.name + "ftbutilities.chat.name_format {name}"
        );
        utils.server.runCommand(
            "ranks set_permission " + player.name + " " + CURRENT + " \"\""
        )
    }else{
        utils.server.runCommand(
            "ranks set_permission " + player.name + " ftbutilities.chat.name_format \"[" + title + "]{name}\""
        );
        utils.server.runCommand(
            "ranks set_permission " + player.name + " " + CURRENT + " " + title
        );
    }
    ftbutilities.saveRanks();
}

// Returns a java String list
function getAvailableTitles(player){
    var rank = getPlayerRank(player);
    var list_str = rank.getPermission(TITLE_LIST);
    return list_str.split("\\|");
}


if (ftbutilities & ftbutilities.ranksActive)
{
    // Give each player a unique rank
    events.listen("player.logged_in", function(event){
        var player = event.player;
        var rank_id = "personal_rank_" + player.name;
        if (!ftbutilities.ranks.contains(rank_id))
        {
            event.server.runCommand(
                "ranks create " + rank_id + " " + "player"
            );
        }
        var newRank = ftbutilities.getRank(rank_id);
        if (getPlayerRank(player).id != rank_id){
            events.postCancellable('ftbutilities.rank.promoted.' + rank_id, {'player':event.player, 'rank': newRank});
        }
        ftbutilities.saveRanks();
    });

    // For admin
    function command_titles_admin(sender, args){
        var subcommand = {
            "list": function(player_name){
                var player = sender.server.getPlayer(player_name);
                if (player)
                {
                    sender.tell(getAvailableTitles(player))
                }else{
                    sender.tell("Please select a player")
                }
            }
        }
        subcommand[args[0]](args.slice(1))
    }

    // For player
    function command_titles(sender, args){
        var subcommand = {
            "list": function(player){
                var title_list = getAvailableTitles(player);
                for (var i = 0; i < title_list.length; i ++){
                    player.tell(String(i) + ". " + title);
                }
            }, 
            "get": function(player){
                player.tell("Your cuurent title:");
                player.tell(getPlayerRank(player).getPermission(CURRENT));
            }, 
            "set": function(player, idx){
                var list = getAvailableTitles(player);
                if (idx >= 0 && idx < list.length)
                {
                    setTitle(player, list[idx]);
                }
            },
            "clear": function(player){
                setTitle(player, null);
            }
        };

        if (args.length >= 1){
            subcommand[args[0]](sender.player, args.slice(1));
        }else{
            sender.player.tell("/titles get   显示当前称号");
        }
    }

    events.listen("command.registry", function (event){
        event
            .create('titles_admin')
            .op()
            .execute(command_titles_admin)
            .add();

        event
            .create('titles')
            .execute(command_titles)
            .add();
    })

}else {
    utils.server.tell("Title system is currently disabled.");
    utils.server.tell("Please install FTB Utilities and activate rank system to get access to title system.");
}
