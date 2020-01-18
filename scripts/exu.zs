#modloaded extrautils2 abyssalcraft
recipes.remove(<extrautils2:rainbowgenerator:1>);
recipes.remove(<extrautils2:rainbowgenerator:2>);

recipes.addShaped(
    "extrautils2__rainbow_gen_bottom", 
    <extrautils2:rainbowgenerator:1>, 
    [
        [
            <extrautils2:machine>.withTag({Type: "extrautils2:generator_netherstar"}), 
            <extrautils2:machine>.withTag({Type: "extrautils2:generator_overclock"}), 
            <extrautils2:machine>.withTag({Type: "extrautils2:generator_pink"})
        ], 
        [
            <extrautils2:machine>.withTag({Type: "extrautils2:generator_potion"}), 
            <abyssalcraft:gatekeeperessence>, 
            <extrautils2:machine>.withTag({Type: "extrautils2:generator_redstone"})
        ], 
        [
            <extrautils2:machine>.withTag({Type: "extrautils2:generator_slime"}), 
            <extrautils2:machine>.withTag({Type: "extrautils2:generator_survival"}), 
            <extrautils2:machine>.withTag({Type: "extrautils2:generator_tnt"})
        ]
    ]
);

recipes.addShaped(
    "extrautils2__rainbow_gen_top", 
    <extrautils2:rainbowgenerator:2>, 
    [
        [
            <extrautils2:machine>.withTag({Type: "extrautils2:generator_culinary"}), 
            <extrautils2:machine>.withTag({Type: "extrautils2:generator_death"}), 
            <extrautils2:machine>.withTag({Type: "extrautils2:generator_dragonsbreath"})
        ], 
        [
            <extrautils2:machine>.withTag({Type: "extrautils2:generator_enchant"}), 
            <abyssalcraft:gatekeeperessence>, 
            <extrautils2:machine>.withTag({Type: "extrautils2:generator_ender"})
        ], 
        [
            <extrautils2:machine>.withTag({Type: "extrautils2:generator"}), 
            <extrautils2:machine>.withTag({Type: "extrautils2:generator_ice"}), 
            <extrautils2:machine>.withTag({Type: "extrautils2:generator_lava"})
        ]
    ]
);

