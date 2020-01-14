var min_distance = 1000;
var max_distance = 5000;

var range = max_distance - min_distance;
var pi2 = 6.28318530717959;
events.listen("command.registry", function(event){
	event.create("admin_rtp")
		.op()
		.execute(function(sender, args){
			if (args.size == 1){
				var d = utils.random.nextDouble();
				d *= range;
				d += min_distance;
				var angle = utils.random.nextDouble();
				angle = angle * pi2;
				var x = Math.cos(angle) * d;
				var z = Math.sin(angle) * d;
				var player_list = utils.server.getEntities(args[0]);
				sender.runCommand("effect " + args[0] + " minecraft:resistance 10 5");
				player_list.forEach(function(entity){
					entity.setPosition(x, 256.0, z);
				});
				
			}
			else{
				sender.tell("Usage: admin_op <player>");
			}
		})
		.add();

});
