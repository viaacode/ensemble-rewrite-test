#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import logging
import random
import requests
import time
from requests.auth import HTTPBasicAuth

__author__ = 'viaa'

BASEURL_QAS = 'https://archief-qas.viaa.be'
BASEURL_PRD = 'https://archief.viaa.be'
PATH = '/mediahaven-rest-api/resources/media/'


def checknumberofchildren(arguments, base_url, fragmentid):
    url = base_url + fragmentid + '/children'
    getchildrenrequest = requests.get(url, auth=HTTPBasicAuth(arguments.username, arguments.password))
    jsonresult = getchildrenrequest.json()
    totalnrofresults = jsonresult['totalNrOfResults']
    return totalnrofresults

def performoperations(arguments, base_url, fragmentid):
    # Requests authorization object
    mh_auth = HTTPBasicAuth(arguments.username, arguments.password)
    url = base_url + fragmentid + '/children'
    getchildrenrequest = requests.get(url, auth=mh_auth)
    jsonresult = getchildrenrequest.json()
    children = jsonresult['mediaDataList']

    rewritedata = []
    counter = 1
    for child in children:
        logging.info('\t%s: %s', counter, child['externalId'])
        rewritedata.append(('id', child['fragmentId']))
        counter += 1

    randomindex = random.randint(0, len(children) - 1)

    logging.info('Removing item with index %s (%s) from the ensemble',
                    randomindex, children[randomindex]['externalId'])
    deletedchild = children[randomindex]['fragmentId']

    # Remove the object from the ensemble
    url = base_url + fragmentid + '/children/' + deletedchild
    deletefromensemblerequest = requests.delete(url, auth=mh_auth)

    # Add object back to ensemble
    url = base_url + fragmentid + '/children'
    deletedata = {'id': (None, deletedchild)}
    logging.info('Re-adding the previously deleted object')
    addensemblerequest = requests.post(url, files=deletedata,
                                       auth=mh_auth)

    # Rewrite ensemble
    url = base_url + fragmentid + '/children'
    logging.info('Rewriting the object')
    rewriteensemblerequest = requests.put(url, files=rewritedata,
                                          auth=mh_auth)

    # Sleep
    logging.info('Sleeping to make sure the update persisted')
    time.sleep(5)

    url = base_url + fragmentid + '/children'
    getchildrenrequest = requests.get(url, auth=mh_auth)
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

def close(message):
    logging.error(message)
    exit(1)


def main(cmd_args):
    logging.info('Running in environment: %s', cmd_args.environment)
    base_url = BASEURL_QAS if cmd_args.environment.lower() == 'qas' else BASEURL_PRD
    getseturl = base_url + PATH
    # We need to construct the query ourselves (see https://github.com/requests/requests/issues/1454).
    # If we don't, the URL will be: '/mediahaven-rest-api/resources/media/?q=%2B%28MediaObjectType%3ASet%29&nrOfResults=1'
    # Request multiple sets since not all will have children
    logging.info('Fetching sets from: %s', getseturl)
    getsetrequest = requests.get(getseturl + '?q=%2B(MediaObjectType:Set)',
                                 auth=HTTPBasicAuth(cmd_args.username, cmd_args.password))
    getsetresponse = getsetrequest.json();
    nr_of_results = getsetresponse['totalNrOfResults']
    logging.info('Sets found (totalNrOfResults): %s', nr_of_results)
    setresults = getsetresponse['mediaDataList']
    if setresults:
        for complex in setresults:
            fragmentid = complex['fragmentId']
            logging.debug('Checking fragmentId "%s" for children...', fragmentid)
            nrofchildren = checknumberofchildren(cmd_args, getseturl, fragmentid)
            if nrofchildren > 0:
                logging.info('Found a set (%s) with %s children.', fragmentid, nrofchildren)
                performoperations(cmd_args, getseturl, fragmentid)
                break

if __name__ == "__main__":
    init_logger()
    # Parse the command line arguments
    parser = argparse.ArgumentParser(prog="ensemble-rewrite-test",
                description="""Tests the rewrite methods of MediaHaven
                    for ensembles.""")
    parser.add_argument('-u', '--username', type=str, dest='username',
            required=True,
            help='Username to use when connecting to mediahaven.')
    parser.add_argument('-p', '--password', type=str, dest='password',
            required=True,
            help='Password to use when connecting to mediahaven.')
    parser.add_argument('-e', '--environment', type=str, choices=['QAS', 'PRD'],
            help='The environment to test. QAS or PRD.')
    cmd_args = parser.parse_args()
    # And off we go...
    main(cmd_args)
