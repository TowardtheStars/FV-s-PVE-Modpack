
version:=2.0.1-alpha
build_dir:=./build
pack_name:=FVs PVE
zipfile_name:="${build_dir}/${pack_name}-v${version}.zip"

all: init mod_list packup

init:
	if [ ! -d ${build_dir} ]; then mkdir ${build_dir}; fi

update_readme: init
	cp ./readme.md ./build/readme.md
	sed -i 's/%{version}/$(version)/g' ./build/readme.md

packup: init
	if [ -f ${zipfile_name} ]; then rm ${zipfile_name}; fi
	xargs -r -a zip.whitelist zip -r -q ${zipfile_name}
	xargs -r -a zip.nodir     zip -j -q ${zipfile_name}
	xargs -r -a zip.blacklist zip    -q ${zipfile_name} -d

mod_list:
	if [ ! -f mod_list.txt ]; then rm mod_list.txt; fi
	find ./mods -maxdepth 1 -type f >> mod_list.txt
	sed -i 's/.\/mods\///g' mod_list.txt
	sed -i 's/.jar//g' mod_list.txt

clear_log:
	if [ -d logs ]; then rm -r logs; fi

update_shop_list:
	python3 ".workspace/shop/shop_list.py"

update_mod_icon:
	python3 ".workspace/generate_icon.py"

clean:
	if [ -d $(build_dir) ]; then rm -r $(build_dir); fi