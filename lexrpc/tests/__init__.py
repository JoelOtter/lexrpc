import logging, os, sys

# Piggyback on unittest's -v and -q flags to show/hide logging.
logging.basicConfig()
if '-v' in sys.argv:
    logging.getLogger().setLevel(logging.DEBUG)
elif 'discover' in sys.argv or '-q' in sys.argv or '--quiet' in sys.argv:
    logging.disable(logging.CRITICAL + 1)

