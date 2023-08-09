# RefTrace
the Implementation of HTTP-Based APT Malware Infection Detection Using URL Correlation Analysis

## Target:

- uncover for APT malware traffic related to data exfiltration
- uncover other suspect APT activities 

## Testing Dataset:

- [CTU-Mixed-Capture-5-bro(zeek)](https://mcfp.felk.cvut.cz/publicDatasets/CTU-Mixed-Capture-5/bro/http.log)

    - the infected time:
        First packet after infection (not necessary an infected packet) 1970-01-01 02:22:39.378395 IP 10.0.2.200.61691 > 8.8.8.8.53: 23144+ A? clients2.google.com. (37)


## Features
- distributed data processing
- distributed computation
- asynchronous processing to improve execution efficiency

## Doing
- redirection reconstruction


## Structure
- src
    - reconstruct: implementation of redirection refactoring for refer graphs
    - similarity: implementation of computation for similarity of any two urls
    - request_filter: implementation of local outlier factor

- utils
    - preprocess: extract the relevent URL (ori: mitmproxy, optional: zeek)

## Extension:

- detection for encrypted and forged normal HTTP/HTTPs traffic

## Running
