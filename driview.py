import dfile

v_path = "./../../../../Volumes"

drives = dfile.get_drive_list(v_path)
dfile.print_all(v_path, drives)
