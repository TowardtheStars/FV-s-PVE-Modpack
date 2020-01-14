events.listen("command.registry", function(event){
	event
		.create('runkjs')
		.op()
		.execute(function(sender, args){
			var c = "";
			args.forEach(function (e){
				c += " " + e.toString();
			});
			sender.tell(c);
			sender.tell(eval(c).toString());
		})
		.add();
});

