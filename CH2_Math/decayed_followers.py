def decayed_followers(intl_followers, fraction_lost_daily, days):
    return intl_followers * ((1 - fraction_lost_daily) ** days)
        
