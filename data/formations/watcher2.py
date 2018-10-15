import os
import argparse
import inotify.adapters

target_events=[ 'IN_CREATE', 'IN_MODIFY' ]

parser = argparse.ArgumentParser(description='Command watcher')
parser.add_argument("-v", "--verbose", dest='verbose', help="increase output verbosity",
                    action="store_true")
parser.add_argument("-p", "--path", dest='path', help="define path to watched directory")
parser.add_argument("-c", "--command", dest='cmd', help="define command to execute")
args = parser.parse_args();

path='.'
if args.path:
	path=args.path

cmd="echo 'Modification detected'"
if args.cmd:
	cmd=args.cmd

notifier = inotify.adapters.Inotify()
if args.verbose:
	print("Starting watching %s directory..." % path)
notifier.add_watch(path)

for event in notifier.event_gen():
    if event is not None and event[1][0] in target_events:
        if args.verbose:
            print("EVENT : %s " % str(event))      # uncomment to see all events generated
            print("file '{0}' created in '{1}'".format(event[3], event[2]))
            for idx, elt in enumerate(event):
            	print("EVT %d: %s" % (idx, str(elt)))
            print("Running command : %s" % cmd)
            os.system(cmd)
