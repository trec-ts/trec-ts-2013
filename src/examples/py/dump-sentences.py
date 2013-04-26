#!/usr/bin/python
import streamcorpus
import sys

## iterate over StreamItem messages in a flat file
for si in streamcorpus.Chunk(path=sys.argv[1]):
  ## iterate over the sentences map for each tagger, using 'lingpipe' segmentation
  for sentence_index in range(len(si.body.sentences["lingpipe"])):    
    # unique document id
    document_id = si.stream_id
    # seconds from 1970 (UTC)
    document_time = "%d"%(si.stream_time.epoch_ticks)
    # sentence index
    sentence_index_string = "%d"%(sentence_index)
    # sentence tokens
    sentence_tokens = si.body.sentences["lingpipe"][sentence_index].tokens
    # concatenate token strings into a sentence
    sentence=""
    for token in sentence_tokens:
      sentence = "%s%s "%(sentence,token.token)
    print "\t".join([document_id,document_time,sentence_index_string,sentence])
