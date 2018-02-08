import argparse
import logging
import random
import requests
import time
from requests.auth import HTTPBasicAuth

from arguments import Arguments

__author__ = 'viaa'

BASEURL_QAS = 'https://archief-qas.viaa.be'
BASEURL_PRD = 'https://archief-qas.viaa.be'
PATH = '/mediahaven-rest-api/resources/media/'


def main():
    arguments = Arguments()
    init_logger()
    parser = argparse.ArgumentParser()
    parser.add_argument('--fragment_id', help='the fragment id of the complex object', type=str)
    parser.add_argument('--username', help='the username to use when connecting to mediahaven', type=str)
    parser.add_argument('--password', help='the password to use when connecting to mediahaven', type=str)
    parser.add_argument('--environment', help='the environment to test. QAS or PRD', type=str)
    parser.parse_args(namespace=arguments)

    check_arguments(arguments)

    logging.info('Running in environment: ' + arguments.environment)

    url = arguments.baseurl + PATH + arguments.fragment_id + '/children'
    getchildrenrequest = requests.get(url, auth=HTTPBasicAuth(arguments.username, arguments.password))
    jsonresult = getchildrenrequest.json()
    totalnrofresults = jsonresult['totalNrOfResults']
    children = jsonresult['mediaDataList']
    logging.info('Fragment has ' + str(totalnrofresults) + ' children: ')

    rewritedata = []
    counter = 1
    for child in children:
        logging.info('\t' + str(counter) + ': ' + child['externalId'])
        rewritedata.append(('id', child['fragmentId']))
        counter += 1

    randomindex = random.randint(0, len(children) - 1)

    logging.info('Removing item with index ' +
                 str(randomindex) + ' (' + children[randomindex]['externalId'] +
                 ') from the ensemble')
    deletedchild = children[randomindex]['fragmentId']

    # Remove the object from the ensemble
    url = arguments.baseurl + PATH + arguments.fragment_id + '/children/' + deletedchild
    deletefromensemblerequest = requests.delete(url, auth=HTTPBasicAuth(arguments.username, arguments.password))

    # Add object back to ensemble
    url = arguments.baseurl + PATH + arguments.fragment_id + '/children'
    deletedata = {'id': (None, deletedchild)}
    logging.info('Re-adding the previously deleted object')
    addensemblerequest = requests.post(url, files=deletedata, auth=HTTPBasicAuth(arguments.username, arguments.password))

    # Rewrite ensemble
    url = arguments.baseurl + PATH + arguments.fragment_id + '/children'
    logging.info('Rewriting the object')
    rewriteensemblerequest = requests.put(url, files=rewritedata, auth=HTTPBasicAuth(arguments.username, arguments.password))

    # Sleep
    logging.info('Sleeping to make sure the update persisted')
    time.sleep(5)

    url = arguments.baseurl + PATH + arguments.fragment_id + '/children'
    getchildrenrequest = requests.get(url, auth=HTTPBasicAuth(arguments.username, arguments.password))
    jsonresult = getchildrenrequest.json()
    totalnrofresults = jsonresult['totalNrOfResults']
    children = jsonresult['mediaDataList']
    logging.info('Fragment has ' + str(totalnrofresults) + ' children.')


def init_logger():
    # create logger with 'spam_application'
    logger = logging.getLogger('')
    formatter = logging.Formatter('%(asctime)-15s   %(levelname)-8s: %(message)s')
    logger.setLevel(logging.INFO)

    # Create Console Logger
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Create File Logger
    try:
        logfile = './test_complex_objects.log'
        fh = logging.FileHandler('%s' % logfile)
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    except PermissionError:
        logging.error("Permission denied for {}".format(logfile))


def check_arguments(arguments):
    if arguments.fragment_id is None:
        close("No fragment id specified")

    if arguments.username is None:
        close("No username specified")

    if arguments.password is None:
        close("No password specified")
    if arguments.environment is None:
        arguments.environment = 'QAS'
    if arguments.environment == 'QAS':
        arguments.baseurl = BASEURL_QAS
    else:
        arguments.baseurl = BASEURL_PRD


def close(message):
    logging.error(message)
    exit(1)


main()
