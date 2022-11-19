import os
from github import Github


# Getting needed path
path = os.path.join(os.getcwd(), "Data")
Files = os.listdir(path)
Files_List = [os.path.join(path, x) for x in Files]


# Setting up Github Api
user = Github("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")
repo = user.get_user().get_repo("RuminantBin")
Files = repo.get_contents("Data")


def Fload():
    # Updating file in server
    try:
        for index in range(len(Files_List)):
            repo.update_file(
                Files[index].path,
                "Dustbin Data Update",
                Files_List[index],
                Files[index].sha,
                branch="main",
            )

        return "File Complete"

    except:
        return "Network connection Lost"
