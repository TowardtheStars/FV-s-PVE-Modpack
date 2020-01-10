# Modpack config
version:=2.2.1-beta
pack_name:=FVs-PVE

# Build config
## Directories
build_dir:=./build
build_config:=./build_config
sh_script_dir:=./shell_scripts

## Files
mod_list_file:=${build_dir}/mod_list.txt
zipfile_name:=${build_dir}/${pack_name}-v${version}.zip

all: init update_readme mod_list shop_list bounty_list packup dev_mode

init:
	if [ ! -d "${build_dir}" ];		\
		then mkdir ${build_dir};		\
	fi					

update_readme: init
	cp ./readme.md ${build_dir}/README.md
	sed -i 's/%{version}/$(version)/g' ${build_dir}/README.md
	cp ${build_dir}/README.md ${build_dir}/使用前必读.txt

packup: init lan_mode
	if [ -f "${zipfile_name}" ]; then rm "${zipfile_name}" ; fi
	xargs --arg-file=${build_config}/zip.files find 		\
		| grep -v --file=${build_config}/zip.blacklist 		\
		| xargs -d "\n" zip -r ${zipfile_name}
	xargs --arg-file=${build_config}/zip.nodir find | xargs zip -j "${zipfile_name}"
	@echo "Pack up finished"
	@echo "Result: ${zipfile_name}"

mod_list: init sp_mode
	@echo "Recording mod list..."
	if [ -f ${mod_list_file} ]; then rm ${mod_list_file}; fi
	find ./mods -maxdepth 1 -type f >> ${mod_list_file}
	sed -i 's/.\/mods\///g' ${mod_list_file}
	sed -i 's/.jar//g' ${mod_list_file}
	@echo "Finished"

clear_log:
	if [ -d logs ]; then rm -r logs; fi
	if [ -d "./crash-reports" ]; then rm -r "./crash-reports"; fi
	@echo "log and crash-reports cleared"

shop_list:
	@python3 ".workspace/shop/shop_list.py"

dump_doc:
	@python3 ".workspace/Aurora_web/dump_web.py"
	rm .workspace/Aurora_web/pages.txt
	

bounty_list:
	@python3 ".workspace/bounty/bounty.py"

lan_mode:
	@echo "Into single player mode"
	@sh ${sh_script_dir}/ModpackModeSelector.sh l

client_mode:
	@echo "Into client mode"
	@sh ${sh_script_dir}/ModpackModeSelector.sh c

server_mode:
	@echo "Into server mode"
	@sh ${sh_script_dir}/ModpackModeSelector.sh s

clean:
	if [ -d $(build_dir) ]; then rm -r $(build_dir); fi