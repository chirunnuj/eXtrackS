import requests
import sys
import argparse

METHODS = ['GET', 'POST']
GET = 0
POST = 1

def main(argv):
    parser = argparse.ArgumentParser(prog='python eXtrackS.py', description = 'eXtrackS - Time Base SQLi Attack. Tool to automate extraction of known Time-Based SQLi vulnerability.')
    parser.add_argument('TargetURL')
    parser.add_argument('-u', '--url', help='The URL to attack, eg. "https://www.target.com".')
    parser.add_argument('-m', '--method', help='The request method, ie. GET, POST.')
    parser.add_argument('-d', '--data', help='Attack\'s Payload.')
    parser.add_argument('-tc', '--timecheck', help='Idle Time (Seconds) for True response.')
    parser.add_argument('-ts', '--truestring', help='String to check for True response.')
    parser.add_argument('-fs', '--falsestring', help='String to check for False response.')
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    # print(args)

    headers = {
        
    }

    method = METHODS[GET]
    if args.method is not None:
        method = args.method

    if args.timecheck is None:
        parser.print_help()
        sys.exit()
        
    # target_url = args.url
    # time_check = args.timecheck
    # data = args.data
    # true_string = args.truestring
    # false_string = args.falsestring

    # if method == METHODS[GET]:
    #     response = get(target_url, headers, data=data)
    # elif method == METHODS[POST]:
    #     response = post()
    # else:
    #     return None

    # if response.elapsed.total_seconds() > time_check:
    #     return True
    # else:
    #     return False

def get(target_url, headers, data):
    return requests.get(target_url, headers = headers, params = data)


def post(target_url, headers, data):
    return requests.post(target_url, headers = headers, params = data)


def test():
    r = requests.get('https://www.securitas.co.th')
    #print(r.content)
    print(r.headers)
    print(r.elapsed.total_seconds())

if __name__ == "__main__":
    main(sys.argv[1:])