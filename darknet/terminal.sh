gnome-terminal --geometry=150x50 --tab --title="echo" -e "bash -c \"python result_img/resize.py ;exec bash\"" --tab --title="idea" -e "bash -c \"./darknet detector demo cfg/obj.data cfg/yolo-voc.2.0.cfg backup/yolo-voc_last.weights ~/final_test.mp4 ;exec bash\""