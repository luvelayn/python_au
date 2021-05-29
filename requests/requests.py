import requests
import json
import datetime

TOKEN = ''
BEGIN = 'VERIFICATION RESULT'
LOGIN = 'OcTatiana'
PREFIX = ['LEETCODE', 'GENERATOR', 'TRIANGLE', 'HEXNUMBER', 'ITERATOR', 'REQUESTS']
GROUP = ['1012', '1013']
ACTION = ['Added', 'Deleted', 'Refactored', 'Moved']


def prepare_headers():
    return {'Authorization': 'Token {}'.format(TOKEN),
            'Content-Type': "application/json",
            'Accept': "application/vnd.github.v3+json"
            }


def get_all_user_pull_reqs(user_name, repos_name, state):
    url = 'https://api.github.com/repos/{}/{}/pulls?state={}'.format(user_name, repos_name, state)
    all_pr = requests.get(url, headers=prepare_headers())
    return all_pr


def get_all_pr_commits(pull_req):
    all_commits = requests.get(pull_req['commits_url'], headers=prepare_headers())
    return all_commits


def check_comment(message):
    res = []
    mass = []
    mass = message.split('-')
    pre = mass[0]
    post = mass[1].split(' ')
    if pre not in PREFIX:
        res.append("The prefix of your comment must be from {}".format(PREFIX))
    if post[0] not in GROUP:
        res.append("Number of your group must be from {}".format(GROUP))
    if len(post) > 1 and post[1] not in ACTION:
        res.append("Action of your comment must be from {}".format(ACTION))
    return '\n'.join(res)


def create_message(pull_req):
    message = "{}\n\n".format(BEGIN)
    message += "Your pull request: {}\n".format(pull_req['title'])
    message += check_comment(pull_req['title'])
    message += '\n\n'
    comment_time = get_time_of_the_last_comment(pull_req)
    for com in get_all_pr_commits(pull_req).json():
        commit_time = get_time_of_the_commit(com)
        if compare_dates(comment_time, commit_time):
            comm = com['commit']
            if len(check_comment(comm['message'])) > 1:
                message += 'Your commit: {}\n'.format(comm['message'])
                message += check_comment(comm['message'])
                message += '\n'
    return message


def send_message(pull_req, message):
    data = {'body': message,
            'path': requests.get(pull_req['url'] + '/files', headers=prepare_headers()).json()[0]['filename'],
            'position': 1,
            'commit_id': pull_req['head']['sha']}
    r = requests.post(pull_req['url'] + '/comments', headers=prepare_headers(), json=data)
    print(r.json())


def get_time_of_the_last_comment(pull_req):
    all_comments = requests.get(pull_req['review_comments_url'], headers=prepare_headers()).json()
    last_comment = "0000-00-00T00:00:00Z"
    for comment in all_comments:
        user_name = comment['user']['login']
        if check_author(LOGIN, user_name):
            message = comment['body']
            if message[:19:] == BEGIN:
                last_comment = comment['created_at']
    return last_comment


def get_time_of_the_commit(com):
    comm = com['commit']['author']
    return comm['date']


def compare_dates(last_comment_date, commit_date):
    if last_comment_date > commit_date:
        return False
    else:
        return True


def check_author(verifying, user_name):
    return verifying == user_name


def main():
    for pr in get_all_user_pull_reqs('ktotoch', 'python_au', 'open').json():
        if len(create_message(pr)) > 120:
            send_message(pr, create_message(pr))


if __name__ == '__main__':
    main()
