
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

#
# loader = insta_handler.init_loader()
#
# profile = instaloader.Profile.from_username(loader.context, 's0cial_menace')
#
