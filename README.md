# ensemble-rewrite-test

## Synopsis

Tests the rewrite methods of MediaHaven for ensembles. Ensembles are sets or collections of media objects. API information on ensembles can be found here: [https://archief.viaa.be/mediahaven-rest-api/#mediahaven-rest-api-manual-working-with-ensembles](https://archief.viaa.be/mediahaven-rest-api/#mediahaven-rest-api-manual-working-with-ensembles).

## Goal

This code tests the MediaHaven API to:

- List children within an ensemble
- Delete a child from an ensemble
- Add a child to an ensemble
- Rewrite the whole ensemble

## Usage

```$ python3 test_complex_objects.py --help

usage: test_complex_objects.py [-h] -u USERNAME -p PASSWORD [-e {QAS,PRD}]

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Username to use when connecting to mediahaven.
  -p PASSWORD, --password PASSWORD
                        Password to use when connecting to mediahaven.
  -e {QAS,PRD}, --environment {QAS,PRD}
                        The environment to test. QAS or PRD.```

Thus, run the code using python3 in the following manner:

```$ python3 test_complex_objects.py --username myusername --password mypwd```

Optionally, an `environment` argument (`--environment QAS` or `--environment PRD`) can be used to perform the tests on either of those environments. Defaults to `QAS` (run in `PRD` at your own risk!).

The code will list how many (and which) children the object has, delete one, re-add it, and completely re-write the ensemble.

### Example output:

```
2018-02-08 09:30:12,514   INFO    : Running in environment: QAS
2018-02-08 09:30:14,017   INFO    : Fragment has 25 children:
2018-02-08 09:30:14,017   INFO    :     1: qs6d5p8m4q_0006_tif
2018-02-08 09:30:14,017   INFO    :     2: qs6d5p8m4q_0005_tif
2018-02-08 09:30:14,017   INFO    :     3: qs6d5p8m4q_0006_alto
2018-02-08 09:30:14,017   INFO    :     4: qs6d5p8m4q_0004_tif
2018-02-08 09:30:14,017   INFO    :     5: qs6d5p8m4q_0005_alto
2018-02-08 09:30:14,017   INFO    :     6: qs6d5p8m4q_0002_alto
2018-02-08 09:30:14,017   INFO    :     7: qs6d5p8m4q_0001_alto
2018-02-08 09:30:14,018   INFO    :     8: qs6d5p8m4q_mets
2018-02-08 09:30:14,018   INFO    :     9: qs6d5p8m4q_0003_jp2
2018-02-08 09:30:14,018   INFO    :     10: qs6d5p8m4q_0003_alto
2018-02-08 09:30:14,018   INFO    :     11: qs6d5p8m4q_0004_alto
2018-02-08 09:30:14,018   INFO    :     12: qs6d5p8m4q_0004_jpg
2018-02-08 09:30:14,018   INFO    :     13: qs6d5p8m4q_0003_jpg
2018-02-08 09:30:14,018   INFO    :     14: qs6d5p8m4q_0003_tif
2018-02-08 09:30:14,018   INFO    :     15: qs6d5p8m4q_0002_tif
2018-02-08 09:30:14,018   INFO    :     16: qs6d5p8m4q_0001_tif
2018-02-08 09:30:14,018   INFO    :     17: qs6d5p8m4q_pdf
2018-02-08 09:30:14,018   INFO    :     18: qs6d5p8m4q_original_mets
2018-02-08 09:30:14,019   INFO    :     19: qs6d5p8m4q_0002_jpg
2018-02-08 09:30:14,019   INFO    :     20: qs6d5p8m4q_0001_jp2
2018-02-08 09:30:14,019   INFO    :     21: qs6d5p8m4q_0001_jpg
2018-02-08 09:30:14,019   INFO    :     22: qs6d5p8m4q_0006_jp2
2018-02-08 09:30:14,019   INFO    :     23: qs6d5p8m4q_0005_jp2
2018-02-08 09:30:14,019   INFO    :     24: qs6d5p8m4q_0004_jp2
2018-02-08 09:30:14,019   INFO    :     25: qs6d5p8m4q_0002_jp2
2018-02-08 09:30:14,019   INFO    : Removing item with index 14 (qs6d5p8m4q_0002_tif) from the ensemble
2018-02-08 09:30:15,277   INFO    : Re-adding the previously deleted object
2018-02-08 09:30:16,307   INFO    : Rewriting the object
2018-02-08 09:30:17,918   INFO    : Sleeping to make sure the update persisted
2018-02-08 09:30:24,335   INFO    : Fragment has 25 children
```
