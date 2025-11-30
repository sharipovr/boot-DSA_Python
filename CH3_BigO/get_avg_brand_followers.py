def get_avg_brand_followers(all_handles, brand_name):
    count = 0
    for infl in all_handles:
        for handle in infl:
            if brand_name in handle:
                count += 1
    return count/len(all_handles)                

