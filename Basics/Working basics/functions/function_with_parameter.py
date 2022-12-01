def escape_by(plan):
    if plan == "jumping over":
        print("we cannot escape that way the boulder is too big")
    elif plan == "running around":
        print("we cannot escape that way the boulder is moving to fast")
    elif plan == "going deeper":
        print("that might just work lets go deeper")
    else:
        print("we cannot escape that way the boulder is in the way")


escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")
