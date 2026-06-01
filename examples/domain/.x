case "$1" in
e)	vi -p .x
	;;
1)	./domain_from_json.py --json input_room.json ;;
2)	./domain_stadium.py ;;
3)	./domain_shibuya_crossing.py ;;
"")	./domain_room.py ;;
esac
