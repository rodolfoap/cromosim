case "$1" in
e)	vi -p .x
	;;
i)	[ -e .venv ] || python3 -m venv .venv;
	.venv/bin/pip3 install -r requirements.txt;
	echo "$(pwd)" > "$(.venv/bin/python3 -c 'import site; print(site.getsitepackages()[0])')/cromosim-dev.pth"
	;;
"")	true
	;;
esac
