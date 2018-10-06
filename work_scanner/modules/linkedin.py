from linkedin import linkedin
from modules.base.site import Site


class LinkedIn(Site):

    def __init__(self, keywords=None):

        # Fill it with your token, in case you don't have one use scripts/linkedin_auth_bot
        TOKEN = None

        try:
            self.application = linkedin.LinkedInApplication(token=TOKEN)
        except AssertionError as a:
            print('LinkedIn is not configured')
            print(a)

        if keywords is None:
            keywords = []
        self.keywords = keywords

    def scan(self):
        for keyword in self.keywords:
            jobs = self.application.search_job(selectors=[{'jobs': ['id', 'customer-job-code', 'posting-date']}],
                                               params={'title': keyword, 'count': 2})
            print(jobs)
