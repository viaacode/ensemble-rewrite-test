# ensemble-rewrite-test
Tests the rewrite methods of MH

## Goal
This code tests the MH API to:
- List children within an ensemble
- Delete a child from an ensemble
- Add a child to an ensemble
- Rewrite the whole ensemble

## Usage
Run the code using python3 in the following manner:
`python3 test_complex_objects.py --fragment_id 3274e0c3b03743dda7f96ec0b28d904f9bdcc87f625645a69dde31ccaea0b3e907198c9d6b0d480a9f6af70862663c6e --username myusername --password mypwd`

The `fragment_id` parameter must be a `fragment_id` from an ensemble. The code will list how many (and which) children the object has, delete one, re-add it, and completely re-write the ensemble.

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