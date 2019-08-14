
import instaloader

class Insta_handler:
    login = '\0'
    password = '\0'
    profile = '\0'

    def init_loader(self):
        loader = instaloader.Instaloader()
        loader.login(self.login, self.password)
        return loader

    def init_profile(self, loader):
        self.profile = instaloader.Profile.from_username(loader.context, self.login)

    def dont_follow_back(self):
        followers = []
        following = []
        not_following_back = []

        for follower in self.profile.get_followers():
            followers.append(follower.username)

        for follower in self.profile.get_followees():
            following.append(follower.username)

        not_following_back = set(following) - set(followers)

        msg = '\n'.join(not_following_back)

        return msg
