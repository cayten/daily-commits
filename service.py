class Repo:
    def get_user(self, user_id:int):
        raise NotImplementedError

class Service:
    def __init__(self, repo: Repo):
        self.repo=repo
    def welcome(self, user_id:int)->str:
        user=self.repo.get_user(user_id)
        if not user:
            return 'not found'
        return f"hello {user['name']}"
