#!/usr/bin/env python3.6
import configargparse

from box import Box
from emailer import santa_email
from random import randint
from yaml import load

def select(names, debug=False):

    chosen = set([])

    selections = {}
    try:
        for name in names.keys():
            if debug:
                print("Name: %s" % name)
            available = list(set(names.keys()) - set([name, names[name]['exclude']]) - chosen)
            if debug:
                print("Available: %s" %  ','.join(available))
            index = randint(0, len(available) - 1)
            selected = available[index]
            if debug:
                print("Selected: %s" % selected)
            selections[name] = selected
            chosen.add(selected)
    except:
        print('Retrying after exception')
    #    selections = select(names)

    return selections


def main():
    parser = configargparse.ArgParser(description='Send secret Santa emails', default_config_files=['/etc/secret_santa/*.conf', '/Users/dvitone/.secret_santa/*.conf'])
    parser.add_argument('--names', '-n', metavar='NAMES.yaml',
                               default='~/.secret_santa/names.yaml',
                               type=configargparse.FileType('r'),
                               help='yaml file containing participant data')
    parser.add_argument('--debug', action='store_true',
                               help='print out hidden data such as the secret santa choices')
    parser.add_argument('--dry_run', action='store_true',
                               help='dry run mode which does not send emails')
    parser.add_argument('--dry_run_email', type=str,
                               default=None,
                               help='dry run mode which does not send emails address')
    parser.add_argument('--password', type=str,
                               required=True,
                               help='Email Password')
    parser.add_argument('--username', type=str,
                               required=True,
                               help='Email Username')
    parser.add_argument('--font', type=str,
                               default='Arial.TTF',
                               help='Font Name Username')
    parser.add_argument('--font_path', type=str,
                               default='/opt/homebrew-cask/Caskroom/font-arial/2.82/',
                               help='Font Path')

    args = parser.parse_args()

    config, credentials, images = {}, {}, {}

    credentials['password'] = args.password
    credentials['username'] = args.username

    images['font'] = args.font
    images[ 'font_path'] = args.font_path

    config['email'] = credentials
    config['images'] = images
    config = Box(config)

    names = load(args.names.read())

    selection = select(names, debug=args.debug)
    for name in names.keys():
        if not names[name]['exclude']:
            names[name]['exclude'] = 'anyone'
        if args.debug:
            print("Emailing %s <%s>: %s" % (name, names[name]['email'], selection[name]))
        else:
            print("Emailing %s <%s>: HIDDEN" % (name, names[name]['email']))
        email_recipient = args.dry_run_email or names[name]['email']
        if not args.dry_run:
            santa_email(name, names[name]['email'], selection[name], names[name]['exclude'], config=config)


if __name__ == '__main__':
    main()
