# RefTrace
the Implementation of HTTP-Based APT Malware Infection Detection Using URL Correlation Analysis

## Target:

- uncover for APT malware traffic related to data exfiltration
- uncover other suspect APT activities 

## Features
- distributed data processing
- distributed computation
- asynchronous processing to improve execution efficiency

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
