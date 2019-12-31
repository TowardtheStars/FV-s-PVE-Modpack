#modloaded opencomputers

recipes.remove(<opencomputers:card:8>);

recipes.removeShapeless(<opencomputers:storage:1>, [<opencomputers:storage:1>, <opencomputers:tool:4>]);

recipes.addShapeless(
    "openOSDiskRecipe", 
    <opencomputers:storage:1>.withTag(
        {
            "oc:data": {"oc:fs.label": "openos"}, 
            "oc:color": 2, 
            display: {
                Name: "OpenOS (Operating System)"
            }, 
            "oc:lootFactory": "opencomputers:openos"
        }
    ), 
    [
        <opencomputers:storage:1>, 
        <opencomputers:tool:4>,
        <abyssalcraft:gatekeeperessence>
    ],
    null,
    null
);
