#m is the number of health element can get in health
#for example [1,2,3,4,5] can get 1,2,3,4 or 2,3,4,5, etc
#servertype is type of server [1,4, 6] there are 3 type of server which is 1,4, and 6
#find the maxhealth that can sum up to


def maxhealthsum(health, serverType, m):
    server_groups = {}
    for h, t in zip(health, serverType):
        if t not in server_groups:
            server_groups[t] = []
        server_groups[t].append(h)

    type_health_sums = []
    for h_list in server_groups.values():
        type_health_sums.append(sum(h_list))

    type_health_sums.sort(reverse=True)
    return sum(type_health_sums[:m])