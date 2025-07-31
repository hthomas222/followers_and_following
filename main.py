def followers_and_following():

    with open("following.txt") as fr:
        f1 = fr.readlines()
    following = []
    for i in f1:
        following.append(i.strip())

    with open("followers.txt") as fr:
        f2 = fr.readlines()
    followers = []
    for i in f2:
        followers.append(i.strip())

    only_in_following = set(following) - set(followers)
    print("Following only:", only_in_following)
    for i in only_in_following:
        print(i)

    # Find elements only in list2
    only_in_followers = set(followers) - set(following)
    print("Followers only:")
    for i in only_in_followers:
        print(i)

# main
followers_and_following()
