


function getFromArray(array, pos, default_value)
{
    var result = default_value;
    if (array.length >= pos + 1){
        result = array[pos];
    }
    return result;
}

var scoreboard = {
    __gen_scoreboard_command:function(){
        var i = 0;
        var result = '/scoreboard';
        for (i = 0; i < arguments.length; i++)
        {
            result += ' ';
            result += (arguments[i]).toString();
        }
        return result;
    },
    objectives: {
        add: function (id, criteria) {
            var disp_name = getFromArray(arguments, 2, '');
            return scoreboard.__gen_scoreboard_command('objectives', 'add', id, criteria, disp_name);
        },
        list: function (){
            return scoreboard.__gen_scoreboard_command('objectives', 'list');
        },
        remove: function (id)
        {
            return scoreboard.__gen_scoreboard_command('objectives', 'remove', id);
        },
        setdisplay: function (position)
        {
            var id = getFromArray(arguments, 1, '');
            return scoreboard.__gen_scoreboard_command('objectives', 'setdisplay', position, id);
        }
    },
    players: {
        add: function(player, id, amount){
            var nbt_tag = getFromArray(arguments, 3, '');
            return scoreboard.__gen_scoreboard_command('players', 'add', player, id, amount, nbt_tag);
        },
        enable: function(player, trigger){
            return scoreboard.__gen_scoreboard_command('players', 'enable', player, trigger);
        },
        list: function(){
            var player = getFromArray(arguments, 0, '');
            return scoreboard.__gen_scoreboard_command('players', 'list', player);
        },
        operation: function(target_player, target_id, operation, selector, id){
            return scoreboard.__gen_scoreboard_command('players', 'operation', target_player, target_id, operation, selector, id);
        },
        remove: function(player, id, amount){
            var nbt_tag = getFromArray(arguments, 3, '');
            return scoreboard.__gen_scoreboard_command('players', 'remove', player, id, amount, nbt_tag);
        },
        reset: function(player){
            var id = getFromArray(arguments, 1, '');
            return scoreboard.__gen_scoreboard_command('players', 'reset', player, id);
        },
        set: function(player, id, amount){
            var nbt_tag = getFromArray(arguments, 3, '');
            return scoreboard.__gen_scoreboard_command('players', 'set', player, id, amount, nbt_tag);
        },
        tag: {
            add: function(player, tag){
                var nbt_tag = getFromArray(arguments, 2, '');
                return scoreboard.__gen_scoreboard_command('players', 'tag', player, "add", tag, nbt_tag);
            },
            remove: function(player, tag){
                var nbt_tag = getFromArray(arguments, 2, '');
                return scoreboard.__gen_scoreboard_command('players', 'tag', player, "remove", tag, nbt_tag);
            },
            list: function(player, tag){
                var nbt_tag = getFromArray(arguments, 2, '');
                return scoreboard.__gen_scoreboard_command('players', 'tag', player, "list", tag, nbt_tag);
            }
        },
        test: function(player, id, min){
            var max = getFromArray(arguments, 3, 2147483647);
            return scoreboard.__gen_scoreboard_command('players', 'test', player, id, min, max);
        }
    },
    teams: {
        add: function(){

        },
        empty: function(){

        },
        join: function(){

        },
        leave: function(){

        },
        list: function(){

        },
        option: function(){

        },
        remove: function(){

        }
    }
};

