# Invoice phrase matching.

The following code contains an implementation for matching words/phrases from an Invoice which resemble similar thing but are either shortened or jargoned.
  - I have referred mentioned links for implementing.
    https://bergvca.github.io/2017/10/14/super-fast-string-matching.html
    https://medium.com/wbaa/https-medium-com-ingwbaa-boosting-selection-of-the-most-similar-entities-in-large-scale-datasets-450b3242e618

# New Features!

  - I have reduced number of similarity multiplication operation by using negative index search on the data.
  - Have also implemented multiprocessing module for the same, but only to use if one can justify the amount of data supersede than conventional model.

## Elucidation
- I have used awesome_cossim_topn module to calculate sparse vector similarity.
- I have used gRPC client-server model for local deployment. There is no reason for choosing gRPC over REST, just I wanted to try and implement.
- Also one needs to have bloomRPC installed to test which is equivalent to POSTMAN in REST. If not, one can modify the client file and will still get the result expected.

### Setup to RUN

Install the dependencies from the requirement.txt and also one needs to have [protobuf](https://developers.google.com/protocol-buffers/docs/downloads) installed.
Also grpc python module and protobuf version should match to roll gRPC server,

Server setup
```sh
> Activate venv
> pip install -r requirements.txt
> cd to project root directory
> python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ingestor.proto
> python service.py
```

Client setup
You can run client from cmd or from bloomRPC.

```sh
> cd to project directory
> ingest appropriate data for source and target fields to data.py file
> python client.py
```

### Development
Want to contribute? Great!
Please write to me on jay7ta@outlook.com or create a pull modification request.

### Future Enhancements

 - Need to connect to database and take advantage of indexing.
 - Improve service part on gRPC.
 - Improve matching by introducing ACRONYM & Abbreviations.


Note: Code in the repository is not Modular or follows strict writing rules. Kindly be ok with me on that.



