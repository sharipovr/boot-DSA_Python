def does_name_exist(first_names, last_names, full_name):
    for fn in first_names:
        for ln in last_names:
            if f"{fn} {ln}" == full_name:
                return True
            
    return False
